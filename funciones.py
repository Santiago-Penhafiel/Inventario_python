inventario=[[[]for j in range (2)]for k in range (3)]
import json, os
try:
    with open(os.path.dirname(__file__)+"/inventario.json","r") as file:
        inventario=json.load(file)
except:
    0

def default():
    return

def menu():
    global opc
    print("\n\t\t\tMENU")
    print("1 Para ingresar nuevos objetos",
          "2 Para editar los objetos",
          "3 Para eliminar los objetos",
          "4 Para ver la lista de objetos",
          "5 Para salir",
          "Opcion : ",sep="\n",end="")
    try:
        opc=int(input())
        while opc not in range (1,6):
            print("Elija un respuesta válida : ",end="")
            opc=int(input())
    except:
        print("Opcion ingresada no valida")
        opc=0
    return 

def añadir():
    print("\n\t\t\tAÑADIR")
    return obtenerTipo()

def editar():
    print("\t\t\tEDITAR")
    return obtenerTipo()

def eliminar():
    print("\t\t\tELIMINAR")
    return obtenerTipo()


def obtenerTipo():
    print("Elija el tipo de joyería",
          "1 Para collares",
          "2 Para pulseras",
          "3 Para anillos",
          "Opcion : ",sep="\n",end="")
    global tipo
    try:
        tipo=int(input())
        while tipo not in range (1,4):
            print("Ingrese una opcion válida : ",end="")
            tipo=int(input())
    except:
        print("Respuesta no procesable")
        return
    return obtenerMaterial()
    

def obtenerMaterial():
    global material
    print("\n1 Para oro",
          "2 Para plata",
          "Material a Ingresar : ",sep="\n",end="")
    try:
        material=int(input())
        while material not in range (1,3):
            print("Ingrese una de las respuestas numeradas")
            material=int(input())
    except:
        print("Respuesta no procesable")
        return
    if opc==1:
        return numObjAñadir()
    elif opc==2:
        return buscarNombre()
    elif opc==3:
        return buscarNombre()

def numObjAñadir():
    global numObj
    print("Ingrese el numero de objetos a añadir : ",end="")
    try:
        numObj=int(input())
    except:
        print("Respuesta no procesable")
        return
    return añadirObjetos()

def añadirObjetos():
    global inventario
    cont=False
    for i in range(0,numObj):
        obj=[]
        try:
            print("\nOBJETO",i+1)
            print("Ingrese el nombre del objeto a añadir : ",end="")
            nombre=input()
            #print(material, tipo)
            for nombres in inventario[tipo-1][material-1]:
                if nombre==nombres[0]:
                    print("\nEl nombre ingresado ya existe")
                    cont=True
                    continue
            if cont==True:
                continue
            print("Ingrese la cantidad de objetos : ",end="")
            cantidad=int(input())
            print("Ingrese el precio de los objetos : ",end="")
            precio=float(input())
        except:
            print("Opcion ingresada no procesable")
            return
        #print(obj)
        obj.append(nombre)
        obj.append(cantidad)
        obj.append(precio)
        inventario[tipo-1][material-1].append(obj[:])
        #inventario[tipo][material][0]=nombre
    return

def buscarNombre():
    global index
    if opc==2:
        dif="editar"
    if opc==3:
        dif="eliminar"
    index=0
    print("Ingrese el nombre del producto a",dif,": ",end="")
    nombre=input()
    for objetos in inventario[tipo-1][material-1]:
        if objetos[0]==nombre:
            if opc==2:
                return opcEditar()
            if opc==3:
                return eliminarObjeto()
        index+=1
    print("No se ha encontrado ese artículo")
    index=-1
    return

def opcEditar():
    if index!=-1:
        global opcE
        print("Para el artículo \"",inventario[tipo-1][material-1][index][0],"\"",sep="")
        print("Ingrese",
              "1 Para editar nombre",
              "2 Para editar cantidad",
              "3 Para editar precio",
              "Opción : ",sep="\n",end="")
        try:
            opcE=int(input())
            while opcE not in range (1,4):
                print("Ingrese una opción válida")
                opcE=int(input())
        except:
            print("Respuesta no procesable")
            return
        if opcE==1:
            return editarNombre()
        elif opcE==2:
            return editarCantidad()
        elif opcE==3:
            return editarPrecio()
    return
        
def editarNombre():
    print("Ingrese el nuevo nombre : ",end="")
    nombre=input()
    for nombres in inventario[tipo-1][material-1]:
        if nombre==nombres[0]:
            print("El nombre ingresado coincide con un nombre existente")
            return
    inventario[tipo-1][material-1][index][0]=nombre
    return

def editarCantidad():
    print("Ingrese la nueva cantidad : ",end="")
    try:
        cantidad=int(input())
    except:
        print("Respuesta no procesable")
        return
    inventario[tipo-1][material-1][index][1]=cantidad
    return

def editarPrecio():
    print("Ingrese el nuevo precio : ",end="")
    try:
        precio=float(input())
    except:
        print("Respuesta no procesable")
        return
    inventario[tipo-1][material-1][index][2]=precio
    return

def eliminarObjeto():
    if index!=-1:
        print("¿Está seguro de querer eliminar el objeto ",inventario[tipo-1][material-1][index][0],"? (si/no) : ",sep="",end="")
        resp=input()
        if resp=="si":
            inventario[tipo-1][material-1].pop(index)
    return

def imprimirTabla():
    x=0
    for tipo in inventario:
        for material in tipo:
            if len(material)>0:
                if tipo==inventario[0]:
                    print("\n\t\tCOLLARES",end="")
                    j=0
                elif tipo==inventario[1]:
                    print("\n\t\tPULSERAS",end="")
                    j=2
                elif tipo==inventario[2]:
                    print("\n\t\tANILLOS",end="")
                    j=3
                if material==inventario[j][0]:
                    print("(ORO)")
                else:
                    print("(PLATA)")
                print("NOMBRE\t\t","CANTIDAD\t","PRECIO")
                for objetos in material:
                    for i in range(len(objetos)):
                        print(objetos[i],end="\t\t")
                    print()
            else:
                x+=1
    if x==6:
        print("Inventario vacio")                   
    return
                    
def salir():
    print("¿Está seguro que quiere salir del inventario? (si/no) : ",end="")
    resp=input()
    global opc
    if resp=="no":
        opc=0
        return
    elif resp=="si":
        with open("inventario.json","w") as file:
            json.dump(inventario,file,indent=4)
            file.close()
        opc=5
        return
    else:
        opc=0
        return