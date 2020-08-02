from SyntaxAnalyser.lark import parser
text = '''int main() {
    string s;
    Student t;
    int x;
    s = "ddfdfdfdf";
}
'''
print(parser.parse(text).pretty())