from lark import Transformer
class CodeGen(Transformer):
    def push_ss(self, args):
        print(args[0].value)
