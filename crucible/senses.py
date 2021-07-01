

class Sense:
    def __init__(self, title, value):
        self.title = title
        self.desc = value

    def __str__(self):
        return "{} {}".format(self.title, self.desc)