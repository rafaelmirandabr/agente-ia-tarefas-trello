# Agente de IA para Gerenciamento de Tarefas no Trello

Projeto desenvolvido em Python utilizando **Google ADK, Gemini e Trello API**, com o objetivo de criar um assistente inteligente capaz de organizar e gerenciar tarefas por meio de linguagem natural.

## Sobre o projeto

O agente utiliza inteligência artificial para interpretar solicitações do usuário e executar operações em um quadro do Trello.

A proposta é facilitar o gerenciamento de atividades, permitindo criar tarefas, consultar cartões existentes, atualizar seu andamento e remover tarefas mediante confirmação do usuário.

## Funcionalidades

- **Consulta de data e hora:** identifica o contexto temporal da conversa.
- **Criação de tarefas:** cria cartões no Trello com título e descrição.
- **Listagem de tarefas:** consulta os cartões cadastrados.
- **Filtro por status:** permite consultar tarefas conforme sua situação.
- **Atualização de status:** movimenta cartões entre listas.
- **Remoção de tarefas:** solicita confirmação antes de excluir um cartão.

## Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Linguagem de programação |
| Google ADK | Estruturação e execução do agente |
| Google Gemini | Interpretação das solicitações |
| Trello API | Gerenciamento dos cartões |
| Py-Trello | Integração Python com Trello |
| Python-dotenv | Gerenciamento de variáveis de ambiente |

## Arquitetura do projeto

```text
agente_ia_tarefas_trello/
│
├── agente_tarefas/
│   ├── __init__.py
│   ├── agent.py
│   └── tools.py
│
├── .env
├── .env.exemplo
├── .gitignore
├── requirements.txt
└── README.md
```

### Organização dos arquivos

- `agent.py`: define o agente, o modelo Gemini, as instruções e as ferramentas disponíveis.
- `tools.py`: implementa as funções de integração com o Trello.
- `__init__.py`: permite o reconhecimento do pacote Python.
- `.env`: armazena as credenciais e configurações privadas.
- `.env.exemplo`: apresenta os nomes das variáveis necessárias, sem credenciais reais.
- `requirements.txt`: lista as dependências do projeto.

## Configuração e execução

### 1. Pré-requisitos

- Python instalado.
- Conta no Trello.
- Chave de API do Trello e token de acesso.
- Chave de API do Google AI Studio.
- Visual Studio Code (opcional).

### 2. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
cd agente_ia_tarefas_trello
```

### 3. Criar o ambiente virtual

No Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências

```powershell
pip install -r requirements.txt
```

### 5. Configurar as credenciais

Crie um arquivo `.env` na raiz do projeto, seguindo o modelo:

```env
TRELLO_API_KEY=sua_chave_trello
TRELLO_API_SECRET=seu_secret_trello
TRELLO_TOKEN=seu_token_trello
GOOGLE_API_KEY=sua_chave_google
```

**Importante:** nunca publique o arquivo `.env` ou compartilhe suas credenciais.

### 6. Configurar o quadro do Trello

O projeto utiliza um quadro configurado no arquivo `tools.py`.

Por padrão, o nome utilizado no desenvolvimento foi:

`Meu quadro do Trello`

O quadro deve possuir as seguintes listas:

- A Fazer
- Em Andamento
- Concluída

As listas de introdução do Trello podem permanecer no quadro.

### 7. Executar o agente

Na pasta principal do projeto, com o ambiente virtual ativado:

```powershell
adk web
```

Abra no navegador o endereço local apresentado no terminal, normalmente:

`http://127.0.0.1:8000`

Selecione o agente `agente_tarefas` e inicie uma conversa.

## Exemplos de utilização

**Criar uma tarefa:**

> Preciso estudar Python por uma hora hoje. Crie uma tarefa chamada Estudar Python.

**Consultar tarefas:**

> Liste todas as minhas tarefas cadastradas no Trello.

**Alterar status:**

> Altere a tarefa Estudar Python para Em Andamento.

**Remover uma tarefa:**

> Quero remover a tarefa Estudar Python.

O agente deve solicitar confirmação antes de realizar a exclusão.

## Testes realizados

Durante o desenvolvimento, foram realizados testes de integração e utilização:

| Teste | Resultado |
|---|---|
| Importação das ferramentas Python | Aprovado |
| Conexão com o Trello | Aprovado |
| Localização do quadro | Aprovado |
| Consulta dos cartões | Aprovado |
| Filtro por status | Aprovado |
| Inicialização do agente pelo ADK | Aprovado |
| Comunicação com o Gemini | Aprovado |
| Criação de cartão | Aprovado |
| Listagem de tarefas pelo agente | Aprovado |
| Movimentação entre listas | Aprovado |
| Exclusão mediante confirmação | Aprovado |

## Segurança

- As credenciais são armazenadas em variáveis de ambiente.
- O arquivo `.env` não deve ser enviado ao GitHub.
- O `.gitignore` deve impedir a publicação de arquivos privados.
- A exclusão de tarefas deve ser precedida de confirmação do usuário.

## Objetivo de aprendizagem

O projeto foi desenvolvido como atividade prática de aprendizado em inteligência artificial, automação e integração de serviços.

A implementação permitiu explorar a construção de agentes de IA, o uso de ferramentas externas, a integração com APIs e a execução de operações a partir de comandos em linguagem natural.

## Autor

Projeto desenvolvido como parte de um desafio prático da **Digital Innovation One (DIO)**.