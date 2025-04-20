(base) dummyUser@dummyUsers-MacBook-Air 7_CSM_Aware_Agent % touch main.py
(base) dummyUser@dummyUsers-MacBook-Air 7_CSM_Aware_Agent % ls
main.py
(base) dummyUser@dummyUsers-MacBook-Air 7_CSM_Aware_Agent % python main.py
/Users/dummyUser/anaconda3/lib/python3.11/site-packages/langchain/chat_models/__init__.py:33: LangChainDeprecationWarning: Importing chat models from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.chat_models import ChatOpenAI`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
/Users/dummyUser/anaconda3/lib/python3.11/site-packages/langchain/chat_models/__init__.py:33: LangChainDeprecationWarning: Importing chat models from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.chat_models import ChatOpenAI`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
/Users/dummyUser/Documents/Learning/AgenticAI/7_CSM_Aware_Agent/main.py:4: LangChainDeprecationWarning: Importing get_openai_callback from /Users/dummyUser/anaconda3/lib/python3.11/site-packages/langchain/callbacks/__init__.py is deprecated. Please replace deprecated imports:

>> from /Users/dummyUser/anaconda3/lib/python3.11/site-packages/langchain/callbacks/__init__.py import get_openai_callback

with new imports of:

>> from langchain_community.callbacks.manager import get_openai_callback
You can use the langchain cli to **automatically** upgrade many imports. Please see documentation here <https://python.langchain.com/docs/versions/v0_2/>
  from langchain.callbacks import get_openai_callback
/Users/dummyUser/Documents/Learning/AgenticAI/7_CSM_Aware_Agent/main.py:7: LangChainDeprecationWarning: The class `ChatOpenAI` was deprecated in LangChain 0.0.10 and will be removed in 1.0. An updated version of the class exists in the :class:`~langchain-openai package and should be used instead. To use it run `pip install -U :class:`~langchain-openai` and import as `from :class:`~langchain_openai import ChatOpenAI``.
  llm = ChatOpenAI(
/Users/dummyUser/Documents/Learning/AgenticAI/7_CSM_Aware_Agent/main.py:14: LangChainDeprecationWarning: Please see the migration guide at: https://python.langchain.com/docs/versions/migrating_memory/
  summary_memory = ConversationSummaryMemory(
/Users/dummyUser/Documents/Learning/AgenticAI/7_CSM_Aware_Agent/main.py:21: LangChainDeprecationWarning: The class `ConversationChain` was deprecated in LangChain 0.2.7 and will be removed in 1.0. Use :meth:`~RunnableWithMessageHistory: https://python.langchain.com/v0.2/api_reference/core/runnables/langchain_core.runnables.history.RunnableWithMessageHistory.html` instead.
  conversation = ConversationChain(
 Summary Memory Agent

 User: Write a function to convert Celsius to Fahrenheit


> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
[SystemMessage(content='', additional_kwargs={}, response_metadata={})]
Human: Write a function to convert Celsius to Fahrenheit
AI:

> Finished chain.
 Assistant:
Sure! Here is a Python function that converts Celsius to Fahrenheit:

```python
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
```

You can use this function by passing a temperature in Celsius as an argument, and it will return the equivalent temperature in Fahrenheit.

 User: Now add an option to handle Kelvin as well


> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
[SystemMessage(content='The human asks the AI to write a function to convert Celsius to Fahrenheit. The AI provides a Python function that successfully converts Celsius to Fahrenheit.', additional_kwargs={}, response_metadata={})]
Human: Now add an option to handle Kelvin as well
AI:

> Finished chain.
 Assistant:
Sure! Here's the updated Python function that can handle converting Celsius, Fahrenheit, and Kelvin:

```python
def convert_temperature(value, unit):
    if unit == 'Celsius':
        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15
        return fahrenheit, kelvin
    elif unit == 'Fahrenheit':
        celsius = (value - 32) * 5/9
        kelvin = (value - 32) * 5/9 + 273.15
        return celsius, kelvin
    elif unit == 'Kelvin':
        celsius = value - 273.15
        fahrenheit = (value - 273.15) * 9/5 + 32
        return celsius, fahrenheit
    else:
        return "Invalid unit. Please enter Celsius, Fahrenheit, or Kelvin."

# Example usage
celsius_to_fahrenheit, celsius_to_kelvin = convert_temperature(25, 'Celsius')
print(f"25 degrees Celsius is equal to {celsius_to_fahrenheit} degrees Fahrenheit and {celsius_to_kelvin} Kelvin.")
``` 

Feel free to test it out with different values and units!

 Current Summary of Memory:
The human asks the AI to write a function to convert Celsius to Fahrenheit. The AI provides a Python function that successfully converts Celsius to Fahrenheit. The human then asks to add an option to handle Kelvin as well. The AI updates the Python function to handle converting Celsius, Fahrenheit, and Kelvin, providing a versatile temperature conversion tool.

📊 Token Usage Summary:
Tokens Used: 1281
	Prompt Tokens: 852
		Prompt Tokens Cached: 0
	Completion Tokens: 429
		Reasoning Tokens: 0
Successful Requests: 4
Total Cost (USD): $0.002136
(base) dummyUser@dummyUsers-MacBook-Air 7_CSM_Aware_Agent % 
