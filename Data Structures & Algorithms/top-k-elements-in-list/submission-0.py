class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_e = Counter(nums).most_common(k)
        top_k = []
        for k in top_e:
            top_k.append(k[0])
        return top_k