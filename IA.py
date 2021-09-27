examenes=[1,2,3,4,5]
Problema ={ # es la definición del problema, a cada clave (alumno) se le relaciona una lista de amigos
	'Juan':['Jorge','Diana','Laura'],
	'Jorge':['Juan'],
	'Diana':['Jorge','Laura'],
	'Laura':['Diana','Juan'],
	'Carlos':[]	
}
Asignacion = {} # se inicia un diccionario vacio para agregar la asignación
for node in Alumnos.keys(): #inicializamos el diccionario de asignaciones con los alumnos, asignando 0 a todos (no se ha asignado examen)
	Asignacion[node] = 0
print("Asignación Inicial: ")
print(Asignacion)

print(examenes)
print(Asignacion)