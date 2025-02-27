from crewai import Agent
from tools import my_pdf_searcher, my_internet_explorer
from templates import(evaluator_system_template,evaluator_prompt_template,score_provider_system_template,score_provider_prompt_template,feedback_provider_system_template,mistake_corrector_system_template)
import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq
#GROQ_API_KEY= os.getenv("GROQ_API_KEY")
my_llm=ChatGroq(api_key="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",
             model_name="llama3-70b-8192",
             temperature=0.5)

evaluation_agent = Agent(
    role='Evaluation Agent',
    goal='''Evaluate the student essay based on the prompt{prompt} and compare it with the essay{essay} using the rubric.
    You are an Essay Evaluator, responsible for scoring essays based on a detailed rubric provided in a PDFdocument.
    The rubric contains specific traits.
    Your goal is to:
    1. Read and interpret the rubric using the PDF search tool.
    2. Evaluate the essay against each rubric trait/scoring system.
    3. Provide a detailed score for each trait/scoring system, along with a justification.
    Prompt: {prompt}
    Essay: {essay}
    You must always adhere strictly to the rubric for consistent scoring.
    Use my_pdf_searcher to retrieve the specific rubric details.

    Behave as an expert essay evaluator with experience in grading essays.''',
    backstory="""You are an experienced evaluation agent for assessing essays. You are an experienced evaluator, responsible for evaluating student essays based on a given prompt. """,
    tools=[my_pdf_searcher, my_internet_explorer],  # Using tools like PDF Searcher and Internet Explorer for referencing
    llm=my_llm,
    max_iter=10,
    verbose=True,
    allow_delegation=False,  # Direct evaluation responsibility
    #system_template=evaluator_system_template,  # Optional: System template for evaluation logic
    #prompt_template=evaluator_prompt_template,  # Optional: Custom prompts for evaluation  configuration
    cache=True,
)
score_agent = Agent(
    role='Score Provider Agent',
    goal="""Score essays{essay} based on predefined criteria.
    You are a Expert Score Provider. Your job is to provide a final score for the essay based on the scores given for each trait by the Evaluator.
    Ensure that the final score reflects the rubric's criteria and the justification provided for each trait.
    Prompt: {prompt}
    Essay: {essay}
    Always ensure the score aligns with the rubric retrieved using my_pdf_searcher.
""",
    backstory="""You are responsible for providing a detailed numeric score for the essay based on the provided rubrics and relevance to the prompt.""",
    tools=[my_pdf_searcher],  # This agent may use PDF searcher or reference tools
    llm=my_llm,
    max_iter=5,  # Fewer iterations needed for scoring
    verbose=True,
    allow_delegation=False,  # Direct scoring responsibility
    #system_template=score_provider_system_template,  # Optional: Logic for score evaluation
    #prompt_template=score_provider_prompt_template,  # Optional: Custom scoring criteria
    cache=False,  # No need to cache scores, depends on the project
)

feedback_agent = Agent(
    role='Feedback Provider Agent',
    goal='''
    You are a Feedback Provider responsible for providing constructive feedback to students based on their essay scores.
    Use the Evaluator's scoring of each rubric trait to provide feedback.
    Focus on what the student did well, and suggest specific areas for improvement for each trait.
    Prompt: {prompt}
    Essay: {essay}
    You should offer actionable suggestions that will help the student improve their essay writing skills''',
    backstory="""You are an expert feedback provider for academic writing. Your responsibility is to offer constructive feedback on how the essay can be improved in terms of grammar, structure, and overall clarity.""",
    tools=[my_internet_explorer],  # The agent may use the internet for examples and references
    llm=my_llm,
    max_iter=10,
    verbose=True,
    allow_delegation=False,  # Direct feedback responsibility
    #system_template=feedback_provider_system_template,  # Optional: Custom feedback system template
    #response_template=,  # Optional: Response template for structured feedback
    cache=True,  # Feedback may need to be reused
)


mistake_corrector_agent = Agent(
    role='Mistake Corrector Agent',
    goal='''You are a Mistake Corrector responsible for identifying mistakes in essays and suggesting corrections.
    Your focus is on grammar, spelling, punctuation, and sentence structure errors. Use the rubric to determine if there are specific areas where the student has made mistakes.''',
    backstory="""You specialize in finding and correcting grammatical, structural, and content-related mistakes in essays.""",
    tools=[my_internet_explorer],  # Uses web resources to suggest corrections
    llm=my_llm,
    max_iter=15,
    verbose=True,
    #system_template = mistake_corrector_system_template,
    allow_delegation=False,  # Direct responsibility to correct mistakes  
)


writer_agent = Agent(
    role='Writer Agent',
    goal='Rewrite sections of the essay{essay} to improve clarity and structure',
    backstory="""You are an experienced writer agent responsible for rewriting and improving essay content. You take into account feedback and corrections to refine the writing.""",
    tools=[my_internet_explorer, my_pdf_searcher],  # Tools for writing and referencing
    llm=my_llm,
    max_iter=10,
    verbose=True,
    allow_delegation=False,  # Direct writing improvement responsibility
    cache=True,  # Can cache previous improvements for reusability
)
overall_agent = Agent(
  role='Essay Processing Manager',
  goal='Orchestrate essay evaluation, scoring, feedback, mistake correction, and writing improvements.',
  backstory="""You manage a team of agents responsible for different aspects of essay processing, 
  ensuring high-quality evaluations, scoring, feedback, and corrections.""",
  tools=[],  # Optional, as the sub-agents handle the tools
  llm=my_llm,  
  verbose=True,
  allow_delegation=True,  # Allows delegation to the sub-agents
  crew=[evaluation_agent, score_agent, feedback_agent,mistake_corrector_agent , writer_agent],  # Crew of agents working together
  cache=True,
  allow_code_execution=False,
  max_retry_limit=3,
)
