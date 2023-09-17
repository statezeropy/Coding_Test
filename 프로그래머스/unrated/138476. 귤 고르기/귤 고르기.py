from collections import Counter

def solution(k, tangerine):
    tangerine_count = Counter(tangerine)
    sorted_counts = sorted(tangerine_count.values(), reverse=True)
    
    count = 0
    for count_val in sorted_counts:
        k -= count_val
        count += 1
        if k <= 0:
            return count
