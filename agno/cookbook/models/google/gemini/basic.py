from agno.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.google import Gemini
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools

memory = Memory(
    # Use qualquer modelo para criar e gerenciar memórias
    model=Gemini(id="gemini-2.0-flash"),
    # Armazene memórias em um banco de dados SQLite
    db=SqliteMemoryDb(table_name="user_memories", db_file="tmp/agent.db"),
    # Desabilitamos a exclusão por padrão, habilite-a se necessário
    delete_memories=True,
    clear_memories=True,
)

agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(stock_price=True, analyst_recommendations=True,company_info=True, company_news=True),
    ],
    # ID do usuário para armazenar memórias, `padrão` se não fornecido
    user_id="ava",
    instructions=[
        "Use tabelas para exibir dados.",
        "Inclua fontes em sua resposta.",
        "inclua apenas o relatório em sua resposta.Nenhum outro testo."
    ],
    memory=memory,
    # Deixe o Agente gerenciar suas memórias
    enable_agentic_memory=True,
    markdown=True,
)

if __name__ == "__main__":
    # Isso criará uma memória de que as ações favoritas de "ava" são NVIDIA e TSLA
    agent.print_response(
        "minhas ações favoritas são NVIDIA e TSLA",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )
    