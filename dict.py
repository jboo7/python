d1 = {}
d1['one'] = 'First'
d1[2] = 'Second'
d1[3] = 3
print d1.keys()
print d1.values()
for k in sorted(d1.keys()):
    print ("d1[%s]=[%s]") % (k, d1[k])

