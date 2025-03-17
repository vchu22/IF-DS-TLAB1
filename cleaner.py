def filter_nondigits(data: list) -> list:
    """
    This function takes in a list as the input and returns an integer list of the valid digits appeared in the input list.

    Args:
        data (list): A list containing the input data.
    Returns:
        list: A list containing only the valid digits from the data list.
    """

    # create an empty list
    result = []
    # iterate through the data
    for _ in data:
        if type(_) == float or type(_) == int:
            result.append(_)
        elif _.strip().isdigit():
            result.append(int(_.strip()))
    return result