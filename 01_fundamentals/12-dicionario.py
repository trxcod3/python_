filmeDict = {
  "titanic": {
    "yearRelease": 2010,
    "imdbRating": 8.8,
    "genre": ["Sci-fi", "Action", "Thriller"]
  },
   "Interstellar": {
    "yearRelease": 2014,
    "imdbRating": 9.0,
    "genre": ["Sci-fi", "Drama"]
  },
   " Top Gun": {
    "yearRelease": 2023,
    "imdbRating": 7.9,
    "genre": [ "Action", "Thriller"]
  },
   "Thor": {
    "yearRelease": 2010,
    "imdbRating": 5.71 ,
    "genre": ["Sci-fi", "Action", "Thriller"]
  },
}

#pp = pprint.PrettyPrinter(depth=4)

print(filmeDict)

# 1 - Buscar informacows  no dicionario

print(filmeDict["Interstellar"]["genre"])