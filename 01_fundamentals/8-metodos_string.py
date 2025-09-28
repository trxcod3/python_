movieName = "Top Gun"
movieDescription = "Top Gun is a 1986 American action drama film directed by Tony Scott, produced by Don Simpson and Jerry Bruckheimer, and starring Tom Cruise as Lieutenant Pete 'Maverick' Mitchell, a young naval aviator aboard the aircraft carrier USS Enterprise. The film also features Kelly McGillis, Val Kilmer, Anthony Edwards, and Tom Skerritt in supporting roles. The screenplay was written by Jim Cash and Jack Epps Jr., based on a story by Cash and Donald Glut."

print(movieName.upper()) # Transforma todos os caracteres em maiusculo
print(movieName.lower()) # Transforma todos os caracteres em minusculo
print(movieName.title()) # Transforma a primeira letra de cada palavra em maiusculo
print(movieName.strip()) # Remove espacos no inicio e no fim da string
print(movieName.replace("Gun", "Gun 2")) # Substitui uma parte da string por outra
print(movieName.split(" ")) # Divide a string em uma lista, usando o espaco como separador
print(" ".join(movieName)) # Junta os caracteres da string, usando o espaco como separador
print(movieName.find("Gun")) # Retorna o indice da primeira ocorrencia da substring
print(movieName.find("War")) # Retorna -1 se a substring nao for encontrada
print(movieName.count("o")) # Conta quantas vezes a substring aparece na string
print(movieDescription.count("the")) # Conta quantas vezes a substring aparece na string
print(movieName.startswith("Top")) # Retorna True se a string comeca com a substring
print(movieName.endswith("Gun")) # Retorna True se a string termina com a substring     