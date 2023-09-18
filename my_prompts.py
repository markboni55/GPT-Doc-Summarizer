file_map = """
You will be given a single section from a text. This will be enclosed in triple backticks.
Provide Detailed Summary including the following sections, [CALL TO ORDER: ROLL CALL: APPROVAL OF MINUTES PUBLIC COMMENT:  NEW BUSINESS: OLD BUSINESS: ADJOURNMENT:] 

'''{text}'''

DETAILED SUMMARY:
"""


file_combine = """
Read all the provided summaries from a larger document. They will be enclosed in triple backticks. 
Determine what the overall document is about and summarize it with this information in mind.
Synthesize the info into a well-formatted easy-to-read synopsis, structured like an essay that summarizes them cohesively. 
Do not simply reword the provided text. Do not copy the structure from the provided text.
Avoid repetition. Connect all the ideas together.
Preceding the synopsis, write a short, bullet form list of key takeaways.
Format in HTML. Text should be divided into paragraphs. Paragraphs should be indented. 

'''{text}'''


"""

youtube_map = """
You will be presented with a segment from the minutes of a municipal village board meeting, encapsulated within triple backticks. Your task is to craft a concise and coherent summary of that section, 
emphasizing the primary points and central themes, akin to the Action Minutes format commonly utilized by several government entities. Ensure that the summary maintains the clear and succinct nature characteristic of meeting minutes.

'''{text}'''

FULL SUMMARY:
"""

youtube_combine = """
Read all the provided summaries from a youtube transcript. They will be enclosed in triple backticks.
Determine what the overall video is about and summarize it with this information in mind. 
Synthesize the info into a well-formatted easy-to-read synopsis, structured like an essay that summarizes them cohesively. 
Do not simply reword the provided text. Do not copy the structure from the provided text.
Avoid repetition. Connect all the ideas together.
Preceding the synopsis, write a short, bullet form list of key takeaways.
Format in HTML. Text should be divided into paragraphs. Paragraphs should be indented. 

'''{text}'''


"""
