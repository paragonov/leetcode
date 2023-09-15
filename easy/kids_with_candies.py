def kids_with_candies(candies: list, extra_candies: int) -> list[bool]:
    result = []
    for candi in candies:
        for second_candi in candies:
            if not candi + extra_candies >= second_candi:
                result.append(False)
                break
        else:
            result.append(True)

    return result


kids_with_candies([2, 3, 5, 1, 3], 3)
kids_with_candies([4, 2, 1, 1, 2], 1)
