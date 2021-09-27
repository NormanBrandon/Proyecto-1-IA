
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

def getCostMin():
	global costmin
	return costmin
def setCostmin(value):
	global costmin
	costmin = value
def getBestAsig():
	global mejorAsig
	return mejorAsig
def setBestAsig(value):
	global mejorAsig
	mejorAsig = value

def GetAsig(prof):

	if prof < len(Alumnos):
		for i in examenes:
			Asignacion[Alumnos[prof]] = i
			GetAsig(prof +1) 
	else:
		if IsValid(Asignacion):
			if  cost(Asignacion) < getCostMin():
				setCostmin(cost(Asignacion))
				setBestAsig(Asignacion)
				print("Una asignación optima es: "+str(getBestAsig()))
				print("Su costo : " + str(cost(getBestAsig())))
				

mejorAsig ={}

Problema ={
	'Juan':['Jorge','Diana'],
	'Jorge':['Juan'],
	'Diana':['Juan'],
}

examenes=[] # [1,2,3,4,5]

Asignacion = {}

Alumnos = list(Problema.keys())#Hacemos una lista con los alumnos 
i=0
for alumno in Problema.keys(): #inicializamos el diccionario de asignaciones con los alumnos, asignando 0 a todos (no se ha asignado examen)
	Asignacion[alumno] = 0 
	i = i +1
	examenes.append(i)

costmin =100000#5

GetAsig(0)
