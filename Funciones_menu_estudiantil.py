import datetime as tm
import webbrowser as wb

def studentsInfo(file):
    '''Esta funcion tiene como parametro principal el nombre del archivo txt donde esta la informacion
    de los estudiantes, de esta se deriva un diccionario donde toda la informacion de los estudiantes,
    donde las claves seran las cedulas y los valores los nombres de cada estudiante, y una lista con todas
    las cedulas'''
    openFile=open(file)
    dicInfo={}
    students=[]
    
    for i in openFile:
        if i=='\n':
            pass
        else:
            dicInfo[i[:i.find(";")]]=i[i.find(";")+1:-1]
            students.append(i[:i.find(";")])
    openFile.close()          
    return [dicInfo,students]

def coursesInfo(file):
    """Esta funcion tiene como parametro principal el nombre del archivo txt donde esta la informacion
    de los cursos, de esta se deriva un diccionario donde como valores tendremos una tupla con
    los creditos y el total de notas del cada curso y conjunto de listas con la cedula de cada estudiante
    y sus respectivas notas, y una lista con todos los nombres de los cursos"""
    openFile=open(file)
    subject={}
    courses=[]
    for i in openFile:
        if i=='\n' or i=="":
            pass
        elif i[0].isalpha():
            j=i[0:i.index(";")]
            subject[j]=[tuple(i[i.index(";")+1:-1].split(";"))]
            courses.append(j)
        else:
            i=i[:-1]
            subject[j].append(i.split(";"))
    openFile.close()
    return [subject,courses]


def database():
    """Esta funcion une las 2 bases de datos principales que son la de los cursos y la de los estudiantes
    y retorna un diccionario donde las claves seran Cursos y Estudiantes y cada uno tiene su respectiva
    informacion"""
    courses=coursesInfo("subjects.txt")
    students=studentsInfo("students.txt")
    database_1={"Cursos":courses,"Estudiantes":students}
    return database_1
   
'''def deleteCharacter(character,character2,word):
    Esta funcion tiene como funcionamiento basico eleminar 2 caracteres 
    dados de un string igualmente dado, como variables tenemos a info que es un string
    vacio que ira almacenando un nuevo string sin los caracteres dados como parametros, 
    retorna la cadena nueva.
    info=""
    word=word[:-1]
    for j in word:
        if j==character or j==character2:
            pass
        else:
            info=info+j
    return info '''

def coursesPath(database,student):
    """Esta funcion tiene como parametros de entrada la base de datos completa y el nombre del
    estudiante, esta funcion busca entre todo el diccionario de cursos a ver a cuales pertenece el
    estudiante, y apartir de aqui se añaden a un acumulador la cantidad de creditos de todos los cursos 
     y todas las notas para asi sacar un parte del promedio del estudiante"""
    studentSubject=[]
    totalCredits=0
    credit_finalNote=0
    for i in database["Cursos"][1]:
        finalNote=0
        for j in database["Cursos"][0][i]:
            if type(j)==type(()):
                creditNotes=j
            else:
                if j[0]==student:
                    studentSubject.append(i)
                    totalCredits=totalCredits+int(creditNotes[0])
                    totalNotes=0
                    for h in j:
                        if h==student:
                            pass
                        else:
                            finalNote=finalNote+float(h)
                            totalNotes=int(creditNotes[1])
                    if totalNotes==0:
                        pass
                    else:
                        finalNote=finalNote/totalNotes
                        credit_finalNote=credit_finalNote+finalNote*int(creditNotes[0])
    return [totalCredits,credit_finalNote,studentSubject]

def finalNotes(database,student,course):
    """ Esta funcion tiene como parametros de entrada la base de datos completa, student que el estudiante
    al que le vamos a sacar su nota fiaal de un curso especifico, en este caso course especifica este 
     haciendo uso de las notas totales que tiene cada curso y de las notas que presente cada estudiante"""
    finalNote=0
    for i in database["Cursos"][0][course]:
        if type(i)==type(()):
            totalNotes=i
            pass
        else:
            if i[0]==student:
                for j in i:
                    if j==student:
                        pass
                    else:
                        finalNote=finalNote+float(j)
    finalNote=finalNote/int(totalNotes[1])
    return finalNote
def limits(cedula,limit):
    """Esta funcion tiene como parametros de entrada, cedula que es el dato que vamos a verificar y
    limit que es el limite de datos que se supone que debe haber en el dato, se verifica primero que sean
    todos numeros y que no contengan espacio, despues que este dato no se pase del limite o sea menor a este
    """
    if cedula.isdigit():
        if len(cedula)!=limit:
            return False
        else:
            return True
    else:
        return False

