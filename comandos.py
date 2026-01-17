# Parser de comandos del juego

def normalizar_entrada(texto):
    """
    Normaliza la entrada del usuario eliminando espacios extra
    y convirtiendo a minúsculas.
    
    Args:
        texto (str): Texto ingresado por el usuario
        
    Returns:
        str: Texto normalizado
    """
    return texto.strip().lower()