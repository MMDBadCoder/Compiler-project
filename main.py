from LexicalAnalyser.configs import output_file_address, input_file_address
from LexicalAnalyser.scanner import get_tokens

input_file = open(input_file_address, 'r')
content = input_file.read()

tokens = get_tokens(content)
print(tokens)

