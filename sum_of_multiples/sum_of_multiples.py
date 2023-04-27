def sum_of_multiples(limit, multiples):
    for nums in multiples:
        if nums == 0:
            multiples.remove(0)
    result = []

    for item in range(limit):
        for num in multiples:
            if item == 0:
                result = [0]
                break
            elif item % num == 0:
                result.append(item)

    return sum(set(result))
