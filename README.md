# Hackathon - Desenvolvimento Web

A ideia é passar uma semana criando um site, na segunda fazemos o front, terça a api, na quarta o banco, na quinta o javascript pra conectar o front com o back e na sexta a conexão.

Site que recebe um cadastro de disciplinas e informações
Nós precisamos ter o poder de criar uma nova disciplina, ela precisa receber uma série de informações e precisa ter a possibilidade de apertar um botão que envia e registra a disciplina.

Alguns dos campos esperados, são:

- Dia da semana
- Período
- Nome
- Código
- Nota
- Frequência
- Botão de Enviar

Nessa tela, também será importante retornar todas as disciplinas cadastradas em formato tabelado. Contendo todas as informações cadastradas.

Front é simples, desenvolvido apenas com HTML, CSS e JavaScript(sem frameworks) e o Back ta sendo desenvolvido com Python e FastAPI, o banco com SQLite

Temos até o momento Duas rotas:

- /disciplinas/ GET
- /disciplinas/ POST

Porém a ideia é criar uma rota de edição de disciplina e outra para deletar
