#function that, given a number, can find the sum of all the multiples of particular numbers up to but not including that number.
def sum_of_multiples(limit, multiples):
    for nums in multiples:
        if nums == 0:
            multiples.remove(0)
    result = []

#loop through the multiples list and check if the number is a multiple of the limit

    for item in range(limit):
        for num in multiples:
            if item == 0:
                result = [0]
                break
            elif item % num == 0:
                result.append(item)

    return sum(set(result))