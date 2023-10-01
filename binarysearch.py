def binarysearch(arr,n,key):
    l,h=1,n-1
    while(l<=h):
        mid=(h+l)//2
        if(arr[mid]==key):
            return mid
        elif(arr[mid]<key):
            h=mid-1
        else:
            l=mid+1
    return "not found"

arr=[3,6,8,9,7,4,2]
n=len(arr)
print(binarysearch(arr,n,1))
