# Find the average of largest and smallest numbers in an unsorted integer array?
# Eg. 
# Input Case 1:  
# input: [1, 4, 3, 2]
# output:  2.5
# solution : average = (1+4)/2 =>5/2 => 2.5

# input: [1, 4, 3, 4]
# output:  3

def average_of_largest_and_smallest(arr):
    arr.sort()
    smallest = arr[0]
    largest = arr[-1]
    average = (smallest + largest) / 2
    return average
arr1 = [1, 4, 3, 2]

print(average_of_largest_and_smallest(arr1)) 

