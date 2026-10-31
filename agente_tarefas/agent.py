
from google.adk.agents.llm_agent import Agent

from .tools import (
    get_temporal_context,
    adicionar_tarefa,
    listar_tarefas,
    mudar_status_tarefa,
    remover_tarefa,
)

root_agent = Agent(
    model="gemini-3.5-flash-lite",
    name="agente_tarefas",
    description="Agente de Inteligência Artificial para gerenciamento de tarefas.",

    instruction="""
    Você é um assistente de organização de tarefas.

    Seu objetivo é ajudar o usuário a gerenciar suas tarefas de forma
    eficiente, utilizando o Trello como ferramenta principal.

    Ao iniciar uma conversa:
    1. Consulte get_temporal_context para obter a data e hora atuais.
    2. Informe a data ao usuário.
    3. Pergunte quais tarefas ele precisa realizar no dia.

    Durante a conversa:
    - Pergunte se existem outras tarefas a adicionar.
    - Crie um card para cada tarefa informada usando adicionar_tarefa.
    - Registre o nome e a descrição de cada tarefa.
    - Utilize listar_tarefas para consultar e apresentar as tarefas.
    - Utilize mudar_status_tarefa para atualizar o andamento.
    - Utilize remover_tarefa somente quando o usuário solicitar explicitamente.

    Regras:
    - Não invente tarefas ou informações.
    - Não informe que uma operação foi concluída sem confirmação da ferramenta.
    - Antes de excluir uma tarefa, confirme com o usuário.
    - Seja objetivo, organizado e cordial.
    - Utilize as ferramentas disponíveis sempre que necessário.
    """,

    tools=[
        get_temporal_context,
        adicionar_tarefa,
        listar_tarefas,
        mudar_status_tarefa,
        remover_tarefa,
    ],
)
