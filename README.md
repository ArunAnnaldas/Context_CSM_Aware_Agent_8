# 🧠 Context-Aware Agent with ConversationSummaryMemory (LangChain + OpenAI)

This project demonstrates how to build a **memory-efficient, multi-turn conversational AI agent** using [LangChain](https://www.langchain.com/) and OpenAI's GPT-3.5. It uses `ConversationSummaryMemory` (CSM) to summarize the chat history instead of storing full messages, making it ideal for long-running sessions and multi-agent workflows.

---

## Compressed Memory with CSM

### 🎯 Goal:
Build an AI assistant that:
- Remembers past user prompts
- Uses memory summaries instead of full raw history
- Supports long-term, token-efficient conversations

---

## 🧠 Key Features

- Uses `ConversationSummaryMemory` for lightweight context retention
- Responds intelligently across multi-turn interactions
- Displays memory summary for transparency
- Tracks token usage via OpenAI callback
- Built with LangChain’s `ConversationChain`

---

## 🧪 Sample Dialogue

```text
💬 User: Write a function to convert Celsius to Fahrenheit
🤖 Assistant: def c_to_f(c): return c * 9/5 + 32

💬 User: Now add an option to handle Kelvin as well
🤖 Assistant: def convert_temp(temp, unit): ...

---

## 🛠 Tech Stack
Python 3.9+

LangChain

OpenAI GPT-3.5 Turbo

ConversationSummaryMemory

Token callback via LangChain
