file_map = """
You will be given a single section from a text. This will be enclosed in triple backticks.
Please provide a cohesive summary of the following section excerpt, focusing on the key points and main ideas, while maintaining clarity and conciseness.

'''{text}'''

FULL SUMMARY:
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
You will be given a single section from a transcript of a youtube video. This will be enclosed in triple backticks. In the first chunk, identify the date and time of the meeting, even if it is not properly formatted. Please format it correctly in the "CALL TO ORDER" section. 

Please provide a cohesive summary of the section of the transcript in the style of Action Minutes, focusing on the key points and main ideas, while maintaining clarity and conciseness. Ensure to include sections such as "CALL TO ORDER", "ROLL CALL", and others as appropriate.

'''
{text}
'''

FULL SUMMARY:

- CALL TO ORDER:
    "Chair Brunner called to order the Planning and Zoning & Historic Commission ('PZHC') meeting on {date}, at {time}."

- ROLL CALL:
    Commissioners: Steneck, Brunner, Myers, Feck, Krueger, Reyes-Brahar, Scarpelli
    (Identify which commissioners were present and which were absent in this section of the video)
    
- MAIN DISCUSSION:
    (Summarize the key points discussed in this section)
   
- ACTION ITEMS:
    (List any action items or notable moments from this section)

- ADJOURNMENT:
    (Mention the conclusion of this section of the video)

"""


youtube_combine = """
Read all the provided summaries from a youtube transcript. They will be enclosed in triple backticks.
Determine what the overall video is about and summarize it with this information in mind. Structure the summary in the style of Action Minutes with sections like "CALL TO ORDER", "ROLL CALL", "MAIN DISCUSSION", "ACTION ITEMS", and "ADJOURNMENT". 
Synthesize the info into a well-formatted easy-to-read synopsis, structured like an essay that summarizes them cohesively. 
Do not simply reword the provided text. Do not copy the structure from the provided text.
Avoid repetition. Connect all the ideas together.
Preceding the synopsis, write a short, bullet form list of key takeaways.
Format in HTML. Text should be divided into paragraphs. Paragraphs should be indented. 

'''
{text}
'''

- CALL TO ORDER:
    "Chair Brunner called to order the Planning and Zoning & Historic Commission ('PZHC') meeting on {date}, at {time}."

- ROLL CALL:
    Commissioners: Steneck, Brunner, Myers, Feck, Krueger, Reyes-Brahar, Scarpelli
    (Summarize the attendance of the commissioners throughout the video)
   
- MAIN DISCUSSION:
    (Provide a comprehensive summary of the main discussion points throughout the video)
    
- ACTION ITEMS:
    (List any key takeaways or action items from the video)
   
- ADJOURNMENT:
    (Summarize the conclusion of the video)
   
- KEY TAKEAWAYS:
    (Bullet list of the most important points from the video)
   
<!-- Begin HTML formatted synopsis here -->
...
"""
