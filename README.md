
<h1 align="center">
  <br>
  <a><img src="./images/logo.png" alt="Team Logo" width="200"></a>
  <br>
  Analytics Sync Regression Test Repo
  <br>
</h1>

<p>
    <a href="https://docs.aws.amazon.com/"> 
        <img src="https://img.shields.io/badge/AWS-%23FF9900.svg?style=flat&logo=amazon-aws&logoColor=white" 
            alt="Gitter">
    </a>
    <a href="https://docs.python.org/3/">
        <img src="https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54" 
            alt="Gitter">
    </a>
    <a href="">
        <img src="https://img.shields.io/badge/DataMesh-confluence-brightgreen.svg">
    </a>
</p>

Repositório de testes regressivos para o componente [Metadata Sync]("https://www.google.com").


<br>

# Índice
1. [Estrutura de Pastas](#estrutura-de-pastas)
2. [Pré-requisitos](#pré-requisitos)
3. [Como usar](#como-usar)
4. [Evoluções mapeadas](#evoluções-mapeadas)

# Estrutura de pastas
Abaixo, destacamos a estrutura e organização das pastas e arquivos importantes deste repositório:

<br>

# Pré-requisitos
Para trabalhar com o código deste repositório, os seguintes pré-requisitos são necessários:
1. Git instalado na máquina local;
2. Python versão 3.7 ou acima;
3. Pip configurado

<br>

# Como usar

Escolha um local na sua máquina local e, do seu Git Bash:

```bash
# Clone este repositório
$ git clone https://github.com/amitmerchant1990/electron-markdownify

# Entre no repositório local
$ cd electron-markdownify

# Crie um ambiente virtual para execução
$ python -m venv venv

# Instale as libs de dependência
$ pip install -r requirements.txt
```
Abra o diretório no seu editor preferido e configure:
1. A conta que deseja realizar os testes;
2. As credenciais para acesso à conta em questão.

Na documentação, estão destacados os cenários contemplados na execução do script, na seção [Cenários de Teste]()

Para executar os testes regressivos, na pasta raiz do projeto, execute o seguinte comando no terminal ou execute o arquivo main.py na sua IDE de preferência:
```bash
$ python main.py
```

<br>

# Evoluções mapeadas
Abaixo, destacamos as evoluções mapeadas a serem implementadas neste repositório, assim que tivermos oportunidade:
1. Inclusão de cenário de teste de chamadas ListPermissions
2. Gerar novas tabelas via CDP com diferentes formatos para teste (parquet, avro, LZO, etc.)
3. Inclusão de cenários de teste no Athena utilizando conexão com Impala
4. Inclusão de cenários de validação para contas Producer
