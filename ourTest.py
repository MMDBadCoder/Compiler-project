from SyntaxAnalyser.lark import parser
from CodeGen.symbolTableGenerator import dfs, dataMips, codeMips, symbolTable

text = '''int main() {
    int a;
    int b;

    a = ReadInteger();
    b = ReadInteger();

    Print(a);
    Print(b);
}
'''

myTree = parser.parse(text)
# print(myTree.pretty())
# print(myTree.data)
# if(myTree.data == 'start'):
#     print('yes')
dfs(myTree, myTree)
dataMips.append('true: .asciiz "true"')
dataMips.append('false: .asciiz "false"')
dataMips.append('newLine: .asciiz "\\n"')
for i in dataMips:
    print(i)
for i in codeMips:
    print(i)
# print(myTree.children[0].children[0].children[5].children[5].children[0].children[2].
#       children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0]
#       .children[0].children[0].value)
