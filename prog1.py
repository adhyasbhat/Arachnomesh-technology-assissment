# Find the counts of elements of an unsorted integer array which are equal to the average of all elements of that array.
# Ex:
# Input Case 1:  
# input: [2,2,2,2,2] 
# output:  5
# solution : 2+ 2+ 2+ 2+ 2 = 10/5 ==> 2
# it contain five 2 element

# Input Case 2:  
# input: [ 1,3,2,4,5]  
# output:  1
# solution : 1+ 3+ 2+ 4+ 5 = 15/5 ==> 3
# it contain one 3 element

def count_average_elements(arr):
    sum = 0
    count = len(arr)
    for num in arr:
        sum += num
    avg = sum / count
    result = 0
    for num in arr:
        if num == avg:
            result += 1
    return result

arr1 = [2,2,2,2,2]
print(count_average_elements(arr1))


arr2 = [1,3,2,4,5]
print(count_average_elements(arr2))  
