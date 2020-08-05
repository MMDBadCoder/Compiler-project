class symbolTableItem:
    def __init__(self, type, name, value):
        self.type = type
        self.name = name
        self.value = value
        # self.id = id

    def __str__(self):
        return '{}, {}, {}'.format(self.type, self.name, self.value)
