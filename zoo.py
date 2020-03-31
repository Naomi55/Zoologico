matriz=[]
x=input("¿cuántos animales quieres?)
for i in x
n=input("¿Cuál es el nombre?")
x=input("¿Cuál es el tipo?")
matriz=n[1,0]
matriz=ID[0,i]
i++
ID++
print (matriz)


class Zoologico:
	def __init__(self, nombre, tipo):
		self.nombre = nombre
		self.tipo = tipo

	def set_brand(self,tipo):
		self.tipo = tipo
		print ("El nuevo tipo es" + self.tipo)
	
	def get_brand(self):
		print ("El tipo de animal actual es " + self.tipo)

def main():
	zoo = Zoologico("n","x")
	zoo.set_tipo("n")
	zoo.get_tipo()


if __name__ == "__main__":
	main()