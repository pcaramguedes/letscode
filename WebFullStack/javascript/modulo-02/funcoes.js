console.log("=== FUNCOES ===");

// Declaração de "Função Nomeada"
// ES6 => default parameter
function soma(a=0, b=0) {
  const result = a + b;
  return result;
}

// Executar uma Função
// NaN - Not a Number
console.log( soma() ); // 0 
console.log( soma(14) ); // 14 
console.log( soma(8, 12) ); // 20


// Declaração de "Função Anônima"
const sum = function (a=0, b=0) {
  return a + b;
}

// Executar uma Função
console.log( sum() ); // 0
console.log( sum(14) ); // 14
console.log( sum(8, 12) ); // 20
