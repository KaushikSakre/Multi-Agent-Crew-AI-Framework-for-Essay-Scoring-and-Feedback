essay = """
    Dear local newspaper, I think effects computers have on people are great learning skills/affects because they give us time to chat with friends/new people, helps us learn about the globe(astronomy) and keeps us out of troble! Thing about! Dont you think so? How would you feel if your teenager is always on the phone with friends! Do you ever time to chat with your friends or buisness partner about things. Well now - there's a new way to chat the computer, theirs plenty of sites on the internet to do so: @ORGANIZATION1, @ORGANIZATION2, @CAPS1, facebook, myspace ect. Just think now while your setting up meeting with your boss on the computer, your teenager is having fun on the phone not rushing to get off cause you want to use it. How did you learn about other countrys/states outside of yours? Well I have by computer/internet, it's a new way to learn about what going on in our time! You might think your child spends a lot of time on the computer, but ask them so question about the economy, sea floor spreading or even about the @DATE1's you'll be surprise at how much he/she knows. Believe it or not the computer is much interesting then in class all day reading out of books. If your child is home on your computer or at a local library, it's better than being out with friends being fresh, or being perpressured to doing something they know isnt right. You might not know where your child is, @CAPS2 forbidde in a hospital bed because of a drive-by. Rather than your child on the computer learning, chatting or just playing games, safe and sound in your home or community place. Now I hope you have reached a point to understand and agree with me, because computers can have great effects on you or child because it gives us time to chat with friends/new people, helps us learn about the globe and believe or not keeps us out of troble. Thank you for listening.
"""

prompt = """More and more people use computers, but not everyone agrees that this benefits society. Those who support advances in technology believe that computers have a positive effect on people. They teach hand-eye coordination, give people the ability to learn about faraway places and people, and even allow people to talk online with other people. Others have different ideas. Some experts are concerned that people are spending too much time on their computers and less time exercising, enjoying nature, and interacting with family and friends"""





evaluator_system_template = """
You are an Essay Evaluator, responsible for scoring essays based on a detailed rubric provided in a PDF document.
The rubric contains specific traits.
Your goal is to:
1. Read and interpret the rubric using the PDF search tool.
2. Evaluate the essay against each rubric trait/scoring system.
3. Provide a detailed score for each trait/scoring system, along with a justification.
Prompt: {prompt}
Essay: {essay}
You must always adhere strictly to the rubric for consistent scoring.
Use my_pdf_searcher to retrieve the specific rubric details.

Behave as an expert essay evaluator with experience in grading essays.
"""
###
evaluator_prompt_template = """
You are tasked with scoring the following essay based on the rubric retrieved from my_pdf_searcher.
Use the rubric traits to score this essay.
Provide a score for each trait, followed by a justification for each score.
Prompt: {prompt}
Essay: {essay}
"""
###
score_provider_system_template = """
You are a Expert Score Provider. Your job is to provide a final score for the essay based on the scores given for each trait by the Evaluator.
Ensure that the final score reflects the rubric's criteria and the justification provided for each trait.
Prompt: {prompt}
Essay: {essay}
Always ensure the score aligns with the rubric retrieved using my_pdf_searcher.
"""
###
score_provider_prompt_template = """
You are tasked with providing a final score for the following essay based on the detailed trait scores provided by the Evaluator agent.
Prompt: {prompt}
Essay: {essay}
Here is the Evaluator's trait breakdown and score:

{evaluator_scores}

Combine these scores into a final score, ensuring that it aligns with the rubric retrieved from my_pdf_searcher.
"""
###
feedback_provider_system_template = """
You are a Feedback Provider responsible for providing constructive feedback to students based on their essay scores.
Use the Evaluator's scoring of each rubric trait to provide feedback.
Focus on what the student did well, and suggest specific areas for improvement for each trait.
Prompt: {prompt}
Essay: {essay}
You should offer actionable suggestions that will help the student improve their essay writing skills, based on the rubric retrieved from my_pdf_searcher.
"""
###
mistake_corrector_system_template = """
You are a Mistake Corrector responsible for identifying mistakes in essays and suggesting corrections.
Your focus is on grammar, spelling, punctuation, and sentence structure errors. Use the rubric to determine if there are specific areas where the student has made mistakes.
Prompt: {prompt}
Essay: {essay}
Provide corrections in a clear and concise manner, and explain why the correction is necessary. If needed you can use my_internet_explorer tool.
"""
###


