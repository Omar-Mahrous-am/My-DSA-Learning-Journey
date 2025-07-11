#Array And Hashing Problems 

#1.Conatin_Dublicates
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_set=set()
        for i in nums:
            if i in check_set:
                return True
            check_set.add(i)
        return False
nums = [1, 2, 3, 4, 1]

test=Solution()
print(test.hasDuplicate(nums))



#2.Valid_Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len (s)!=len(t):
            return False
        s_map={}
        t_map={}

        for char in s:
            s_map[char]=s_map.get(char,0) +1
        for char in t:
            t_map[char]=t_map.get(char,0) +1

        return s_map==t_map

s = "racecar"
t = "carrace"
test=Solution()
print(test.isAnagram(s,t))

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check_map={}
        diff=0
        for i,n in enumerate(nums):
            diff=target-n
            
            if diff in check_map:
                return [check_map[diff],i]
            check_map[n]=i
        return []

test=Solution()
print(test.twoSum([3,4,5,6],7))

#Group_Anagram
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord("a")]+=1

            sol[tuple(count)].append(s)
        return list(sol.values())

test= Solution()
print(test.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
