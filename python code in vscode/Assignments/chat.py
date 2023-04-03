import datetime
import re

def get_current_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def math_operation(expression):
    try:
        return eval(expression)
    except:
        return "Invalid expression. Please enter a valid mathematical expression."

def process_query(query):
    current_time = get_current_time()
    current_date = get_current_date()

    if "what is the current time" in query:
        return current_time
    elif "what is the current date" in query:
        return current_date
    elif "set a reminder" in query:
        reminder = query.replace("set a reminder", "").strip()
        return f"Reminder set for {current_time} on {current_date}: {reminder}"
    elif re.search("^[0-9\+\-\*\/\(\)]+$", query):
        return math_operation(query)
    else:
        return "Sorry, I am not sure how to help with that."

if __name__ == "__main__":
    query = input("What can I help you with? ")
    response = process_query(query.lower())
    print(response)