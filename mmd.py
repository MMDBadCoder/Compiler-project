from SyntaxAnalyser.parser import parse

text = '''

int main() {
    int[] array
}

'''
parse(text)
