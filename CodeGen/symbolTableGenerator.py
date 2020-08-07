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
        dataMips.append(symbol.id + ': .word 0')
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


def complex_variable_change(var, values):
    typeCheck = ['T_ID', 'T_INTLITERAL', 'T_DOUBLELITERAL', 'stack']
    operatorTypes = ['T_PLUS', 'T_MINUS', 'T_MULT', 'T_DIVIDE', 'T_PERCENTAGE']
    ALU_stack = []
    operandType = ''
    # print(values)
    for i in values:
        if i.type in typeCheck:
            if i.type == 'T_INTLITERAL':
                operandType = 'int'
            elif i.type == 'T_DOUBLELITERAL':
                operandType = 'double'
            elif i.type == 'T_ID':
                foundSymbol = findInSymbolTable(i.value)
                if foundSymbol.type == 'int':
                    operandType = 'int'
                elif foundSymbol.type == 'double':
                    operandType = 'double'
            break
    ALU_stack.append(values[0])
    ALU_stack.append(values[1])
    i = 2
    while len(ALU_stack) != 0:
        if len(ALU_stack) == 1 and i == len(values):
            break
        elif ALU_stack[-1].type in typeCheck:
            if ALU_stack[-2].type in typeCheck:
                operand1 = ALU_stack.pop(-1)
                operand2 = ALU_stack.pop(-1)
                operator = ALU_stack.pop(-1)
                # print(operand1, operator, operand2)
                calculateOperation(operand1, operator, operand2, operandType)
                tempSymbol = SymbolTableItem('stack', 'lastOfStack', 0, 0)
                ALU_stack.append(tempSymbol)
            else:
                ALU_stack.append(values[i])
                i += 1
        else:
            ALU_stack.append(values[i])
            i += 1
    varSymbol = findInSymbolTable(var.value)
    if varSymbol.type == 'int':
        code = '''lw $t0, 0($sp)\naddi $sp, $sp, 4\nsw $t0, {}'''.format(varSymbol.id)
        codeMips.append(code)
    elif varSymbol.type == 'double':
        code = '''l.s $f0, 0($sp)\naddi $sp, $sp, 4\ns.s $f0, {}'''.format(varSymbol.id)
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
            infixExpression.clear()
            postFixExpression.clear()
            preFixExpression.clear()
            getInfix(value)
            # for i in infixExpression:
            #     print(i, end='')
            # print()
            getPostFix(infixExpression)
            # for i in postFixExpression:
            #     print(i, end='')
            # print()
            desiredValues = []
            for i in range(len(postFixExpression) - 1, -1, -1):
                desiredValues.append(postFixExpression[i])
            # for i in desiredValues:
            #     print(i, end='')
            # print()
            while type(var) is not Token:
                var = var.children[0]
            # while type(value) is not Token:
            #     value = value.children[0]
            if len(postFixExpression) == 1:
                variable_change(var, postFixExpression[0])
            elif postFixExpression[1].value == 'ReadInteger' or postFixExpression[1].value == 'ReadLine':
                variable_change(var, postFixExpression[1])
            else:
                complex_variable_change(var, desiredValues)


infixExpression = []
postFixExpression = []
preFixExpression = []


def getInfix(node):
    if type(node) is not Token:
        if len(node.children) == 1:
            getInfix(node.children[0])
        else:
            for i in range(len(node.children)):
                getInfix(node.children[i])
    else:
        infixExpression.append(node)


def getPostFix(array):
    operators = ['+', '-', '*', '/', '%']
    tempStack = []
    for i in array:
        # print('********')
        # print(tempStack)
        # print(postFixExpression)
        if i not in operators and i != '(' and i != ')':
            postFixExpression.append(i)
        elif i == '(':
            tempStack.append(i)
        elif i == ')':
            while tempStack[-1] != '(':
                postFixExpression.append(tempStack[-1])
                tempStack.pop(-1)
            tempStack.pop(-1)
        elif i in operators:
            if i == '+':
                if len(tempStack) == 0:
                    tempStack.append(i)
                elif tempStack[-1] not in operators:
                    tempStack.append(i)
                else:
                    while len(tempStack) != 0 and tempStack[-1] != '(' and tempStack[-1] != ')':
                        postFixExpression.append(tempStack[-1])
                        tempStack.pop(-1)
                    tempStack.append(i)
            elif i == '-':
                if len(tempStack) == 0:
                    tempStack.append(i)
                elif tempStack[-1] not in operators:
                    tempStack.append(i)
                else:
                    while len(tempStack) != 0 and tempStack[-1] != '(' and tempStack[-1] != ')':
                        postFixExpression.append(tempStack[-1])
                        tempStack.pop(-1)
                    tempStack.append(i)
            elif i == '*':
                if len(tempStack) == 0:
                    tempStack.append(i)
                elif tempStack[-1] not in operators or tempStack[-1] == '+' or tempStack[-1] == '-':
                    tempStack.append(i)
                else:
                    while len(tempStack) != 0 and tempStack[-1] != '(' and tempStack[-1] != ')' and tempStack[-1] != '+' and tempStack[-1] != '-':
                        postFixExpression.append(tempStack[-1])
                        tempStack.pop(-1)
                    tempStack.append(i)
            elif i == '/':
                if len(tempStack) == 0:
                    tempStack.append(i)
                elif tempStack[-1] not in operators or tempStack[-1] == '+' or tempStack[-1] == '-':
                    tempStack.append(i)
                else:
                    while len(tempStack) != 0 and tempStack[-1] != '(' and tempStack[-1] != ')' and tempStack[-1] != '+' and tempStack[-1] != '-':
                        postFixExpression.append(tempStack[-1])
                        tempStack.pop(-1)
                    tempStack.append(i)
            elif i == '%':
                if len(tempStack) == 0:
                    tempStack.append(i)
                elif tempStack[-1] not in operators or tempStack[-1] == '+' or tempStack[-1] == '-':
                    tempStack.append(i)
                else:
                    while len(tempStack) != 0 and tempStack[-1] != '(' and tempStack[-1] != ')' and tempStack[-1] != '+' and tempStack[-1] != '-':
                        postFixExpression.append(tempStack[-1])
                        tempStack.pop(-1)
                    tempStack.append(i)
    while len(tempStack) != 0:
        postFixExpression.append(tempStack[-1])
        tempStack.pop(-1)


