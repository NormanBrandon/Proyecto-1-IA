def cost(Asig):
	exdif =[] #lista vacia llamada examenes distintos abreviado
	for alumno in Alumnos: 
		if Asig.get(alumno) not in exdif: #si el examen asignado al alumno N no esta en la lista, agregarlo
			exdif.append(Asig.get(alumno))

	costo = len(exdif)#exdif contendra solo examenes distintos, no repetidos, por lo tanto su longitud es el numero de examenes asignados y eso corresponde al coste
	return costo

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
			print(cost(Asignacion))
		

Problema ={
	'Juan':['Jorge','Diana'],
	'Jorge':['Juan','Laura'],
	'Diana':['Jorge'],
	'Laura':['Jorge'],
	'Carlos':[]
}
examenes=[]

Asignacion = {}

Alumnos = list(Problema.keys())#Hacemos una lista con los alumnos 
i=0
for alumno in Problema.keys(): #inicializamos el diccionario de asignaciones con los alumnos, asignando 0 a todos (no se ha asignado examen)
	Asignacion[alumno] = 0
	i = i +1
	examenes.append(i)
GetAsig(0)
