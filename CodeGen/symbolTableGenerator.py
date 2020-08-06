from lark import Token
from CodeGen.symbolTableItem import SymbolTableItem

symbolTable = []
# scopes are separated by !!!
customId = [0]
registerId = [0]
dataMips = ['.data', 'true : .asciiz "true"', 'false : .asciiz "false"']
codeMips = ['''.text\nmain:''']


def dfs(tree, node):
    if type(node) is not Token:
        if node.data == 'variable_decl':
            variable_decl_f(node)
        elif node.data == 'print_stmt':
            print_stmt_f(node)
        elif node.data == 'stmt':
            stmt_f(node)
    else:
        if node == '{':
            symbolTable.append('!!!')
        if node == '}':
            cleanScope()
    if type(node) is not Token:
        for i in range(node.children.__len__()):
            dfs(tree, node.children[i])


def variable_decl_f(node):
    variableType = node.children[0].children[0].children[0]
    variableName = node.children[0].children[1]
    if variableType == 'int' or variableType == 'bool':
        symbol = SymbolTableItem(variableType, variableName, customId[0], 0)
        customId[0] += 1
        symbolTable.append(symbol)
        dataMips.append(symbol.id + ': 0')
    elif variableType == 'string':
        symbol = SymbolTableItem(variableType, variableName, customId[0], ' ')
        customId[0] += 1
        symbolTable.append(symbol)
        dataMips.append(symbol.id + ': .asciiz " "')


def variable_change(var, value):
    if value.type == 'T_ID':
        if value.value != 'true' and value.value != 'false':
            symbolOfValue = findInSymbolTable(value.value)
            tempSymbol = SymbolTableItem(var.type, var.value, customId[0], symbolOfValue.value)
            customId[0] += 1
            symbolTable.append(tempSymbol)
            # dataMips.append(tempSymbol.id + ': {}'.format(symbolOfValue.value))
            code = '''la $t{}, $t{}'''.format(registerId[0], registerId[0] - 1)
            codeMips.append(code)
            registerId[0] += 1
        else:
            tempSymbol = SymbolTableItem(var.type, var.value, customId[0], 'true')
            customId[0] += 1
            symbolTable.append(tempSymbol)
            # dataMips.append(tempSymbol.id + ': {}'.format(value.value))
            code = '''la $t{}, {}'''.format(registerId[0], value.value)
            codeMips.append(code)
            registerId[0] += 1
    elif value.type == 'T_INTLITERAL':
        tempSymbol = SymbolTableItem(var.type, var.value, customId[0], value.value)
        customId[0] += 1
        symbolTable.append(tempSymbol)
        # dataMips.append(tempSymbol.id + ': {}'.format(value.value))
        code = '''li $t{}, {}'''.format(registerId[0], value.value)
        codeMips.append(code)
        registerId[0] += 1
    elif value.type == 'T_STRINGLITERAL':
        tempSymbol = SymbolTableItem(var.type, var.value, customId[0], value.value)
        customId[0] += 1
        symbolTable.append(tempSymbol)
        dataMips.append('str{} : .asciiz {}'.format(customId[0], value.value))
        code = '''la $t{}, str{}'''.format(registerId[0], customId[0])
        codeMips.append(code)
        customId[0] += 1
        registerId[0] += 1
    elif value.type == 'T_DOUBLELITERAL':
        pass


def print_stmt_f(node):
    for i in range(2, node.children.__len__() - 2, 2):
        temp = node.children[i]
        while type(temp) is not Token:
            temp = temp.children[0]
        # print(temp)
        # print(temp.type)
        if temp.type == 'T_ID':
            if temp.value != 'true' and temp.value != 'false':
                foundSymbol = findInSymbolTable(temp.value)
                if foundSymbol.type == 'int':
                    code = '''li $v0, 1\nlw $a0, {}\nsyscall'''.format(foundSymbol.id)
                    codeMips.append(code)
                elif foundSymbol.type == 'string':
                    code = '''li $v0, 4\nla $a0, {}\nsyscall'''.format(foundSymbol.id)
                    codeMips.append(code)
                elif foundSymbol.type == 'bool':
                    code = '''li $v0, 4\nlw $t0, {}\nbeq $zero , $t0, label{}\nla $a0, true\nj label{}\nlabel{}\nla $a0, false\nlabel{}\nsyscall'''.format(foundSymbol.id, customId[0], customId[0]+1, customId[0], customId[0] + 1)
                    codeMips.append(code)
                    customId[0] += 2
            else:
                code = '''li $v0, 4\nla $a0, {}\nsyscall'''.format(temp.value)
                codeMips.append(code)
            # find in symbol table and write mips code
        elif temp.type == 'T_INTLITERAL':
            code = '''li $v0, 1\nli $a0, {}\nsyscall'''.format(temp.value)
            codeMips.append(code)
        # elif temp.type == 'T_BOOLEANLITERAL':
        #     code = '''li $v0, 4\nla $a0, {}\nsyscall'''.format(temp.value)
        #     codeMips.append(code)
        #     # customId[0] += 2
        elif temp.type == 'T_STRINGLITERAL':
            dataMips.append('str{} : .asciiz {}'.format(customId[0], temp.value))
            code = '''li $v0, 4\nla $a0, str{}\nsyscall'''.format(customId[0])
            codeMips.append(code)
            customId[0] += 1


def stmt_f(node):
    if node.children[0].children[0] != 'Print':
        var = node.children[0]
        value = node.children[0].children[2]
        while type(var) is not Token:
            var = var.children[0]
        while type(value) is not Token:
            value = value.children[0]
        variable_change(var, value)


def findInSymbolTable(name):
    for i in range(symbolTable.__len__() - 1, -1, -1):
        if name == symbolTable[i].name:
            return symbolTable[i]


def cleanScope():
    while symbolTable[-1] != '!!!':
        symbolTable.pop(-1)
    symbolTable.pop(-1)