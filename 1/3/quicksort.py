def partition(a,l,h):
    #pivot = first element
    pivot=a[l]
    i=l
    for j in range(l+1,h+1):
        if a[j]<=pivot:
            i=i+1
            a[i],a[j]=a[j],a[i]
    a[i],a[l]=a[l],a[i]
    return i

def partition2(a,l,h):
    #pivot = last element
    pivot=a[h]
    a[h],a[l]=a[l],a[h]  
    i=l
    for j in range(l+1,h+1):
        if a[j]<=pivot:
            i=i+1
            a[i],a[j]=a[j],a[i]
    a[i],a[l]=a[l],a[i]
    return i

def partition3(a,l,h):
    #pivot = median element
    p=median(a,l,h)
    pivot=a[p]
    a[p],a[l]=a[l],a[p]
    i=l
    for j in range(l+1,h+1):
        if a[j]<=pivot:
            i=i+1
            a[i],a[j]=a[j],a[i]
    a[i],a[l]=a[l],a[i]
    return i

def median(a,low,high):
    l=a[low]
    h=a[high]
    size=high-low+1
    #print size
    if size%2==0:
        middle=low+size/2-1
        m=a[middle]
        
    else:
        middle=low+size/2
        m=a[middle]
    #print m   
    if l<h:
        if m<l:
            return low;
        elif m<h:
            return middle;
        else:
            return high;
    else:
        if m<h:
            return high
        elif m<l:
            return middle
        else:
            return low
            
def quicksort(a,l,h):
    if l<h: 
        j=partition3(a,l,h)
        m_left=quicksort(a,l,j-1)
        m_right=quicksort(a,j+1,h)
        return m_left+m_right+h-l
    return 0
      


def read(name):
    arrayFile=open(name)
    arrayContent=arrayFile.read()
    #print arrayContent
    arrayFile.close()
    array=arrayContent.split('\n')
    #print array
    result=[]
    for i in array:
        result.append(int(i))
    return result        



array=read("QuickSort.txt")
#array=read("10.txt")
sum=quicksort(array,0,len(array)-1)
print sum


