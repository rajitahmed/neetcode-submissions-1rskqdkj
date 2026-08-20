class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        top_k = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        buckets = [[] for _ in range(len(nums) + 1)]
        for i, freq in count.items():
            buckets[freq].append(i)
        index = len(buckets) - 1
        while k > 0:
            if len(buckets[index]) == 0:
                index -= 1
                continue
            top_k.append(buckets[index].pop())
            k -= 1    
        return top_k