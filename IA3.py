def IsValid(Asig):
	for alumno in Alumnos:
		for friend in Problema.get(alumno):
			if Asig.get(friend) == Asig.get(alumno):
				return 0
	return 1			
			

examenes=[1,2,3]
Problema ={
	'Juan':['Jorge','Diana'],
	'Jorge':['Juan'],
	'Diana':['Juan'],}

Asignacion = {}
Alumnos = list(Problema.keys()) #Lista que contiene los alumnos [Juan, Jorge, Diana]


for node in Problema.keys(): #inicializamos el diccionario de asignaciones con los alumnos, asignando 0 a todos (no se ha asignado examen)
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
		
