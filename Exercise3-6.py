guests = ["tiara", "renaya", "cantika"]

print("I found a bigger dinner table!")

guests.insert(0, "alexa")
guests.insert(2, "destin")
guests.append("rivi")

for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")