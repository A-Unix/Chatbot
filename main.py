import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses based on patterns.
tech_responses = [
    ["(Hi|Hello|Hey)", ["Hello! I'm a chatbot, How can I help you today?", "Hi there! I'm a chatbot, What can I assist you with?"]],
    ["How can I (.*)", ["You can ask questions related to our tech services."]],
    ["What tech services do you offer?", ["We provide a range of tech services, including software development, IT consulting, and cybersecurity."]],
    ["Tell me about your (.*) service", ["Our {0} service is designed to help clients with their tech needs. Would you like more details?"]],
    ["(.*) software development", ["Our software development services encompass custom software solutions tailored to your business needs."]],
    ["(.*) IT consulting", ["Our IT consulting services offer expert guidance to optimize your IT infrastructure."]],
    ["(.*) cybersecurity", ["Our cybersecurity services aim to protect your data and systems from cyber threats."]],
    ["(Bye|Exit|I want to exit|Quit)", ["Goodbye! If you have more questions in the future, don't hesitate to ask."]],
]

# Create an instance of the Chat class.
tech_chatbot = Chat(tech_responses, reflections)

print("Tech Company Chatbot: Hello, how can I assist you today?")
print("Type 'bye' to exit.")

# Start the conversation loop.
tech_chatbot.converse()
