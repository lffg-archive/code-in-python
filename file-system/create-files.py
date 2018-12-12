def createFile (name):
	open(name, "w")

for num in range(0, 25):
	print("Criando o arquivo: " + str(num))
	createFile(str(num))
