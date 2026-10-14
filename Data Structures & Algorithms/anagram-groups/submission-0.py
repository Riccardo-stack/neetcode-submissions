class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        sol = []

        for string in strs:
            anagram = [0 for _ in range(26)]
            for letter in string:
                anagram[-97 + ord(letter)] += 1
            anagram = tuple(anagram)
            
            if anagram in anagrams:
                anagrams[anagram].append(string)
            else:
                anagrams[anagram] = [string]
        

        for i in anagrams:
            sol.append(anagrams[i])
        
        return sol