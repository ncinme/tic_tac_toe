class Chart:
    def __init__(self):
        self.row1 = ['___', '___', '___']
        self.row2 = ['___', '___', '___']
        self.row3 = ['   ', '   ', '   ']

    def print_ttt(self):
        print(*self.row1, sep="|")
        print(*self.row2, sep="|")
        print(*self.row3, sep="|")


