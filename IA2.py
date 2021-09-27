from queue import Queue

examenes=[1,2,3]#lista de exámenes
Asignacion = {}#inicialización de diccionario de asignación vacio
Problema = {
	'Juan':['Jorge','Diana'],
	'Jorge':['Juan'],
	'Diana':['Juan'],
}
#Problema.keys obtiene todos los alumnos del problema
for node in Problema.keys(): #inicializamos el diccionario de asignaciones con los alumnos, asignando 0 a todos (no se ha asignado examen)
	Asignacion[node] = 0 # Asigna 0 a cada alumno, donde node el es alumno, rellena el diccionario

print(Asignacion)#imprime ['Juan':0,'Jorge':0,'Diana':0], el diccionario tiene el formato adecuado en este punto
	 
for i in examenes: #iteramos 3 veces; i itera en la lista [1 2 3]
	Asignacion['Juan'] = i #asignamos el valor de i a Juan en el diccionario de asignacion
	for j in examenes: #iteramos 3 veces; j itera en la lista [1 2 3]
		Asignacion['Jorge'] = j	#asignamos el valor de j a Juan en el diccionario de asignacion
		for k in examenes: # iteramos 3 veces; k itera en la lista [1 2 3]
			Asignacion['Diana'] = k # asignamos el valor de k a Juan en el diccionario de asignacion
			print(Asignacion) # imprime la asignación Final	
		print()
		
