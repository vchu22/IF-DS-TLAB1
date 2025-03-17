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
    return average


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
    return max_num


def variance(data: list) -> float:
    """
    INSERT DOCSTRING HERE
    (calculate population variance)
    """
    pass


def standard_deviation(data: list) -> float:
    """
    INSERT DOCSTRING HERE
    (calculate population standard deviation)
    """
    pass
