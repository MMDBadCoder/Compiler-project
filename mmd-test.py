import re
import sys, getopt

import os

test_file_address = './tests/'

for file in os.listdir(test_file_address):
    if file.endswith(".in"):
        file_name_without_format = str(file)[:-3]

        input_file = open(test_file_address + file_name_without_format + '.in', 'r')
        output_file = open(test_file_address + file_name_without_format + '.out', 'r')

        code = input_file.read()
        correct_answer = output_file.readline()

        from SyntaxAnalyser.parser import parse

        result = parse(code)

        print('-------------')
        print(file_name_without_format)
        print(result)
        print(re.search('YES', correct_answer) != None)
        print('-------------')
