str = input().lower()
dict = set()
for i in range(1, len(str)) :
    if str[i].isalpha() and str[i - 1].isalpha() :
        dict.add(str[i - 1 : i + 1])
print(len(dict))
