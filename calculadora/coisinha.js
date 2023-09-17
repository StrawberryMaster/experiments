const resultado = document.getElementById("resultado");

function inserir(num) {
    resultado.textContent += num;
}

function calcular() {
    resultado.textContent = resultado.textContent ? eval(resultado.textContent) : "Nada.";
}

function voltar() {
    resultado.textContent = resultado.textContent.slice(0, -1);
}

function limpar() {
    resultado.textContent = "";
}
