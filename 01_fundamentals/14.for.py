movieList = ["Titanic", "The Godfather", "Top Gun", "Duro de Matar4"]

# 1 - Iterando valores de uma lista
for movie in movieList:
  print(movie)

# 2 - Quando a condiça for atendida, o loop sera encerrado
for movie in movieList:
  if movie == "Top Gun":
    break
  print(movie)

# 3 - Quando a condiça for atendida, o loop vai para proxima iteração
for movie in movieList:
  if movie == "Duro de Matar4":
    continue
  print(movie)