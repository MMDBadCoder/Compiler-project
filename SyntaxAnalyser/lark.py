from lark import Lark
from SyntaxAnalyser.grammar import grammar
from CodeGen.codeGeneraotor import push_ss

parser = Lark(grammar, parser="lalr", transformer=push_ss(), debug=True)
