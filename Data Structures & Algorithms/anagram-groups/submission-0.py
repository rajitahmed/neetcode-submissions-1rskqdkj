class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = {}
        for word in strs:
            occur = [0] * 26
            for c in word:
                occur[ord(c) - ord('a')] += 1
            if tuple(occur) in group_dict:
                group_dict[tuple(occur)].append(word)
            else:
                group_dict[tuple(occur)] = [word]
        
        group_ananagrams = []
        for v in group_dict.values():
            group_ananagrams.append(v)
        return group_ananagrams