def notas(*n, sit=False):
    """
    It takes an arbitrary number of arguments, and returns a dictionary with the total number of
    arguments, the highest value, the lowest value, the average value, and the situation (if the
    optional argument sit is set to True)
    
    :param sit: False, defaults to False (optional)
    :return: A dictionary with the total, highest, lowest, and average of the numbers passed in.
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
           r['situação']  = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r


#Programa Principal
resp = notas(5.5, 9.5, 9, 8.5, sit=True)
print(resp)
