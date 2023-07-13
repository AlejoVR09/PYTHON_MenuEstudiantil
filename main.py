import Funciones_menu_estudiantil as bd

database=bd.database()
print(database)
while True:
    print("\nBASE DE DATOS ESTUDIANTIL\n\n1.Menu de estudiantes\n2.Menu de cursos\n3.Salir")
    choice=input("Digite la opcion: ")
    if choice=="1":
        while True:
            print("\nMENU DE ESTUDIANTES\n\n1.Agregar estudiante\n2.Estudiantes registrados\n3.Informacion de estudiantes\n4.Salir")
            choice_1=input("Digite la opcion: ")
            idStudents=database["Estudiantes"][1]
            if choice_1=="1":
                nameStudent=input("Digite el nombre del estudiante: ")
                while bd.name(nameStudent)==False:
                    nameStudent=input("Digite el nombre del estudiante: ")
                    
                idStudent=input("Digite la cedula del estudiante: ")
                while bd.limits(idStudent,10)==False:
                    idStudent=input("Digite la cedula del estudiante: ")
                if idStudent in idStudents:
                    print("Este estudiante ya esta registrado.")
                    continue
                
                database["Estudiantes"][1].append(idStudent)
                database["Estudiantes"][0][idStudent]=nameStudent
                
            elif choice_1=="2":
                j=1
                print()
                for i in idStudents:
                    print(str(j)+"."+str(i)+": "+database["Estudiantes"][0][i])
                    j=j+1
                print("\nPresione ENTER para continuar: ")
                input()
            elif choice_1=="3":
                j=1
                list_1=[]
                print()
                for i in idStudents:
                    print(str(j)+"."+str(i)+": "+database["Estudiantes"][0][i])
                    list_1.append(str(j))
                    j=j+1
                choice_e1=input("Seleccione un estudiante: ")
                while choice_e1 not in list_1:
                    choice_e1=input("Seleccione un estudiante: ")
                choice_e1=int(choice_e1)-1
                estudiante_2=idStudents[choice_e1]
                while True:
                    print("\n1.Promedio de estudiante\n2.Matricular estudiante a un curso\n3.Ingresar notas de un curso\n4.Cursos matriculados del estudiante\n5.Generar informacion del estudiante\n6.Salir\n")
                    choice_2=input("Digite la opcion: ")
                    coursesStudent=bd.coursesPath(database,estudiante_2)
                    if choice_2=="1":
                        average_1=bd.coursesPath(database,estudiante_2)
                        if average_1[0]==0:
                            print("\nEl estudiante no esta matriculado en ningun curso\n")
                            print("\nPresiones ENTER para continuar: ")   
                            input()
                        else:
                            average=average_1[1]/average_1[0]
                            print("\nESTUDIANTE\n"+database["Estudiantes"][0][estudiante_2]+":"+estudiante_2+"\n\nPromedio semestre actual: {0:.2f}".format(average))
                            print("\nPresiones ENTER para continuar: ")   
                            input()
                    elif choice_2=="2":
                        matriculateCourses=[]
                        index_s=[]
                        j=1
                        for i in database["Cursos"][1]:
                            if i not in coursesStudent[2]:
                                matriculateCourses.append(i)
                                index_s.append(str(j))
                                j=j+1
                        if len(matriculateCourses)==0:
                            print("No hay cursos dispobles para este estudiante.")
                        else:
                            j=1
                            print("\nCURSOS DISPONIBLES\n")
                            for i in matriculateCourses:
                                print(str(j)+"."+i.title())
                                j=j+1
                            choice_4=input("Seleccione el curso o ingrese q para salir: ")
                            if choice_4=="q":
                                continue
                            else:
                                while choice_4 not in index_s:
                                    choice_4=input("Seleccione el curso o ingrese format q para salir: ")
                                database["Cursos"][0][matriculateCourses[int(choice_4)-1]].append([estudiante_2])
                    elif choice_2=="3":
                        matriculateCourses=[]
                        index_s=[]
                        j=1
                        for i in database["Cursos"][1]:
                            if i in coursesStudent[2]:
                                matriculateCourses.append(i)
                                index_s.append(str(j))
                                j=j+1
                        if len(matriculateCourses)==0:
                            print("No hay cursos dispobles para este estudiante.")
                        else:
                            j=1
                            print("\nCURSOS MATRICULADOS\n")
                            for i in matriculateCourses:
                                print(str(j)+"."+i.title())
                                j=j+1
                            choice_4=input("Seleccione el curso: ")
                            while choice_4 not in index_s:
                                choice_4=input("Seleccione el curso: ")
                        position=database["Cursos"][0][matriculateCourses[int(choice_4)-1]]
                        for h in position:
                            if h[0]==estudiante_2:
                                position=database["Cursos"][0][matriculateCourses[int(choice_4)-1]][position.index(h)]
                                position_1=database["Cursos"][0][matriculateCourses[int(choice_4)-1]].index(h)
                        maxNotes=int(database["Cursos"][0][matriculateCourses[int(choice_4)-1]][0][1])
                        minusNotes=(maxNotes+1)-len(position[0:])
                        if minusNotes==0:
                            print("\nEl estudiante tiene todas las notas del curso")
                            print("\nPresione ENTER para continuar: ")
                            input()
                        else:
                            comp=0
                            print("NOTAS DISPONIBLES: "+str(minusNotes))
                            for j in range(0,minusNotes):
                                if comp==1:
                                    break
                                notes=""
                                while True:
                                    try:
                                        notes=input("Digite la nota o q para salir: ")
                                        if notes=="q":
                                            comp=1
                                            break
                                        else:
                                            notes=float(notes)
                                    except ValueError:
                                        print("Solo numeros.")
                                    else:
                                         if notes<0 or notes>5:
                                            print("Rango (0 hasta 5).")
                                            continue
                                         else:
                                            database["Cursos"][0][matriculateCourses[int(choice_4)-1]][position_1].append(str(notes))
                                            break
                                
                        print("\nDATOS INGRESADOS\n\nPresione ENTER para continuar: ")
                        input()
                        
                    elif choice_2=="4":
                        j=1
                        print("\nMATERIAS MATRICULADAS POR: "+database["Estudiantes"][0][estudiante_2]+"\n")
                        for i in coursesStudent[2]:
                            print(str(j)+"."+i.title())
                            j=j+1
                        print("\nPresione ENTER para continuar: ")
                        input()
                    elif choice_2=="5":
                        bd.htmlVis(database,estudiante_2)
                    elif choice_2=="6":
                        break
            elif choice_1=="4":
                break
    elif choice=="2":
        while True:
                print("\nMENU DE CURSOS\n\n1.Crear curso nuevo\n2.Cursos registrados\n3.Porcentaje de estudiantes que aprueba un curso\n4.Estudiantes matriculados en un curso\n5.Salir")
                choice_3=input("Digite la opcion: ")
                courses=database["Cursos"][1]
                if choice_3=="1":
                    courseName=input("Digite el nombre del curso: ").lower()

                    if courseName in courses:
                        print("Ese curso ya existe")
                        continue
                    else:
                        credit=""
                        while bd.limits(credit,1)==False:
                            credit=input("Digite el numero de creditos que tendra el curso(maximo 9): ")
                        notes=""
                        while bd.limits(notes,1)==False:
                            notes=input("Digite el numero de notas que tendra el curso(maximo 9): ")
                        database["Cursos"][1].append(courseName)
                        database["Cursos"][0][courseName]=[(credit,notes)]
                elif choice_3=="2":
                    print()
                    j=1
                    for i in courses:
                        print(str(j)+"."+i+"---"+"Creditos: "+str(database["Cursos"][0][i][0][0]))
                        j=j+1
                    print("\nPresione ENTER para continuar: ")
                    input()
                elif choice_3=="3":
                    print()
                    
                    j=1
                    index_s=[]
                    for i in courses:
                        print(str(j)+"."+i)
                        index_s.append(str(j))
                        j=j+1           
                    choice_course1=input("Seleccione el curso: ")
                    while choice_course1 not in index_s:
                        choice_course1=input("Seleccione el curso: ")
            
                    winners=0
                    losers=0
                    totalStudents=0

                    for i in database["Cursos"][0][courses[int(choice_course1)-1]][1:]:
                        validatedNote=bd.finalNotes(database,i[0],courses[int(choice_course1)-1])
                        if validatedNote<3.0:
                            losers=losers+1
                        else:
                            winners=winners+1
                        totalStudents=totalStudents+1 
                    if totalStudents==0:
                        print("Este curso no tiene estudiantes matriculadoss.")
                    else:
                        print("Porcentaje de estudiante que ganan el curso: "+str((winners/totalStudents)*100)+"%")
                        print("Porcentaje de estudiante que pierden el curso: "+str((losers/totalStudents)*100)+"%")    
                        print("Presione ENTER para continuar: ")
                        input()
                elif choice_3=="4":
                    print()
                    j=1
                    index_s=[]
                    for i in courses:
                        print(str(j)+"."+i)
                        index_s.append(str(j))
                        j=j+1           
                    choice_course1=input("Seleccione el curso: ")
                    while choice_course1 not in index_s:
                        choice_course1=input("Seleccione el curso: ")
                    j=1
                    print()
                    for i in database["Cursos"][0][courses[int(choice_course1)-1]][1:]:
                        print(str(j)+"."+i[0]+":"+database["Estudiantes"][0][i[0]])
                        j=j+1
                    if j==1:
                        print("No hay estudiantes matriculados en este curso")
                        print("\nPresione ENTER para contuniar: ")
                        input()
                    else:
                        print("\nPresione ENTER para contuniar: ")
                        input()
                    
                elif choice_3=="5":
                    break
    elif choice=="3":
        break

bd.saveFile("students.txt",bd.returnStudents(database))
bd.saveFile("subjects.txt",bd.returnCourses(database))