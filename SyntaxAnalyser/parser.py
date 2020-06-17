def parse(input):
    from SyntaxAnalyser.lark import parser
    error = False
    try:
        parser.parse(input)
    except Exception as e:
        error = True
    return not error
