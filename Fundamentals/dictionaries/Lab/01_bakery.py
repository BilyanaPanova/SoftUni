bakery = input().split()
keys, values = bakery[::2], [int(x)for x in bakery[1::2]]
dict_bakery = dict(zip(keys, values))
print(dict_bakery)
