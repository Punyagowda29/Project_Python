def binarysearch(arr,l,h,key):
    if h>=l:
        mid=(h+l)//2
        if(arr[mid]==key):
            return mid
        elif(arr[mid]<key):
            return binarysearch(arr,mid+1,h,key)
        else:
            return binarysearch(arr,l,mid-1,key)

arr=[3,6,8,9,7,4,2]
print(binarysearch(arr,0,len(arr)-1,8))
