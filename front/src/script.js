async function enviar(ev) {
    ev.preventDefault();

    const form = document.getElementById('formulario');
    const dados = new FormData(form);

    try {
        const resposta = await fetch(
            "http://127.0.0.1:8000/disciplinas/",
            {
                method: "POST",
                body: dados
            }
        );
        if (!resposta.ok) {
            const erro = await resposta.json();
            console.error("Erro ao cadastrar:", erro);
            alert("Não foi possível cadastrar a disciplina.");
            return;
        }
        const resultado = await resposta.json();
        alert(resultado.message);
        form.reset();
        await cria_tabela();
    } catch (erro) {
        console.error("Erro na requisição:", erro);
        alert("Não foi possível conectar ao servidor.");
    }
}

async function cria_tabela() {
    const resposta = await fetch(
        "http://127.0.0.1:8000/disciplinas/",
        {
            method: "GET"
        }
    );
    if (!resposta.ok) {
        throw new Error("Erro ao buscar disciplinas.");
    }
    const dados = await resposta.json();
    const tbody = document.querySelector(
        '#disciplinas_cadastradas tbody'
    );
    tbody.innerHTML = '';
    dados.forEach(element => {
        const linha = document.createElement('tr');
        linha.innerHTML = `
            <td>${element[0]}</td>
            <td>${element[1]}</td>
            <td>${element[2]}</td>
            <td>${element[3]}</td>
            <td>${element[4]}</td>
            <td>${element[5]}</td>
        `;
        tbody.appendChild(linha);
    });
}

window.addEventListener('load', cria_tabela);
