from lark import Lark
from SyntaxAnalyser.grammar import grammar
from CodeGen.codeGeneraotor import CodeGen

parser = Lark(grammar, parser="lalr", transformer=CodeGen(), debug=True)
