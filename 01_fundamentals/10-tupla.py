filmsTuple = ("Matrix", "Titanic", "Interstellar", "Batman")
print(type(filmsTuple))

# 1 - Buscar os dois primeiros itens da tupla
print(filmsTuple[:2])

# 2 - Buscar o ultimo item da tupla
print(filmsTuple[-1])

# 3 - Buscar filmes até uma determinada posição
print(filmsTuple[:3])

# 4 - Buscar filmes de uma posicao em diante
print(filmsTuple[2:])

# 5 - Recuperar um item da tupla pelo nome
print(filmsTuple.index("Titanic"))