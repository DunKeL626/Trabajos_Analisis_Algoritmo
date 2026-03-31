#Tiempo: O(n²)
#Espacio: O(n)
def lengthOfLIS(nums: list[int]) -> int:
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(lengthOfLIS([10,9,2,5,3,7,101,18])) #poner aca el TEST CASE
    #[10,9,2,5,3,7,101,18] TEST CASE 2
    #[7,7,7,7,7,7,7] TEST CASE 3