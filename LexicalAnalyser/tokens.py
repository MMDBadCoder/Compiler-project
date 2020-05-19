undefined_token = 'UNDEFINED_TOKEN'

tokens = [
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
        'pattern': '[0-9]+'
    },
    {
        'token': 'T_CLASS',
        'pattern': 'class'
    },
    {
        'token': 'T_IF',
        'pattern': 'if'
    },
    {
        'token': 'I_WHILE',
        'pattern': 'while'
    },
    {
        'token': 'T_{',
        'pattern': '{'
    },
    {
        'token': 'T_}',
        'pattern': '}'
    },
    {
        'token': 'T_)',
        'pattern': '[)]'
    },
    {
        'token': 'T_(',
        'pattern': '[(]'
    },
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
        'token': 'T_;',
        'pattern': ';'
    },
    {
        'token': 'T_==',
        'pattern': '=='
    },
    {
        'token': 'T_ID',
        'pattern': '[a-z|A-Z][0-9|a-z|A-Z]*'
    },
]
