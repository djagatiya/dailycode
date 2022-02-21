from typing import List
import math

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_map = {}
        for i, n in enumerate(nums):
            ls = num_map.get(n, [])
            ls.append(i)
            num_map[n] = ls
        
        for n, id_list in num_map.items():
            second_num = target - n
            second_num_index = num_map.get(second_num)

            if second_num_index is None:
                continue

            result = set([*id_list, *second_num_index])

            if len(result) == 2:
                return list(result)
        
        return None

if __name__ == "__main__":
    
    assert Solution().twoSum([2,7,11,15], 9) == [0,1]
    assert Solution().twoSum([3,2,4], 6) == [1,2]
    assert Solution().twoSum([3,3], 6) == [0,1]
    assert Solution().twoSum([3,3], 6) == [0,1]
    assert Solution().twoSum([-1,-2,-3,-4,-5], -8) == [2,4]