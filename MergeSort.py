# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr1,arr2):
    res = []
    arr2 = sorted(arr2)
    print(arr2)
    for x in arr1:
        low = 0
        high = len(arr2) - 1
        mid = 0
        
        
        if x>arr2[-1]:
            res.append(len(arr2))
        else:
            
            while low <= high:
         
                mid = (high + low) // 2
         
                # If x is greater, ignore left half
                if arr2[mid] < x:
                    low = mid + 1
                # If x is smaller, ignore right half
                elif arr2[mid] > x:
                    high = mid - 1
                # means x is present at mid
                else:
                    mid''
                    break
 
    # If we reach here, then the element was not present
            res.append(mid)
    return res
 
 
# Test array
arr1 = [3,41,100]
arr2 = [ 2, 3, 4, 44, 40, 24, 18]
 
# Function call
result = binary_search(arr1,arr2)

print(result)