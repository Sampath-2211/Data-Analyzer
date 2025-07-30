import pandas as pd
from langchain_community.llms import Ollama
from langchain.agents import Tool, initialize_agent, AgentType

# Read the CSV file
df = pd.read_csv("/Users/kittusmac/Downloads/indian_ocean_water_vapor.csv")

def execute_code(code: str) -> str:
    code = code.strip().strip("'\"")
    
    local_vars = {"df": df}
    global_vars = {"df": df}
    try:
        exec(code, global_vars, local_vars)
        if "result" in local_vars:
            return f"Result: {local_vars['result']}"
        else:
            return "No result variable found. Make sure to use 'result = ...' in your code."
    except Exception as e:
        return f"Error: {e}"

tool = Tool(
    name="CSVExecutor",
    func=execute_code,
)

llm = Ollama(model="mistral:7b", temperature=0)

agent = initialize_agent(
    tools=[tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

query = "Calculate the mean of the 'value' column and store it in result"
response = agent.invoke({"input": query})
print("👉 Result:", response["output"])