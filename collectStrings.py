def collectStrings(obj):
    # TODO
    res = []
    for key in obj:
        if type(obj[key]) is dict:
            res.extend(collectStrings(obj[key]))
        elif type(obj[key]) is str:
            res.append(obj[key])
    return res        