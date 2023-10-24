import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk  # Import the Tkinter library

# Define chatbot responses based on patterns.
tech_responses = [
    ["(Hi|Hello|Hey)", ["Hello! I'm a chatbot, How can I help you today?", "Hi there! I'm a chatbot, What can I assist you with?"]],
    ["How can I (.*)", ["You can ask questions related to our tech services."]],
    ["What tech services do you offer?", ["We provide a range of tech services, including software development, IT consulting, and cybersecurity."]],
    ["Tell me about your (.*) service", ["Our {0} service is designed to help clients with their tech needs. Would you like more details?"]],
    ["(.*) software development", ["Our software development services encompass custom software solutions tailored to your business needs."]],
    ["(.*) IT consulting", ["Our IT consulting services offer expert guidance to optimize your IT infrastructure."]],
    ["(.*) cybersecurity", ["Our cybersecurity services aim to protect your data and systems from cyber threats."]],
    ["Bye", ["Goodbye! If you have more questions in the future, don't hesitate to ask."]],
]

# Create an instance of the Chat class.
tech_chatbot = Chat(tech_responses, reflections)

# Define a function to handle user input and chatbot responses.
def chat():
    user_input = user_entry.get()
    response = tech_chatbot.respond(user_input)
    chat_display.config(state=tk.NORMAL)  # Allow text widget to be edited
    chat_display.insert(tk.END, "You: " + user_input + "\n", "user")
    chat_display.insert(tk.END, "Bot: " + " ".join(response) + "\n", "bot")
    chat_display.see(tk.END)  # Scroll to the end of the text
    chat_display.config(state=tk.DISABLED)  # Disable text widget editing
    user_entry.delete(0, tk.END)  # Clear the user input field

# Create the main GUI window
root = tk.Tk()
root.title("Tech Company Chatbot")

# Create a text widget to display the chat
chat_display = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED)
chat_display.tag_configure("user", foreground="blue")
chat_display.tag_configure("bot", foreground="green")
chat_display.pack()

# Create an entry field for user input
user_entry = tk.Entry(root)
user_entry.pack()

# Create a button to send user input
send_button = tk.Button(root, text="Send", command=chat)
send_button.pack()

# Start the GUI main loop
root.mainloop()
