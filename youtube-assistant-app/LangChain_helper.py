from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama.llms import OllamaLLM
from langchain.embeddings.ollama import OllamaEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.vectorstores import FAISS 

embeddings = OllamaEmbeddings(model="llama3.2:1b")


video_url = "https://www.youtube.com/watch?v=hBMoPUAeLnY"
def create_vector_db_from_youtube_url(video_url: str ) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcript)

    db = FAISS.from_documents(docs, embeddings)
    return db



print(create_vector_db_from_youtube_url(video_url))