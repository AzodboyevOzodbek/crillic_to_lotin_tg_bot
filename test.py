from trans import to_cyrillic, to_latin
# print(to_cyrillic('assalomu alaykum'))
# print(to_latin('ассалому алайкум'))
# string.isascii()
s = input()
if s.isascii():
    print(to_cyrillic(s))
else:
    print(to_latin(s))

