from dotenv import load_dotenv
import openai
import os

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
CHAT_COMPLETION_MODEL = os.environ['CHAT_COMPLETION_MODEL']
COMPLETION_MODEL = os.environ['COMPLETION_MODEL']
TEMPERATURE = float(os.environ['TEMPERATURE'])

openai.api_key = OPENAI_API_KEY


def get_prompt():
    prompt = input("Enter a prompt: ")
    return prompt


def show_env():
    print('''
    CHAT_COMPLETION_MODEL: f.{CHAT_COMPLETION_MODEL}
    COMPLETION_MODEL: f.{COMPLETION_MODEL}
    TEMPERATURE: f.{TEMPERATURE}
    ''')


def completion(prompt: str):
    """the response text is available in `response.choices[0].text`
    """
    response = openai.Completion.create(
        model=COMPLETION_MODEL,
        prompt=prompt,
        temperature=TEMPERATURE,
    )
    return response


def chat_completion(past_messages: list | None, new_message: str):
    """the response text is available in `response.choices[0].message.content`
    """
    if past_messages is None:
        past_messages = []
        role = assume_role(new_message)
    else:
        role = 'user'
    new_message = {'role': role, 'content': new_message}

    past_messages.append(new_message)
    response = openai.ChatCompletion.create(
        model=CHAT_COMPLETION_MODEL,
        messages=past_messages,
        temperature=TEMPERATURE,
    )

    return response


def assume_role(message: str) -> str:
    """Assume the role of the message for the chat completion API.(system, assistant, user)

    Args:
        message (str): Message to assume the role.

    Returns:
        role (str): system, assistant, user
    """

    prompt = '''
    Assume the situation that the following message is to specify the situation or to ask you something, or to want your response.
    If to specify the situation, say "system" only.
    If to ask you something, say "assistant" only.
    If to want your response, say "user" only.
    If you cannot understand the message, say "user" only.

    Message: ''' + message

    result = completion(prompt).choices[0].text

    result = str.lower(result).replace('\n', '')

    return result


if __name__ == '__main__':
    prompt = get_prompt()

    print('DEBUG MODE')

    r = chat_completion(None, prompt)

    print(r.choices[0].message.role)
    print(r.choices[0].message.content)
