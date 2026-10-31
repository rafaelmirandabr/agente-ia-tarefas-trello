
import os
import unicodedata
from datetime import datetime

from dotenv import load_dotenv
from trello import TrelloClient


# Carrega as variáveis de ambiente
load_dotenv()


# Credenciais do Trello
TRELLO_API_KEY = os.getenv("TRELLO_API_KEY")
TRELLO_API_SECRET = os.getenv("TRELLO_API_SECRET")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")


# Configuração do quadro
BOARD_NAME = "Meu quadro do Trello"


# Nomes das listas
LIST_NAMES = {
    "a fazer": "A Fazer",
    "em andamento": "Em Andamento",
    "concluido": "Concluída",
}


def conectar_trello():
    """
    Estabelece a conexão com o Trello.
    """

    if not TRELLO_API_KEY or not TRELLO_API_SECRET or not TRELLO_TOKEN:
        raise ValueError(
            "Credenciais do Trello não configuradas no arquivo .env."
        )

    return TrelloClient(
        api_key=TRELLO_API_KEY,
        api_secret=TRELLO_API_SECRET,
        token=TRELLO_TOKEN,
    )


def obter_quadro(client):
    """
    Localiza o quadro do Trello configurado no projeto.
    """

    quadros = client.list_boards()

    quadro = next(
        (b for b in quadros if b.name == BOARD_NAME),
        None,
    )

    if quadro is None:
        raise ValueError(
            f"Quadro '{BOARD_NAME}' não encontrado no Trello."
        )

    return quadro


def normalizar_texto(texto):
    """
    Padroniza textos, removendo diferenças entre
    letras maiúsculas e minúsculas e acentos.
    """

    texto = unicodedata.normalize("NFD", texto.lower())

    return "".join(
        caractere
        for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )


def normalizar_status(status):
    """
    Padroniza as formas de escrever o status concluído.
    """

    status = normalizar_texto(status)

    if status in ("concluida", "concluido"):
        return "concluido"

    return status


def get_temporal_context():
    """
    Retorna a data e a hora atuais.
    """

    agora = datetime.now()

    return agora.strftime("%d/%m/%Y %H:%M:%S")


def adicionar_tarefa(
    nome_da_task: str,
    descricao_da_task: str,
    due_date: str = None
):
    """
    Cria uma nova tarefa no quadro do Trello.
    """

    try:
        client = conectar_trello()
        quadro = obter_quadro(client)

        listas = quadro.list_lists()

        minha_lista = next(
            (
                lista for lista in listas
                if normalizar_texto(lista.name)
                == normalizar_texto(LIST_NAMES["a fazer"])
            ),
            None,
        )

        if minha_lista is None:
            return "Erro: lista 'A fazer' não encontrada no Trello."

        minha_lista.add_card(
            name=nome_da_task,
            desc=descricao_da_task,
            due=due_date,
        )

        return f"Tarefa '{nome_da_task}' adicionada com sucesso ao Trello."

    except Exception as erro:
        return f"Erro ao adicionar tarefa: {str(erro)}"


def listar_tarefas(status: str = "todas"):
    """
    Lista as tarefas cadastradas no Trello,
    permitindo filtrar pelo status.
    """

    try:
        client = conectar_trello()
        quadro = obter_quadro(client)

        listas = quadro.list_lists()

        status_normalizado = normalizar_status(status)

        status_permitidos = {
            "todas",
            "a fazer",
            "em andamento",
            "concluido",
        }

        if status_normalizado not in status_permitidos:
            return (
                "Status inválido. Utilize: todas, a fazer, "
                "em andamento ou concluido."
            )

        tarefas = []

        for lista in listas:

            nome_lista = normalizar_texto(lista.name)

            if status_normalizado != "todas":
                nome_lista_filtro = normalizar_texto(
                    LIST_NAMES[status_normalizado]
                )

                if nome_lista != nome_lista_filtro:
                    continue

            cards = lista.list_cards()

            for card in cards:
                tarefas.append({
                    "nome": card.name,
                    "descricao": card.desc,
                    "vencimento": card.due,
                    "status": lista.name,
                    "id": card.id,
                })

        if not tarefas:
            return "Nenhuma tarefa encontrada para o filtro informado."

        return tarefas

    except Exception as erro:
        return f"Erro ao listar tarefas: {str(erro)}"


def mudar_status_tarefa(
    nome_da_task: str,
    novo_status: str
):
    """
    Altera o status de uma tarefa no Trello.
    """

    try:
        client = conectar_trello()
        quadro = obter_quadro(client)

        listas = quadro.list_lists()

        status_normalizado = normalizar_status(novo_status)

        if status_normalizado not in LIST_NAMES:
            return (
                "Status inválido. Utilize: a fazer, "
                "em andamento ou concluido."
            )

        nome_lista_destino = LIST_NAMES[status_normalizado]

        lista_destino = next(
            (
                lista for lista in listas
                if normalizar_texto(lista.name)
                == normalizar_texto(nome_lista_destino)
            ),
            None,
        )

        if lista_destino is None:
            return f"Lista '{nome_lista_destino}' não encontrada."

        card_encontrado = None
        lista_origem = None

        for lista in listas:
            cards = lista.list_cards()

            card_encontrado = next(
                (
                    card for card in cards
                    if card.name.lower() == nome_da_task.lower()
                ),
                None,
            )

            if card_encontrado:
                lista_origem = lista
                break

        if card_encontrado is None:
            return f"Tarefa '{nome_da_task}' não encontrada."

        if lista_origem.id == lista_destino.id:
            return (
                f"A tarefa '{nome_da_task}' já está "
                f"na lista '{lista_destino.name}'."
            )

        card_encontrado.change_list(lista_destino.id)

        return (
            f"Tarefa '{nome_da_task}' movimentada com sucesso: "
            f"{lista_origem.name} → {lista_destino.name}."
        )

    except Exception as erro:
        return f"Erro ao alterar status da tarefa: {str(erro)}"


def remover_tarefa(nome_da_task: str):
    """
    Remove uma tarefa do quadro do Trello.
    """

    try:
        client = conectar_trello()
        quadro = obter_quadro(client)

        listas = quadro.list_lists()

        card_encontrado = None

        for lista in listas:
            cards = lista.list_cards()

            card_encontrado = next(
                (
                    card for card in cards
                    if card.name.lower() == nome_da_task.lower()
                ),
                None,
            )

            if card_encontrado:
                break

        if card_encontrado is None:
            return f"Tarefa '{nome_da_task}' não encontrada."

        card_encontrado.delete()

        return f"Tarefa '{nome_da_task}' removida com sucesso."

    except Exception as erro:
        return f"Erro ao remover tarefa: {str(erro)}"
