console.log("==== CONDICIONAIS ===");
// let retorno = null;

// alert('Boa Noite !!');
// if (confirm("Você é maior de idade? ")){
//     retorno = 'acesso permitido !!';
// } else {
//    retorno = 'acesso negado !!';
// }
// alert(retorno);

// const idade = parseInt(prompt('Digite sua idade: '));
// let mensagem = null;

// if (idade >=18) {
//     mensagem = 'Maior de idade';
// } else if (idade<=0) {
//     mensagem = 'vc nao nasceu ainda';
// } else if (idade >12 && idade<=17) {
//     mensagem = 'Adolescente';
// } else {
//     mensagem = 'Criança ';
// }
// console.log(mensagem);

const mes = parseInt(prompt('Digite o número do mês (1 à 12): '));
switch (mes) {
    case 1:
        console.log('Janeiro');
        break;
    case 2:
        console.log('Fevereiro');
        break;
    case 3:
        console.log('março');
        break;
    case 4:
        console.log('Abril');
        break;
    case 5:
        console.log('Maio');
        break;
    case 6:
        console.log('Junho');
        break;
    case 7:
        console.log('Julho');
        break;
    case 8:
        console.log('Agosto');
        break;
    case 9:
        console.log('Setembro');
        break;
    case 10:
        console.log('Outubro');
        break;
    case 11:
        console.log('Novembro');
        break;         
    case 12:
        console.log('Dezembro');
        break;         
    default:
        console.log(`Mês ${mes} digitado não é válido`);
        break;
}