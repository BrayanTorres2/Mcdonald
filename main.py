from funciones import confirmarLista, ListaHamburguesas, mostrarMenu, validar_seleccion, ListaAcompañamientos, ListaAdicionales, bigMc, MCnifica, MCqueso, CuartoLB, cajitaFeliz, Queso, Carne, Tomate, Lechuga, Pepinillos, Coca_Cola, McFlurry_Jet, MCpapas, Ensalada, Sundae, Pedido, Cliente, validar_letras,validar_numeros,error,error_1,verde
import time

alimentos=['COMIDAS RAPIDAS', 'ACOMPAÑAMIENTO']	
validaciones=['SI', 'NO']

#BIENVENIDA AL RESTAURANTE Y ELECCION PARA COMER O NO EN EL LOCAL
hello=('Bienvenido a McDonald´s.')
print (hello.center(50,'='))

pedidoactual = Pedido()

lista_pedidos=[]

print('\n¿Desea comer en el restaurante?')
welcome=validar_seleccion(validaciones)


terminar=True

while terminar:
#SELECCION DE LOS ALIMENTOS 
  while True:
  	print('\nSELECCIONE EL TIPO DE ALIMENTO QUE DESEA DISFRUTAR.\n')
  	mostrarMenu(alimentos)	
  	seleccion=validar_seleccion(alimentos)
  
  	if seleccion.upper()=='COMIDAS RAPIDAS':
  		while True:
  			mostrarMenu(ListaHamburguesas)
  			comida=validar_seleccion(ListaHamburguesas)
  			if comida =='BIGMAC':
  				bigMc.imprimirDatos()
  				comidaRapida=bigMc
  			elif comida == 'MCNIFICA':
  				MCnifica.imprimirDatos()
  				comidaRapida=MCnifica
  			elif comida == 'MCQUESO':
  				MCqueso.imprimirDatos()
  				comidaRapida=MCqueso
  			elif comida == 'CUARTO DE LIBRA':
  				CuartoLB.imprimirDatos()
  				comidaRapida=CuartoLB
  			elif comida == 'CAJITA FELIZ':
  				cajitaFeliz.imprimirDatos()
  				comidaRapida=cajitaFeliz
  			print('\n¿Desea confirmar su pedido?')
  			confirmar=validar_seleccion(validaciones)
  			if confirmar == 'SI':
  			  pedidoactual.add_alimento(comidaRapida)
  			  break
  	
  		print('\n¿Desea algún adicional?\n')
  		add_comida=validar_seleccion(validaciones)
  		if add_comida == 'SI':
  			count=3
  			while count!=0:
  				mostrarMenu(ListaAdicionales)
  				print('\nSeleccione su adicional (MAX ', count,')')
  				add_acompañamiento=validar_seleccion(ListaAdicionales)
  				if add_acompañamiento == 'QUESO':
  					comidaRapida.add_ingredientes(Queso.precio, Queso.valNutricional, Queso.tiempoPrep)
  				elif add_acompañamiento == 'CARNE':
  					comidaRapida.add_ingredientes(Carne.precio, Carne.valNutricional, Carne.tiempoPrep)
  				elif add_acompañamiento == 'TOMATE':
  					comidaRapida.add_ingredientes(Tomate.precio, Tomate.valNutricional, Tomate.tiempoPrep)
  				elif add_acompañamiento == 'LECHUGA':
  					comidaRapida.add_ingredientes(Lechuga.precio, Lechuga.valNutricional, Lechuga.tiempoPrep)
  				elif add_acompañamiento == 'PEPINILLOS':
  					comidaRapida.add_ingredientes(Pepinillos.precio, Pepinillos.valNutricional, Pepinillos.tiempoPrep)
  				if count != 1:
  					print('¿Más adicionales a tu McPedido?')
  					mcpedido=validar_seleccion(validaciones)
  					if mcpedido == 'NO':
  						break
  					else:
  					  count-=1
  				else:
  					count-=1
  		  
  		print('\n¿Quiere agregar otro alimento a su McPedido?')
  		addAcomp=validar_seleccion(validaciones)
  		if addAcomp == 'SI':
  			newO=('Nuevo pedido')
  			print(newO.center(50,'='))
  		else:
  		  print('\n¿Desea pagar en efectivo?')
  		  metPago=validar_seleccion(validaciones)
  		  if metPago=='NO':
  		    n_1=0
  		    para_usu=0
  		    para_contra=0
  		    usuario=["juan","brayan","santiago","sebastian","MC"]
  		    capital=[200000,500000,100000,0,0]
  		    contraseña1=["1234","3333","1111","2222"]
  		    r="Bienvenido a Tu Banco💰"
  		    error_1(r)
  		    while True:
  		      try: 
  		        print(time.strftime("%x"))
  		        g=int(input("1.Iniciar Sesión"))
  		        break
  		      except:
  		        a="Error Lo Que Digito No Es Un Numero🤦"
  		        error(a)
  		    while(g>1 or g<1):
  		      a="Numero Digitado No Es Valido Intente Nuevamente 🤦"
  		      error(a)
  		      while True:
  		        try: 
  		          g=int(input("1.Iniciar Sesión"))  
  		          break
  		        except:
  		          a="Error Lo Que Digito No Es Un Numero🤦"
  		          error(a)
  		      (validar_numeros(g))
  		    while g==1:
  		      u=input("digite Usuario🙍:  ")
  		      (validar_letras(u))
  		      c=input("digite contraseña🔑:  ")
  		      m=usuario.count(u)
  		      f=contraseña1.count(c)
  		      if(m==1 and f==0):
  		        print("Contraseña incorrecta🤦")
  		        para_contra=para_contra+1
  		      elif(m==0 and f==1 ):
  		        print("usuario incorrecto🤦")
  		        para_usu=para_usu+1
  		      elif(m==0 and f==0):
  		        print("Usuario y Contraseña Incorrectas🤦")
  		        n_1=n_1+1
  		      if(n_1>4):
  		        print("Mas De 5 Intentos")
  		        i="Lo Sentimos el Sistema no funcionará por 2 horas Intentos Excesivos🤷"
  		        error(i)
  		        d="Llamado a La Policia🚔..."
  		        verde(d)
  		        time.sleep(60)#7200s==2h
  		        n_1=0
  		        g=2
  		        break
  		      if(para_usu>2):
  		        print("Mas De 3 Intentos")
  		        i="Lo Sentimos el sistema se bloqueara por 5 minutos🤷"
  		        error(i)
  		        time.sleep(5)
  		        para_usus=0
  		        g=2
  		        break
  		      if(para_contra>3):
  		        print("Mas De 3 Intentos")
  		        i="Lo Sentimos el sistema se bloqueara por 5 minutos🤷"
  		        error(i)
  		        time.sleep(5)  
  		        para_contra=0
  		        g=2
  		        break
  		      if(m==1 and f==1):
  		        a=usuario.index(u)
  		        b=contraseña1.index(c)
  		        if(a==b):
  		          a="Bienvenido"
  		          verde(a)
  		          print('')
  		          trans="Su transaccion se esta realizando..."
  		          verde(trans)
  		          x=usuario.index(u)
  		          if capital[x]<=0: #AÑADIR VALOR A PAGAR
  		            a="Fondos de cuenta insuficientes, pedido cancelado"
  		            error(a)
  		            quit()
  		          else:
  		            capital[x]=capital[x]-100 #CAMBIAR 100 POR VALOR A PAGAR
  		            a="Transaccion realizada con exito!"
  		            verde(a)
  		            zz=(input("Telefono movil: "))
  		            z=int(zz)
  		            validar_numeros(z)
  		            while len(zz)<10:
  		              zz=int(input("Reingrese su telefono movil: "))
  		              z=int(zz)
  		              validar_numeros(z)
  		            hzz=(input("ID: "))
  		            hz=int(hzz)
  		            validar_numeros(hz)
  		            while len(hzz)<10:
  		              hzz=int(input("Reingrese su ID: "))
  		              hz=int(hzz)
  		              validar_numeros(hz)
  		                
  		            c=Cliente(usuario[x],z,hz)
  		            for i in range(60):
  		              print("")
  		            pedidoactual.add_cliente(c)
  		            pedidoactual.imprimirPedido()
  		            lista_pedidos.append(pedidoactual)
  		            pedidoactual=Pedido()
  		            terminar=False
  		            quit()
  		                

  		  else:
  		      print("Ya casi terminamos, solo falta que llenes lo siguiente:\n\n========DATOS DEL COMPRADOR========\n")
  		      h=(str(input("\nNombre Cliente: ")))
  		      validar_letras(h)
  		      zz=(input("Telefono movil: "))
  		      z=int(zz)
  		      validar_numeros(z)
  		      while len(zz)<10:
  		        zz=(input("Reingrese su telefono movil: "))
  		        z=int(zz)
  		        validar_numeros(z)
  		      hzz=(input("ID: "))
  		      hz=int(hzz)
  		      validar_numeros(hz)
  		      while len(hzz)<10:
  		        hzz=(input("Reingrese su ID: "))
  		        hz=int(hzz)
  		        validar_numeros(hz)
  		                
  		      c=Cliente(h,z,hz)
  		      for i in range(60):
  		        print("")
  		      pedidoactual.add_cliente(c)
  		      pedidoactual.imprimirPedido()
  		      lista_pedidos.append(pedidoactual)
  		      pedidoactual=Pedido()
  		      terminar=False
  		      quit()
  			
  	elif seleccion.upper()=='ACOMPAÑAMIENTO':
  		mostrarMenu(ListaAcompañamientos)
  		while True:
  			comida=validar_seleccion(ListaAcompañamientos)
  			if comida == 'COCA COLA':
  				Coca_Cola.imprimirDatos()
  				acompañamiento=Coca_Cola
  			elif comida =='MCFLURRY JET':
  				McFlurry_Jet.imprimirDatos()
  				acompañamiento=McFlurry_Jet
  			elif comida =='MCPAPAS':
  				MCpapas.imprimirDatos()
  				acompañamiento=MCpapas
  			elif comida =='ENSALADA':
  				Ensalada.imprimirDatos()
  				acompañamiento=Ensalada
  			elif comida == 'SUNDAE':
  				Sundae.imprimirDatos()
  				acompañamiento=Sundae
  			print('\n¿Desea confirmar su pedido?')
  			confirmar=validar_seleccion(validaciones)
  			if confirmar == 'SI':
  			  pedidoactual.add_alimento(acompañamiento)
  			  break
  		print('\nPedido solicitado:')
  		print('\n¿Quiere agregar un alimento más a su MCpedido?')
  		addAlimento=validar_seleccion(validaciones)
  		if addAlimento == 'SI':
  			break
  		else:
  		  print('\n¿Desea pagar en efectivo?')
  		  metPago=validar_seleccion(validaciones)
  		  if metPago=='NO':
  		    n_1=0
  		    para_usu=0
  		    para_contra=0
  		    usuario=["juan","brayan","santiago","sebastian","MC"]
  		    capital=[200000,500000,100000,0,0]
  		    contraseña1=["1234","3333","1111","2222"]
  		    r="Bienvenido a Tu Banco💰"
  		    error_1(r)
  		    while True:
  		      try: 
  		        print(time.strftime("%x"))
  		        g=int(input("1.Iniciar Sesión"))
  		        break
  		      except:
  		        a="Error Lo Que Digito No Es Un Numero🤦"
  		        error(a)
  		    while(g>1 or g<1):
  		      a="Numero Digitado No Es Valido Intente Nuevamente 🤦"
  		      error(a)
  		      while True:
  		        try: 
  		          g=int(input("1.Iniciar Sesión"))  
  		          break
  		        except:
  		          a="Error Lo Que Digito No Es Un Numero🤦"
  		          error(a)
  		      (validar_numeros(g))
  		    while g==1:
  		      u=input("digite Usuario🙍:  ")
  		      (validar_letras(u))
  		      c=input("digite contraseña🔑:  ")
  		      m=usuario.count(u)
  		      f=contraseña1.count(c)
  		      if(m==1 and f==0):
  		        print("Contraseña incorrecta🤦")
  		        para_contra=para_contra+1
  		      elif(m==0 and f==1 ):
  		        print("usuario incorrecto🤦")
  		        para_usu=para_usu+1
  		      elif(m==0 and f==0):
  		        print("Usuario y Contraseña Incorrectas🤦")
  		        n_1=n_1+1
  		      if(n_1>4):
  		        print("Mas De 5 Intentos")
  		        i="Lo Sentimos el Sistema no funcionará por 2 horas Intentos Excesivos🤷"
  		        error(i)
  		        d="Llamado a La Policia🚔..."
  		        verde(d)
  		        time.sleep(60)#7200s==2h
  		        n_1=0
  		        g=2
  		        break
  		      if(para_usu>2):
  		        print("Mas De 3 Intentos")
  		        i="Lo Sentimos el sistema se bloqueara por 5 minutos🤷"
  		        error(i)
  		        time.sleep(5)
  		        para_usus=0
  		        g=2
  		        break
  		      if(para_contra>3):
  		        print("Mas De 3 Intentos")
  		        i="Lo Sentimos el sistema se bloqueara por 5 minutos🤷"
  		        error(i)
  		        time.sleep(5)  
  		        para_contra=0
  		        g=2
  		        break
  		      if(m==1 and f==1):
  		        a=usuario.index(u)
  		        b=contraseña1.index(c)
  		        if(a==b):
  		          a="Bienvenido"
  		          verde(a)
  		          print('')
  		          trans="Su transaccion se esta realizando..."
  		          verde(trans)
  		          x=usuario.index(u)
  		          if capital[x]<=0: #AÑADIR VALOR A PAGAR
  		            a="Fondos de cuenta insuficientes, pedido cancelado"
  		            error(a)
  		            quit()
  		          else:
  		            capital[x]=capital[x]-100 #CAMBIAR 100 POR VALOR A PAGAR
  		            print(capital)
  		            a="Transaccion realizada con exito!"
  		            verde(a)
  		            zz=(input("Telefono movil: "))
  		            z=int(zz)
  		            validar_numeros(z)
  		            while len(zz)<10:
  		              zz=int(input("Reingrese su telefono movil: "))
  		              z=int(zz)
  		              validar_numeros(z)
  		            hzz=(input("ID: "))
  		            hz=int(hzz)
  		            validar_numeros(hz)
  		            while len(hzz)<10:
  		              hzz=int(input("Reingrese su ID: "))
  		              hz=int(hzz)
  		              validar_numeros(hz)
  		                
  		            c=Cliente(usuario[x],z,hz)
  		            for i in range(60):
  		              print("")
  		            pedidoactual.add_cliente(c)
  		            pedidoactual.imprimirPedido()
  		            lista_pedidos.append(pedidoactual)
  		            pedidoactual=Pedido()
  		            terminar=False
  		            quit()
  		  else:
  		    print("Ya casi terminamos, solo falta que llenes lo siguiente:\n\n========DATOS DEL COMPRADOR========\n")
  		    h=(str(input("\nNombre Cliente: ")))
  		    validar_letras(h)
  		    zz=(input("Telefono movil: "))
  		    z=int(zz)
  		    validar_numeros(z)
  		    while len(zz)<10:
  		      zz=(input("Reingrese su telefono movil: "))
  		      z=int(zz)
  		      validar_numeros(z)
  		    hzz=(input("ID: "))
  		    hz=int(hzz)
  		    validar_numeros(hz)
  		    while len(hzz)<10:
  		      hzz=(input("Reingrese su ID: "))
  		      hz=int(hzz)
  		      validar_numeros(hz)
  		                
  		    c=Cliente(h,z,hz)
  		    for i in range(60):
  		      print("")
  		    pedidoactual.add_cliente(c)
  		    pedidoactual.imprimirPedido()
  		    lista_pedidos.append(pedidoactual)
  		    pedidoactual=Pedido()
  		    terminar=False
  		    quit()
  	
 
#PARA USAR LOS ATRIBUTOS DE LAS CLASES EN LA FACTURACION, PARA LAS HAMBURGUESAS INVOCARLAS CON => comidaRapida.imprimirDatos() y para los acompañamientos => acompañamiento.imprimirDatos()


	
