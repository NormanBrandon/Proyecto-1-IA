from queue import Queue

def IsValid(Asig):
	for alumno in Amigos:
		for friend in Alumnos.get(alumno):
			if Asig.get(friend) == Asig.get(alumno):
				return 0
	return 1			
			

examenes=[1,2,3]
amigos =[]
alumnos_visitados =[]
Alumnos ={
	'Juan':['Jorge','Diana'],
	'Jorge':['Juan'],
	'Diana':['Juan'],

}
Asignacion = {}
Amigos = list(Alumnos.keys());
for node in Alumnos.keys(): #inicializamos el diccionario de asignaciones con los alumnos, asignando 0 a todos (no se ha asignado examen)
	Asignacion[node] = 0
	 
Amigos1 = list(Alumnos.keys())
Amigos1.remove('Juan')	
for i in examenes:
	Asignacion['Juan'] = i
	for j in examenes:
		Asignacion['Jorge'] = j	
		for k in examenes:
			Asignacion['Diana'] = k
			if (IsValid(Asignacion)):
				print(Asignacion)

		print()
		