def name(name):
    """Esta funcion tiene como paramtro de entrada un string, al cual se le verificara que tiene al menos 
    un espacio que separara el nombre del apellido, y verifica si en el nombre hay numeros o caracteres 
    para retornar un false si no presenta ningun tipo de error, saldra del bucle y retornara true"""
    if " " not in name:
        return False
    numbers=["1","2","3","4","5","6","7","8","9","0"]
    caracter=["$","#",".",",","-","]","[","}","{","*","+","´"]
    for i in name:
        if i in numbers:
            return False
        elif i in caracter:
            return False
    return True
    
def returnStudents(database_1):
    """Esta funcion tiene como parametro de entrada la base de datos completa, la limitaremos para
    utilizar la informacion de los estudiantes, y de esta forma situar la informacion como en las 
    plantillas para poder ser guardada"""
    students_Id=database_1["Estudiantes"][1]
    txt=""
    for i in students_Id:
        student_Name=database_1["Estudiantes"][0][i]
        result=i+";"+student_Name
        txt=txt+result+'\n'
    return txt

def returnCourses(database_1):
    """Como parametro de entrada tendremos a database_1 que es la base de datos completa, la limitaremos 
    a utilizar la informacion de los cursos para ir desglosando su informacion y poniendola en una variable
    vacia, para que quede como en la plantilla"""
    courses=database_1["Cursos"]
    txt=""
    for i in courses[1]:
        txt=txt+i+";"+courses[0][i][0][0]+";"+courses[0][i][0][1]+'\n'
        for j in courses[0][i]:
            if type(j)==type(()):
                pass
            else:
                txt_1=""
                for h in j:
                    txt_1=txt_1+h+";"
                txt_1=txt_1[:-1]
                txt=txt+txt_1+'\n'
        txt=txt+'\n'
    return txt
    return txt
                
def saveFile(File,message):
    """Como parametros de entrada tenemos a file que es el nombre del documento en el que guardaremos
    la informacion, y message que es la informacion que escribiremos en el documento"""
    file=open(File,"w")
    file.write(message)
    file.close()

def htmlVis(database,student):
    #basic='<!DOCTYPE html><html><title>W3.CSS</title><meta name="viewport" content="width=device-width, initial-scale=1"><body><div class="w3-container"><h1 style="text-align: center">Reporte Final de notas</h1><h3 style="text-align: center">Informacion del estudiante</h3><h4 style="text-align: center">Nombre del estudiante: </h4><h4 style="text-align: center">Cedula del estudiante: </h4><h2 style="text-align: center">Reporte Notas</h2><table class="w3-table"><tr style="text-align: center"><th>Curso</th><th style="text-align: center">Creditos</th><th style="text-align: center">Nota Final</th></tr>'
    date=str(tm.datetime.now())
    date=date[:-7]
    average=coursesPath(database,student)
    basic="""<!DOCTYPE html>
    <html>
    <head>
    <title>Page Title</title>
   <style>
	h1,h3,h4,th,td,p{text-align: center}
    th{font-size: 20px}
    table{
    	margin-left: auto; 
        margin-right: auto; 
        width: 90%; 
        border-collapse: collapse;
    }
    tr,th,td{
        border: 1px solid grey;
        border-collapse: collapse;
    }
    tr:nth-child(even) {
  		background-color: #eee;
	}
	tr:nth-child(odd) {
 		background-color: #fff;
	}
    </style>
    </head>
    <body>
    <h1>Reporte final de notas</h1>
    <h4>Informacion del estudiante</h4>
    <p>Estudiante: """+database["Estudiantes"][0][student]+"""</p>
    <p>Cedula :"""+student+""" </p>
    <h4>Reporte notas </h4>
    <table>
    	<tr>
          <th>Nombre</th>
          <th>Creditos</th>
          <th>Nota final</th>
        </tr>
    
    """
    rest="""</table>    
    <table>
        <tr>
            <th colspan="3">Promedio actual</th>
        </tr>
    </table>
    <table>
      <tr>
          <th colspan=="3">{average:.2f}""".format(average=average[1]/average[0])+"""</th>
      </tr>
    </table>
    </div>
    </body>
    </html>"""
    
    date=date.replace(":",".")
    nameFile=date+"-"+database["Estudiantes"][0][student]+"-"+student
    nameFile_1=nameFile+".html"
    file=open(nameFile_1,'w')
    info=coursesPath(database,student)[2]
    txt=""
    for i in info:
        note=finalNotes(database,student,i)
        txt=txt+"<tr><td>"+i+"</td>"+"<td>"+database["Cursos"][0][i][0][0]+"</td>"+"<td>{notes:.2f}</td>".format(notes=note)+"</tr>"
    txt=basic+txt+rest
    file.write(txt)
    file.close()
    wb.open_new_tab(nameFile_1)
