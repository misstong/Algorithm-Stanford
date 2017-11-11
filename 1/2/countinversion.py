def merge_list(left,right):
    result=[]
    i=j=count=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
            count+=len(left)-i
    result+=left[i:]
    result+=right[j:]
    return result,count

def sort_and_count(array):
    if len(array)<2:
        return array,0
    middle=len(array)/2
    left,inv_left=sort_and_count(array[0:middle])
    right,inv_right=sort_and_count(array[middle:])
    merged,count=merge_list(left,right)
    return merged,inv_left+inv_right+count

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

#array = [2,3,1,4,5]
#array=[5,4,3,2,1]
array=read("IntegerArray.txt")
#array=read("test.txt")

merge_array,inversions = sort_and_count(array)
#print 'Start with array: %s;\nSorted array:     %s;\nInversions: %s.'%(array,merge_array,inversions)
print inversions
