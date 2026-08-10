message = "I am a global variable"


def display_message():
    # Local variable
    local_message = "I am a local variable"

    print("Inside the function:")
    print(local_message)
    print(message)


display_message()

print("\nOutside the function:")
print(message)
