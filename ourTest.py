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
    t = 5.5;
    Print(x, s, 23, true, bb);
}
'''

myTree = parser.parse(text)
# print(myTree.pretty())
# print(myTree.data)
# if(myTree.data == 'start'):
#     print('yes')
dfs(myTree, myTree)
for i in dataMips:
    print(i)
for i in codeMips:
    print(i)
# print(myTree.children[0].children[0].children[5].children[5].children[0].children[2].
#       children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0]
#       .children[0].children[0].value)
