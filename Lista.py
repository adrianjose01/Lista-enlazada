from Nodo import Nodo

class Lista:
    def __init__(self):
        self.inicio = None

    def insertarF(self, item):
        auxiliar = Nodo()
        auxiliar.dato = item
        if(self.inicio == None):
            self.inicio = auxiliar
        else:
            puntero = self.inicio
            while(puntero.siguiente != None):
                puntero = puntero.siguiente

            puntero.siguiente = auxiliar

    def insertarI(self, item):
        auxiliar = Nodo()
        auxiliar.dato = item
        if(self.inicio == None):
            self.inicio = auxiliar
        else:
            auxiliar.siguiente = self.inicio
            self.inicio = auxiliar

    def insertarPos(self, item, pos):
        auxiliar = Nodo()
        auxiliar.dato = item
        if(self.inicio == None):
            self.inicio = auxiliar
        else:
            if(pos == 1):
                auxiliar.siguiente = self.inicio
                self.inicio = auxiliar
            else:
                puntero = self.inicio
                punteroPrevio = self.inicio
                for i in range(0, pos - 1):
                    if(puntero == None):
                        print("La posicion es mayor al numero de elementos, tu elemento se insertara al final.")
                        break
                    punteroPrevio = puntero
                    puntero = puntero.siguiente
                punteroPrevio.siguiente = auxiliar
                auxiliar.siguiente = puntero

    def insertarEnOrden(self, item):
        auxiliar = Nodo()
        auxiliar.dato = item
        if(self.inicio == None):
            self.inicio = auxiliar
        elif(self.inicio.dato > item):
            auxiliar.siguiente = self.inicio
            self.inicio = auxiliar
        else:
            puntero = self.inicio
            while(puntero.siguiente != None and puntero.siguiente.dato < item):
                puntero = puntero.siguiente
            auxiliar.siguiente = puntero.siguiente
            puntero.siguiente = auxiliar
            
    def eliminarI(self):
        if(self.inicio == None):
            print("Tu Lista esta vacia")
        else:
            self.inicio = self.inicio.siguiente

    def eliminarF(self):
        if(self.inicio == None):
            print("Tu lsita esta vacia")
        else:
            puntero = self.inicio
            punteroPrevio = self.inicio
            while(puntero.siguiente != None):
                punteroPrevio = puntero
                puntero = puntero.siguiente
            punteroPrevio.siguiente = None

    def mostrar(self):
        if(self.inicio == None):
            print("Esta lista esta vacia")
        else:
            puntero = self.inicio
            print(f'Nodo: {puntero.dato}')
            while(puntero.siguiente != None):
                puntero = puntero.siguiente
                print(f"Nodo: {puntero.dato}")