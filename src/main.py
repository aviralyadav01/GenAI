import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")


# DEFINING THE GROQ LLM
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=None,
)
result = llm.invoke("what is genai")
print(result)

# # DATA INGESTION 
# from langchain_docling.loader import DoclingLoader
# FILE_PATH = "https://en.wikipedia.org/wiki/History_of_India"

# loader = DoclingLoader(file_path = FILE_PATH)
# docs=loader.load()


# # DATA TRANSFORMATION 
# from langchain_text_splitters import RecursiveCharacterTextSplitter

# text_splitter = RecursiveCharacterTextSplitter(chunk_size = 300 , chunk_overlap = 20)
# documents = text_splitter.split_documents(docs)

# #EMBEDDING HUGGINGFACE
# from langchain_huggingface import HuggingFaceEmbeddings

# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-mpnet-base-v2",
#     encode_kwargs={"normalize_embeddings": True},
# )

# query_result = embeddings.embed_query(documents)
