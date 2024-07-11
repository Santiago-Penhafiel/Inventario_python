import funciones
opcs={0:funciones.default,
      1:funciones.añadir,
      2:funciones.editar,
      3:funciones.eliminar,
      4:funciones.imprimirTabla,
      5:funciones.salir}

funciones.menu()
from funciones import opc
if opc==5:
      funciones.salir() 
      from funciones import opc
while opc!=5:    
      opcs.get(opc)()
      funciones.menu()
      from funciones import opc
      if opc==5:
            funciones.salir() 
            from funciones import opc
