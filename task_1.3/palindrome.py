inp = input("Введите строку: ")
print("Вы ввели", inp)
inp_clean = inp.replace(" ", "")
print(inp)
rev = inp[::-1]
rev_clean = rev.replace(" ", "")
print(rev)
if (inp_clean == rev_clean):
    print(f"{inp} = {rev} - палиндром!")
else:
    print(f"{inp} != {rev} - не палиндром.")