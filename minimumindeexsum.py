

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = {}
        dict2 = {}
        for i in range(len(list1)):
            dict1[list1[i]] = i
        for i in range(len(list2)):
            dict2[list2[i]] = i
        min_sum = float('inf')
        ans = []
        for key in dict1:
            if key in dict2:
                sum_indices = dict1[key] + dict2[key]
                if sum_indices < min_sum:
                    min_sum = sum_indices
                    ans = [key]
                elif sum_indices == min_sum:
                    ans.append(key)
        return ans