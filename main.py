import sys, getopt
def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('main.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    with open("tests/" + inputfile, "r") as input_file:
        from SyntaxAnalyser.lark import parser
        from CodeGen.symbolTableGenerator import dfs, dataMips, codeMips, constantsOfData
        text = input_file.read()
        myTree = parser.parse(text)
        dfs(myTree, myTree)
        dataMips = dataMips + constantsOfData
        result = ''
        for i in dataMips:
            result = result + i + '\n'
        for i in codeMips:
            result = result + i + '\n'


    with open("out/" + outputfile, "w") as output_file:
        output_file.write(result)


if __name__ == "__main__":
    main(sys.argv[1:])