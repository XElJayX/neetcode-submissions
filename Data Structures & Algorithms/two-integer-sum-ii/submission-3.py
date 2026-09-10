class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[]
        for i in range(len(numbers)):
            key = numbers[i]
            find = target - key
            start = i+1
            end = len(numbers) - 1
            while start <= end:
                mid = (start+end)//2
                if numbers[mid] == find:
                    res.append(i+1)
                    res.append(mid+1)
                    break
                else:
                    if find > numbers[mid]:
                        start = mid + 1
                    else:
                        end = mid - 1
        return res

