import sys, getopt


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('main.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    with open("tests/" + inputfile, "r") as input_file:
        content = input_file.read()
        input_file.close()

    from LexicalAnalyser.scanner import get_tokens
    tokens = get_tokens(content)

    out_text = ''
    shown_tokens = ['T_ID', 'T_BOOLEANLITERAL', 'T_STRINGLITERAL', 'T_INTLITERAL', 'T_DOUBLELITERAL',
                    'UNDEFINED_TOKEN']
    for token in tokens:
        if token['token'] in shown_tokens:
            out_text += token['token'] + ' ' + token['matched_content'] + '\n'
        else:
            out_text += token['matched_content'] + '\n'

    with open("out/" + outputfile, "w") as output_file:
        output_file.write(out_text)
        output_file.close()


if __name__ == "__main__":
    main(sys.argv[1:])
