class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            w_dict = dict(Counter(s))
            other = t
        else:
            w_dict = dict(Counter(t))
            other = s
        for l in other:
            if l in w_dict:
                w_dict[l] -= 1
                if w_dict[l] == 0:
                    del w_dict[l]
        return len(w_dict) == 0