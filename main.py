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
        print(result)
        if result is True:
            output_file.write("YES")
        else:
            output_file.write("NO")


if __name__ == "__main__":
    main(sys.argv[1:])
