duplicadas = []
for img in archivo:
  for recorrer in archivo:
    if (img[0] == recorrer[0]) & (img[1] == recorrer[1]) & (archivo.index(img) != archivo.index(recorrer)):
      #añadir a duplicadas
      duplicadas.append((img[0],recorrer[0]))
