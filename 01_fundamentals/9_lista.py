filmMatrix = ["Matrix", 1999, 8.7, True]

print(filmMatrix)

filmsList = ["Matrix", "Inception", "Interstellar", "The Dark Knight"]

print(filmsList[:2]) # Busca os dois primeiros elementos da lista
print(filmsList[1:]) # Busca todos os elementos a partir do indice 1
print(filmsList[1:3]) # Busca os elementos do indice 1 ao 2 (3-1)
print(filmsList[::2]) # Busca todos os elementos de 2 em 2
print(filmsList[::-1]) # Inverte a lista comeca do ultimo elemento ate o primeiro   
print(filmsList[-1]) # Busca o ultimo elemento da lista
print(filmsList[-3:]) # Busca os tres ultimos elementos da lista
print(filmsList + ["Pulp Fiction", "Fight Club"]) # Adiciona novos elementos a lista
print(filmsList * 2) # Repete a lista duas vezes
filmsList.append("Pulp Fiction") # Adiciona um novo elemento ao final da lista
print(filmsList)
filmsList.insert(1, "Fight Club") # Adiciona um novo elemento na posicao desejada
print(filmsList)
filmsList.remove("Inception") # Remove o elemento desejado
print(filmsList)
filmsList.pop() # Remove o ultimo elemento da lista
print(filmsList)
filmsList.pop(1) # Remove o elemento da posicao desejada
print(filmsList)
filmsList[0] = "The Matrix" # Altera o valor do elemento da posicao desejada
print(filmsList)
print(len(filmsList)) # Retorna o tamanho da lista
print(filmsList.index("Interstellar")) # Retorna o indice do elemento desejado
print(filmsList.count("The Dark Knight")) # Conta quantas vezes o elemento aparece
filmsList.sort() # Ordena a lista em ordem alfabetica
print(filmsList)
filmsList.reverse() # Inverte a ordem da lista
print(filmsList)
filmsList.clear() # Remove todos os elementos da lista
print(filmsList)          # Retorna uma lista vazia     
filmsList = ["Matrix", "Inception", "Interstellar", "The Dark Knight"]
filmsTuple = tuple(filmsList) # Converte a lista em tupla               