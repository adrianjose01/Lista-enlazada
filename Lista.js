const Nodo = require("./Nodo");

class Lista {
  constructor() {
    this.incio = null;
  }

  insertarF(item) {
    // Crea el Nodo nuevo.
    const auxiliar = new Nodo();
    auxiliar.dato = item;
    auxiliar.siguiente = null;
    // Si la lista esta vacia, coloca el nuevo Nodo como cabeza.
    if (this.incio === null) {
      this.incio = auxiliar;
    } else {
      // Si la lista no esta vacia.
      // Crea el puntero para recorrer la lista.
      let puntero = this.incio;
      // Recorre la lista hasta el final.
      while (puntero.siguiente !== null) {
        puntero = puntero.siguiente;
      }
      // El Nodo final ahora apunta al nuevo Nodo.
      puntero.siguiente = auxiliar;
    }
  }

  insertarI(item) {
    // Crea el Nodo nuevo.
    let auxiliar = new Nodo();
    auxiliar.dato = item;
    auxiliar.siguiente = null;
    // Si la lista esta vacia, coloca el nuevo Nodo como cabeza.
    if (this.incio === null) {
      this.incio = auxiliar;
    } else {
      // Si no esta vacía.
      auxiliar.siguiente = this.incio; // El nuevo Nodo ahora señala a el Nodo incio.
      this.incio = auxiliar; // Pasa el nuevo nodo a ser el inicio.
    }
  }

  insertarPos(item, pos) {
    // Crea el nuevo Nodo con sus atributos
    const auxiliar = new Nodo();
    auxiliar.dato = item;
    auxiliar.siguiente = null;
    // Si la lista esta vacia inserta el Nodo en el inicio.
    if (this.incio === null) {
      this.incio = auxiliar;
    } else {
      // Si la posicion es 1, coloca la cabeza como referencia del nuevo Nodo y al nuevo Nodo como cabeza.
      if (pos === 1) {
        auxiliar.siguiente = this.incio;
        this.incio = auxiliar;
      } else {
        // Si es mayor a 1, crea dos punteros.
        let puntero = this.incio;
        let punteroPrevio = this.incio;
        for (let i = 0; i < pos - 1; i++) {
          if (puntero === null) break; // Rompe el ciclo si el puntero es null.
          punteroPrevio = puntero; // Recorre 1 Nodo antes de la posicion.
          puntero = puntero.siguiente; // recorre hasta un Nodo despues de la posicion.
        }
        punteroPrevio.siguiente = auxiliar; // El Nodo antes de la posicion señala al Nodo nuevo.
        auxiliar.siguiente = puntero; // El Nodo nuevo señala al Nodo posterior (puede ser null).
      }
    }
  }

  eliminarI() {
    if (this.incio === null) {
      // Imprime este mensaje cuando la lista esta vacia.
      console.log("Tu lista esta vacia");
    } else {
      // Pone de cabeza el Nodo al que hacia referencia el primer Nodo lo cual elimina este primer Nodo.
      this.incio = this.incio.siguiente;
    }
  }

  eliminarF() {
    if (this.incio === null) {
      // Imprime este mensaje cuando la lista esta vacia.
      console.log("Tu lista esta vacia");
    } else {
      // Crea el puntero para recorrer todos la lista y un puntero previo que se quedara un Nodo Atras del puntero.
      let puntero = this.incio;
      let punteroPrevio = this.incio;
      // Recorre los Nodos existentes
      while (puntero.siguiente !== null) {
        punteroPrevio = puntero;
        puntero = puntero.siguiente;
      }
      // Elimina referencia del Nodo que esta antes del ultimo.
      punteroPrevio.siguiente = null;
    }
  }

  mostrar() {
    if (this.incio === null) {
      // Imprime este mensaje cuando la lista esta vacia.
      console.log("Esta lista esta vacia.");
    } else {
      // Crea el puntero para recorrer la lista.
      let puntero = this.incio;
      // Imprime el dato del primer Nodo.
      console.log(`Nodo: ${puntero.dato}`);
      // Recorre todos los Nodos existentes e imprime su dato.
      while (puntero.siguiente !== null) {
        puntero = puntero.siguiente;
        console.log(`Nodo: ${puntero.dato}`);
      }
    }
  }
}

module.exports = Lista;
