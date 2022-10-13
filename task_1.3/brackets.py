brackets = {"[":0, "]": 0, "{":0, "}":0, "(":0, ")":0}
x = input("Введите строку из скобок: ")
for c in x:
    brackets[c] += 1
if (brackets["["] == brackets["]"] and brackets["{"] == brackets["}"] and brackets["("] == brackets[")"]):
    print(True)
else:
    print(False)
