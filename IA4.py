def GetAsig(prof):#1
	if prof < len(Alumnos):
		for i in examenes:
			Asignacion[Alumnos[prof]] = i # juan 2, jorge 1 diana 0
			GetAsig(prof + 1)  # 1 + 1 = 2
	else:
		print(Asignacion) # juan 2 jorge 1 diana 3
	
	
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
	 
GetAsig(0)
