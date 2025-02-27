from crewai import Task
from agents import (evaluation_agent,score_agent,feedback_agent,mistake_corrector_agent,writer_agent,overall_agent)
from tools import my_pdf_searcher, my_internet_explorer

# Evaluation Task - Based on Rubrics Retrieved by PDF Searcher
evaluation_task = Task(
    description='Evaluate the essay based on the rubrics provided by pdf and compare it to the ideal solution. This includes assessing content, structure, grammar, and adherence to the rubric.',
    expected_output='An evaluation report that highlights strengths and weaknesses based on content, structure, and grammar, according to the rubric.',
    async_execution=False,  # Synchronous execution for evaluation
    agent=evaluation_agent,
    tools=[my_pdf_searcher],  # Use the PDF searcher to fetch the rubric dynamically
    
)

# Scoring Task - Rubric-Based Scoring
score_task = Task(
    description='Score the essay based on the rubric provided in the PDF file. Use criteria such as structure, grammar, coherence, and other performance metrics defined in the rubric. The scoring range and categories will be determined by the rubric.',
    expected_output='A numerical score, with a range defined by the rubric (e.g., 0 to 100), along with detailed justification based on each scoring criterion.',
    async_execution=False,
    agent=score_agent,
    tools=[my_pdf_searcher],  # Use the PDF searcher to get scoring criteria and range
)

feedback_task = Task(
    description='Provide detailed feedback on the essay, including strengths and areas for improvement.',
    expected_output='A paragraph of constructive feedback covering grammar, structure, and argument strength.',
    async_execution=False,
    agent=feedback_agent,
    tools=[my_pdf_searcher]  # Optional, can be used to search for additional reference material
)
mistake_correction_task = Task(
    description='Identify and correct grammatical and logical mistakes in the essay.',
    expected_output='A list of suggested corrections for grammatical errors and logical improvements.',
    async_execution=False,
    agent=mistake_corrector_agent,
    tools=[my_internet_explorer]  # Uses a grammar tool to assist in correction
)
writing_improvement_task = Task(
    description='Rewrite and improve sections of the essay that require clarity and better structure.',
    expected_output='Rewritten sections of the essay, with improved sentence structure, grammar, and clarity.',
    async_execution=False,
    agent=writer_agent,
    tools=[my_pdf_searcher]  # May use references and grammar tools to assist with writing
)
essay_processing_task = Task(
    description='Orchestrate essay evaluation, scoring, feedback, mistake correction, and rewriting.',
    expected_output='A final report with evaluation, score, feedback, corrections, and writing improvements.',
    async_execution=False,
    agent=overall_agent,
    context=[evaluation_task, score_task, feedback_task, mistake_correction_task, writing_improvement_task]
)

