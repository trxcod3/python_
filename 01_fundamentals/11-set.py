filmsSet = {"Matrix", "Titanic", "Interstellar", "Batman"}
print(type(filmsSet))

# 1 - Busca o tamanho do set
print(len(filmsSet))

# 2 - True e 1 sao considerados o mesmo valor.
exampleSet = {"Batman", True, 1, 8.7}
print(exampleSet)

# 3 - Adcionar item de outro set
filmsSet.update(exampleSet)
print(filmsSet)

# 4 - Remover item no set

filmsSet.remove(True)
filmsSet.remove(8.7)
print(filmsSet)
