# CSV Data Analysis Agent

A coding agent that analyzes CSV data and solves queries using natural language. Built with LangChain and Ollama to understand questions and generate Python code for data analysis.

## Features

- Ask questions about your CSV data in plain English
- Automatic Python code generation and execution
- Handles calculations, statistics, filtering, and data manipulation
- Works with any CSV file

## Installation

1. Install Ollama from [ollama.ai](https://ollama.ai)

2. Pull the Mistral model:
   ```bash
   ollama pull mistral:7b
   ```

3. Install Python packages:
   ```bash
   pip install pandas langchain-community langchain
   ```

## Usage

1. Start Ollama:
   ```bash
   ollama serve
   ```

2. Update the CSV file path in the code:
   ```python
   df = pd.read_csv("your_file_path.csv")
   ```

3. Run the script:
   ```python
   python csv_agent.py
   ```

## Example Queries

- "Calculate the mean of the 'value' column and store it in result"
- "Show rows where temperature is above 25" 
- "Group by category and sum the values"
- "Find the maximum value in each column"
- "Count how many rows have missing values"

The agent generates and executes Python code to answer your questions about the data.
