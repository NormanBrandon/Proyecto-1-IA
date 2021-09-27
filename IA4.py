##Este programa obtiene todos los nodos hoja del árbol de estados, es decir, todas las asignaciones completas
## Lo hace para n alumnos gracias a la función recursiva
def GetAsig(prof):# Funcion recursiva búsqueda en profundidad
	if prof < len(Alumnos):# si la profundidad del árbol de búsqueda aún no es la máxima (no hemos llegado a los nodos hoojas)
		for i in examenes: # iterando en los valores de los posibles exámenes [1 2 3]
			Asignacion[Alumnos[prof]] = i #se le asigna el valor de el examen i al alumno de profundidad prof, p.e Juan tiene profundidad 0, Jorge profundidad 1, Diana profundidad 2 en ele arbol de estados
			GetAsig(prof + 1)  # Se llama a esta misma funcion para bajar en profundidad, sumando profundidad más 1, así se baja en el arbol de estados
	else:					# si la profundidad es máxima tenemos una asignación completa (se ha asignado un examen a cada alumno)
		print(Asignacion) # Imprimimos la asignación completa 
	
		
examenes=[1,2,3]
Problema ={
	'Juan':['Jorge','Diana'],
	'Jorge':['Juan','Laura'],
	'Diana':['Jorge'],
	'Laura':['Jorge'],
	'Carlos':[]
}
Asignacion = {}
Alumnos = list(Problema.keys())#Hacemos una lista con los alumnos [Juan, Jorge, Diana, Laura, Carlos] 
for alumno in Problema.keys(): #inicializamos el diccionario de asignaciones con los alumnos, asignando 0 a todos (no se ha asignado examen)
	Asignacion[alumno] = 0
	 
GetAsig(0)# llamamos a la funcion recursiva iniciando con una profundidad 0
