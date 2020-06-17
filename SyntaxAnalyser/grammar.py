grammar = '''
    //main grammar
    
    start : decl+
    decl : variable_decl | function_decl | class_decl | interface_decl
    variable_decl : variable T_SEMICOLON
    variable : type T_ID
    type: T_INT | T_BOOL | T_DOUBLE | T_STRING | T_ID | type T_BRACKET_OPEN T_BRACKET_CLOSE
    
    //terminals
    
    //keywords
    T_VOID : "void"
    T_INT : "int"
    T_BOOL : "bool"
    T_DOUBLE : "double"
    T_STRING : "string"
    T_CLASS : "class"
    T_INTERFACE : "interface"
    T_NULL : "null"
    T_THIS : "this"
    T_EXTENDS : "extends"
    T_IMPLEMENTS : "implements"
    T_FOR : "for"
    I_WHILE : "while"
    T_IF : "if"
    I_ELSE : "else"
    I_RETURN : "return"
    I_BREAK : "break"
    I_NEW : "new"
    I_NEWARRAY : "NewArray"
    I_PRINT : "Print"
    I_READINTEGER : "ReadInteger"
    I_READLINE : "ReadLine"
    
    //literals
    T_BOOLEANLITERAL : /(false|true)/
    T_STRINGLITERAL : /".*"/
    T_INTLITERAL : /((0[xX](\d|[a-f|A-F])+)|\d+)/
    T_DOUBLELITERAL : /\d+\.\d*([eE][+-]?\d+)?/
    T_ID : /[a-z|A-Z]\w{0,30}/
    
    //comments
    T_INLINE_COMMENT : /\/\/.*\n/
    T_COMMENT : /\/\*(.*\n*)*\*\//
    
    //punctuations
    T_PLUS : "+"
    T_MINUS : "-"
    T_MULT : "*"
    T_DIVIDE : "/"
    T_PERCENTAGE : "%"
    T_SMALLER : "<"
    T_SMALLER_EQUAL : "<="
    T_BIGGER : ">"
    T_BIGGER_EQUAL : ">="
    T_EQUAL_EQUAL : "=="
    T_EQUAL : "="
    T_NOT_EQUAL : "!="
    T_AND : "&&"
    T_OR : "||"
    T_NOT : "!"
    T_SEMICOLON : ";"
    T_COMMA : ","
    T_DOT : "."
    T_ROUND_BRACKET_OPEN : "{"
    T_ROUND_BRACKET_CLOSE : "}"
    T_PARENTHESES_CLOSE : ")"
    T_PARENTHESES_OPEN : "("
    T_BRACKET_CLOSE : "]"
    T_BRACKET_OPEN : "["
    T_COLON : ":"
    
    //ignores
    %import common.WS
    %ignore WS
    %ignore COMMENT
    %ignore INLINE_COMMENT
'''
