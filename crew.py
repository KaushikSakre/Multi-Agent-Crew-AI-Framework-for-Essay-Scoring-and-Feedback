from crewai import Crew,Process
from tasks import (evaluation_task,score_task,feedback_task,mistake_correction_task,writing_improvement_task,essay_processing_task)
from agents import (evaluation_agent,score_agent,feedback_agent,mistake_corrector_agent,writer_agent,overall_agent)
from tools import my_pdf_searcher, my_internet_explorer


crew = Crew(
  agents=[evaluation_agent,score_agent,feedback_agent,mistake_corrector_agent,writer_agent,overall_agent],#evaluation_agent
  tasks=[evaluation_task,score_task,feedback_task,mistake_correction_task,writing_improvement_task,essay_processing_task],
  verbose = True,
  max_rpm = 29,
  max_iter = 2,
  # Optional: Sequential task execution is default
)

## start the task execution process with enhanced feedback
result=crew.kickoff(inputs={'prompt':'More and more people use computers, but not everyone agrees that this benefits society. Those who support advances in technology believe that computers have a positive effect on people. They teach hand-eye coordination, give people the ability to learn about faraway places and people, and even allow people to talk online with other people. Others have different ideas. Some experts are concerned that people are spending too much time on their computers and less time exercising, enjoying nature, and interacting with family and friends.',
                            "essay": "Dear local newspaper, I think effects computers have on people are great learning skills/affects because they give us time to chat with friends/new people, helps us learn about the globe(astronomy) and keeps us out of troble! Thing about! Dont you think so? How would you feel if your teenager is always on the phone with friends! Do you ever time to chat with your friends or buisness partner about things. Well now - there's a new way to chat the computer, theirs plenty of sites on the internet to do so: @ORGANIZATION1, @ORGANIZATION2, @CAPS1, facebook, myspace ect. Just think now while your setting up meeting with your boss on the computer, your teenager is having fun on the phone not rushing to get off cause you want to use it. How did you learn about other countrys/states outside of yours? Well I have by computer/internet, it's a new way to learn about what going on in our time! You might think your child spends a lot of time on the computer, but ask them so question about the economy, sea floor spreading or even about the @DATE1's you'll be surprise at how much he/she knows. Believe it or not the computer is much interesting then in class all day reading out of books. If your child is home on your computer or at a local library, it's better than being out with friends being fresh, or being perpressured to doing something they know isnt right. You might not know where your child is, @CAPS2 forbidde in a hospital bed because of a drive-by. Rather than your child on the computer learning, chatting or just playing games, safe and sound in your home or community place. Now I hope you have reached a point to understand and agree with me, because computers can have great effects on you or child because it gives us time to chat with friends/new people, helps us learn about the globe and believe or not keeps us out of troble. Thank you for listening."})
print(result)
from IPython.display import Markdown
#Markdown(result)