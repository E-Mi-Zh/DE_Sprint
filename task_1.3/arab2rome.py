digits = {1:"I", 4:"IV", 5:"V", 9:"IX", 10: "X", 40:"XL", 50: "L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
x = int(input("Введите арабское число от 1 до 2000: "))
res = ""
for k in reversed(list(digits.keys())):
    #print("---------------")
    #print(k, x)
    while (x >= k):
        x = x - k
        res = res + digits[k]
        #print("ret dig")
        #print(k)
        #print(x)
        #print(digits[k])
print(res)