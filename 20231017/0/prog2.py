import string as string
str = input().lower()
vow = set(['e', 'y', 'u', 'i', 'o', 'a'])
con = set(string.ascii_lowercase) - vow
print("vowels:", len(vow & set(str))) 
print("consonants:", len(set(str) & con))
