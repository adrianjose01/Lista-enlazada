from Nodo import Nodo
from Lista import Lista

lstEnlazada = Lista()

# lstEnlazada.insertarF(67);
# lstEnlazada.insertarF(78);
# lstEnlazada.insertarF(45);
# lstEnlazada.mostrar(); # resultado => 67, 78, 45
# print("");

# lstEnlazada.insertarI(35);
# lstEnlazada.insertarI(15);
# lstEnlazada.mostrar(); # resultado => 15, 35, 67, 78, 45
# print("");

# lstEnlazada.eliminarI();
# lstEnlazada.eliminarF();
# lstEnlazada.mostrar(); # resultado => 35, 67, 78
# print("");

# lstEnlazada.insertarPos(70, 3);
# lstEnlazada.mostrar(); # resultado => 35, 67, 70, 78

continuar_lista = True

while(continuar_lista):
    respuesta = input("""\n\n    a. Insertar al Frente 
    b. Insertar al Final 
    c. Insertar en una posición específica 
    d. Insertar en orden
    e. Eliminar al Frente 
    f. Eliminar al Final 
    g. Mostrar lista 
    h. Salir\n\n  """)
    if(respuesta == "h"):
        continuar_lista = False
    elif(respuesta == "a"):
        item = int(input("Que numero quieres insertar?\n"))
        lstEnlazada.insertarI(item)
    elif(respuesta == "b"):
        item = int(input("Que numero quieres insertar?\n"))
        lstEnlazada.insertarF(item)
    elif(respuesta == "c"):
        item = int(input("Que numero quieres insertar?\n"))
        pos = int(input("En que posicion quiere insertar el numero?\n"))
        lstEnlazada.insertarPos(item, pos)
    elif(respuesta == "d"):
        item = int(input("Que numero quieres insertar?\n"))
        lstEnlazada.insertarEnOrden(item)
    elif(respuesta == "e"):
        lstEnlazada.eliminarI()
    elif(respuesta == "f"):
        lstEnlazada.eliminarF()
    elif(respuesta == "g"):
        lstEnlazada.mostrar()
    else:
        print("No es una opcion valida")