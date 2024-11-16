#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters. 
# You may introduce private/protected utility methods though.
class ProfanityFilter:



    def __init__(self, keywords, template):
        self.wordList=sorted([word.lower() for word in keywords], key=len, reverse=True)
        self.replacement=template

    def filter(self, msg):
        for word in self.wordList:
            while word in msg.lower():
                x=msg.lower().find(word)
                msg = msg[0:x] + self.create_replacement(word) +  msg[x + len(word):]

                #msg = msg.replace(word.lower(), self.create_replacement(word))
        return msg

    def create_replacement(self, word):
        s = self.replacement * len(word)
        return s[0:len(word)]

# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["ducK", "shot", "batch", "Mastard"], "?#$")
    offensive_msg = "abc defghi dUck mastARDius jklmno"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno
