0##SI VAN A USAR FUNCIONES, TAMBIEN BASENSE EN ESTAS, ALGUNA PREGUNTA ME AVISAN, SI ALGO LE AGREGAN FUNCIONES, PERO LA GRACIA ES QUE TODOS UTILICEMOS LAS MISMAS

def confirmarLista(dato, lista):
	for i in lista:
		if i==dato:
			return True
			break
	return False
	
def mostrarMenu(lista):
	pos=1
	print ('\nSELECCIONE UNA OPCIÓN DEL MENÚ.\n')
	for i in lista:
		print (pos,')', i)
		pos+=1
		
def validar_seleccion(lista):
	while True:
		seleccion=input(':')
		if confirmarLista(seleccion.upper(), lista) == True:
			break
		else:
			print('Ingrese una opción valida')
	return seleccion.upper()
	

#CLASES

##A LAS CLASES LES COLOQUE EL PASS PORQUE NO ESTOY MUY SEGURO DE QUE TIPO DE FUNCION METER EN CADA SITIO

from funciones import confirmarLista


class Cliente:
	def __init__(self, nombre_cliente, telefono, id):
		self.nombre=nombre_cliente
		self.telefono=telefono
		self.id=id


class Alimento:
	def __init__(self, nombre, descripcion, precio, valNutricional, codigo, HoraI, HoraF, tiempoPrep):
		self.nombre=nombre
		self.descripcion=descripcion
		self.precio=precio
		self.valNutricional=valNutricional
		self.codigo=codigo
		self.HoraI=HoraI
		self.HoraF=HoraF
		self.tiempoPrep=tiempoPrep
	
	def imprimirDatos (self):
		print('\nNombre: ', self.nombre)
		print('descripcion: ', self.descripcion)
		print('Precio: $', self.precio)
		print('Valor nutricional: ', self.valNutricional, 'KCal')
		print('Tiempo espera aprox: ', self.tiempoPrep, 'Min.')

	
class Comida (Alimento):
	def add_ingredientes (self, precioADD, ValNut, tiempo ):
		self.precio+=precioADD
		self.valNutricional+=ValNut
		self.tiempoPrep+=tiempo
		print('\n¡Se han agregado datos a su pedido!\n')
	

	def add_adicional (self):
		pass
	
class Adicional (Alimento):
	pass

class Acompañamientos (Alimento):
	pass

##ESTE ES EL MENÚ, CADA UNO ESTÁ EN SU PROPIA CLASE, ASÍ QUE LOS MÓDULOS QUE CADA UNO TENDRÁ QUE IR DENTRO DE SU PROPIA CLASE

#hamburguesas
ListaHamburguesas=['BIGMAC', 'MCNIFICA', 'MCQUESO', 'CUARTO DE LIBRA', 'CAJITA FELIZ']


bigMc=Comida('bigMC','Prueba la deliciosa Big Mac de McDonalds Colombia. Dos hamburguesas de pura carne con salsa especial Big Mac y queso derretido.', 7000, 490, 1, 0, 0, 15)
MCnifica=Comida('MCnífica', 'Es real y es más que buena, es magnífica', 10000, 543, 2, 0, 0, 15)
MCqueso=Comida('MCqueso', 'Hamburguesa con pan fresco caramelizado, carne de 50 gramos, queso cheddar, cebolla, pepinillos, salsa de tomate y mostaza McDonalds.', 6000, 300, 3, 0, 0, 10)
CuartoLB=Comida('Cuarto de libra', 'Prueba la deliciosa hamburguesa cuarto de libra con queso: la compañía perfecta para que la hamburguesa no se sienta sola.', 8000, 500, 4, 0, 0, 13)
cajitaFeliz=Comida('Cajita feliz', 'Hamburguesa con pan fresco caramelizado, carne de 50 gramos, cebolla, pepinillos, salsa de tomate y mostaza intensa de McDonalds.', 5000, 249, 5, 0, 0, 8)

ListaHamburguesas2={bigMc, MCnifica, MCqueso, CuartoLB, cajitaFeliz}


#Acompañamientos

ListaAcompañamientos=['COCA COLA', 'MCFLURRY JET' , 'MCPAPAS', 'ENSALADA', 'SUNDAE']

Coca_Cola=Acompañamientos('Coca_Cola','No te puede faltar para bajar tus delicionas comidas.', 5000, 230, 6, 0, 0, 0)
McFlurry_Jet=Acompañamientos('McFlurry_Jet', '¡Nuevo McFlurry Jet Cookies & Cream #Irresistible!', 4600, 466, 7, 'HI', 'HF', 5 )
MCpapas=Acompañamientos('MCpapas', 'Calientes, crujientes y deliciosas. Disfruta de nuestras papas mundialmente famosas, desde la primera hasta la última.', 6000, 288, 8, 0, 0, 5)
Ensalada=Acompañamientos('Ensalada', 'La ensalada para acompañar tu McCombo fue mejorada con una mayor variedad de hojas y tomate en rodajas.', 8000, 9, 9, 0, 0, 7)
Sundae=Acompañamientos('Sundae', 'El tradicional Sundae de McDonalds Delicioso helado en vaso, acompañado de nuestra salsa de chocolate.', 5000, 268, 10, 0, 0, 8)



#Adicionales

ListaAdicionales=["QUESO","CARNE","TOMATE","LECHUGA","PEPINILLOS"]

Queso=Adicional("Queso","Delicioso Queso campesino",2000, 90,11,0,0,0)
Carne=Adicional("Carne","Carne de res fresca",6000, 204, 12,0,0,5)
Tomate=Adicional("Tomate","Tomate de la mejor calidad",600,18, 13,0,0,0)
Lechuga=Adicional("Lechuga","Fresca y deliciosa lechuga",300,15, 14,0,0,0)
Pepinillos=Adicional("Pepinillos","Pepinillos muy deliciosa",500, 11, 15,0,0,0)

from datetime import datetime,timedelta
hoy = datetime.now()

class Pedido():
  
  pedido=[]

  def imprimirPedido(self):
  	a=('')
  	print(a.center(50,'='))
  	a=("Factura")
  	print(a.center(50,'='))
  	print(f"\nSeñor/a: {self.cliente.nombre}")
  	print(f"Su pedido esta en proceso, se le mandara un msj a {self.cliente.telefono} para recoger su pedido.")
  	print("\nPedido:\n")
  	
  	total=0
  	
  	for i in self.pedido:
  		print(i.nombre)
  		print(f"Precio: $ {i.precio}")
  		total+=i.precio

  
  	print(f"\nTotal: $ {total}")
    
    
  def add_alimento(self,Alimento):
    self.pedido.append(Alimento)
  
  
  def add_cliente(self,Cliente):
    self.cliente=Cliente


#VALIDACIONES CAJERO   
from colorama import init, Fore, Back, Style
#-----------------------------------------------------------------------------
#Validaciones
def validar_letras(p):#Solo Letras
  while(p.isalpha()==False):
    p=input("DIGITE SOLO LETRAS🅰:   ")
    if(p.isalpha()==True):
      break
  return p  
  #Solo Numeros Positivos
#---------------------------------------------------------------------  
def validar_numeros(N):
 while True:
  try:
    while(N<0):
      N=int(input("digite un numero Positivo ➕"))
    break
  except:
    print("valor no valido digite un numero🤦")
 return N 
#------------------------------------------------------------------------  
def error(d):
  print((Fore.RED+Style.BRIGHT+d))
  return d, print(Style.RESET_ALL + "")
def error_1(E):
  print((Fore.BLUE+Style.BRIGHT+E))
  return E, print(Style.RESET_ALL + "")
def verde(m):
  print((Fore.GREEN+Style.BRIGHT+m))
  return m, print(Style.RESET_ALL + "")
def hora(k):
  print((Fore.CYAN+Style.BRIGHT+k))
  return k, print(Style.RESET_ALL + "")
#-------------------------------------------------
    
