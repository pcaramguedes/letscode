console.log("=== CALCULADORA IMC ===");

function calcular() {
  const peso = document.getElementById("peso");
  const altura = document.getElementById("altura");

  const result = parseFloat(peso.value) / (parseFloat(altura.value) ** 2);

  const imc = document.getElementById("imc");

  imc.value = result.toFixed(2);

  const classificacao = document.getElementById("classificacao");

  if (imc.value < 18) {
    classificacao.value = "Abaixo do normal"
  } else if (imc.value >= 18 && imc.value < 25) {
    classificacao.value = "Peso normal"
  } else if (imc.value >= 25 && imc.value < 30) {
    classificacao.value = "Sobrepeso"
  } else if (imc.value >= 30 && imc.value < 35) {
    classificacao.value = "Obesidade grau 1"
  } else if (imc.value >= 35 && imc.value < 40) {
    classificacao.value = "Obesidade grau 2"
  } else {
    classificacao.value = "Obesidade grau 3"
  }
}

/*

  Abaixo do normal: IMC abaixo de 18
  Peso normal: IMC entre 18.0 a 24,9 kg/m2
  Sobrepeso: IMC entre 25.0 a 29,9 kg/m2
  Obesidade grau 1: IMC entre 30.0 - 34.9 kg/m2;
  Obesidade grau 2: IMC entre 35.0 - 39.9 kg/m2;
  Obesidade grau 3 ou obesidade mórbida: IMC igual ou superior 40 kg/m2.

*/