const Lista = require("./Lista");
const lstEnlazada = new Lista();

lstEnlazada.insertarF(67);
lstEnlazada.insertarF(78);
lstEnlazada.insertarF(45);
lstEnlazada.mostrar(); // resultado => 67, 78, 45
console.log("");

lstEnlazada.insertarI(35);
lstEnlazada.insertarI(15);
lstEnlazada.mostrar(); // resultado => 15, 35, 67, 78, 45
console.log("");

lstEnlazada.eliminarI();
lstEnlazada.eliminarF();
lstEnlazada.mostrar(); // resultado => 35, 67, 78
console.log("");

lstEnlazada.insertarPos(70, 3);
lstEnlazada.mostrar(); // resultado => 35, 67, 70, 78
