
graph={}
graphT={}
reverseOrder=[]
def read(filename):
    with open(filename) as file:
        for index, line in enumerate(file):
            edge=[int(n) for n in line.split()]
            if edge[0] not in graph:
                graph[edge[0]]=[]
            if edge[1] not in graphT:
                graphT[edge[1]]=[]
            graph[edge[0]].append(edge[1])
            graphT[edge[1]].append(edge[0])

def dfs(g,v):
    stack=[]
    stack.append(v)
    marked[v]=True
    while len(stack)!=0:
        top=stack[len(stack)-1]
        adj=g.get(top)
        
            
        flag=False
        if adj!=None:
            for i in adj:
            
                if not marked[i]:
                    stack.append(i)
                    marked[i]=True
                    #print i
                    flag=True
                    break
        if flag==False:
            reverseOrder.append(stack.pop())

def dfs1(g,v):
    stack=[]
    stack.append(v)
    marked[v]=True
    scc[count]=0
    while len(stack)!=0:
        top=stack[len(stack)-1]
        adj=g.get(top)
        
            
        flag=False
        if adj!=None:
            for i in adj:
            
                if not marked[i]:
                    stack.append(i)
                    #print i
                    marked[i]=True
                    flag=True
                    break
        if flag==False:
            stack.pop()
            scc[count]+=1
read('SCC.txt')
#print graph
marked=[]
leng=875714
for i in range(0,leng+1):
    marked.append(False)
#print len(marked)
#print 'graphT'
#print graphT
#print 'keys'
#print graphT.keys()
#print 'dfs--- '
for i in graphT.keys():
    if not marked[i]:
        dfs(graphT,i)
        
reverseOrder.reverse()
marked=[]

for i in range(0,leng+1):
    marked.append(False)
count=0
scc={}
for i in reverseOrder:
    if not marked[i]:
        dfs1(graph,i)
        count+=1
#print scc
sl=scc.values()
#print sl
sl.sort(reverse=True)
print sl[0],sl[1],sl[2],sl[3],sl[4]
