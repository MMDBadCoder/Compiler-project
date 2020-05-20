from LexicalAnalyser.configs import output_file_address, input_file_address
from LexicalAnalyser.scanner import get_tokens

input_file = open(input_file_address, 'r')
content = input_file.read()
input_file.close()

tokens = get_tokens(content)

out_text = ''
for token in tokens:
    if token['token'] == 'T_ID' or 'T_BOOLEANLITERAL' or 'T_STRINGLITERAL' or 'T_INTEGERLITERAL' or 'T_DOUBLELITERAL' or 'UNDEFINED_TOKEN':
        out_text += token['token'] + ' ' + token['matched_content'] + '\n'
    else :
        out_text += token['matched_content'] + '\n'

output_file = open(output_file_address, 'w')
output_file.write(out_text)
output_file.close()