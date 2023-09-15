def number_of_employees_who_met_target(hours: list, target: int) -> int:
    result = 0
    for hour in hours:
        if hour >= target:
            result += 1
    return result


number_of_employees_who_met_target([0,1,2,3,4], 2)
number_of_employees_who_met_target([5,1,4,2,2], 6)
