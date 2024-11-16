#!/usr/bin/env python3

# The signatures of this class and its task methods are required for the automated grading to work.
# You must not change the names or the list of parameters.
# You may introduce grading/protected utility methods though.
class Publication:

    def __init__(self, authors: list, title: str, year: int):
        self.__authors = authors
        self.__title = title
        self.__year = year

    def get_authors(self):
        return self.__authors.copy()

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    # To implement the required functionality, you will also have to implement several
    # of the special functions that typically include a double underscore.
    # We've provided a starting point for one of the operators:
    def __lt__(self, other): #less than
        if not isinstance(other, Publication):
            return NotImplemented
        if sorted(self.__authors) != sorted(other.get_authors()):
            return sorted(self.__authors) < sorted(other.get_authors())
        elif self.__title != other.get_title():
            return self.__title < other.get_title()
        return self.__year < other.get_year()

    def __le__(self, other): #less equal
        if not isinstance(other, Publication):
            return NotImplemented
        if sorted(self.__authors) != sorted(other.get_authors()):
            return sorted(self.__authors) <= sorted(other.get_authors())
        elif self.__title != other.get_title():
            return self.__title <= other.get_title()
        return self.__year <= other.get_year()

    def __gt__(self, other): #greater than
        if not isinstance(other, Publication):
            return NotImplemented
        if sorted(self.__authors) != sorted(other.get_authors()):
            return sorted(self.__authors) > sorted(other.get_authors())
        elif self.__title != other.get_title():
            return self.__title > other.get_title()
        return self.__year > other.get_year()

    def __ge__(self, other): #greater equal
        if not isinstance(other, Publication):
            return NotImplemented
        if sorted(self.__authors) != sorted(other.get_authors()):
            return sorted(self.__authors) >= sorted(other.get_authors())
        elif self.__title != other.get_title():
            return self.__title >= other.get_title()
        return self.__year >= other.get_year()

    def __eq__(self, other): # equal
        if not isinstance(other, Publication):
            return NotImplemented
        return sorted(self.__authors) == sorted(other.get_authors()) and self.__title == other.get_title() and self.__year == other.get_year()

#    def __ne__(self, other): # not equal only used if class inherits from builtin
#        pass

    def __str__(self):
        mystr = f"Publication({self.__authors}, \"{self.__title}\", {self.__year})"
        return str(mystr).replace("'", '"')

    def __repr__(self):
        mystr = f"Publication({self.__authors}, \"{self.__title}\", {self.__year})"
        return str(mystr).replace("'", '"')


    def __hash__(self):
        return hash(tuple([tuple(self.__authors), self.__title, self.__year]))



# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    references = [
        Publication(["Gamma", "Helm", "Johnson", "Vlissides"], "Design Patterns", 1994),
        Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
        Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    ]

    p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    s = "Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"
    print(str(p))
    print(s)
    print(str(p) == s)

    p1 = Publication(["A"], "B", 1234)
    p2 = Publication(["A"], "B", 1234)
    p3 = Publication(["B"], "C", 2345)
    print(p1 == p2)  # True
    print(p2 == p3)  # False

    sales = {
        p1: 273,
        p2: 398,
    }

print(sales)