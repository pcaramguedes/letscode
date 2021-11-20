console.log("=== CALCULADORA ===");

function calcular() {
  const n1 = document.getElementById("n1");
  const n2 = document.getElementById("n2");

  // console.log(n1, n1.id, n1.value);
  // console.log(n2, n2.id, n2.value);

  // const result = n1.value + n2.value;
  const result = parseInt(n1.value) + parseInt(n2.value);

  // console.log(result);

  const resultado = document.getElementById("resultado");

  // console.log(resultado);

  resultado.value = result;
}
