# script to remove parathesis in python
import pandas
import os

list_of_script = []
stringlol = ''
remove_para = []
with open("C:\\Users\\super\\Desktop\\Discord_Messages\\conan.txt", "r") as reader:
    for line in reader.readlines():
        list_of_script.append(line)


    def listToString(s):

        # initialize an empty string
        str1 = ""

        # traverse in the string
        for ele in s:
            str1 += ele

            # return string
        return str1

    def parentheses_text_remove(text):
            # keep removing pairs of '(' and ')' as long as there are any
            while '(' in text and ')' in text:
                for i, character in enumerate(text):
                    # step through the characters until you encounter a closing bracket
                    if character == ')':
                        j = i
                        # walk back until you encounter an opening bracket
                        while text[j] != '(':
                            j -= 1
                        # strip out the part in brackets
                        text = text[:j] + text[i + 1:]
                        break
            return text

#conversion to list from string

stufflol = listToString(list_of_script)
usable_script = parentheses_text_remove(stufflol)

with open("C:\\Users\\super\\Desktop\\Discord_Messages\\conan1.txt", "w") as f:
    for i in usable_script:
        f.write(i)
