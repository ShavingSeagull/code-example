# O(n) time | O(1) space
def sum_interval(array, start, stop):
    total = 0

    for num in range(start, stop + 1):
        total += array[num]
    
    return total

# O(n^2) time | O(n) space
def rev_cumulutive_sum(array):
    result = []

    for x in range(len(array)):
        result.append(sum_interval(array, x, len(array) - 1))

    return result

# O(n^2) time | O(n) space
def sum_triplets(array):
    left = 0
    right = left + 2
    result = []

    while right <= len(array) - 1:
        result.append(sum_interval(array, left, right))
        left += 1
        right = left + 2

    return result