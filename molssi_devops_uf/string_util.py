"""
string_util.py
A sample repository for MolSSI Workshop.

Misc. string processing functions
"""


def title_case(sentence):
    """
    Convert a  string to title case.

    Parameters
    ----------
    sentence: string
        String to be converted to title case

    Returns
    -------
    ret : string
        String converted to title case

    Example
    -------
    >>> title_case('ThIS iS a StrInG to BE ConVerTed.')
        'This Is A String To Be Converted.'
    """

    #Check that input is a string
    if not isinstance(sentence, str):
        raise TypeError('Invalid input %s - Input must be type string' % (sentence))
    
    #Error if empty string
    if sentence == ' ':
        raise Warning('Input is an empty string!')

    #Handle empty string
    if len(sentence)==0:
        raise ValueError('Input is an empty string!')
    
    ret = sentence[0].upper()

    for i in range(1, len(sentence)):
        if sentence[i - 1] == ' ':
            ret += sentence[i].upper()
        else:
            ret += sentence[i].lower()
    return ret


y = 'ThIS iS a StrInG to BE ConVerTed.'
print(title_case(y))
