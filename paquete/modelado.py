class Persona(object):#Creamos la clase Persona que hereda de Object por defecto
  
	def __init__ (self): #Creo el metodo que define los atributos
		self.nombres= " "
		self.edad= 0
	
	def agregar_nombres(self,n): #Set del atributo nombres
		self.nombres= n
	
	def agregar_edad(self,e):#Set del atributo edad
		self.edad= e
	
	def obtener_nombres(self):#Get atributo nombres
		return self.nombres
	
	def obtener_edad(self):#Get atributo edad
		return self.edad
	
	def presentar_datos(self):#Retornamos una cadena  mediante el metodo presentar_datos
		c= "%s -%s "%(self.obtener_edad(),self.nombres)
		return c

##Creamos la clase Estudiante que es hija de la clase Persona
class Estudiante(Persona):

	def __init__(self):#Creo el metodo que define los atributos
		super(Estudiante,self).__init__()
		self.nota = 0
	
	def agregar_nota(self,t):#Set de atributo nota
		self.nota= t

	def obtener_nota(self):#Get de atributo nota
		return self.nota

	def presentar_datos(self):#Retornamos una cadena  mediante el metodo presentar_datos
		#c="%s-%s-%s"%(self.nombres,self.edad,self.nota
		c="%s-%s"%(super(Estudiante,self).presentar_datos(),self.nota)
		return c
