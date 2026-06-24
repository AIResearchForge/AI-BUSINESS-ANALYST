# src/memory.py (prostsza wersja)
from langchain.memory import ConversationBufferMemory


def get_memory_base():
    """Tworzy i zwraca prostą pamięć dla Agenta 4."""
    memory = ConversationBufferMemory(
        return_messages=True,
        memory_key="chat_history",
        input_key="input",
        output_key="output",
    )
    return memory
