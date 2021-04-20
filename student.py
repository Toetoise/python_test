class Student:
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score

    def __str__(self):
        return "%s,%s,%s" % (self.id, self.name, self.score)
