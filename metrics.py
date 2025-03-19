import math

def average(data: list) -> float:
    """
    Calculate average value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list
    """
    average = 0
    sum = 0
    for _ in data:
        if type(_) == int or type(_) == float:
            sum += _
    if len(data) == 0:
        return []
    average = sum / len(data)
    return round(average, 2)


def maximum(data: list) -> float:
    """
    Find the largest number in the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the maximum of in the list
    """
    if (len(data) == 0):
        return []
    max_num = data[0]
    for _ in data[1:]:
        if max_num < _:
            max_num = _
    return round(max_num, 2)


def variance(data: list) -> float:
    """
    Calculate the population variance given a list of heart rate data.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the population variance of the sample
    """
    if len(data) == 0:
        return 0
    mean = average(data)
    sum_deviations = 0
    for _ in data:
        sum_deviations += abs(_ - mean) ** 2
    return round(sum_deviations / len(data), 2)


def standard_deviation(data: list) -> float:
    """
    Calculate the standard deviation given a list of heart rate data.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the population variance of the sample
    """
    if len(data) == 0:
        return []
    return round(math.sqrt(variance(data)), 2)
