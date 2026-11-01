def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending: {current_message}")
        sent_messages.append(current_message)


messages = [
    "Hello, how are you?",
    "Keep learning Python!",
    "Practice makes progress."]

sent_messages = []

send_messages(messages[:], sent_messages)

print("\nOriginal messages:")
print(messages)

print("\nSent messages:")
print(sent_messages)