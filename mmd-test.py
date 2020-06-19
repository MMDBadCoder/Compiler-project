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
        print(correct_answer)
        print('-------------')


def test_file(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('main.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('mmd.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    with open("tests/" + inputfile, "r") as input_file:
        from SyntaxAnalyser.parser import parse
        result = parse(input_file)

    with open("out/" + outputfile, "w") as output_file:
        if result is True:
            output_file.write("YES")
        else:
            output_file.write("NO")
