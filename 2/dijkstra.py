
graph={}
def read(filename):
    with open(filename) as file:
        for index,line in enumerate(file):
            nodes=line.split()
            v=int(nodes[0])
            graph[v]=[]
            for i in range(1,len(nodes)):
                #print nodes[i].split(',')
                e=[int(num) for num in nodes[i].split(',')]
                #print e
                graph[v].append(e)
def minDistance(q):
    m=1000000
    n=1
    pos=0
    for i in q.keys():
        if q[i]<m:
            m=q[i]
            n=i
            
    return n

read('dijkstraData.txt')
#print graph

dist=[]
size=len(graph)
for i in range(0,size+1):
    dist.append(1000000)
dist[1]=0
queue={}
s=[]
s.append(1)
adj=graph[1]
for i in adj:
    dist[i[0]]=i[1]
    queue[i[0]]=i[1]
while len(s)<size:
    n=minDistance(queue)
    del queue[n]
    s.append(n)
    adj=graph[n]
    for i in adj:
        if dist[i[0]]>dist[n]+i[1]:
            dist[i[0]]=dist[n]+i[1]
            queue[i[0]]=dist[i[0]]

print dist[7],dist[37],dist[59],dist[82],dist[99],dist[115],dist[133],dist[165],dist[188],dist[197]
