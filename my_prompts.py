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
You will be given a single section from a transcript of a youtube video. This will be enclosed in triple backticks. Please identify the date and time of the meeting from the start and end of the transcript section, even if it is not properly formatted, and format it correctly in the "CALL TO ORDER" and "ADJOURNMENT" sections.

Also, pay special attention to capturing motions, votes, and key discussion points in the "ACTION ITEMS" section.

Please provide a cohesive summary of the section of the transcript in the style of Action Minutes, focusing on the key points and main ideas, while maintaining clarity and conciseness. Ensure to include the following sections as appropriate:

'''
{text}
'''

FULL SUMMARY:

- CALL TO ORDER:
    "Chair Brunner called to order the Planning and Zoning & Historic Commission ('PZHC') meeting."

- ROLL CALL:
    Commissioners: Steneck, Brunner, Myers, Feck, Krueger, Reyes-Brahar, Scarpelli
    (Identify which commissioners were present and which were absent in this section of the video)

- APPROVAL OF MINUTES:
    (Summarize any discussions or motions related to the approval of minutes from previous meetings)

- PUBLIC COMMENT:
    (Summarize any public comments presented during this section)

- NEW BUSINESS:
    (Provide a detailed summary of the new business discussed during the meeting, including any motions made and votes cast)

- OLD BUSINESS:
    (Summarize discussions pertaining to old business, including any action items or decisions made)

- ACTION ITEMS:
    (List any action items or notable moments from this section, particularly emphasizing motions and votes)

- ADJOURNMENT:
    "The meeting was adjourned on {date}, at {time}."
    (Mention the conclusion of this section of the video, including the time it ended)
"""


youtube_combine = """
Read all the provided summaries from a youtube transcript. They will be enclosed in triple backticks.
Determine what the overall video is about and summarize it with this information in mind, structured in the style of Action Minutes with the sections "CALL TO ORDER", "ROLL CALL", "APPROVAL OF MINUTES", "PUBLIC COMMENT", "NEW BUSINESS", "OLD BUSINESS", "ACTION ITEMS", and "ADJOURNMENT". 

Synthesize the info into a well-formatted, easy-to-read synopsis, structured like an essay that summarizes them cohesively. Connect all the ideas together and avoid repetition. Do not simply reword the provided text. Do not copy the structure from the provided text.

Preceding the synopsis, write a short, bullet form list of key takeaways. Format in HTML. Text should be divided into paragraphs. Paragraphs should be indented.

'''
{text}
'''

- CALL TO ORDER:
    "Chair Brunner called to order the Planning and Zoning & Historic Commission ('PZHC') meeting."

- ROLL CALL:
    Commissioners: Steneck, Brunner, Myers, Feck, Krueger, Reyes-Brahar, Scarpelli
    (Summarize the attendance of the commissioners throughout the video)

- APPROVAL OF MINUTES:
    (Summarize any discussions or motions pertaining to the approval of minutes throughout the video)

- PUBLIC COMMENT:
    (Provide a comprehensive summary of public comments throughout the video)

- NEW BUSINESS:
    (Summarize new business discussed throughout the video, including any key motions and votes)

- OLD BUSINESS:
    (Summarize discussions on old business throughout the video, including any significant decisions or action items)

- ACTION ITEMS:
    (List key action items or notable moments from the video, especially emphasizing motions and votes)

- ADJOURNMENT:
    "The meeting was adjourned on {date}, at {time}."
    (Summarize the conclusion of the video, including the time it ended)
   
- KEY TAKEAWAYS:
    (Bullet list of the most important points from the video)
   
<!-- Begin HTML formatted synopsis here -->
...
"""
