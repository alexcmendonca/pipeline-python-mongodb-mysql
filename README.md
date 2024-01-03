# Pipeline ETL utilizando a biblioteca Requests do Python e Integração com API do GitHub

## 💡Objetivos
Pipeline de dados responsável por extrair informações de uma API, disponibilizando esses dados em diversas fontes. Esta abordagem é implementada através da integração de Python, MongoDB e MySQL, proporcionando versatilidade e eficiência no gerenciamento e distribuição das informações obtidas.

###### Imagem 1: Pipeline do Projeto (Crédito da imagem: Alura)
<img src="/assets/img/img-pipeline.png">


## 🖥️Desafios do Projeto
Extrair os dados de uma API e, inicialmente, disponibilizá-los em um banco de dados não-relacional, que em nosso caso será o MongoDB. Aplicar algumas transformações nesses dados, e uma vez que essas transformações sejam aplicadas, salvar esses dados estruturados em tabelas em um banco de dados relacional, que será o MySQL.

## 📄Desenvolvimento de Competências:
|Atividades|Realizadas |
|----------|-----------|
| Criar uma conta no MongoDB Atlas | Configurar um cluster no MongoDB Atlas |
| Utilizar a biblioteca pymongo | Realizar a conexão do Python com o MongoDB |
| Criar e Excluir bancos de dados no MongoDB | Criar coleções no MongoDB |
| Extrair dados de uma API | Inserir dados em um banco de dados usando pymongo |
| Deletar documentos de uma coleção | Construir funções em um script Python |
| Realizar a leitura de dados do MongoDB | Utilizar o método find para percorrer os dados |
| Atualizar os dados do MongoDB utilizando o update_many | Estruturar queries no MongoDB |
| Manipular datas utilizando Pandas | Trabalhar com diferentes operadores de consulta |
| Desenvolver uma expressão regular para selecionar dados específicos | Instalar o MySQL no WSL2 e criar usuário e senha no MySQL |
| Garantir todos os privilégios a um usuário MySQL | Conectar o Python ao MySQL |
| Criar base de dados e tabelas no MySQL com Python | Identificar diferentes tipos de dados do MySQL |
| Adicionar dados de um arquivo csv em uma tabela MySQL | Utilizar uma extensão do VS Code para visualizar uma tabela estruturada do MySQL |

## 🗂️Organização dos Arquivos
- Pasta notebooks: Arquivos com as análises detalhadas e explorações aprofundadas dos dados e solução dos desafios propostos no treinamento;
- Scripts: Arquivos python estruturado em funções, que facilitam execução de testes, reutilização de código, manutenção mais simples e automação do pipeline. Sem contar que, em um ambiente de produção, geralmente são utilizados scripts ao invés de notebooks;
- Pasta data: Nesta pasta abriga arquivos CSV que contêm os dados extraídos da API, obtidos por meio do desenvolvimento dos notebooks;
- Pasta data teste: Aqui são armazenados os arquivos CSV gerados a partir da execução dos scripts em Python.

## 🎞️Imagens do Projeto

###### Imagem 2: MongoDB Atlas
<img src="/assets/img/img-mongodb.png">

###### Imagem 3: MySQL no WSL2
<img src="/assets/img/img-mysql-wsl.png">

###### Imagem 4: Configurando extensão MySQL para VSCode
<img src="/assets/img/img-con-mysql.png">

###### Imagem 5: Visuando dados MySQL dentro do VS Code
<img src="/assets/img/img-tabela-mysql.png">


## 🔍Referências
- [Alura](https://www.alura.com.br/)