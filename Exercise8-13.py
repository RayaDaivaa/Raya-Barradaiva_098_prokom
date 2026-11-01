def build_profile(first_name, last_name, **user_info):
    profile = {
        "first_name": first_name,
        "last_name": last_name}

    profile.update(user_info)
    return profile


my_profile = build_profile(
    "Raya",
    "Daiva",
    age=18,
    location="Indonesia",
    hobby="Learning Python")

print(my_profile)