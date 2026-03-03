def send_messages(messages, sent_messages):
    """Print each message in a list."""
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

def show_sent_messages(sent_messages):
    """Show all the messages that were sent."""
    print("\nThe following messages have been sent: ")
    for sent_message in sent_messages:
        print(sent_message)

messages = ['Hello', 'Hi', 'How are you?']
sent_messages = []

send_messages(messages, sent_messages)
show_sent_messages(sent_messages)