def greetings(**user):
    first_name = user.get("first_name", "Anonymous")
    last_name = user.get("last_name", 13)
    print(f"\033[31m Hello {first_name} {last_name} Welcome to hell!\033[31m")
greetings(last_name = "313")