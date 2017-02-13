import dis

def foo():
    pass
    x = 3
    return True

text1 = '"- I like Python! Do you?\n- Yes, very much."'
text2 = "\"I don't want to go home.\""
text3 = '"He said: "No, I don\'t know""'
text4 = "\"You canuse # to comment a line.\""
print text1
print text2
print text3
print text4
print text1[::-1]

print "11111".replace("1", "2", 2);

a, b, c, d = 3, 3.2, "John Smith", "Learn"

print a + b
print str(a) + c
print c + d
print str(b) + c
print a * 3
print d * 3
print d

l1 = ['abcd', 786, 2.23, 'john', 70.2]
print l1
print l1[0]
print l1[2:]
l1 = l1*2
print l1

l2 = ['second', '123']

l3 = l1 + l2
l1[1] += 1
print l1
print l3

l4 = [] + l2
l2[0] = 'third'
print l4

l5 = [1, 2, 3, 4]
l5[:2] = '1', '2'
l5.insert(1, [7,7,7,7,7,7])
l5.insert(0, l5[:]);
print l5
l5 = []

l6 = []
l6.extend(l1)
l6.extend(l2)
l6.extend(l5)
l1[0] = '1'
print l6

l1.sort()
l2.sort()
l3.sort()

print len(l1)
print len(l2)
print len(l3)

l = [1, 2, 3, 4]
l[:0] = l
print l