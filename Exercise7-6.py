prompt = "Enter a pizza topping: "
prompt += "\nEnter 'quit' to finish. "

topping = ""

while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")

prompt = "Enter a pizza topping: "
prompt += "\nEnter 'quit' to finish. "

active = True

while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")

prompt = "Enter a pizza topping: "
prompt += "\nEnter 'quit' to finish. "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break

    print(f"I'll add {topping} to your pizza.")