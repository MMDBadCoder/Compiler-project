from SyntaxAnalyser.parser import parse

text = '''
int main() {
    int z;
}
'''
parse(text)