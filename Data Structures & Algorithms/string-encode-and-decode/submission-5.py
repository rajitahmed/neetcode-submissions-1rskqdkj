class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        else:
            word = ""
            for s in strs:
                word += f"{len(s)}#{s}"
            return word
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        else:
            words = []
            i = 0
            while i < len(s):
                j = i
                while s[j] != '#':
                    j += 1
                word_len = int(s[i:j])
                start = j + 1
                end = start + word_len
                words.append(s[start:end])
                i = end
            return words