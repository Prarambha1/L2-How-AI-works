# Import necessary libraries
# - TextBlob for natural language processing tasks like sentiment analysis
# - Colorama for colored terminal output
# - sys and time for animations and delays
from textblob import TextBlob
import colorama 
from colorama import Fore, Style
import sys
import time


# Initialize Colorama to reset terminal colors automatically after each output

# Define global variables
user_name = "" # - `user_name`: To store the name of the user (Agent)
conversation_history = []# - `conversation_history`: A list to store all user inputs
positive_count = 0
negative_count = 0
neutral_count = 0
# - Sentiment counters (`positive_count`, `negative_count`, `neutral_count`) to track sentiment trends


# Define a function to simulate a processing animation
def show_processing_animation():
    print(f"{Fore.CYAN}🕵️ Detecting sentiment clues.",end="")
# - Prints "loading dots" to make the chatbot feel interactive
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
        sys.stdout.flush()
        
# - Use a loop to display three dots with a slight delay


# Define a function to analyze sentiment of the text
def analyze_sentiment(text):
    try:
        global positive_count, negative_count, neutral_count
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        conversation_history.append(text)

        if sentiment > 0.75:
            positive_count +=1
            return f"\n{Fore.GREEN}😄 Very positive sentiment detected, agent {user_name}! (score: {sentiment:.25})"

        elif 0.25 < sentiment <=0.75:
            positive_count +=1
            return f"\n{Fore.GREEN}😀 Positive sentiment detected, agent {user_name}! (score: {sentiment:.25})"

        elif -0.25 <= sentiment <= 0.25:
            neutral_count +=1
            return f"\n{Fore.YELLOW}😐 Neutral sentiment detected, agent {user_name}! (score: {sentiment:.25})"

        elif -0.75 <= sentiment <= -0.25:
            negative_count +=1
            return f"\n{Fore.RED}🤕 Negative sentiment detected, agent {user_name}! (score: {sentiment:.25})"

        else:
            negative_count +=1
            return f"\n{Fore.RED}💔 Very negative sentiment detected, agent {user_name}! (score: {sentiment:.25})"
    except Exception as e:
        return f"{Fore.RED}an error occured during the sentiment analysis: {str(e)}"

# - Use TextBlob to calculate the polarity of the input text
# - Categorize the sentiment into "Very Positive," "Positive," "Neutral," "Negative," or "Very Negative"
# - Append the user input to `conversation_history`
# - Update the sentiment counters based on the category
# - Handle exceptions to avoid crashes


def execute_command(command):
    global positive_count, negative_count, neutral_count

    if command == "summary":
        return(f"{Fore.CYAN}🕵️ Mission report:\n"
                f"{Fore.GREEN} Positive sentiments detected: {positive_count}\n"
                f"{Fore.YELLOW} Neutral sentiments detected: {neutral_count}\n"
                f"{Fore.RED} Negative sentiments detected: {negative_count}\n"
        )
    elif command == "reset":
        conversation_history.clear()
        positive_count = negative_count = neutral_count = 0
        return f"{Fore.CYAN}🕵️ Mission reset, All previous data has been cleared."

    elif command == "history":
        return "\n".join([f"{Fore.CYAN} Message{i+1}: {msg}" for i, msg in enumerate(conversation_history)]) \
            if conversation_history else f"{Fore.YELLOW}🕵️ No conversation history available."
    
    elif command == "help":
        return (f"{Fore.CYAN}🔎 Available commands:\n"
                "- Type any sentence to analyse its sentiment.\n"
                "- Type 'summary' to get a mission report on analysed sentiments.\n"
                "- Type 'reset' to clear all mission data and start fresh.\n"
                "- Type 'history' to View all previous messages and analyses.\n"
                "- Type 'exit' to conclude your mission and leave the chat.\n")
    else:
        return f"{Fore.RED}Unknown command. Type 'Help' for a list of commands."
    
# Define a function to handle commands
# - Handle commands like `summary`, `reset`, `history`, and `help`
# - `summary`: Displays the count of positive, negative, and neutral sentiments
# - `reset`: Clears the conversation history and resets counters
# - `history`: Shows all previous user inputs
# - `help`: Displays a list of available commands
# - Return appropriate responses for each command



def get_valid_name():
    while True:
        name = input("What's your name?").strip()
        if name and name.isalpha():
            return name
        else:
            print(f"{Fore.RED}Please enter a valid name with only alphabet characters.")
# Define a function to validate the user's name
# - Continuously prompt the user for a name until they enter a valid alphabetic string
# - Strip any extra spaces and ensure the input is not empty or invalid


def start_sentiment_chat():
    print(f"{Fore.CYAN}{Style.BRIGHT} Welcome to Sentiment Spy! Your personal emotion detective is here.")
    global user_name
    user_name = get_valid_name()
    print(f"\n{Fore.MAGENTA} Nice to meet you, agent {user_name}! Type your sentences to analyse emotions. Type 'help' for options.")
    
    while True:
        user_input = input(f"\n{Fore.MAGENTA}{Style.BRIGHT}Agent {user_name}: {Style.RESET_ALL}").strip()
        if not user_input:
            print(f"{Fore.RED} please enter a non-empty message or type 'help' for available commands.")
            continue
        if user_input.lower()== 'exit':
            print(f"\n{Fore.BLUE}👋 mission complete! Exciting Sentiment Spy. Farewell, Agent {user_name}!")
            print(execute_command("summary"))
            break
        elif user_input.lower() in ["summary", "reset", "history", "help"]:
            print(execute_command(user_input.lower()))
        else:
            show_processing_animation()
            result = analyze_sentiment(user_input)
            print(result)

# - Display a welcome message and introduce the Sentiment Spy activity
# - Ask the user for their name and store it in the `user_name` variable
# - Enter an infinite loop to interact with the user:
#   - Prompt the user to enter a sentence or command
#   - Check for empty input and prompt the user to enter a valid sentence
#   - If the input matches specific commands (`exit`, `summary`, `reset`, `history`, `help`), execute the corresponding functionality
#   - Otherwise, call the `analyze_sentiment` function to analyze the input text
#   - Display the sentiment analysis result with color-coded feedback
# - Exit the loop and display a final summary when the user types `exit`



if __name__ == "__main__":
    start_sentiment_chat()
# Define the main function to start the chatbot
# Define the entry point for the script
# - Ensure the chatbot starts only when the script is run directly (not imported)
# - Call the `start_sentiment_chat` function to begin the activity