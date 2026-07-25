# Product Query Agent with Memory

This project is an agentic system for answering product-related questions using LangChain, tools, reasoning, conversational memory, and an LLM.

## Description

This project is a brief demo of an agentic AI assistant that uses LangChain, an LLM, and memory to answer product questions in a more natural and contextual way.

## What the system does

The agent combines:
- an LLM for reasoning and response generation
- tool-based actions for structured product lookups
- memory for session continuity
- a simple workflow that demonstrates agentic behavior in practice

## Project structure

- `product_query_agent_with_memory.ipynb` — notebook implementation of the agentic system

## Repository

GitHub repository: https://github.com/eyosiasbisrat/Product_Agent_with_Insession_Memory.git

## Setup

1. Create and activate a Python environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install langchain langchain-groq python-dotenv
```

3. Create a `.env` file with your Groq API key:

```env
GROQ_API_KEY=your_key_here
```

## Usage

Open the notebook and run the cells in order:
1. define the product and review tools
2. create the agent
3. test product and review queries
4. enable memory with a checkpointer
5. run follow-up questions in the same session

## Notes

- This is a small educational example of an agentic system.
- The memory layer makes the assistant behave more like a persistent conversational agent.
- Product and review data are hardcoded for demonstration purposes.
