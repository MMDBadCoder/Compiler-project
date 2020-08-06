class SymbolTableItem:
    def __init__(self, type, name, customId, value):
        self.type = type
        self.name = name
        self.value = value
        # if type == 'int' or type == 'bool':
        #     self.value = 0
        # elif type == 'string':
        #     self.value = ' '
        # else:
        #     self.value = None
        self.id = 'id{}'.format(customId)

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.type, self.name, self.value, self.id)
