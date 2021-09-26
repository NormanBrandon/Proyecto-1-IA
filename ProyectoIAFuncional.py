def cost(Asig):
	numexa =[]
	for alumno in Alumnos:
		if Asig.get(alumno) not in numexa:
			numexa.append(Asig.get(alumno))

	costo = len(numexa)
	return costo

def IsValid(Asig):
	for alumno in Alumnos:
		for friend in Problema.get(alumno):
			if Asig.get(friend) == Asig.get(alumno):
				return 0
	return 1	

def GetAsig(prof):
	global costmin

	if prof < len(Alumnos):
		for i in examenes:
			Asignacion[Alumnos[prof]] = i
			GetAsig(prof +1) 
	else:
		if IsValid(Asignacion):
			costoactual = cost(Asignacion)
			if  costoactual < costmin:
				costmin = costoactual
				print("Una asignación optima es: "+str(Asignacion))
				print("Su costo : " + str(costoactual))
				
			


Problema ={
	'Juan':['Jorge','Diana'],
	'Jorge':['Juan','Laura'],
	'Diana':['Jorge'],
	'Laura':['Jorge'],
	'Carlos':[]
}
#Problema ={
#	'Juan':['Jorge','Diana'],
#	'Jorge':['Juan'],
#	'Diana':['Juan'],
#}

examenes=[]

Asignacion = {}

Alumnos = list(Problema.keys())#Hacemos una lista con los alumnos 
i=0
for alumno in Problema.keys(): #inicializamos el diccionario de asignaciones con los alumnos, asignando 0 a todos (no se ha asignado examen)
	Asignacion[alumno] = 0
	#bestAsig[alumno] = 0 
	i = i +1
	examenes.append(i)

costmin =len(examenes)

GetAsig(0)
