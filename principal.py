#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:17:18 2020

@author: raquel
"""
#programa principal que tendrá el menú inicial y la llamada a las clases utilidades y hospital.
from hospital import Hospital
from utilidades import Utilidades
from paciente import Paciente
from medica import Medica
from datetime import datetime

def comprobar(nombre,apellido,direccion,ciudad,cp,telf,email,espe_gruposang):
    if len(nombre)!=0 and len(apellido)!=0 and len(direccion)!=0 and len(ciudad)!=0 and len(cp)!=0 and len(telf)!=0 and len(email)!=0 and len(espe_gruposang)!=0:
        if len(nombre)>=2 and len(apellido)>=2 and len(telf)>=2: #asi puedo hacer la contraseña
            if nombre.isalpha()==True and apellido.isalpha()==True:
                nom=nombre+' '+apellido #dado como un unico parametro dentro de los atributos
            elif cp.isnumeric()==True:
                #NO SE QUE PONER
    else:
        #algun campo esta vacio

def main():
    util=Utilidades() #creo objeto de la clase Utilidades
    dic_especialidades,dic_medicas,dic_pacientes,dic_enfermeras,dic_recepcionistas,dic_medicamentos,lista_hosp=util.lectura('especialidades.csv','informacion.csv','medicina.csv') #llamada al metodo de Utilidades para guardar lo que nos devuelve en variables 
    hosp=Hospital(lista_hosp[0],lista_hosp[1],lista_hosp[2],lista_hosp[3],lista_hosp[4],None,dic_pacientes,dic_medicas,dic_especialidades,dic_enfermeras,dic_recepcionistas,dic_medicamentos) #creo el objeto de hospital donde los primeros parámetros los toma de la lista de info hospital
    recep=dic_recepcionistas[1] #objeto de la clase Recepcionista
    enf=dic_enfermeras[1]
    opcion=0
    lista_info=[]
    #MENU DE OPCIONES
    while opcion!=5: 
        try: 
            print('\nMenú de opciones\n 1) Altas\n 2) Consultas\n 3) Revisiones\n 4)Archivos\n 5) Salida\n')
            opcion=int(input('Seleccione una opción: '))
            if opcion==1:
                #MENU ALTAS
                opcion1=0
                while opcion1!=7:
                    try:
                        print('\nMenú de altas\n 1) Médica\n 2) Paciente\n 3) Enfermeras\n 4) Recepcionista\n 5)Especialidad\n 6)Medicamento\n 7)Regresar al menú de opciones')
                        opcion1=int(input('Seleccione una opción: ')) #input ha de ser un integer, sino salta a la expeción
                        if opcion1==1: #ALTA MEDICA
                                
                            print('\nInformación de la médica a dar de alta: ')
                            #pido por pantalla todos los inputs necesarios para dar de alta una médica, en este caso no ponemos criterios de entrada por pantalla
                            nombre=input('-> Nombre: ').title()
                            apellido=input('-> Primer apellido: ').title()
                            nom=nombre+' '+apellido #dado como un unico parametro dentro de los atributos
                            direccion=input('-> Dirección: ')
                            ciudad=input('-> Ciudad: ')
                            cp=input('-> CP: ')
                            telf=input('-> Telf: ')
                            email=input('-> Email: ')
                            especialidad=input('-> Especialidad: ') #ningún criterio de entrada de especialidad, no se especifica que tenga que estar dentro del dic_especialidades
                            
                            id_m=len(dic_medicas.keys())+1 #el identificador será el siguiente a tantas claves del diccionario habrá
                            password=util.crea_password(nombre,apellido,telf) #creo la contraseña con el metodo de la clase utilidades
                            med=Medica(id_m,nom,direccion,ciudad,cp,telf,email,especialidad,password) #creo el objeto de la clase médica
                            hosp.metodo_alta(med,id_m,recep,'med') #llamada al método de hospital
                            print('Médica dada de alta con éxito')
                        
                        
                        elif opcion1==2: #ALTA PACIENTE
                            
                            print('\nInformación de la paciente a dar de alta: ')
                            nombre=input('-> Nombre: ').title()
                            apellido=input('-> Primer apellido: ').title()
                            nom=nombre+' '+apellido
                            direccion=input('-> Dirección: ')
                            ciudad=input('-> Ciudad: ')
                            cp=input('-> CP: ')
                            telf=input('-> Telf: ')
                            email=input('-> Email: ')
                            
                            grupos_sanguineos=('AB+','AB-','A+','A-','B+','B-','0+','0-')
                            while True:
                                grupo_sanguineo=input('-> Grupo Sanguíneo: ') #compruebo que el grupo sanguieno introducido por pantalla estea dentro de la tupla
                                if grupo_sanguineo in grupos_sanguineos:
                                    id_p=len(dic_pacientes.keys())+1
                                    pac=Paciente(id_p,nom,direccion,ciudad,cp,telf,email,grupo_sanguineo)
                                    hosp.metodo_alta(pac,id_p,recep,'pac')
                                    print('Paciente dada de alta con éxito')
                                    break
                                else: 
                                    print('No existe tal grupo sanguíneo')
                                    
                        elif opcion1==3: #ALTA ENFERMERA
                            
                            print('\nInformación de la enfermera a dar de alta: ')
                            nombre=input('-> Nombre: ').title()
                            apellido=input('-> Primer apellido: ').title()
                            nom=nombre+' '+apellido
                            direccion=input('-> Dirección: ')
                            ciudad=input('-> Ciudad: ')
                            cp=input('-> CP: ')
                            telf=input('-> Telf: ')
                            email=input('-> Email: ')
                            
                            id_e=len(dic_enfermeras.keys())+1 #el identificador será el siguiente a tantas claves del diccionario habrá
                            password=util.crea_password(nombre,apellido,telf)
                            
                            categorias_disponibles=['J:enfermera junior','M:enfermera senior'] #solo me quedan por asigar estas dos categorias
                            if categorias_disponibles[0] in dic_enfermeras[-1]:
                                enf=Enfermera(id_e,nom,direccion,ciudad,cp,telf,email,password,categorias_disponibles[1])
                            elif categorias_disponibles[1] in dic_enfermeras[-1]:
                                enf=Enfermera(id_e,nom,direccion,ciudad,cp,telf,email,password,categorias_disponibles[0])
                                
                            hosp.metodo_alta(enf,id_e,recep,'enf')
                            print('Enfermera dada de alta con éxito')
                            
                        elif opcion1==4: # ALTA RECEPCIONISTA
                            
                            print('\nInformación de la recepcionista a dar de alta: ')
                            nombre=input('-> Nombre: ').title()
                            apellido=input('-> Primer apellido: ').title()
                            nom=nombre+' '+apellido
                            direccion=input('-> Dirección: ')
                            ciudad=input('-> Ciudad: ')
                            cp=input('-> CP: ')
                            telf=input('-> Telf: ')
                            email=input('-> Email: ')
                            
                            id_r=len(dic_recepcionistas.keys())+1 #el identificador será el siguiente a tantas claves del diccionario habrá
                            password=util.crea_password(nombre,apellido,telf)
                            
                            #NO SE COMO OTORGAR LOS TURNOS
                            turnos=['1:matutino','2:verspertino','3:nocturno','4:rotatorio'] #turnos de recepcionistas
                            for i in turnos:
                                if turnos[i] is in dic_recepcionistas[-1]:
                                    rec=Recepcionista(id_r,nom,direccion,ciudad,cp,telf,email,password,turno[i-1])
        
                            hosp.metodo_alta(rec,id_r,recep,'recep')
                            print('Recepcionista dada de alta con éxito')
                            
                        elif opcion1==5: #ALTA ESPECIALIDAD
                             print('Información de la especialidad a dar de alta: ')
                             especialidad=input('-> Nombre: ').title()
                             if especialidad is in dic.especialidades:
                                 print('La especialidad ya existe')
                             elif especialidad is not in dic_especialidades:
                                try:
                                    codigo=int(input('Introduzca el codigo de la especialidad: '))
                                    espe=Especialidad(codigo,nombre)
                                    hosp.metodo_altas(espe,codigo,recep,'espe')
                                except ValueError:
                                    print('EL codigo no es un numero')
                                 
                        elif opcion1==6: #ALTA MEDICAMENTO
                            print('Infromación sobre le medicamento a dar de alta: ')
                            codigo=input('Código: ')
                            princ_activ=input('Principio Activo: ')
                            marca=input('Marca: ')
                            laboratorio=('Laboratorio: ')
                            
                            #FALTA COMPROBAR SI YA EXISTE Y NOTIFICAR
                            medicamento=Medicamento(codigo,princ_activ,marca,laboratorio)
                            hosp.metodo_alta(medicamento,codigo,recep,'medicamento')
                            print('Medicamento dado de alta con éxito')
                            
                        elif opcion1<1 or opcion1>6: #SALIDA MENU ALTAS
                            print('La opcion seleccionada no está disponible')
                            
                    except ValueError:
                        print('Opción seleccionada no válida')
                        
                print('Ha salido del menú de altas')
                            
                                
              elif opcion==2: #MENU CONSULTAS
                  opcion2=0
                  while opcion2!=7:
                    try:
                        print('\nMenú de consulta\n 1) Médica\n 2) Paciente\n 3) Enfermera\n 4) Recepcionista\n 5)Especialidad\n 6)Medicamento\n 7)Recetas\n 8)Derivaciones 9)Medico por especialidad 10)Regresar al menú de opciones')
                        opcion2=int(input('Seleccione una opción: ')) #input ha de ser un integer, sino salta a la expeción
                        if opcion2==1: #BUSQUEDA MÉDICA
                            opcion3=0
                            while opcion3!=3: 
                                try: 
                                    print('\nOpciones de consulta de médicas\n 1) Por nombre y apellido\n 2) Por número identificador\n 3) Regresar al menú de búsqueda\n')
                                    opcion3=int(input('Seleccione una opción: '))
                                    if opcion3==1: #busqueda medica por nombre
                                        nom=input('Introduzca el nombre y apellido de la médica: ').title()
                                        if nom.replace(' ','').isalpha()==True:
                                            lista_med=[]
                                            med=consulta_dics(lista_med,'med'): 
                                            if med==[]: #si la lista esta vacía quiere decir que no ha encontrado ninguna médica con ese nombre
                                                print('\nNo figura una médica con ese nombre')
                                            else: #la lista no está vacía, hay una o más médicas con el nombre introducido
                                                for i in range(len(med)): #recorro la lista, puede que recorra más posiciones de las que necesito, pero solo me imprimirá las que encuentre en la lista
                                                    print('\n -> ',med[i],'\n') #me imprime una flechita por cada médica que haya
                                        else:
                                            print('Debe introducir letras') #cuando lo introducido no son letras y son números o símbolos
                                        
                                    elif opcion3==2: #busqueda medica por identificador 
                                        try:
                                            id_m=int(input('Introduzca el número identificador: ')) #input ha de ser un número
                                            med=hosp.consulta_ident(id_m,'med') #me devulve el número identificador si existe
                                            if med==None: #no ha encontrado ninguna coincidencia
                                                print('\nNo figura una médica con ese número identificador')
                                            else: #lo ha encontrado
                                                print(med)
                                        except ValueError: #si mete cualquier cosa que no sea un entero
                                            print('\nDebe introducir un número')
                                            
                                    elif opcion3<1 or opcion3>3:
                                        print('\nLa opción seleccionada no está disponible')
                                        
                                        
#PLANTEAR DE NUEVO ELL METODO DE CONSULTA PACIENTES Y ESTRUCTURARLOOOOOOOOOOOOOOO                                        
                                        
                                        
                                              
                        elif opcion2==2: #BUSQUEDA PACIENTE
                            opcion3=0
                            while opcion3!=3: 
                                try: 
                                    print('\nOpciones de consulta de pacientes\n 1) Por nombre y apellido\n 2) Por número identificador\n 3) Regresar al menú de búsqueda\n')
                                    opcion3=int(input('Seleccione una opción: '))
                                    if opcion3==1: #busqueda paciente por nombre
                                        nom=input('Introduzca el nombre y apellido de la paciente: ').title()
                                        if nom.replace(' ','').isalpha()==True: #input han de ser letras
                                            pac=hosp.consulta_dics(nom,recep,dic_pacientes)
                                            if p==[]: #si la lista esta vacía quiere decir que no ha encontrado ninguna paciente con ese nombre
                                                print('\nNo figura una paciente con ese nombre')
                                            else: #la lista no está vacía, hay una o más pacientes con el nombre introducido
                                                for i in range(len(p)): #recorro la lista, puede que recorra más posiciones de las que necesito, pero solo me imprimirá las que encuentre en la lista
                                                    print(' -> ',p[i][i].muestra_datos(),'\n') #me imprime una flechita por cada paciente que haya
                                        else:
                                            print('Debe introducir letras') #cuando lo introducido no son letras y son números o símbolos
                                    elif opcion3==2: #busqueda paciente por identificador
                                        try:
                                            id_p=int(input('Introduzca el número identificador: ')) #input ha de ser un número
                                            p=hosp.ipaciente(id_p) #me devulve el número identificador si existe
                                            if p==None: #no ha encontrado ninguna coincidencia
                                                print('\nNo figura una paciente con ese número identificador')
                                            else: #lo ha encontrado
                                                print(p)
                                        except ValueError: #si mete cualquier cosa que no sea un entero
                                            print('\nDebe introducir un número')
                                            
                                    elif opcion3<1 or opcion3>3:
                                        print('\nLa opción seleccionada no está disponible')
                                        
                                except ValueError: #cuando al introducir la opcion introduzca algo que no sea un entero
                                    print('La opción seleccionada no es válida, por favor, seleccione otra opción')
                            
                        elif opcion2==3: #BUSQUEDA ENFERMERA
                        elif opcion2==4: #BUSQUEDA RECEPCIONISTA   
                        elif opcion2==5: #BUSQUEDA ESPECIALIDAD
                        elif opcion2==6: #BUSQUEDA MEDICAMENTO
                        elif opcion2==7: #BUSQUEDA RECETAS
                        elif opcion2==8: #BUSQUEDA DERIVACIONES
                        elif opcion2==9: #BUSQUEDA MEDICO POR ESPECIALIDAD
                        elif opcion2<0 or opcion2>9: #SALIDA
                            print('la opcion seleccionada no está disponible')
                    except ValueError:
                        print('opcion seleccionada no es valida')

                        elif opcion1==2: #busqueda paciente
                            #MENÚ OPCIONES BÚSQUEDA
                            opcion2=0
                            while opcion2!=3: 
                                try: 
                                    print('\nOpciones de búsqueda\n 1) Por nombre y apellido\n 2) Por número identificador\n 3) Regresar al menú de búsqueda\n')
                                    opcion2=int(input('Seleccione una opción: '))
                                    if opcion2==1: #busqueda paciente por nombre
                                        nom=input('Introduzca el nombre y apellido de la paciente: ').title()
                                        if nom.replace(' ','').isalpha()==True: #input han de ser letras
                                            p=hosp.consulta_paciente(nom,recep,dic_pacientes)
                                            if p==[]: #si la lista esta vacía quiere decir que no ha encontrado ninguna paciente con ese nombre
                                                print('\nNo figura una paciente con ese nombre')
                                            else: #la lista no está vacía, hay una o más pacientes con el nombre introducido
                                                for i in range(len(p)): #recorro la lista, puede que recorra más posiciones de las que necesito, pero solo me imprimirá las que encuentre en la lista
                                                    print(' -> ',p[i][i].muestra_datos(),'\n') #me imprime una flechita por cada paciente que haya
                                        else:
                                            print('Debe introducir letras') #cuando lo introducido no son letras y son números o símbolos
                                    elif opcion2==2: #busqueda paciente por identificador
                                        try:
                                            id_p=int(input('Introduzca el número identificador: ')) #input ha de ser un número
                                            p=hosp.ipaciente(id_p) #me devulve el número identificador si existe
                                            if p==None: #no ha encontrado ninguna coincidencia
                                                print('\nNo figura una paciente con ese número identificador')
                                            else: #lo ha encontrado
                                                print(p)
                                        except ValueError: #si mete cualquier cosa que no sea un entero
                                            print('\nDebe introducir un número')
                                            
                                    elif opcion1<1 or opcion1>3:
                                        print('\nLa opción seleccionada no está disponible')
                                        
                                except ValueError: #cuando al introducir la opcion introduzca algo que no sea un entero
                                    print('La opción seleccionada no es válida, por favor, seleccione otra opción')
                                    
                        elif opcion1==3: #busqueda revisiones
                            opcion2=0
                            while opcion2!=3:
                                try: 
                                    print('\nOpciones de búsqueda de revisiones médicas\n 1) Por nombre y apellido de la paciente\n 2) Por número identificador\n 3) Regresar al menú de búsqueda\n')
                                    opcion2=int(input('Seleccione una opción: '))
                                    
                                    if opcion2==1: 
                                        nom=input('Introduzca el nombre y apellido de la paciente: ').title()
                                        if nom.replace(' ','').isalpha():
                                            for i in dic_pacientes:
                                                if nom in dic_pacientes[i].regresa_nombre():
                                                    pac=dic_pacientes[i] #cada vez que encuentre un paciente en el diccionario con el nombre introducido nos umará uno a b
                                                    b+=1
                                            if b==0: #si no ha encontrado ningun paciente b será cero
                                                print('No existe tal paciente')
                                            elif b!=1: #mas de unx paciente con el nombre introducido
                                                print('Hay',b,'paceintes con el nombre introducido: ')
                                                for i in dic_pacientes:
                                                    if nom in dic_pacientes[i].regresa_nombre():
                                                        print(dic_pacientes[i].muestra_datos()) #me imprime los datos de las pacientes que haya encontrado
                                                id_p=int(input('Introduzca el número identificador de la paciente: ')) #pido por pantalla el número de identificador del paciente que deseemos
                                                pac=dic_pacientes[id_p] #me crea el objeto paciente con el que haya seleccionado
                                                
                                                if hosp.consulta_revmed(nom)==[]: #si la lista de revisiones esta vacía
                                                    print('\nEsta paciente no tiene revisiones médicas')
                                                else: 
                                                    print('\nLas revisiones médicas de la paciente',nom,'son:\n',hosp.consulta_revmed(nom))
                                            else: #si simplemente hay una paciente
                                                if hosp.consulta_revmed(nom)==[]:
                                                    print('\nEsta paciente no tiene revisiones médicas')
                                                else:
                                                    print('\nLas revisiones médicas de la paciente',nom,'son:\n',hosp.consulta_revmed(nom)) 
                                        else:
                                            print('Debe introducir letras') #cuando lo introducido no son letras y son números o símbolos
                                                    
                                    elif opcion2==2:
                                        try: 
                                            ident=int(input('Introduzca el número identificador de la paciente: ')) #directamente a través del número identificador, solo habrá una paciente con tal número
                                            if hosp.irevmed(ident)==[]:
                                                print('Esta paciente no tiene revisiones médicas')
                                            else:
                                                print('Las revisiones médicas de la paciente son:\n',hosp.irevmed(ident))
                                        except ValueError: #si el id no es número
                                            print('\nDebe introducir un número')
                                    elif opcion2<1 or opcion>3:
                                        print('\nLa opción seleccionada no está disponible')
                                      
                                except ValueError: #cuando al introducir la opcion introduzca algo que no sea un entero
                                    print('La opción seleccionada no es válida, por favor, seleccione otra opción')
                         
                        elif opcion1<1 or opcion1>3:
                            print('\nLa opción seleccionada no está disponible')
                                    
                    except ValueError: #cuando al introducir la opcion introduzca algo que no sea un entero
                        print('La opción seleccionada no es válida, por favor, seleccione otra opción')
                print('\nHa salido del menú de opciones')                  
                            
                    
                
            elif opcion==2: 
                #ALTAS: usamos funciones dar de alta de hospital y asignar revisione de enfermera??
                opcion2=0
                while opcion2!=4:
                    try:
                        print('\nMenú de altas \n 1) Médica\n 2) Paciente\n 3) Revisión médica\n 4) Regresar al menú de opciones\n')
                        opcion2=int(input('Seleccione una opción: '))
                        if opcion2==1: #alta de una médica
                            print('\nInformación de la médica a dar de alta: ')
                            #pido por pantalla todos los inputs necesarios para dar de alta una médica, en este caso no ponemos criterios de entrada por pantalla
                            nombre=input('-> Nombre: ').title()
                            apellido=input('-> Primer apellido: ').title()
                            nom=nombre+' '+apellido #dado como un unico parametro dentro de los atributos
                            direccion=input('-> Dirección: ')
                            ciudad=input('-> Ciudad: ')
                            cp=input('-> CP: ')
                            telf=input('-> Telf: ')
                            email=input('-> Email: ')
                            especialidad=input('-> Especialidad: ') #ningún criterio de entrada de especialidad, no se especifica que tenga que estar dentro del dic_especialidades
                            id_m=len(dic_medicas.keys())+1 #el identificador será el siguiente a tantas claves del diccionario habrá
                            password=util.crea_password(nombre,apellido,telf) #creo la contraseña con el metodo de la clase utilidades
                            m=Medica(id_m,nom,direccion,ciudad,cp,telf,email,especialidad,password) #creo el objeto de la clase médica
                            hosp.alta_medica(m,id_m,recep) #llamada al método de hospital
                            print('Médica dada de alta con éxito')
                                    
                             #en el caso de que quisisese meter excepciones o criterios de entrada por pantalla podría hacer algo similar
#                            while True:
#                                nombre=input('-> Nombre: ').title()
#                                if nombre.isalpha()==True:
#                                    apellido=input('-> Primer apellido: ').title()
#                                    if apellido.isalpha()==True:
#                                        nom=nombre+' '+apellido #dadro como un unico parametro dentro de los atributos
#                                        direccion=input('-> Dirección: ')
#                                        ciudad=input('-> Ciudad: ')
#                                        try: 
#                                            cp=int(input('-> CP: '))
#                                            telf=input('-> Telf: ') #es muy dificil establecer una condicion para un telefono, ya que puede ser introducido de diversas formas
#                                            email=input('-> Email: ')
#                                            especialidad=input('-> Especialidad: ')
#                                            if especialidad.replace(' ','').isalpha()==True:
#                                                if especialidad in dic_especialidades:
#                                                    id_m=len(dic_medicas.keys())+1 #el identificador será el siguiente a tantas claves del diccionario habrá
#                                                    password=util.crea_password(nombre,apellido,telf) #creo la contraseña con el metodo de la clase utilidades
#                                                    m=Medica(id_m,nom,direccion,ciudad,cp,telf,email,especialidad,password)
#                                                    med=hosp.alta_medica(m,id_m,recep)
#                                                    print('Médica dada de alta con éxito')
#                                                    break
#                                                else: 
#                                                    print('La especialidad introducida no está disponible es este hospital')
#                                            else:
#                                                print('Debe introducir letras')
#                                        except ValueError:
#                                            print('El código postal ha de estar compuesto por números')
#                                    else:
#                                        print('Debe introducir letras')
#                                else:
#                                    print('Debe introducir letras')
                            
                        elif opcion2==2: #alta de un paciente
                            #primero pedimos por pantalla los parametros de entrada necesarios para dar de alta a la paciente, que serán practicmente los atributos de dicha clase Paciente
                            print('\nInformación de la paciente a dar de alta: ')
                            nombre=input('-> Nombre: ').title()
                            apellido=input('-> Primer apellido: ').title()
                            nom=nombre+' '+apellido
                            direccion=input('-> Dirección: ')
                            ciudad=input('-> Ciudad: ')
                            cp=input('-> CP: ')
                            telf=input('-> Telf: ')
                            email=input('-> Email: ')
                            grupos_sanguineos=('AB+','AB-','A+','A-','B+','B-','0+','0-')
                            while True:
                                grupo_sanguineo=input('-> Grupo Sanguíneo: ') #compruebo que el grupo sanguieno introducido por pantalla estea dentro de la tupla
                                if grupo_sanguineo in grupos_sanguineos:
                                    id_p=len(dic_pacientes.keys())+1
                                    p=Paciente(id_p,nom,direccion,ciudad,cp,telf,email,grupo_sanguineo)
                                    hosp.alta_paciente(p,id_p,recep)
                                    print('Paciente dada de alta con éxito')
                                    break
                                else: 
                                    print('No existe tal grupo sanguíneo')
                                
#                            nombre=input('-> Nombre: ').title()
#                                if nombre.isalpha()==True and len(nombre)>1:
#                                    apellido=input('-> Primer apellido: ').title()
#                                    if apellido.isalpha()==True:
#                                        nom=nombre+' '+apellido #dadro como un unico parametro dentro de los atributos
#                                        direccion=input('-> Dirección: ')
#                                        ciudad=input('-> Ciudad: ')
#                                        try: 
#                                            cp=int(input('-> CP: '))
#                                            telf=input('-> Telf: ') #es muy dificil establecer una condicion para un telefono, ya que puede ser introducido de diversas formas
#                                            email=input('-> Email: ')
#                                            grupos_sanguineos=('AB+','AB-','A+','A-','B+','B-','0+','0-')
#                                            grupo_sanguineo=input('-> Grupo Sanguíneo: ')
#                                            if grupo_sanguineo in grupos_sanguineos:
#                                                id_p=len(dic_pacientes.keys())+1
#                                                p=Paciente(id_p,nom,direccion,ciudad,cp,telf,email,grupo_sanguineo)
#                                                pac=hosp.alta_paciente(p,id_p,recep)
#                                                print('Paciente dada de alta con éxito')
#                                            
#                                            else: 
#                                                print('No existe tal grupo sanguíneo')
#                                                
#                                        except ValueError:
#                                            print('El código postal ha de estar compuesto por números')
#                                    else:
#                                        print('Debe introducir letras')
#                                else:
#                                    print('Debe introducir letras')
                            
                        elif opcion2==3: #alta revision medica: asignar revision de enfermera
                            a=0
                            nom=input("Introduzca el nombre y apellido de la paciente: ").title()
                            if nom.replace(' ','').isalpha()==True:
                                while True:
                                    try:
                                        fecha_str=input('\nIntroduzca la fecha de revisión en formato "dd/mm/aaaa": ') #criterio para que la fecha que me introduzca por pantalla mantenga este formato
                                        fecha=datetime.strptime(fecha_str,'%d/%m/%Y')
                                        for i in dic_pacientes:
                                            if nom in dic_pacientes[i].regresa_nombre():
                                                pac=dic_pacientes[i]      
                                                a+=1
                                        if a==0:
                                            print('No existe tal paciente')
                                        elif a!=1: #más de unx paciente con el nombre introducido
                                            print('Hay',a,'pacientes con el nombre introducido:')
                                            for i in dic_pacientes:
                                                if nom in dic_pacientes[i].regresa_nombre():
                                                    print(dic_pacientes[i].muestra_datos())
                                            id_p=int(input('Introduzca el número identificador de la paciente a asignar la revisión: '))
                                            pac=dic_pacientes[id_p]
                                            enf.asigna_revision(pac,fecha_str,dic_medicas)
                                            print('Revisión a',pac.regresa_nombre(),'asignada')
                                        else:
                                            enf.asigna_revision(pac,fecha_str,dic_medicas)
                                            print('Revisión asignada')
                                        break
                                    
                                    except ValueError:
                                        print("\nNo ha introducido una fecha correcta")
            
                            else: 
                                print('Debe introducir letras')
                                
                        elif opcion2<1 or opcion2>4:
                            print('\nLa opción seleccionada no está disponible')

                    except ValueError:
                        print('La opción seleccionada no es válida, por favor, seleccione otra opción')
                print('\nHa salido del menú de altas') 
                
            elif opcion==3: 
                #LISTADOS: usamos todas las funciones de muestra de hospital
                opcion3=0
                while opcion3!=6:
                    try:
                        print('\nMenú Listados \n 1) Mostrar lista médicas\n 2) Mostrar lista pacientes\n 3) Mostrar especialidades\n 4) Mostrar recepcionistas\n 5) Mostrar enfermeras\n 6) Regresar al menú de opciones\n')
                        opcion3=int(input('Seleccione una opción: '))
                        if opcion3==1: #Mostrar lista médicas
                            print('Lista de médicas:\n')
                            for i in range(len(hosp.muestra_medicas())): #recorro la lista que devuelve ese metodo de Hospital
                                print('-> ',hosp.muestra_medicas()[i]) #imprimo cada elemento de la lista con una flechita
                        
                        elif opcion3==2: #Mostrar lista pacientes
                            print('Lista de pacientes:\n')
                            for i in range(len(hosp.muestra_pacientes())):
                                print('-> ',hosp.muestra_pacientes()[i])
                                    
                        elif opcion3==3: #mostrar especialidades
                            print('Lista de especialidades:\n')
                            for i in range(len(hosp.muestra_especialidades())):
                                print('-> ',hosp.muestra_especialidades()[i])
                                
                        elif opcion3==4: #mostrar recepcionistas
                            print('Lista de recepcionistas:\n')
                            for i in range(len(hosp.muestra_recepcionistas())):
                                print('-> ',hosp.muestra_recepcionistas()[i])
                        elif opcion3==5: #mostrar enfermeras
                            print('Lista de enfermeras:\n')
                            for i in range(len(hosp.muestra_enfermeras())):
                                print('-> ',hosp.muestra_enfermeras()[i])
                        elif opcion3<1 or opcion3>6:
                            print('\nLa opción seleccionada no está disponible')
                            
                    except ValueError: #en el caso de que haya introducido algo erroneo como opcion
                        print('\nLa opción seleccionada no es válida, por favor, seleccione otra opción')
                        
            elif opcion<1 or opcion>4:
                print('\nLa opción seleccionada no está disponible')
                
        except ValueError: #en el caso de que haya introducido algo erroneo como opcion
            print('La opción seleccionada no es válida, por favor, seleccione otra opción')
    print('\nHa salido del menú')
    
if __name__=='__main__':
    main()