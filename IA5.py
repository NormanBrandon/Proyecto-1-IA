def IsValid(Asig):
	for alumno in Alumnos:
		for friend in Problema.get(alumno):
			if Asig.get(friend) == Asig.get(alumno):
				return 0
	return 1	

def GetAsig(prof):
	if prof < len(Alumnos):
		for i in examenes:
			Asignacion[Alumnos[prof]] = i
			GetAsig(prof +1) 
	else:
		if IsValid(Asignacion):
			print(Asignacion)
		

examenes=[1,2,3]
Problema ={
	'Juan':['Jorge','Diana'],
	'Jorge':['Juan','Laura'],
	'Diana':['Jorge'],
	'Laura':['Jorge'],
	'Carlos':[]
}
Asignacion = {}
Alumnos = list(Problema.keys())#Hacemos una lista con los alumnos 
for alumno in Problema.keys(): #inicializamos el diccionario de asignaciones con los alumnos, asignando 0 a todos (no se ha asignado examen)
	Asignacion[alumno] = 0
	 
GetAsig(0)
