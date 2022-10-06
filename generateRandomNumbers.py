import numpy as np
import os

# * Alterar os valores de acordo com o necessario
low = 0
high = 10000000
size = 10000000

# Gera os numeros aleatoriamente
listRandom = np.random.randint(low=low, high=high, size=size)

listSort = np.sort(listRandom)
listDescending = -np.sort(-listRandom)

# Converte um array numpy em um array normal
numbersRandom = [''.join(i) for i in listRandom.astype(str)]
numbersSort = [''.join(i) for i in listSort.astype(str)]
numbersDescending = [''.join(i) for i in listDescending.astype(str)]

# Pega o diretorio local e cria um arquivo com o nome do tamanha a ser gerado
# OBS: Aqui estou retrocedendo uma pasta, pois o codigo estava em outra pasta, 
#      caso queira que os arquivos esteja no mesmo diretorio descomenta a linha 23 e comente a linha 24 
#localPath = os.getcwd()
localPath = os.path.normpath(os.getcwd() + os.sep + os.pardir)

os.makedirs(localPath + '/files/' + str(size))

nameFileRandom = str(size) + '/' + str(size) + ' - Aleatorio.txt'
nameFileOrderly = str(size) + '/' + str(size) + ' - Ordenado.txt'
nameFileDescending = str(size) + '/' + str(size) + ' - Decrecente.txt' 

# Cria os arquivos com os numeros gerados
with open('../files/' + nameFileRandom, 'w') as file:
    array = ' '.join(numbersRandom)
    file.write(array)

with open('../files/' + nameFileOrderly, 'w') as file:
    array = ' '.join(numbersSort)
    file.write(array)

with open('../files/' + nameFileDescending, 'w') as file:
    array = ' '.join(numbersDescending)
    file.write(array)