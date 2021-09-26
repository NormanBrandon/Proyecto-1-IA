from queue import Queue

examenes=[]
amigos =[]
alumnos_visitados =[]
Alumnos ={
	'Juan':['Jorge','Diana','Laura'],
	'Jorge':['Juan'],
	'Diana':['Jorge','Laura'],
	'Laura':['Diana','Juan'],
	'Carlos':[]	
}
Asignacion = {}
for node in Alumnos.keys(): #inicializamos el diccionario de asignaciones con los alumnos, asignando 0 a todos (no se ha asignado examen)
	Asignacion[node] = 0
print("Asignación Inicial: ")
print(Asignacion)

print(examenes)
print(Asignacion)