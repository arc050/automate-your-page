def generate_concept_HTML(concept_title, concept_notes):
    html_part_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_part_2 = '''
    </div>
    <div class="concept-notes">
        ''' + concept_notes
    html_part_3 = '''
    </div>
</div>'''
    
    full_html = html_part_1 + html_part_2 + html_part_3 
    return full_html

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('NOTES:')
    title = concept[start_location+7 : end_location-1]
    return title

def get_notes(concept):
    start_location = concept.find('NOTES:')
    notes = concept[start_location+7 :]
    return notes

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        if next_concept_end >= 0:
            concept = text[next_concept_start:next_concept_end]
        else:
            next_concept_end = len(text)
            concept = text[next_concept_start:]
        text = text[next_concept_end:]
    return concept

TEST_TEXT = """TITLE: Computers
NOTES: Computers can be programmed to do anything we want as long as we can correctly 
write out the program telling it what to do.
TITLE: Programs
NOTES: A program is a specific number of steps the computer can follow to do as requested. 
Games, websites, simple apps are examples of programs.
TITLE: Python
NOTES: Python is a programming language that programmers can use to tell a computer what to 
do. When python code is ran it interprets the code and makes it a list of instructions the 
computer can follow.
TITLE: Grammar
NOTES: Now grammar in programming isn't the same as we would think. However, programming 
does have its correct and incorrect situations. We have to be exactly correct for a computer 
to understand what we want otherwise it won't run at all.
TITLE: Variables
NOTES: A way for programmers to give names for values in python.
Assigning variables is simple. To assign the value Anthony to the variable my_name the code 
ooks like this: 
my_name = 'Anthony'
It is important that you think of the equal sign as "is the same as" and not an equal sign 
like in arithmetic. Variables are useful because it allows programmers to make the data 
easier to read and understand. Another important fact is using quotation marks around a 
number makes it a string instead of an integer. This changes the outcome of the code you 
are inputting and gives a completely different answer.
"""


def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        notes = get_notes(concept)
        concept_html = generate_concept_HTML(title, notes)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html


print generate_all_html(TEST_TEXT)