def IsValid(Asig):	#testea si una asignación cumple con las restricciones
	for alumno in Alumnos:	# itera sobre todos los alumnos [Juan, Jorge,Diana]
		for friend in Problema.get(alumno): # obtiene los amigos del alumno en ese momento
			if Asig.get(friend) == Asig.get(alumno): #compara el examen asignado de un amigo con el alumno
				return 0				#si 2 amigos tienen el mismo examen se habrán violado las restricciones, por lo tanto la funcion devuelve 0
	return 1 # si ningún par de amigos han tenido el mismo examen, devuelve 1
			

examenes=[1,2,3]
Problema ={
	'Juan':['Jorge','Diana'],
	'Jorge':['Juan'],
	'Diana':['Juan'],}

Asignacion = {}
Alumnos = list(Problema.keys())


for node in Problema.keys(): 
	Asignacion[node] = 0
	 
for i in examenes:
	Asignacion['Juan'] = i
	for j in examenes:
		Asignacion['Jorge'] = j	
		for k in examenes:
			Asignacion['Diana'] = k
			if (IsValid(Asignacion)):
				print(Asignacion)

		print()
		
