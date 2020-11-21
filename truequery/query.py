from enum import Enum

class Subject(Enum):
    GENERAL = 1
    PROGRAMMING = 2

class Query:
    def __init__(self):
        self.text = ""
        self.full_text = ""
        self.keywords = []
        self.subject = Subject.GENERAL

    def __eq__(self, other):
        if self.subject != other.subject:
            return False
        if self.text != other.text:
            return False
        if len(self.keywords) != len(other.keywords):
            return False
        for kw1, kw2 in zip(self.keywords, other.keywords):
            if kw1 != kw2:
                return False
        return True

    def __repr__(self):
        rep = self.text
        for keyword in self.keywords:
            rep += "kw:" + keyword
        return rep
