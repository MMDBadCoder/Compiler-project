from SyntaxAnalyser.lark import parser
from CodeGen.symbolTableGenerator import dfs, dataMips, codeMips, symbolTable
text = '''int main() {
    string s;
    double t;
    bool bb;
    int x;
    int z;
    s = "ddfdfdfdf";
    bb = true;
    x = 88;
    z = x;
    Print(x, s, 23, true);
}
'''

myTree = parser.parse(text)
# print(myTree.pretty())
# print(myTree.data)
# if(myTree.data == 'start'):
#     print('yes')
dfs(myTree, myTree)
print(dataMips)
for i in codeMips:
    print(i)
for i in symbolTable:
    print(i)
# print(myTree.children[0].children[0].children[5].children[5].children[0].children[2].
#       children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0]
#       .children[0].children[0].value)
