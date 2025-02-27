def separa_letras(Cadena):
    # Verificar si el parámetro es un string (a)
    if not isinstance(Cadena, str):
        return (-100, None, None)

    # Verificar si el string no está vacío (c)
    if len(Cadena) == 0:
        return (-300, None, None)

    # Verificar si solo contiene letras del abecedario (b)
    if not Cadena.isalpha():
        return (-200, None, None)

    # Separar en mayúsculas y minúsculas
    mayusculas = ''.join([c for c in Cadena if c.isupper()])
    minusculas = ''.join([c for c in Cadena if c.islower()])

    # Retornar código de éxito y las cadenas
    return (0, mayusculas, minusculas)


def potencia_manual(base, potencia):
    # Verificar que los parámetros no sean de tipo string (a)
    if isinstance(base, str) or isinstance(potencia, str):
        return (-400, None)

    # Caso especial: si la potencia es 0, el resultado es 1
    if potencia == 0:
        return (0, 1)

    # Caso especial: si la base es 0 y la potencia es negativa, es indefinido
    if base == 0 and potencia < 0:
        return (-2, None)

    # Inicializar el resultado
    resultado = 1

    # Calcular la potencia usando sumas y ciclos for
    if potencia > 0:
        for _ in range(potencia):
            # Multiplicación usando sumas
            temp = 0
            for _ in range(base):
                temp += resultado
            resultado = temp
    else:
        # Si la potencia es negativa, calcular el inverso
        for _ in range(-potencia):
            temp = 0
            for _ in range(base):
                temp += resultado
            resultado = temp
        resultado = 1 / resultado

    # Retornar código de éxito y el resultado
    return (0, resultado)
