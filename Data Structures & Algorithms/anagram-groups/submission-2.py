from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map: tuple of 26 character counts -> list of original strings
        res = defaultdict(list)
        
        for s in strs:
            # Create a fixed-size array of 26 zeroes
            count = [0] * 26 
            
            for char in s:
                # Map 'a' to index 0, 'b' to 1, ..., 'z' to 25
                count[ord(char) - ord('a')] += 1
                
            # Lists are mutable and can't be dictionary keys, so convert to tuple
            res[tuple(count)].append(s)
            
        return list(res.values())