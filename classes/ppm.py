class PPM:
    id = 'P3'
    def __init__(self, size1, size2, comp):
        self.size1 = size1
        self.size2 = size2
        self.comp = comp

    def show(self):
        print(self.id)
        print(self.size1, self.size2)
        print(self.comp)