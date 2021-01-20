def compruebaMail(mailDelUsuario):
    
    """
    Función que verifica el mail del usuario:

    >>> compruebaMail('usuario@dominio.cl')
    True

    >>> compruebaMail('usuario@dominio@.cl')
    False

    >>> compruebaMail('usuariodominio.cl')
    False

    >>> compruebaMail('usuariodominio.cl@')
    False

    >>> compruebaMail('@usuariodominio.cl')
    False

    """

    arroba = mailDelUsuario.count('@')

    if (arroba!=1 or mailDelUsuario.rfind('@')==(len(mailDelUsuario)-1)or mailDelUsuario.find('@')==0):
        return False
    else:
        return True

import doctest
doctest.testmod()