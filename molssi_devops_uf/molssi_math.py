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
    #Check that input is type list
    if not isinstance(num_list,  list):
        raise TypeError('Invalid input %s - must be type list' %(num_list))


    #Check that list is not empty
    if len(num_list) == 0:
        raise ValueError('Input is an empty list!')
   
    #Check that list does not contain mixed variable types (already has error message)
    


    try:
        total = sum(num_list)
        mean_list = total / len(num_list)
    except TypeError:
        raise TypeError('Cannot calculate mean of list - all list elements must be numeric')


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
