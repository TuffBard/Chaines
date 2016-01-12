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

def hasSeries(password):
    pwd = list(password)
    suite = 0
    found = False
    for i in range(0,len(pwd)-1):
        if suite == 3: #Si il y a une suite de trois lettre, passe found a True 
            found = True
            
        if suite == 0: #Si on commence la suite on sauvegarde la lettre dans char
            c = pwd[i]
            suite += 1
        else:
            if pwd[i] == chr(ord(c)+1): #Vérifie si c'es la lettre suivante
                suite += 1
                c = pwd[i]
            else:
                suite = 0
    return found
    
def hasTwoPairs(password):
    pwd = list(password)
    
def hasNoBadChar(password):
    pwd = list(password)

# Grâce à ce fragment de code, si vous exécutez ce fichier, les tests doctests seront exécutés également. 
# Si vous ne voulez plus que les tests s'exécutent, commentez les deux lignes ci-dessous. 
# Si vous préférez lancer vos tests à la main, commentez également les lignes, et utilisez "python -m doctest pass.py" en console. 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
