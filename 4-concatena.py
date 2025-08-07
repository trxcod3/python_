# Concatenação

name = input("Digite o nome do filme:\n")
yaerLauch = int(input("Digite o ano de lançamento:\n"))
noteMovie = float(input("Digite nota para o filme:\n"))

print(name)
print("Dados do filme")
print("=======================================")
# Alternativa 1

# print("Nome do filme: ", name)
# print("Ano de lançamento", yaerLauch)d
# print("Nota do filme", noteMovie)

#Alternativa 2
# print("Nome do filme:", name, "\nAno de Lançamento:", yaerLauch, "\nNota do filme:,", noteMovie)

# Alternativa 3: concatenação com Fstring

print(
  f"Nome do jogo: {name}\n"
  f"Ano de Lançamento: {yaerLauch}\n"
  f"Nota do filme: {noteMovie}\n"
)