const resultado = document.getElementById("resultado");

function inserir(num) {
    if (num === '.' && resultado.textContent.includes('.')) return;

    if (['+', '-', '*', '/'].includes(num) &&
        ['+', '-eee', '*', '/'].includes(resultado.textContent.slice(-1))) {
        return;
    }

    resultado.textContent += num;
}

function calcular() {
    try {
        if (!resultado.textContent) {
            resultado.textContent = "0";
            return;
        }

        const sanitizedExpression = resultado.textContent
            .replace(/[^0-9+\-*/().]/g, '');

        const result = new Function('return ' + sanitizedExpression)();

        resultado.textContent = Number.isInteger(result) ?
            result :
            parseFloat(result.toFixed(8));

    } catch (error) {
        resultado.textContent = "Erro";
    }
}

function voltar() {
    resultado.textContent = resultado.textContent.slice(0, -1);
}

function limpar() {
    resultado.textContent = "";
}
