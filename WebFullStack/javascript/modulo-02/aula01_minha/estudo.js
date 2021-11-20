console.log("===== DESAFIO 01 =====")

function verificar() {
    const anos = document.getElementById('idade').value;

    let mensagem = null;

    if (parseInt(anos) >0 && parseInt(anos)<13){
        mensagem= 'Criança';

    } else if (parseInt(anos) >12 && parseInt(anos)<18) { 
        mensagem = 'Adolescente';
    } else if (parseInt(anos) >=18 && parseInt(anos) <65){
        mensagem = 'Adulto';
    } else if (parseInt(anos)>=65 || parseInt(anos) != 0){
        mensagem = "Terceira idade";
        
    }
    const resultado = document.getElementById('resultado');

    resultado.value = mensagem;
}