from collections import Counter
#Pythonic version- Counter() is a dictionary, used for counting items in iterables
class Solution:    #works for str,List,most_common val's,many other methods
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)