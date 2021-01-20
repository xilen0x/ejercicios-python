def suma(num1, num2):
    
    """
    Función que suma dos números y que mediante la linea siguiente ealiza el test corresp. En caso de estar ok no muestra nada.
    En caso de error en el código, mostrará un error con información:

    >>> suma(5,5)
    10

    >>> suma(2,5)
    7

    >>> suma(15,5)
    20
    """

    return num1+num2a # error intencional para ver el error

import doctest
doctest.testmod()