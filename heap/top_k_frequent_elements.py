class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        inverse_freqs = defaultdict(list)
        for key in freqs:
            inverse_freqs[freqs[key]].append(key)
        top_freqs = list(inverse_freqs.keys())
        top_freqs.sort(reverse=True)
        print(top_freqs)
        print(inverse_freqs)
        result = []
        for freq in top_freqs:
            while k:
                if inverse_freqs[freq]:
                    result.append(inverse_freqs[freq].pop())
                    k -= 1
                else:
                    break
        return result

        