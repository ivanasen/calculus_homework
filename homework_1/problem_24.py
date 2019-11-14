# Problem 24

import math
from decimal import *

cached_terms = []
index_count = 5


def converges(first):
    if first == -8:
        return None
    if first < -8:
        return -math.inf
    if first > 4 or -8 < first < -3:
        return math.inf
    if -2 < first < 4 or first == -2 or 2:
        return 2
    return 4


def calculate_next(prev):
    return Decimal((2 * (prev ** 2) + 2 * prev + 8) / (prev + 8))


def calculate_term(first, term_number):
    if term_number < 1:
        return None

    if term_number < len(cached_terms):
        return cached_terms[term_number - 1]

    current_term = len(cached_terms)
    result = first

    if current_term > 0:
        result = cached_terms[current_term - 1]

    while current_term < term_number:
        current_term += 1
        result = calculate_next(result)
        cached_terms.append(result)

    return result


first = int(input())
result = converges(first)

print(result)

if result == None or result == math.inf or result == -math.inf:
    print(f'When lambda is {first} the series does not converge.')
    exit()

print(f'When lambda is {first} the series converges to: {result}\n')

print('Please enter 5 indexes to calculate the series at:')

for i in range(0, index_count):
    index = int(input())
    print(f'series term at {index} is {calculate_term(first, index)}')
