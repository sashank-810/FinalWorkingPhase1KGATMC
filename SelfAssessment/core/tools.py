# core/tools.py (Corrected and Refactored)

from crewai.tools import BaseTool
from llama_index.core import PromptTemplate, VectorStoreIndex
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.response_synthesizers import get_response_synthesizer, ResponseMode
from typing import Any, Type
import re
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.tools import YouTubeSearchTool # Corrected import for langchain's tool

# Base class for our custom RAG tools to hold the vector_index
class BaseRAGTool(BaseTool):
    vector_index: VectorStoreIndex

    class Config:
        arbitrary_types_allowed = True

# --- Tool for Summaries, Notes, MCQs, and Explanations ---
class RAGQueryTool(BaseRAGTool):
    name: str
    description: str
    prompt_template: str

    def _run(self, query: str) -> str:
        """Executes a prompt-based RAG query."""
        template = PromptTemplate(self.prompt_template)
        synthesizer = get_response_synthesizer(
            response_mode=ResponseMode.COMPACT,
            text_qa_template=template
        )
        retriever = self.vector_index.as_retriever(similarity_top_k=4)
        query_engine = RetrieverQueryEngine(retriever=retriever, response_synthesizer=synthesizer)
        response = query_engine.query(query)
        return str(response)

# --- Tool for Web Search ---
class WebSearchTool(BaseRAGTool):
    name: str = "Web Topic Searcher"
    description: str = "Identifies key topics in a document and finds relevant web resources."

    def _run(self) -> str:
        """Performs a web search for each topic extracted from the document."""
        query_engine = RetrieverQueryEngine(retriever=self.vector_index.as_retriever())
        ans_1 = query_engine.query(
            "Give all the topics which this document is based on as a Python list of strings, each item separated by a comma."
        )
        topics = re.findall(r"'(.*?)'", str(ans_1))

        search = GoogleSerperAPIWrapper()
        all_results = []
        for topic in topics:
            try:
                search_results = search.results(topic)
                links = [r["link"] for r in search_results.get("organic", []) if "link" in r][:3]
                if links:
                    formatted = "\n".join(f"- {url}" for url in links)
                    all_results.append(f"\n### {topic}\n{formatted}")
            except Exception as e:
                all_results.append(f"\n### {topic}\nError fetching results: {str(e)}")
        return "\n".join(all_results)

# --- Tool for YouTube Search ---
class YouTubeSearchTool(BaseRAGTool):
    name: str = "YouTube Video Searcher"
    description: str = "Identifies key topics in a document and finds relevant YouTube videos."

    def _run(self) -> str:
        """Searches YouTube for videos based on extracted document topics."""
        query_engine = RetrieverQueryEngine(retriever=self.vector_index.as_retriever())
        ans_1 = query_engine.query(
            "Give all the topics which this document is based on as a Python list of strings, each item separated by a comma."
        )
        topics = re.findall(r"'(.*?)'", str(ans_1))

        yt_search = YouTubeSearchTool()
        all_results = []
        for topic in topics:
            # The run method of langchain's tool takes a string of comma-separated topics
            video_result = yt_search.run(topic)
            all_results.append(f"\n### {topic}\n{video_result}")
        return "\n".join(all_results)