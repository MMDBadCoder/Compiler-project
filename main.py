from LexicalAnalyser.configs import output_file_address, input_file_address
from LexicalAnalyser.scanner import get_tokens

input_file = open(input_file_address, 'r')
content = input_file.read()
input_file.close()

tokens = get_tokens(content)

out_text = ''
shown_tokens = ['T_ID', 'T_BOOLEANLITERAL', 'T_STRINGLITERAL', 'T_INTEGERLITERAL', 'T_DOUBLELITERAL', 'UNDEFINED_TOKEN']
for token in tokens:
    if token['token'] in shown_tokens:
        out_text += token['token'] + ' ' + token['matched_content'] + '\n'
    else:
        out_text += token['matched_content'] + '\n'

output_file = open(output_file_address, 'w')
output_file.write(out_text)
output_file.close()
