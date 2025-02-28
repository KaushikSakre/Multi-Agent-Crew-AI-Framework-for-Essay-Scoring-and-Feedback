from crewai_tools import tool
from crewai_tools.tools import PDFSearchTool,WebsiteSearchTool
from langchain_groq import ChatGroq
import google.generativeai as genai
#llm=ChatGroq(api_key='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',
#             model_name="llama3-70b-8192")
# PDF Search Tool
pdf_path = input("Enter the full path of the PDF file: ")
my_pdf_searcher = PDFSearchTool(
    config=dict(
        llm=dict(
            provider="groq", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama3-70b-8192",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    ),
    pdf=pdf_path,
	description="""
        A dynamic tool to read and interpret the essay rubric provided by the user. 
        It extracts the expected scoring guidelines based on key traits such as focus, organization, voice, word choice, and grammar. 
        The rubric may change depending on user input and can adapt to different grading criteria, ensuring that essay evaluations are aligned with the specific rubric provided at the time.
        NOTE:- in the rubric it's not nesscary that the traits will be mentioned that time consider (content,organization,language) as trait 
    """
)
# Website Search Tool
my_internet_explorer = WebsiteSearchTool(
    config=dict(
        llm=dict(
            provider="groq", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="gemma-7b-it",
                temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)
