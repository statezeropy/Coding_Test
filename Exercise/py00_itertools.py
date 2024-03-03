from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement


from collections import Counter
import math


# counter = Counter(['A', 'B', 'C', 'A', 'B', 'C', 'A', 'A', 'B'])
# print(f"A: {counter['A']}")
# print(f"B: {counter['B']}")
# print(dict(counter))
# math.gcd()
# num1 = 21
# num2 = 14
# print(math.gcd(num1, num2))


# def lcm(num1, num2):
#     return num1 * num2 // math.gcd(num1, num2)


# print(f'최소공배수: {lcm(num1, num2)}')

# print((lambda a, b: a * b // math.gcd(a, b))(num1, num2))


# data = ['A', 'B', 'C']
# # result = list(permutations(data, 3))
# result = list(combinations(data, 2))
# print(result)

# # result = list(product(data, repeat=3))
# result = list(combinations_with_replacement(data, r=2))
# print(result)




# array = [("사과", 5000), ("배", 13000), ("포도", 9999)]

# dec_array = sorted(array, key=lambda x: x[1], reverse=True)
# print([item[0] for item in dec_array])


