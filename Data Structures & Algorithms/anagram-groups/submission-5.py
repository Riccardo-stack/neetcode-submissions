class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # I'll create a dictionary, containin 26 slots long arrays,
        # that count how many times a letter appears.
        # for each word I'll check if that array is already in the
        # dictionary or not
        anagrams = {}

        count = [0 for _ in range(26)]
        # if slow, I might create the arr here, and create a copy inside
        for i in strs:
            count1 = count.copy()
            for j in i:
                count1[ord(j)-97] += 1
            if tuple(count1) in anagrams:
                anagrams[tuple(count1)].append(i)
            else:
                anagrams[tuple(count1)] = [i]

        result = []
        for i in anagrams:
            result.append(anagrams[i])
        return result