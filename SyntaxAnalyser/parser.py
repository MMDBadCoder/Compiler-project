def parse(input_file):
    input_str = input_file.read()
    from SyntaxAnalyser.lark import parser
    error = False
    try:
        parser.parse(input_str)
    except Exception as e:
        error = True
    return not error
