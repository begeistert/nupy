from pandas import DataFrame


class Iterations(DataFrame):

    def __init__(self, data, columns, root):
        super().__init__(data, columns)
        self.root = root

    def getRoot(self):
        return self.root
