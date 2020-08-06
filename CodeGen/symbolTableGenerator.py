from lark import Token
from CodeGen.symbolTableItem import SymbolTableItem

symbolTable = []
# scopes are separated by !!!
customId = [0]
registerId = [0]
dataMips = ['.data']
codeMips = ['''.text\nmain:''']
constantsOfData = ['true: .asciiz "true"', 'false: .asciiz "false"', 'newLine: .asciiz "\\n"']

def dfs(tree, node):
    flag = False
    if type(node) is not Token:
        if node.data == 'variable_decl':
            variable_decl_f(node)
            flag = True
        elif node.data == 'print_stmt':
            print_stmt_f(node)
            flag = True
        elif node.data == 'stmt':
            stmt_f(node)
    else:
        if node == '{':
            symbolTable.append('!!!')
        if node == '}':
            cleanScope()
    if type(node) is not Token and not flag:
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
    elif variableType == 'double':
        symbol = SymbolTableItem(variableType, variableName, customId[0], 0.0)
        customId[0] += 1
        symbolTable.append(symbol)
        dataMips.append(symbol.id + ': .float 0.0')


def variable_change(var, value):
    if value.type == 'T_ID':
        symbolOfValue = findInSymbolTable(value.value)
        symbolOfVar = findInSymbolTable(var.value)
        if symbolOfVar.type == 'int' or symbolOfVar.type == 'bool':
            code = '''lw $t0 , {}\nsw $t0, {}'''.format(symbolOfValue.id, symbolOfVar.id)
            codeMips.append(code)
            symbolOfVar.value = symbolOfValue.value
        elif symbolOfVar.type == 'double':
            code = '''l.s $t0 , {}\ns.s $t0, {}'''.format(symbolOfValue.id, symbolOfVar.id)
            codeMips.append(code)
            symbolOfVar.value = symbolOfValue.value
        elif symbolOfVar.type == 'string':
            tempSymbol = SymbolTableItem('string', var.value, customId[0], value.value)
            customId[0] += 1
            symbolTable.append(tempSymbol)
            dataMips.append(tempSymbol.id + ': .asciiz {}'.format(value.value))
    elif value.type == 'T_INTLITERAL':
        foundSymbol = findInSymbolTable(var.value)
        foundSymbol.value = value.value
        code = '''li $t0, {}\nsw $t0, {}'''.format(value.value, foundSymbol.id)
        codeMips.append(code)
    elif value.type == 'T_STRINGLITERAL':
        tempSymbol = SymbolTableItem('string', var.value, customId[0], value.value)
        customId[0] += 1
        symbolTable.append(tempSymbol)
        dataMips.append(tempSymbol.id + ': .asciiz {}'.format(value.value))
    elif value.type == 'T_BOOLEANLITERAL':
        foundSymbol = findInSymbolTable(var.value)
        if value.value == 'true':
            foundSymbol.value = 1
        else:
            foundSymbol.value = 0
        code = '''li $t0, {}\nsw $t0, {}'''.format(foundSymbol.value, foundSymbol.id)
        codeMips.append(code)
    elif value.type == 'T_DOUBLELITERAL':
        foundSymbol = findInSymbolTable(var.value)
        foundSymbol.value = value.value
        dataMips.append('dbl{} : .float {}'.format(customId[0], value.value))
        code = '''l.s $f12, dbl{}\ns.s $f12, {}'''.format(customId[0], foundSymbol.id)
        codeMips.append(code)
        customId[0] += 1
    elif value.type == 'T_READINTEGER':
        foundSymbol = findInSymbolTable(var.value)
        foundSymbol.value = value.value
        code = '''li $v0, 5\nsyscall\nsw $v0, {}'''.format(foundSymbol.id)
        codeMips.append(code)
    elif value.type == 'T_READLINE':
        dataMips.append('buffer{}: .space 100'.format(customId[0]))
        code = '''li $v0, 8\nla $a0, buffer{}\nli $a1, 100\nsyscall'''.format(customId[0])
        tempSymbol = SymbolTableItem('string', var.value, customId[0],' ')
        tempSymbol.id = 'buffer' + customId[0].__str__()
        symbolTable.append(tempSymbol)
        customId[0] += 1
        codeMips.append(code)


def print_stmt_f(node):
    for i in range(2, node.children.__len__() - 2, 2):
        temp = node.children[i]
        while type(temp) is not Token:
            temp = temp.children[0]
        # print(temp)
        # print(temp.type)
        if temp.type == 'T_ID':
            foundSymbol = findInSymbolTable(temp.value)
            if foundSymbol.type == 'int':
                code = '''li $v0, 1\nlw $a0, {}\nsyscall'''.format(foundSymbol.id)
                codeMips.append(code)
            elif foundSymbol.type == 'string':
                code = '''li $v0, 4\nla $a0, {}\nsyscall'''.format(foundSymbol.id)
                codeMips.append(code)
            elif foundSymbol.type == 'bool':
                code = '''li $v0, 4\nlw $t0, {}\nbeq $zero , $t0, label{}\nla $a0, true\nj label{}\nlabel{}:\nla $a0, false\nlabel{}:\nsyscall'''.format(
                    foundSymbol.id, customId[0], customId[0] + 1, customId[0], customId[0] + 1)
                codeMips.append(code)
                customId[0] += 2
            elif foundSymbol.type == 'double':
                code = '''l.s $f12, {}\nli $v0, 2\nsyscall'''.format(foundSymbol.id)
                codeMips.append(code)
        elif temp.type == 'T_INTLITERAL':
            code = '''li $v0, 1\nli $a0, {}\nsyscall'''.format(temp.value)
            codeMips.append(code)
        elif temp.type == 'T_BOOLEANLITERAL':
            code = '''li $v0, 4\nla $a0, {}\nsyscall'''.format(temp.value)
            codeMips.append(code)
        elif temp.type == 'T_STRINGLITERAL':
            dataMips.append('str{} : .asciiz {}'.format(customId[0], temp.value))
            code = '''li $v0, 4\nla $a0, str{}\nsyscall'''.format(customId[0])
            codeMips.append(code)
            customId[0] += 1
        elif temp.type == 'T_DOUBLELITERAL':
            dataMips.append('dbl{} : .float {}'.format(customId[0], temp.value))
            code = '''l.s $f12, dbl{}\nli $v0, 2\nsyscall'''.format(customId[0])
            codeMips.append(code)
            customId[0] += 1
        code = '''li $v0, 4\nla $a0, newLine\nsyscall'''
        codeMips.append(code)


def stmt_f(node):
    if node.children[0].data == 'expr':
        if node.children[0].children[1] == '=':
            var = node.children[0].children[0]
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
