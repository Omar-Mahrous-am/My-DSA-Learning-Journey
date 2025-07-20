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


#3.two sums

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

#4.Group_Anagram
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


#5.Top_k_frequent_nums
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        #bucket_sorting_with_a_trick

        res_list = [[] for _ in range(len(nums) + 1)]
        for value, freq in hash_map.items():
            res_list[freq].append(value)

        res = []
        for i in range(len(nums), 0, -1):  # <- fixed this
            for num in res_list[i]:    #it skips the empty lists
                res.append(num)
                if len(res) == k:
                    return res
test = Solution()
print(test.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(test.topKFrequent([4, 5, 6, 7], 2))

#6.Encode and Decode Strings
class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for string in strs:
            s+=str(len(string))+"#"+string
        return s
        

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i <len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            res.append(s[j+1:j+1+length])
            i=j+1+length
        return res
test=Solution()

secret_string=test.encode(["neet","code","love","you"])

print(secret_string)

original_string=test.decode(secret_string)


#7.Product of Array Except Self 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)


        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]


        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]

        return res


sol = Solution()
nums = [1, 2, 3, 4]
result = sol.productExceptSelf(nums)
print(result)

#8.Valid Soduku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_set=collections.defaultdict(set)
        cols_set=collections.defaultdict(set)
        squares_set=collections.defaultdict(set)


        for r in range(9):
            for c in range(9):
                if board[r][c] ==".":
                    continue
                if (board[r][c] in rows_set[r] or
                 board[r][c] in cols_set[c] or 
                 board[r][c] in squares_set[(r//3,c//3)] ):
                    return False
                rows_set[r].add(board[r][c])
                cols_set[c].add(board[r][c])
                squares_set[(r//3,c//3)].add(board[r][c])
        return True
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

sol = Solution()
print(sol.isValidSudoku(board))  # ✅ Expected: True


#9.Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        max_seq=0
        for num in nums:
            
            if num-1 in nums:
                continue
            current_num=num
            counter=1
            while current_num+1 in nums:
                current_num+=1
                counter+=1
            if counter >max_seq:
                max_seq=counter
        return max_seq
nums = [100, 4, 200, 1, 3, 2]
sol = Solution()
print(sol.longestConsecutive(nums)) 
        
