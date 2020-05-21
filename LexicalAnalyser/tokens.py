undefined_token = 'UNDEFINED_TOKEN'
comment_token = 'T_COMMENT'

tokens = [
    # key words
    {
        'token': 'T_VOID',
        'pattern': 'void'
    },
    {
        'token': 'T_INT',
        'pattern': 'int'
    },
    {
        'token': 'T_BOOL',
        'pattern': 'bool'
    },
    {
        'token': 'T_DOUBLE',
        'pattern': 'double'
    },
    {
        'token': 'T_STRING',
        'pattern': 'string'
    },
    {
        'token': 'T_CLASS',
        'pattern': 'class'
    },
    {
        'token': 'T_INTERFACE',
        'pattern': 'interface'
    },
    {
        'token': 'T_NULL',
        'pattern': 'null'
    },
    {
        'token': 'T_EXTENDS',
        'pattern': 'extends'
    },
    {
        'token': 'T_IMPLEMENTS',
        'pattern': 'implements'
    },
    {
        'token': 'T_FOR',
        'pattern': 'for'
    },
    {
        'token': 'I_WHILE',
        'pattern': 'while'
    },
    {
        'token': 'T_IF',
        'pattern': 'if'
    }, {
        'token': 'I_ELSE',
        'pattern': 'else'
    },
    {
        'token': 'I_RETURN',
        'pattern': 'return'
    },
    {
        'token': 'I_BREAK',
        'pattern': 'break'
    },
    {
        'token': 'I_NEW',
        'pattern': 'new'
    },
    {
        'token': 'I_NEWARRAY',
        'pattern': 'NewArray'
    },
    {
        'token': 'I_PRINT',
        'pattern': 'print'
    },
    {
        'token': 'I_READINTEGER',
        'pattern': 'ReadInteger'
    },
    {
        'token': 'I_READLINE',
        'pattern': 'ReadLine'
    },
    {
        'token': 'T_BOOLEANLITERAL',
        'pattern': '(false|true) '
    },
    {
        'token': 'T_STRINGLITERAL',
        'pattern': '".*"'
    },
    {
        'token': 'T_INTEGERLITERAL',
        'pattern': '\d+'
    },
    {
        'token': 'T_DOUBLELITERAL',
        'pattern': '\d+\.\d*([eE][+-]?\d+)?'
    },
    {
        'token': 'T_ID',
        'pattern': '[a-z|A-Z]{0,30}\w'
    },
    # operands and punctuations
    {
        'token': 'T_+',
        'pattern': '\+'
    },
    {
        'token': 'T_-',
        'pattern': '\-'
    },
    {
        'token': 'T_*',
        'pattern': '\*'
    },
    {
        'token': 'T_/',
        'pattern': '/'
    },
    {
        'token': 'T_%',
        'pattern': '%'
    },
    {
        'token': 'T_<',
        'pattern': '<'
    },
    {
        'token': 'T_<=',
        'pattern': '<='
    },
    {
        'token': 'T_>',
        'pattern': '>'
    },
    {
        'token': 'T_>=',
        'pattern': '>='
    },
    {
        'token': 'T_=',
        'pattern': '='
    },
    {
        'token': 'T_==',
        'pattern': '=='
    },
    {
        'token': 'T_!=',
        'pattern': '!='
    },
    {
        'token': 'T_&&',
        'pattern': '&&'
    },
    {
        'token': 'T_||',
        'pattern': '\|\|'
    },
    {
        'token': 'T_!',
        'pattern': '!'
    },
    {
        'token': 'T_;',
        'pattern': ';'
    },
    {
        'token': 'T_,',
        'pattern': ','
    },
    {
        'token': 'T_.',
        'pattern': '\.'
    },
    {
        'token': 'T_{',
        'pattern': '\{'
    },
    {
        'token': 'T_}',
        'pattern': '\}'
    },
    {
        'token': 'T_)',
        'pattern': '\)'
    },
    {
        'token': 'T_(',
        'pattern': '\('
    },
    {
        'token': 'T_]',
        'pattern': '\]'
    },
    {
        'token': 'T_[',
        'pattern': '\['
    },
    {
        'token': 'T_:',
        'pattern': ':'
    },
    {
        'token': comment_token,
        'pattern': '\/\/.*\n',
    },
    {
        'token': comment_token,
        'pattern': '\/\*(.*\n*)*\*\/'
    },
    {
        'token': undefined_token,
        'pattern': '[a-z|A-Z]{30,0}\w'
    }
]
