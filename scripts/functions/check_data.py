def has_duplicates(d):
    '''
    if has duplicate value in a dict data
    '''
    return len(d) != len(set(d.values()))
