// while (enquanto)
let var1 = 3;

while (var1 > 0) {
  console.log('Variável 1:', var1);

  var1 -= 1;
}


let var2 = 10

while (true) {
  console.log('Variável 2:', var2);
  var2 = var2 + 1;

  if (var2 === 17) {
    continue;
  }

  if (var2 === 24) {
    break;
  }

  console.log('linha 27');
}

function geraNumberoAleatorio() {
  return Math.round(Math.random()*10)
}

let numeroSecreto = geraNumberoAleatorio()
let tentativa = -1

while (numeroSecreto != tentativa) {
  tentativa = prompt('Digite um número de 0 a 10:')

  if (numeroSecreto == tentativa) {
    alert(`Acertou! O número é: ${numeroSecreto}`)
  }
}

// do-while (enquanto)

let num = 1;
do {
    console.log(`Numero num (do while)= ${num}`);
    num += 1;
} while (num < 5);

// for (para)

// forEach