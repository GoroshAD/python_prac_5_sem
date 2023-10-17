dictionary = lambda text : " ".join({i: 0 for i in text}.keys())

print(dictionary(input().split()))
