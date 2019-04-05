"""
molssi_math.py
A sample repository for MolSSI Workshop

Some math functions
"""

def mean(num_list): 
    """
    Calculate the mean/average of a list of numbers. 

    Parameters
    __________
    num_list : list 
        The  list to take the average of 

    Returns
    -------
    mean_list : float
        The mean of the list

    """
    
    total = sum(num_list)
    mean_list = total/len(num_list)
    return mean_list



def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
