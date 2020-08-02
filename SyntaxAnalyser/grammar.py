grammar = '''
    //main grammar

    start : decl+
    decl : variable_decl | function_decl | class_decl | interface_decl
    variable_decl : variable T_SEMICOLON
    variable : type T_ID
    type: T_INT | T_BOOL | T_DOUBLE | T_STRING | T_ID | type /\[\]/
    function_decl : type T_ID T_PARENTHESES_OPEN formals T_PARENTHESES_CLOSE stmt_block | T_VOID T_ID T_PARENTHESES_OPEN formals T_PARENTHESES_CLOSE stmt_block
    formals : variable (T_COMMA variable)* |
    class_decl : T_CLASS T_ID (T_EXTENDS T_ID)? (T_IMPLEMENTS T_ID (T_COMMA T_ID)*)? T_ROUND_BRACKET_OPEN field* T_ROUND_BRACKET_CLOSE
    field : variable_decl | function_decl
    interface_decl : T_INTERFACE T_ID T_ROUND_BRACKET_OPEN prototype* T_ROUND_BRACKET_CLOSE
    prototype : type T_ID T_PARENTHESES_OPEN formals T_PARENTHESES_CLOSE T_SEMICOLON | T_VOID T_ID T_PARENTHESES_OPEN formals T_PARENTHESES_CLOSE T_SEMICOLON
    stmt_block : T_ROUND_BRACKET_OPEN variable_decl* stmt* T_ROUND_BRACKET_CLOSE
    stmt : (expr)? T_SEMICOLON | i_f_stmt | while_stmt | for_stmt | break_stmt | return_stmt | print_stmt | stmt_block
    i_f_stmt : T_IF T_PARENTHESES_OPEN expr T_PARENTHESES_CLOSE stmt (T_ELSE stmt)?
    while_stmt : T_WHILE T_PARENTHESES_OPEN expr T_PARENTHESES_CLOSE stmt
    for_stmt : T_FOR T_PARENTHESES_OPEN (expr)? T_SEMICOLON expr T_SEMICOLON (expr)? T_PARENTHESES_CLOSE stmt
    return_stmt : T_RETURN expr? T_SEMICOLON
    break_stmt : T_BREAK T_SEMICOLON
    print_stmt : T_PRINT T_PARENTHESES_OPEN expr (T_COMMA expr)* T_PARENTHESES_CLOSE T_SEMICOLON
    expr : i T_EQUAL expr | a
    a : a T_OR b | b
    b : b T_AND c | c
    c : c T_EQUAL_EQUAL d | c T_NOT_EQUAL d | d
    d : d T_SMALLER e | d T_SMALLER_EQUAL e | d T_BIGGER e | d T_BIGGER_EQUAL e | e
    e : e T_PLUS f | e T_MINUS f | f
    f : f T_MULT g | f T_DIVIDE g | f T_PERCENTAGE g | g
    g : T_NOT g | T_MINUS g | i
    i : i T_DOT T_ID | h T_BRACKET_OPEN expr T_BRACKET_CLOSE | i T_DOT T_ID T_PARENTHESES_OPEN actuals T_PARENTHESES_CLOSE | h
    h : T_PARENTHESES_OPEN expr T_PARENTHESES_CLOSE | atomic
    atomic : constant | T_THIS | call | T_READLINE T_PARENTHESES_OPEN T_PARENTHESES_CLOSE 
    | T_READINTEGER  T_PARENTHESES_OPEN T_PARENTHESES_CLOSE| T_NEW T_ID 
    | T_NEWARRAY T_PARENTHESES_OPEN expr T_COMMA type T_PARENTHESES_CLOSE | T_ID
    call : T_ID T_PARENTHESES_OPEN actuals T_PARENTHESES_CLOSE 
    actuals : expr (T_COMMA expr)* |
    constant : T_INTLITERAL | T_DOUBLELITERAL | T_BOOLEANLITERAL | T_STRINGLITERAL -> push_ss| T_NULL

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
    T_WHILE : "while"
    T_IF : "if"
    T_ELSE : "else"
    T_RETURN : "return"
    T_BREAK : "break"
    T_NEW : "new"
    T_NEWARRAY : "NewArray"
    T_PRINT : "Print"
    T_READINTEGER : "ReadInteger"
    T_READLINE : "ReadLine"

    //literals
    T_BOOLEANLITERAL : /(false|true)/
    T_STRINGLITERAL : /".*"/
    T_INTLITERAL : /((0[xX](\d|[a-f|A-F])+)|\d+)/
    T_DOUBLELITERAL.100 : /\d+\.\d*([eE][+-]?\d+)?/
    T_ID : /[a-z|A-Z]\w{0,30}/

    //comments
    INLINE_COMMENT : "//" /[^\\n]*/ "\\n"
    COMMENT : "/*" /[^\\n]*/ "*/"

    //punctuations
    T_PLUS : "+"
    T_MINUS : "-"
    T_MULT : "*"
    T_DIVIDE : "/"
    T_PERCENTAGE : "%"
    T_SMALLER_EQUAL : "<="
    T_BIGGER_EQUAL : ">="
    T_SMALLER : "<"
    T_BIGGER : ">"
    T_EQUAL_EQUAL : "=="
    T_NOT_EQUAL : "!="
    T_EQUAL : "="
    T_AND : "&&"
    T_OR : "||"
    T_NOT : "!"
    T_SEMICOLON : ";"
    T_COMMA : ","
    T_DOT : "."
    T_ROUND_BRACKET_OPEN : /\{/
    T_ROUND_BRACKET_CLOSE : /\}/
    T_PARENTHESES_CLOSE : /\)/
    T_PARENTHESES_OPEN : /\(/
    T_BRACKET_CLOSE : /\]/
    T_BRACKET_OPEN : /\[/
    T_COLON : ":"

    //ignores
    %import common.WS
    %ignore WS
    %ignore COMMENT
    %ignore INLINE_COMMENT
'''
