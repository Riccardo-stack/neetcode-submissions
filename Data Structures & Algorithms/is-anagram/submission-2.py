class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1 = []
        arr2 = []

        for i in range(26):
            arr1.append(0)
            arr2.append(0)

        for i in s:
            arr1[ord(i)-97] += 1
        
        for i in t:
            arr2[ord(i)-97] += 1
        
        if arr1 == arr2:
            return True
        return False