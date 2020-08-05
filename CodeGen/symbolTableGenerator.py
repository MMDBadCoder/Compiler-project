from lark import Token, Tree
symbolTable = []
#scopes are separated by !!!
def dfs(tree, node):
    if (type(node) is not Token):
        if node.data == 'variable_decl':
            variableType = node.children[0].children[0].children[0]
            variableName = node.children[0].children[1]

    if type(node) is not Token:
        for i in range(node.children.__len__()):
            dfs(tree, node.children[i])