def getPreFix(array):
    temp = []
    for i in range(len(array) - 1, -1, -1):
        if array[i] == '(':
            temp.append(')')
        elif array[i] == ')':
            temp.append('(')
        else:
            temp.append(array[i])
    # for i in temp:
    #     print(i, end='')
    # print()
    getPostFix(temp)
    for i in range(len(postFixExpression) - 1, -1, -1):
        preFixExpression.append(postFixExpression[i])


def calculateOperation(operand1, operator, operand2, operandType):
    if operand1.type == 'stack' and operand2.type == 'stack':
        if operandType == 'int':
            code = '''lw $a1, 0($sp)\naddi $sp, $sp, 4\nlw $a2, 0($sp)\naddi $sp, $sp, 4'''
            codeMips.append(code)
        elif operandType == 'double':
            code = '''l.s $f1, 0($sp)\naddi $sp, $sp, 4\nl.s $f2, 0($sp)\naddi $sp, $sp, 4'''
            codeMips.append(code)
    else:
        if operand1.type == 'T_INTLITERAL':
            code = '''li $a1, {}'''.format(operand1.value)
            codeMips.append(code)
        elif operand1.type == 'T_DOUBLELITERAL':
            dataMips.append('dbl{} : .float {}'.format(customId[0], operand1.value))
            code = '''l.s $f1, dbl{}'''.format(customId[0])
            codeMips.append(code)
            customId[0] += 1
        elif operand1.type == 'stack':
            if operandType == 'int':
                code = '''lw $a1, 0($sp)\naddi $sp, $sp, 4'''
                codeMips.append(code)
            elif operandType == 'double':
                code = '''l.s $f1, 0($sp)\naddi $sp, $sp, 4'''
                codeMips.append(code)
        elif operand1.type == 'T_ID':
            tempSymbol = findInSymbolTable(operand1.value)
            if tempSymbol.type == 'int':
                code = '''lw $a1, {}'''.format(tempSymbol.id)
                codeMips.append(code)
            elif tempSymbol.type == 'double':
                code = '''l.s $f1, {}'''.format(tempSymbol.id)
                codeMips.append(code)

        if operand2.type == 'T_INTLITERAL':
            code = '''li $a2, {}'''.format(operand2.value)
            codeMips.append(code)
        elif operand2.type == 'T_DOUBLELITERAL':
            dataMips.append('dbl{} : .float {}'.format(customId[0], operand2.value))
            code = '''l.s $f2, dbl{}'''.format(customId[0])
            codeMips.append(code)
            customId[0] += 1
        elif operand2.type == 'stack':
            if operandType == 'int':
                code = '''lw $a2, 0($sp)\naddi $sp, $sp, 4'''
                codeMips.append(code)
            elif operandType == 'double':
                code = '''l.s $f2, 0($sp)\naddi $sp, $sp, 4'''
                codeMips.append(code)
        elif operand2.type == 'T_ID':
            tempSymbol = findInSymbolTable(operand2.value)
            if tempSymbol.type == 'int':
                code = '''lw $a2, {}'''.format(tempSymbol.id)
                codeMips.append(code)
            elif tempSymbol.type == 'double':
                code = '''l.s $f2, {}'''.format(tempSymbol.id)
                codeMips.append(code)

    if operandType == 'int':
        if operator.type == 'T_PLUS':
            code = '''add $t0, $a1, $a2'''
            codeMips.append(code)
        elif operator.type == 'T_MINUS':
            code = '''sub $t0, $a1, $a2'''
            codeMips.append(code)
        elif operator.type == 'T_MULT':
            code = '''mul $t0, $a1, $a2'''
            codeMips.append(code)
        elif operator.type == 'T_DIVIDE':
            code = '''div $t0, $a1, $a2'''
            codeMips.append(code)
        elif operator.type == 'T_PERCENTAGE':
            code = '''rem $t0, $a1, $a2'''
            codeMips.append(code)
        code = '''addi $sp, $sp, -4\nsw $t0, 0($sp)'''
        codeMips.append(code)
    elif operandType == 'double':
        if operator.type == 'T_PLUS':
            code = '''add.s $f0, $f1, $f2'''
            codeMips.append(code)
        elif operator.type == 'T_MINUS':
            code = '''sub.s $f0, $f1, $f2'''
            codeMips.append(code)
        elif operator.type == 'T_MULT':
            code = '''mul.s $f0, $f1, $f2'''
            codeMips.append(code)
        elif operator.type == 'T_DIVIDE':
            code = '''div.s $f0, $f1, $f2'''
            codeMips.append(code)
        code = '''addi $sp, $sp, -4\ns.s $f0, 0($sp)'''
        codeMips.append(code)



def findInSymbolTable(name):
    for i in range(symbolTable.__len__() - 1, -1, -1):
        if name == symbolTable[i].name:
            return symbolTable[i]


def cleanScope():
    while symbolTable[-1] != '!!!':
        symbolTable.pop(-1)
    symbolTable.pop(-1)
