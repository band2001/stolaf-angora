import sqlite3 as sql
import json
import os
from read_data import read_database
from sklearn.model_selection import train_test_split

SYSTEM_PROMPT = '''You are very knowledgeable about computer science at St. Olaf College. You have a passion for helping answer computer science questions and troubleshoot issues for students. Your communication style is friendly, engaging, and informative, and you always strive to help students with their inquiries.

If a student asks about topics outside your area of expertise, such as medical advice or legal matters, politely inform them that you are not qualified to provide guidance on those subjects and suggest they consult with the appropriate professionals. If a user becomes hostile or uses inappropriate language, maintain a calm and professional demeanor, and remind them of the purpose and boundaries of your role as a computer science assistant at St. Olaf College.
'''

def generate_prompt(entry, system_prompt = SYSTEM_PROMPT):
    '''
    This function formats a question/answer pair to gemma's chat template.

    :param: entry - a dictionary with an instruction and a response
    :param: system_prompt: the system prompt to be used

    :return: the formated string for gemma's chat template
    '''

    return """<bos><start_of_turn>user
## Instructions
{}
## User
{}<end_of_turn>
<start_of_turn>model
{}<end_of_turn><eos>""".format(system_prompt, entry["instruction"], entry["response"])

def write_jsonl(data, filename):
    '''
    This function is used to create a jsonl file from data of a list of dictionaries where the entries are of the following format: 
        <bos><start_of_turn>user
        {entry['instruction']}<end_of_turn>
        <start_of_turn>model
        {entry['response']}<end_of_turn><eos>
    This is used for fine-tuning the gemma model.

    :param: data: the list of dictionaries
    :param: filename: the name of the file to write to

    There is no return, but a jsonl file will be put in the jsonl_data directory (located in the same directory as this script is run in)
    '''
    string_format_data = []

    for entry in data:
        text = generate_prompt(entry)
        string_format_data.append({"text": text})
    
    if os.path.exists("jsonl_data"):
        if os.path.exists(f"jsonl_data/{filename}"):
            os.remove(f"jsonl_data/{filename}")
        with open(f"jsonl_data/{filename}", 'w') as f:
            for item in string_format_data:
                f.write(json.dumps(item) + "\n")
    else:
        os.mkdir("jsonl_data")
        with open(f"jsonl_data/{filename}", 'w') as f:
            for item in string_format_data:
                f.write(json.dumps(item) + "\n")

def create_jsonl():
    '''
    This function is used to split the data into training, testing, and validation sets. These sets are stored as jsonl files in a data directory
    in the same directory this function is called from. This gets data from a database using the read_database() function.

    :param: None
    :return: None
    '''

    data = read_database()

    train, test = train_test_split(data, test_size=0.2)
    val, test = train_test_split(test, test_size=0.5)

    write_jsonl(train, "train.jsonl")
    write_jsonl(test, "test.jsonl")
    write_jsonl(val, "valid.jsonl")

if __name__ == "__main__":
    create_jsonl()