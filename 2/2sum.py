
l=[]
with open('2Sum.txt') as file:
    for index,line in enumerate(file):
        i=int(line)
        l.append(i)
print len(l)
sum=0
for t in range(-10000,10001):
    for x in l:
        if l.count(t-x)!=0:
            sum=sum+1
            print sum
            break
print sum
