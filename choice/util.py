# outlist contains elements (id, display)
def idNameList(inlist):
    if inlist is None:
        return None

    outlist = []
    for item in inlist:
        if isinstance(item, str):
            outlist.append((item, item))
        elif isinstance(item, tuple):
            if len(item) != 2:
                raise TypeError('List item is not a 2-tuple')
            outlist.append(item)
        else:
            raise TypeError('List item should be string or 2-tuples')
    return outlist

