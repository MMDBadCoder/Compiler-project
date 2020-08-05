from lark import Token
from CodeGen.symbolTableItem import SymbolTableItem

symbolTable = []
# scopes are separated by !!!
customId = [0]
dataMips = ['.data', 'true : .asciiz "true"', 'false : .asciiz "false"']
codeMips = ['''.text
main:''']

def dfs(tree, node):
    if (type(node) is not Token):
        if node.data == 'variable_decl':
            variable_decl_f(node)
        elif node.data == 'print_stmt':
            print_stmt_f(node)

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
    symbol = SymbolTableItem(variableType, variableName, customId[0])
    customId[0] += 1
    symbolTable.append(symbol)
    if variableType == 'int' or variableType == 'bool':
        dataMips.append(symbol.id + ': 0')
    elif variableType == 'string':
        dataMips.append(symbol.id + ': .asciiz " "')

def print_stmt_f(node):
    for i in range(2, node.children.__len__() - 2, 2):
        temp = node.children[i]
        while(type(temp) is not Token):
            temp = temp.children[0]
        if temp.type == 'T_ID':
            foundSymbol = findInSymbolTable(temp.value)
            if foundSymbol.type == 'int':
                code = '''lw $a0, {}
                li $v0, 1
                syscall'''.format(foundSymbol.id)
                codeMips.append(code)
            elif foundSymbol.type == 'string':
                code = '''la $a0, {}
                li $v0, 4
                syscall'''.format(foundSymbol.id)
                codeMips.append(code)
            elif foundSymbol.type == 'bool':
                code = '''li $v0, 4
                lw $t0, {}
                beq $zero , $t0, label{}
                la $a0, true
                j label{}
                label{}
                la $a0, false
                label{}
                syscall'''.format(foundSymbol.id, customId[0], customId[0]+1, customId[0], customId[0] + 1)
                codeMips.append(code)
                customId[0] += 2
            # find in symbol table and write mips code
        elif temp.type == 'T_INTLITERAL':
            code = '''li $a0, {}
            li $v0, 1
            syscall'''.format(temp.value)
            codeMips.append(code)
        elif temp.type == 'T_BOOLEANLITERAL':
            code = '''li $v0, 4
            la $a0, {}
            syscall'''.format(temp.value)
            codeMips.append(code)
            customId[0] += 2
        elif temp.type == 'T_STRINGLITERAL':
            dataMips.append('str{} : .asciiz {}'.format(customId[0], temp.value))
            code = '''la $a0, str{}
            li $v0, 4
            syscall'''.format(customId[0])
            codeMips.append(code)
            customId[0] += 1
def findInSymbolTable(name):
    for i in range(symbolTable.__len__() - 1, -1, -1):
        if(name == symbolTable[i].name):
            return symbolTable[i]
def cleanScope():
    while(symbolTable[-1] != '!!!'):
        symbolTable.pop(-1)
    symbolTable.pop(-1)