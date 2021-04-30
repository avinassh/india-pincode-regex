import os
import re

from pincode.regex_codes import regex_string

regex = []
lines = regex_string.split()
for line in lines:
    l = '^' + line[1:-1] + '$'
    regex.append(re.compile(l))

class Pincode:
    @staticmethod
    def validate(code):
        for r in regex:
            if r.match(code) != None:
                return True
        return False
