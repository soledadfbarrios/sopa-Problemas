import time
import random


class principal:
	print("""
		
			***Bienvenidos a sopa de letras***
			 1.¿Quieres jugar?
			 2.Salir
			 """)
	def menu(self):
		print("""
		
			***Bienvenidos a sopa de letras***
			 1.¿Quieres jugar?
			 2.Salir
			 """)

		opcionmenu1 = int(input("elegir opcion: "))

		if opcionmenu1 == "2":
			print("Salir del programa")
			exit()

		elif opcionmenu1 == "1":
			print("Seleccione modo de juego")
			menu2()

			def menu2():
				print('a- Sopa de letras con sustantivos')
				print('b- Sopa de letras con Adjetivos')
				print('c- Sopa de letras con verbos')

				opcionmenu2= input("Insertar una letra para elegir tema de juego")

				if opcionmenu2 == "a":

					tema2= input("Usted eligio sustantivos")
					sopaletras1=print("""[["v", "e", "n", "t", "i", "l", "a", "d", "o", "r", "w", "f", "p"],
							 ["t", "p", "o", "q", "s", "i", "l", "l", "o", "n", "h", "p", "w"],
							 ["v", "j", "y", "v", "s", "a", "l", "v", "u", "n", "f", "y", "e"],
						 	 ["k", "a", "i", "ñ", "c", "o", "n", "t", "r", "o", "l", "p", "s"],
						     ["b", "u", "i", "p", "q", "a", "s", "l", "o", "t", "r", "i", "u"],
							 ["m", "t", "c", "e", "l", "u", "l", "a", "r", "n", "k", "c", "o"],
							 ["e", "o", "i", "v", "a", "i", "z", "l", "r", "n", "f", "m", "m"],
							 ["s", "j", "i", "v", "s", "t", "e", "r", "m", "o", "g", "n", "j"],
							 ["a", "t", "a", "y", "t", "o", "r", "q", "s", "e", "f", "e", "h"],
							 ["e", "s", "v", "w", "g", "i", "o", "p", "b", "c", "s", "z", "g"],
							 ["s", "g", "r", "a", "n", "d", "e", "i", "f", "k", "v", "m", "a"],
							 ["r", "p", "w", "e", "p", "l", "a", "z", "a", "j", "s", "i", "w"],
							 ["o", "o", "c", "a", "s", "a", "r", "z", "P", "e", "r", "r", "o"],								
							 ["z", "q", "c", "o", "c", "i", "n", "a", "e", "u", "k", "p", "s"],]""")
					inicio = time.time()
					while True:
						preg = input("Ingrese el Adjetivo que encontro:  ")
						if preg == "casa":
							print("La encontraste!. Segui así")
						elif preg == "perro":
							print("La encontraste!. Segui así")
						elif preg == "plaza":
							print("La encontraste!. Segui así")
						elif preg == "ventilador":
							print("La encontraste!. Segui así")
						elif preg == "COCINA":
							print("La encontraste!. Segui así")
						elif preg == "SILLON":
							print("La encontraste!. Segui así")
						elif preg == "MOUSE":
							print("La encontraste!. Segui así")
						elif preg == "termo":
							print("La encontraste!. Segui así")
						elif preg == "auto":
							print("La encontraste!. Segui así")
						elif preg == "mesa":
							print("La encontraste!. Segui así")
						elif preg == "control":
							print("La encontraste!. Segui así")
						elif preg == "celular":
							print("La encontraste!. Segui así")						
						else:
							print("La palabra no se encuentra en la sopa de letras, segui buscando")

					final = time.time()
					if final - inicio >= 200:
						print("")
						print("se te acabo el tiempo")

						elif opcionmenu2 == "b":
							tema3= input("Usted eligio Adjetivos")
							sopaletras2=print("""   [["a", "m", "a", "b", "l", "e", "a", "r", "o", "i", "l", "n", "u", "e", "v", "o"],	
										["b", "s", "d", "ñ", "c", "k", "p", "d", "i", "v", "e", "r", "t", "i", "d", "o"],	
										["c", "t", "a", "l", "t", "o", "r", "q", "s", "c", "t", "s", "a", "a", "e", "q"],	
										["o", "s", "v", "w", "g", "i", "o", "p", "b", "a", "r", "v", "g", "s", "y", "e"],	
										["p", "g", "r", "a", "n", "d", "e", "i", "f", "l", "y", "ñ", "r", "o", "j", "o"],	
										["r", "p", "h", "e", "r", "m", "o", "s", "o", "h", "f", "l", "a", "c", "o", "w"],	
										["a", "o", "u", "d", "f", "g", "r", "z", "r", "s", "a", "d", "w", "g", "i", "r"],	
										["k", "f", "e", "o", "g", "x", "t", "a", "e", "u", "h", "c", "y", "r", "c", "l"],	
										["f", "e", "l", "i", "z", "u", "y", "p", "e", "q", "u", "e", "ñ", "o", "i", "u"],
										["q", "a", "l", "i", "m", "p", "i", "o", "t", "a", "w", "t", "r", "x", "z", "j"],]""")

							inicio= time.time()
							while True:
									preg = input("Ingrese el Adjetivo que encontro:  ")
									if preg == "AMABLE":
										print("La encontraste!. Segui así")
									elif preg == "nuevo":
										print("La encontraste!. Segui así")
									elif preg == "divertido":
										print("La encontraste!. Segui así")
									elif preg == "alto":
										print("La encontraste!. Segui así")
									elif preg == "grande":
										print("La encontraste!. Segui así")
									elif preg == "rojo":
										print("La encontraste!. Segui así")
									elif preg == "flaco":
										print("La encontraste!. Segui así")
									elif preg == "hermoso":
										print("La encontraste!. Segui así")
									elif preg == "feo":
										print("La encontraste!. Segui así")
									elif preg == "feliz":
										print("La encontraste!. Segui así")
									elif preg == "PEQUEÑO":
										print("la encontraste!. Segui así")
									elif preg == "limpio":
										print("la encontraste!. Segui así")							
									else:
										print("La palabra no se encuentra en la sopa de letras, segui buscando")
						
						final= time.time()
						if final - inicio >= 200:
							print("")
							print("se termino el tiempo")

							elif opcionmenu2 == "c":
								tema1= input("Usted eligio verbos")
								sopaletras3=print("""	[["a", "l", "i", "m", "p", "i", "a", "r", "o", "t", "q", "g", "f", "l", "k", "d"],
										  	["b", "x", "r", "u", "q", "a", "x", "c", "h", "l", "m", "i", "r", "a", "r", "ñ"],
							   			  	["c", "t", "e", "s", "t", "u", "d", "i", "a", "r", "j", "a", "e", "h", "i", "p"],
											["o", "s", "v", "w", "g", "i", "o", "p", "b", "s", "x", "ñ", "d", "k", "l", "u"],
											["r", "k", "a", "q", "s", "t", "g", "a", "r", "l", "q", "a", "m", "a", "r", "f"],
											["r", "p", "y", "r", "e", "u", "p", "b", "f", "g", "y", "f", "b", "j", "v", "u"],
											["e", "o", "c", "o", "c", "i", "n", "a", "r", "j", "n", "v", "ñ", "l", "o", "i"],
											["r", "q", "s", "d", "g", "J", "u", "g", "a", "r", "m", "q", "f", "u", "z", "b"],
											["s", "t", "w", "k", "l", "x", "j", "p", "e", "ñ", "a", "c", "o", "m", "e", "r"],
											["h", "R", "e", "i", "r", "b", "f", "i", "d", "l", "r", "p", "b", "r", "t", "l"],
											["u", "a", "r", "b", "ñ", "q", "r", "d", "o", "r", "m", "i", "r", "k", "x", "p"],
											["w", "ñ", "a", "c", "p", "a", "t", "y", "z", "s", "a", "l", "t", "a", "r", "u"],
											["z", "l", "h", "a", "b", "l", "a", "r", "b", "j", "y", "u", "v", "n", "j", "i"],]""")

								inicio = time.time()
								while True:
									preg = input("Ingrese el Adjetivo que encontro:  ")
									if preg == "limpiar":
										print("La encontraste!. Segui así")
									elif preg == "mirar":
										print("La encontraste!. Segui así")
									elif preg == "estudiar":
										print("La encontraste!. Segui así")
									elif preg == "amar":
										print("La encontraste!. Segui así")
									elif preg == "jugar":
										print("La encontraste!. Segui así")
									elif preg == "cocinar":
										print("La encontraste!. Segui así")
									elif preg == "reir":
										print("La encontraste!. Segui así")
									elif preg == "dormir":
										print("La encontraste!. Segui así")
									elif preg == "saltar":
										print("La encontraste!. Segui así")
									elif preg == "hablar":
										print("La encontraste!. Segui así")
									elif preg == "correr":
										print("la encontraste!. Segui así")
									elif preg == "comer":
										print("la encontraste!. Segui así")	
									else:
										print("La palabra no se encuentra en la sopa de letras, segui buscando")

										final = time.time()
										if final - inico >=200:
											print("")
											print("se te termino el tiempo")
		
		temas()
		while op != "A" and op != "B" and op != "C":
			print ("Opcion incorrecta, ingrese una opcion valida")
			op = input("Ingrese una opción: ->  ")
		elif  opcion == "2":
			print("Saliste de la Sopa de Letras")
			print("Intentalo Pronto!!!!")
			exit()
		temas()	
#sopaletras=[[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
#			[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
#			[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
#			[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
#			[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
#			[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
#			[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
#			[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],]

#sopa_letras= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]