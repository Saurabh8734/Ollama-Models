from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.1")

text = """
38.2: Mitchell Starc to Ravichandran Ashwin, OUT! LBW! Mitchell Starc&nbsp;has four now! This is an absolute scorcher of a delivery. The bowling change has worked wonders again for the Aussies. Starc steams in from 'over the wicket and nails a brilliant inswinging yorker, on middle. Ravichandran Ashwin&nbsp;is not expecting that at all, he steps across early&nbsp;and gets very late to put his bat down in time as the ball crushes his toes. There is a huge appeal for LBW, and up goes the finger. However, Ashwin takes the review here. The replay confirms no bat involved and Ball Tracking comes up with three reds. Ashwin goes after a run-a-ball 22 and India&nbsp;are seven down now!"""

query = f"Extract the most important and relevant information from the following text, maintaining the sequence of the information.:{text}"
response = llm.invoke(query)

print(response)