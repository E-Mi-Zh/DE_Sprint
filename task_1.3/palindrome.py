inp = input("Введите строку: ")
print("Вы ввели", inp)
inp_clean = inp.replace(" ", "")
print(inp)
rev = inp[::-1]
rev_clean = rev.replace(" ", "")
print(rev)
if (inp_clean == rev_clean):
    print(True)
else:
    print(False)
