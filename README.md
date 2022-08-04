# Desafio Flask
Este repositório contém uma teste de login e register, com um banco de dados que guarda os usuários registrados. Feito por João Lucas Simões Moreira.

## Tecnologias utilizadas e descrição das pastas
As tecnologias de programação utilizadas foram HTML5, CSS3, Bootstrap e o Flask, sendo este último um framework da linguagem Python. Na pasta **static**, estão localizados os códigos do Bootstrap e o arquivo *style.css*, que é utilizado nas quatro páginas. Já na pasta **templates** estão os códigos *.html*. Por fim, o arquivo *app.py*, que quando executado cria um servidor com esses *htmls* citados, está localizado acima dessas duas pastas.
<br> **Atenção:** ao lado do repositório, existe um dado *94.9% JavaScript*, porém não utilizei essa linguagem no projeto: esse número se deu ao tamanho dos arquivos Bootstrap de JavaScript.

## Como executar?
Após baixar o projeto, **primeiro** modifique o caminho para o banco de dados no programa app.py, já que o caminho explicitado funciona somente na minha máquina. Após isso, basta que você rode o comando *python app.py*, com uma instância sendo criada no localhost(*localhost:5000*). Você pode cadastrar um novo usuário para entrar em uma página que apenas cadastrados possuem acesso. <br> **Detalhe:** se você tentar entrar direto na *localhost:5000* sem ter cadastrado um usuário, você será redirecionado para a tela de login, sendo necessário logar primeiro para acessá-la.

## Atenção para erros!
Se ocorrer o seguinte erro: *AttributeError: 'NoneType' object has no attribute 'password'*, significa que o email que você tentou acessar não está cadastrado. Não consegui redirecionar esse erro para uma mensagem flash ou algo semelhante, porém não desespere: é normal. Ademais, outros erros aparecem em mensagens *flash*, como *Senha incorreta*, *Email já cadastrado*, etc.

## Imagens do projeto

<img src="https://github.com/JNDGitHub/Desafio-Flask/blob/master/images/welcomeflask.jpg" width="800px" height="auto">
<br>
<img src="https://github.com/JNDGitHub/Desafio-Flask/blob/master/images/loginflask.jpg" width="800px" height="auto">
<br>
<img src="https://github.com/JNDGitHub/Desafio-Flask/blob/master/images/registerflask.jpg" width="800px" height="auto">
<br>
<img src="https://github.com/JNDGitHub/Desafio-Flask/blob/master/images/indexflasknewnew.jpg" width="800px" height="auto">
<br>
