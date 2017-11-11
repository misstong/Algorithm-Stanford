import heapq

count=0
low=0
high=0
l=[]
h=[]
sum=0
with open ('Median.txt') as file:
    for index,line in enumerate(file):
        i=int(line)
        if count==0:
            heapq.heappush(l,-i)
            low=low+1
            count=count+1
            sum=sum+i
            continue
        m=-l[0]
        #print m
        if i<m:
            #print 'insert l'+str(i)
            heapq.heappush(l,-i)
            low=low+1
            if low-high>1:
                n=-heapq.heappop(l)
                low=low-1
                heapq.heappush(h,n)
                high=high+1
        else:
           # print 'insert h'+str(i)
            heapq.heappush(h,i)
            high=high+1
            if high-low>1:
                n=heapq.heappop(h)
                high=high-1
                heapq.heappush(l,-n)
                low=low+1       
        count=count+1
        if count%2==0:
            #print str(count)+" median "+str(-l[0])
            sum=sum+(-l[0])
        else:
            if low==(count+1)/2:
               #print str(count)+" median "+str(-l[0])
               sum=sum+(-l[0])
            else:
                #print str(count)+" median "+str(h[0])
                sum=sum+h[0]
#print l
#print h
print sum%10000
