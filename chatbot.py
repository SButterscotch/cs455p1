import re
import random

# Define patterns and responses
patterns = [
    (r"I feel (.*)", ["Why do you feel {}?", "Tell me more about your feelings."]),
    (r"My (.*) doesn’t (.*)", ["What makes you believe your {} doesn’t {}?", "Why do you think your {} doesn’t {}?"]),
    (r"I dont know (.*)", ["Why do you think you don’t know {}?", "What makes {} unclear to you?"]),
    (r"I’m (.*)", ["Why are you {}?", "How does being {} make you feel?"]),
    (r"I feel like (.*)", ["What makes you feel like {}?", "Why do you think you feel like {}?"]),
    (r"I’m (.*) about (.*)", ["Why are you {} about {}?", "What makes you {} about {}?"]),
    (r"I want to (.*)", ["What makes you want to {}?", "Why do you feel the need to {}?"]),
    (r"I’ve been feeling (.*)", ["Can you tell me more about your {}?", "Why do you think you’ve been feeling {}?"]),
    (r"I don’t (.*)", ["Why don’t you {}?", "What stops you from {}?"]),
    (r"I feel (.*) by (.*)", ["Why do you feel {} by {}?", "What makes you feel {} by {}?"]),
]

def match_pattern(user_input):
    for pattern, responses in patterns:
        match = re.match(pattern, user_input, re.IGNORECASE)
        if match:
            return responses, match.groups()
    return None, None

def generate_response(user_input):
    responses, groups = match_pattern(user_input)
    if responses:
        return random.choice(responses).format(*groups)
    return "I'm not sure I understand. Can you elaborate?"


def chat():
    print("ELIZA: Hello! How can I help you today? (Exit/quit to end the conversation)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("ELIZA: Goodbye!")
            break
        response = generate_response(user_input)
        print(f"ELIZA: {response}")


chat()