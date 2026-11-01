current_users = ['Raya','Juna', 'Rafi', 'Niel','Adit']
new_users = ['raya','Dina','Juna','Budi','Salsa']

current_users_lower = []

for user in new_users:
    for user in current_users:
        current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(
            f"Sorry, {new_user} is already taken. "
            "You need to enter a new username.")
    else:
        print(f"{new_user} is available.")