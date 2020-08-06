from SyntaxAnalyser.lark import parser
from CodeGen.symbolTableGenerator import dfs, dataMips, codeMips, symbolTable, constantsOfData

text = '''int main() {
    int a;
    int b;
    int c;
    int d;

    int z;
    
    a = ReadInteger();
    b = ReadInteger();
    c = ReadInteger();
    d = ReadInteger();

    z = a + (b * 5);
    a = z * d;
    z = 2 * a + ((a + b) / (c + d));
    b = z / a;
    c = b * a + z;
    d = a - b - c - d - z;

    Print(a);
    Print(b);
    Print(c);
    Print(d);

    Print(z);
}'''

myTree = parser.parse(text)
# print(myTree.pretty())
# print(myTree.data)
# if(myTree.data == 'start'):
#     print('yes')
dfs(myTree, myTree)
dataMips = dataMips + constantsOfData
for i in dataMips:
    print(i)
for i in codeMips:
    print(i)
# print(myTree.children[0].children[0].children[5].children[5].children[0].children[2].
#       children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0]
#       .children[0].children[0].value)
