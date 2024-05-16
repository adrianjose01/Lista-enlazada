from Nodo import Nodo  # Importa la clase Nodo desde el módulo Nodo

class Lista:
    def __init__(self):
        self.inicio = None  # Inicializa la lista sin ningún nodo inicial (lista vacía)

    def insertarF(self, item):
        auxiliar = Nodo()  # Crea un nuevo nodo
        auxiliar.dato = item  # Asigna el dato al nuevo nodo
        if self.inicio == None:
            self.inicio = auxiliar  # Si la lista está vacía, el nuevo nodo se convierte en el inicio
        else:
            puntero = self.inicio
            while puntero.siguiente != None:
                puntero = puntero.siguiente  # Recorre hasta el final de la lista
            puntero.siguiente = auxiliar  # Añade el nuevo nodo al final

    def insertarI(self, item):
        auxiliar = Nodo()  # Crea un nuevo nodo
        auxiliar.dato = item  # Asigna el dato al nuevo nodo
        if self.inicio == None:
            self.inicio = auxiliar  # Si la lista está vacía, el nuevo nodo se convierte en el inicio
        else:
            auxiliar.siguiente = self.inicio  # El nuevo nodo apunta al inicio actual de la lista
            self.inicio = auxiliar  # El nuevo nodo se convierte en el inicio de la lista

    def insertarPos(self, item, pos):
        auxiliar = Nodo()  # Crea un nuevo nodo
        auxiliar.dato = item  # Asigna el dato al nuevo nodo
        if self.inicio == None:
            self.inicio = auxiliar  # Si la lista está vacía, el nuevo nodo se convierte en el inicio
        else:
            if pos == 1:
                auxiliar.siguiente = self.inicio  # El nuevo nodo apunta al inicio actual
                self.inicio = auxiliar  # El nuevo nodo se convierte en el inicio de la lista
            else:
                puntero = self.inicio
                punteroPrevio = self.inicio
                for i in range(0, pos - 1):
                    if puntero == None:
                        print("La posición es mayor al número de elementos, tu elemento se insertará al final.")
                        break
                    punteroPrevio = puntero
                    puntero = puntero.siguiente  # Recorre la lista hasta la posición deseada
                punteroPrevio.siguiente = auxiliar  # El nodo previo apunta al nuevo nodo
                auxiliar.siguiente = puntero  # El nuevo nodo apunta al nodo actual en la posición

    def insertarEnOrden(self, item):
        auxiliar = Nodo()  # Crea un nuevo nodo
        auxiliar.dato = item  # Asigna el dato al nuevo nodo
        if self.inicio == None:
            self.inicio = auxiliar  # Si la lista está vacía, el nuevo nodo se convierte en el inicio
        elif self.inicio.dato > item:
            auxiliar.siguiente = self.inicio  # El nuevo nodo apunta al inicio actual
            self.inicio = auxiliar  # El nuevo nodo se convierte en el inicio de la lista
        else:
            puntero = self.inicio
            while puntero.siguiente != None and puntero.siguiente.dato < item:
                puntero = puntero.siguiente  # Recorre la lista hasta encontrar la posición correcta
            auxiliar.siguiente = puntero.siguiente  # El nuevo nodo apunta al siguiente nodo
            puntero.siguiente = auxiliar  # El nodo actual apunta al nuevo nodo

    def eliminarI(self):
        if self.inicio == None:
            print("Tu Lista está vacía")
        else:
            self.inicio = self.inicio.siguiente  # El inicio de la lista se convierte en el siguiente nodo

    def eliminarF(self):
        if self.inicio == None:
            print("Tu lista está vacía")
        else:
            puntero = self.inicio
            punteroPrevio = self.inicio
            while puntero.siguiente != None:
                punteroPrevio = puntero
                puntero = puntero.siguiente  # Recorre hasta el final de la lista
            punteroPrevio.siguiente = None  # Elimina el último nodo

    def mostrar(self):
        if self.inicio == None:
            print("Esta lista está vacía")
        else:
            puntero = self.inicio
            print(f'Nodo: {puntero.dato}')  # Muestra el dato del nodo actual
            while puntero.siguiente != None:
                puntero = puntero.siguiente  # Recorre la lista
                print(f'Nodo: {puntero.dato}')  # Muestra el dato de cada nodo
