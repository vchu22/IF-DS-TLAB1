"""
The main Python mpdule that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import average, maximum, standard_deviation
from cleaner import filter_nondigits

import matplotlib.pyplot as plt


def run(filename: str) -> None:
    """
    Process heart rate data from the specified file, clean it, calculate metrics,
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, max, and standard deviation
    """ 
    data = []

    # open file using file I/O and read it into the `data` list
    file_text = open(filename)

    # Use `filter_nondigits` to clean the data and remove invalid entries, save the output to a new variable
    data = filter_nondigits(file_text)

    # plot this data to explore changes in heart rate for this file, save this visualization to the "images" folder
    
    plt.xlabel("Time (5-Minutes Interval)")
    plt.ylabel("Heart Rate")
    plt.plot(data, color = 'blue')
    plt.savefig(f"images/{filename[5:-4]}.png") # name the image file based on phase number
    plt.close()

    # calculate the average, maximum, and standard deviation of this file using the functions you've wrote
    avg_hr = average(data)
    max_hr = maximum(data)
    std_dev_hr = standard_deviation(data)

    # return all 3 values
    return avg_hr, max_hr, std_dev_hr


if __name__ == "__main__":
    print(run("data/phase0.txt"))
    print(run("data/phase1.txt"))
    print(run("data/phase2.txt"))
    print(run("data/phase3.txt"))