# interpolation search >>>>>>> binary search
#o(n)>o(log(n))>o(log(log(n))
def interpilation(a,k):
    low=0
    high=len(a)-1

    while a[high]!=a[low] and a[low]<=k<=a[high]:

        mid = low + (k-a[low])*(high-low)//(a[high]-a[low])

        if a[mid]==k:
            print(mid)
            return
        elif k>a[mid]:
            low=mid+1
        else:
            high=mid-1
    print("no element found")






array = [2, 5, 7, 8, 9, 11, 26]
key = 26
interpilation(array,key)
