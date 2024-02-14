def solution(nums):
    N = len(nums) // 2
    uniq = len(set(nums))
    return min(uniq, N)