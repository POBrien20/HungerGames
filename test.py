s = "epsiuhfsdsoihjewqlnerwqerij"
d = dict()
for c in s:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1
##print(d)
##for key in d:
##    print(d.get(key, 0))
def getMins(d):
    c = d.values()
    print(min(c))
    print(c)
    e = d.iteritems()
    print(e)
getMins(d)
