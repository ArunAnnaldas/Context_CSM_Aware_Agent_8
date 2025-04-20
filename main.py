from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryMemory
from langchain.callbacks import get_openai_callback

# Shared LLM
llm = ChatOpenAI(
    temperature=0,
    model_name="gpt-3.5-turbo",
    openai_api_key="" 
)

# Summary Memory Setup
summary_memory = ConversationSummaryMemory(
    llm=llm,
    memory_key="history",
    return_messages=True
)

# Create the conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=summary_memory,
    verbose=True
)

def run_summary_memory_agent():
    print(" Summary Memory Agent")

    # Prompt 1
    prompt_1 = "Write a function to convert Celsius to Fahrenheit"
    print(f"\n User: {prompt_1}")
    response_1 = conversation.predict(input=prompt_1)
    print(f" Assistant:\n{response_1}")

    # Prompt 2 (Should build on previous)
    prompt_2 = "Now add an option to handle Kelvin as well"
    print(f"\n User: {prompt_2}")
    response_2 = conversation.predict(input=prompt_2)
    print(f" Assistant:\n{response_2}")

    # Show current summary
    print("\n Current Summary of Memory:")
    print(summary_memory.buffer)

if __name__ == "__main__":
    with get_openai_callback() as cb:
        run_summary_memory_agent()
        print("\n📊 Token Usage Summary:")
        print(cb)
