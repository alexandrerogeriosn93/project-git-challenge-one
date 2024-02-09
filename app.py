import random

list_randon = sorted([random.randrange(1, 100, 1) for _ in range(10)])
list_even = [int(x) for x in list_randon if x % 2 == 0]
list_odd = [int(x) for x in list_randon if x % 2 != 0]
