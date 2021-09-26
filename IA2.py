from queue import Queue

examenes=[1,2,3]
amigos =[]
alumnos_visitados =[]
Asignacion = {}

Alumnos = 
{
	'Juan':['Jorge','Diana'],
	'Jorge':['Juan'],
	'Diana':['Juan'],
}

for node in Alumnos.keys(): #inicializamos el diccionario de asignaciones con los alumnos, asignando 0 a todos (no se ha asignado examen)
	Asignacion[node] = 0
print(Asignacion)
	 

for i in examenes:
	Asignacion['Juan'] = i
	for j in examenes:
		Asignacion['Jorge'] = j	
		for k in examenes:
			Asignacion['Diana'] = k
			print(Asignacion)
		print()
		
