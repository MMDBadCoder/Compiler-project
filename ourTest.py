from SyntaxAnalyser.lark import parser
from CodeGen.symbolTableGenerator import dfs
text = '''int main() {
    string s;
    double t;
    int x;
    s = "ddfdfdfdf";
    Print(x);
}
'''

myTree = parser.parse(text)
# print(myTree.pretty())
# print(myTree.data)
# if(myTree.data == 'start'):
#     print('yes')
dfs(myTree, myTree)
# print(myTree.children[0].children[0].children[5].children[5].children[0].children[2].
#       children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0]
#       .children[0].children[0].value)