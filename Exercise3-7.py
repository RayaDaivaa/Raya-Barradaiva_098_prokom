guests = [ "tiara","alexa", "destin","renaya", "cantika","rivi"]

print("Sorry, I can only invite two people for dinner.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I cannot invite you to dinner.")

for guest in guests:
    print(f"{guest}, you are still invited to dinner.")

del guests[0]
del guests[0]

print(guests)