# coding: utf-8 
def getNext(password):
    """
    Série de tests exprimés en doctest
    >>> getNext('aaaaa')
    'aaaab'
    >>> getNext('aaaaz')
    'aaaba'
    >>> getNext('zzzzz')
    'aaaaa'
    """
    pwd = list(password)  #1  pwd contient chaque lettre du lot de passe sous forme de liste
    found = False
    i=len(pwd)-1

    if password == 'zzzzz':
        pwd = list('aaaaa')
        found = True

    while not found:
        if pwd[i] < 'z':
           pwd[i] = chr(ord(pwd[i])+1)  #2 La lettre devient la suivante de l'alphabet
           found = True             
        else:
            pwd[i] = chr(ord(pwd[i])-25) #le 'z' deviens un 'a'
            i = i-1 
    
    return ''.join(pwd) #3 affiche le nouveaux mot de passe



# Grâce à ce fragment de code, si vous exécutez ce fichier, les tests doctests seront exécutés également. 
# Si vous ne voulez plus que les tests s'exécutent, commentez les deux lignes ci-dessous. 
# Si vous préférez lancer vos tests à la main, commentez également les lignes, et utilisez "python -m doctest pass.py" en console. 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
