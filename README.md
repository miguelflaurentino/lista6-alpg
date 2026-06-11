# Projeto de Questões - Faculdade

Este é um projeto simples desenvolvido em Python que contém um conjunto de
questões acadêmicas. A validação das soluções é feita de forma automatizada por
meio de testes com o **Pytest**.

## 🚀 Pré-requisitos

Para rodar o projeto em outra máquina, certifique-se de ter instalado:

- [mise](https://mise.jdx.dev/) (gerenciador de versões)
- Python (gerenciado automaticamente pelo mise)

## 🔧 Configuração do Ambiente

Siga os passos abaixo no terminal para preparar a máquina e executar os testes:

### 1. Entrar na pasta do projeto

```bash
cd lista6-alpg
```

### 2. Configurar a versão correta do Python

Como o projeto utiliza o `mise`, execute o comando abaixo para garantir que a
versão do Python especificada no arquivo `.mise.toml` esteja instalada e ativa
no diretório:

```bash
mise install

```

### 3. Criar e ativar o ambiente virtual

Crie um ambiente isolado para instalar as bibliotecas do projeto:

```bash
# Criar o ambiente virtual
python -m venv .venv

# Ativar o ambiente (Linux/macOS)
source .venv/bin/activate

# Ativar o ambiente (Windows - PowerShell)
# .venv\Scripts\Activate.ps1

```

### 4. Instalar as dependências

Com o ambiente virtual ativado, instale o `pytest` e a biblioteca `tabulate`:

```bash
pip install -r requirements.txt

```

## 🧪 Executando os Testes

Para rodar todas as questões e verificar as respostas, basta executar o comando
do Pytest na raiz do projeto:

```bash
pytest

```

Se quiser ver uma saída mais detalhada com o nome de cada teste executado, utilize:

```bash
pytest -v

```

## 📁 Estrutura básica do projeto

```text
├── .mise.toml          # Configuração de versão do Python pelo mise
├── .gitignore          # Arquivos ignorados pelo Git (.venv, __pycache__, etc.)
├── requirements.txt    # Lista de dependências (pytest, tabulate)
├── README.md           # Instruções do projeto
│
├── questao1/           # Pasta contendo a resolução da primeira questão
│   ├── main.py               # Arquivo principal com a lógica da questão
│   ├── test_calculadora.py   # Arquivo de testes específicos para esta questão
│   └── outros_arquivos.py    # Outros módulos usados na questão
│
└── questao2/           # Estrutura se repete para as demais questões...
    ├── arquivo.py
    └── test_logica.py

```
