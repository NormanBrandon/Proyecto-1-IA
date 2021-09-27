def cost(Asig):
	numexa =[] #lista con asignaciones distintas [5, 2, 1, 4] = 4
	for alumno in Alumnos: #Iteramos en [Juan, Jorge, Diana, laura, Carlos]
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
