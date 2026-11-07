default_settings = {
    "theme": "dark",
    "language": "turkis",
    "notifications": True,
    "font_size": 15
}

user_settings = {
    "theme": "light",
    "font_size": 18
}

final_settings = {**default_settings, **user_settings}

print("Default Settings:", default_settings)

print("User Settings:", user_settings)

print("Final Settings:", final_settings)