class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n =len(numbers)
        for i in range(n):
            key = numbers[i]
            find = target - key
            start = i+1
            end = n - 1
            while start <= end:
                mid = (start+end)//2
                if numbers[mid] == find:
                    return [i+1, mid+1]
                    break
                else:
                    if find > numbers[mid]:
                        start = mid + 1
                    else:
                        end = mid - 1

