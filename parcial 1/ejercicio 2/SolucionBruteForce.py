#CONTAINS DUPLICATE
#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#Complejidad tiempo: O(n)
#Complejidad tiempo: O(n)
def containsDuplicate(nums: list[int]) -> bool:
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] == nums[j]:
                return True
            else:
                j+=1
    return False

print(containsDuplicate([1,1,1,3,3,4,3,2,4,2])) #poner aca el TEST CASE
    #[1,2,3,1] TEST CASE 1 - TRUE
    #[1,2,3,4] TEST CASE 2 - FALSE
    #[1,1,1,3,3,4,3,2,4,2] TEST CASE 3 - TRUE