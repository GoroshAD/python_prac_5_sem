from itertools import dropwhile, islice, accumulate, count

print(list(islice(dropwhile(lambda x : x <= 1.6 , accumulate(1/i**2 for i in count(1))), 10)))
