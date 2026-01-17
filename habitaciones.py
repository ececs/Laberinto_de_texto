# Habitaciones del laberinto

# Diccionario con todas las habitaciones del laberinto

# Es solo un ejemplo hay que modificarlo segun el diseño del laberinto

habitaciones = {
    'entrada': {
        'nombre': 'Entrada del Laberinto',
        'descripcion': 'Estás en la entrada del laberinto. Hay caminos hacia el norte y el este.',
        'salidas': {'norte': 'pasillo', 'este': 'jardin'}
    },
    'pasillo': {
        'nombre': 'Pasillo Oscuro',
        'descripcion': 'Un pasillo oscuro y estrecho. Hay una puerta al sur y otra al este.',
        'salidas': {'sur': 'entrada', 'este': 'biblioteca'}
    },
    'jardin': {
        'nombre': 'Jardín Encantado',
        'descripcion': 'Un hermoso jardín lleno de flores mágicas. Hay un camino al oeste.',
        'salidas': {'oeste': 'entrada'}
    },
    'biblioteca': {
        'nombre': 'Biblioteca Antigua',
        'descripcion': 'Una biblioteca llena de libros polvorientos. Hay una salida al oeste.',
        'salidas': {'oeste': 'pasillo'}
    }
}   