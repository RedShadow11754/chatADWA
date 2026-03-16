from .chroma import Retriever
from .serper import Serper
from google import genai
import time
import os
import dotenv

dotenv.load_dotenv()

gemini_api = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=gemini_api)


class Response:
    def __init__(self, query,context_s,context_r,session_id="default"):
        self.prompt=f'''
        You are an AI assistant specialized in the **Battle of Adwa (1896)**.

Use the provided information from two sources:

1. **Book Context (Chroma Retrieval)** – information extracted from the book *The Battle of Adwa – Milkias & Metaferia*.
2. **Web Results (Serper Search)** – relevant information retrieved from the internet.

Instructions:

* Answer the question **only using the provided context and web results**.
* Focus strictly on **the Battle of Adwa, Ethiopian history related to Adwa, its causes, events, leaders, and impact**.
* If the question is unrelated to Adwa, politely say:
  *"I can only answer questions related to the Battle of Adwa."*
* Prefer information from the **book context** when possible, and use **web results** to support or expand it.
* Keep answers **clear, factual, and concise**.
* Do not invent information that is not present in the provided sources.

Book Context:
{context_r}

Web Results:
{context_s}

Question:
{query}

Answer:
'''
        self.response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=self.prompt,
        )
    def respond(self):
        return self.response.text

class My_AI:
    def __init__(self,question):
        chroma = Retriever(question)
        serper = Serper(question)
        context, meta = chroma.chroma_result()
        search_result,serper_sources = serper.serper_result()
        gemini = Response(query=question,context_s=search_result,context_r=context)
        self.sources = {
            "source":serper_sources,
        }
        self.final_answer = {
            "answer": gemini.respond(),
        }
    def answer(self):
        return self.final_answer,self.sources

# while True:
#     start = time.time()
#     question = input("What would you like to ask about Adwa? ")
#     print("...question recieved ...")
#     chroma = Retriever(question)
#     print("...chroma retrieved ...")
#     serper = Serper(question)
#     print("...serper retrieved ...")
#     context,meta = chroma.chroma_result()
#     search_result = serper.serper_result()
#     print("...results extracted ...\n...Gemini starting...")
#     gemini = Response(query=question,context_s=search_result,context_r=context)
#     print("...gemini set ...")
#
#     print(gemini.respond())
#     final_answer = {
#         "answer": gemini.respond()
#     }
#     finish = time.time()
#     print(f"finished with {round(finish-start,2)} seconds")
#


















# import os
# import dotenv
# from langchain_chroma import Chroma
# from langchain_huggingface import HuggingFaceEmbeddings
#
#
# _embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
# _persist_dir = os.path.join(os.path.dirname(__file__), "chroma_db")
#
# _vector_store = Chroma(
#     persist_directory=_persist_dir,
#     embedding_function=_embeddings
# )
#
# _retriever = _vector_store.as_retriever(search_kwargs={"k": 4})
#
# _chat_memory = {}
# def clear_memory(session_id):
#     if session_id in _chat_memory:
#         del _chat_memory[session_id]
# from chroma import Retriever
# from serper import Serper
# q = Retriever("tell me about adwa victory")
# print("chroma done!!!\n\n\n")
# p = Serper("tell me about adwa victory")
# print(f"Chroma: {q.chroma_result()}\n\nSerper: {p.serper_result()}")