from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from config.settings import llm_1

def load_and_index(input_pdf_path: str):
    reader = SimpleDirectoryReader(input_files=[input_pdf_path])
    documents = reader.load_data()
    splitter = SentenceSplitter(chunk_size=1024)
    nodes = splitter.get_nodes_from_documents(documents)

    embed_model = GoogleGenAIEmbedding(model_name="text-embedding-004", embed_batch_size=100)
    Settings.llm = llm_1
    Settings.embed_model = embed_model

    return VectorStoreIndex(nodes)
