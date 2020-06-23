#!python3
#Extract the phone number from the lines of text


import re
phoneNumRegex = re.compile(r'\d\d\d\d\d\d\d\d\d\d')
print('Enter the text to search: ')
text=input()
mo = phoneNumRegex.search(text)
print('The phone number is : ' + mo.group())
