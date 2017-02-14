a = 3
b = 'test'
c = [1, 2, 3]
d = 'none'
e = None
f = 0

print a or b
print a and b
print a and c
print a and d
print b or d
print a and e
print a and f

var = 6.0

if (isinstance(var, (int, float))):
    if (var > 5):
        print 'Yes'
    else:
        print 'No'
elif (isinstance(var, str)):
    print 'String'
else:
    print 'Other'

l1 = [1,2,3,4,5]
for i in l1:
    print i,
print

for i in range(len(l1)):
    print l1[i],
print

for i in sorted(set(range(6, 47, 2)).difference(set([20, 24, 36]))):
    print i,
print