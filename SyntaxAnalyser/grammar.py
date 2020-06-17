grammar = '''
    //main grammar
    
    start : decl+
    decl : variable_decl | function_decl | class_decl | interface_decl
    variable_decl : variable T_SEMICOLON
    variable : type T_ID
    type: T_INT | T_BOOL | T_DOUBLE | T_STRING | T_ID | type T_BRACKET_OPEN T_BRACKET_CLOSE
    function_decl : type T_ID T_PARENTHESES_OPEN formals T_PARENTHESES_CLOSE stmt_block | T_VOID T_ID T_PARENTHESES_OPEN formals T_PARENTHESES_CLOSE stmt_block
    formals : variable (T_COMMA variable)* |
    class_decl : T_CLASS T_ID T_SMALLER T_EXTENDS T_ID T_BIGGER T_SMALLER T_IMPLEMENTS T_ID (T_COMMA T_ID)* T_BIGGER T_ROUND_BRACKET_OPEN field* T_ROUND_BRACKET_CLOSE
    field : variable_decl | function_decl
    interface_decl : T_INTERFACE T_ID T_ROUND_BRACKET_OPEN prototype* T_ROUND_BRACKET_CLOSE
    prototype : type T_ID T_PARENTHESES_OPEN formals T_PARENTHESES_CLOSE T_SEMICOLON | T_VOID T_ID T_PARENTHESES_OPEN formals T_PARENTHESES_CLOSE T_SEMICOLON
    stmt_block : T_ROUND_BRACKET_OPEN variable_decl* stmt* T_ROUND_BRACKET_CLOSE
    stmt : T_SMALLER expr T_BIGGER T_SEMICOLON | i_f_stmt | while_stmt | for_stmt | break_stmt | return_stmt | print_stmt | stmt_block
    i_f_stmt : T_IF T_ROUND_BRACKET_OPEN expr T_ROUND_BRACKET_CLOSE
    while_stmt : I_WHILE T_PARENTHESES_OPEN expr T_PARENTHESES_CLOSE stmt
    for_stmt = T_FOR T_PARENTHESES_OPEN T_SMALLER expr T_BIGGER T_SEMICOLON T_SMALLER expr T_BIGGER T_SEMICOLON T_SMALLER expr T_BIGGER T_PARENTHESES_CLOSE stmt
    return_stmt = I_RETURN T_SMALLER expr T_BIGGER T_SEMICOLON
    break_stmt : I_BREAK T_SEMICOLON
    print_stmt : I_PRINT T_PARENTHESES_OPEN expr (T_COMMA expr)* T_PARENTHESES_CLOSE T_SEMICOLON
    
    expr : 
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
