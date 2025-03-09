# Solution 1: Algorithm to automate the login process

# List of approved users and their corresponding devices
approved_users = ["AbdiRahman", "Reyes", "John", "Raha"]
approved_devices = ["Mac-pro", "Windows", "PC", "Mac-Air"]

def login(username, device_id):
    """
    Function to validate user login based on approved users and devices.

    Parameters:
    username (str): The username attempting to log in.
    device_id (str): The device ID from which the login attempt is made.

    Returns:
    str: A message indicating the result of the login attempt.
    """
    result = ""  # Initialize an empty string to collect results

    if username in approved_users:
        # User is approved
        result += f"The user {username} is approved.\n"

        # Find the index of the user in the approved_users list
        ind = approved_users.index(username)

        # Check if the provided device matches the assigned device
        if device_id == approved_devices[ind]:
            result += f"{device_id} is the assigned device for {username}.\n"
        else:
            result += f"{device_id} is not their assigned device.\n"
    else:
        # User is not approved
        result += f"The username {username} is not approved to access the system.\n"

    return result  # Return the collected result

# Example usage: print login messages by calling the function
print(login("AbdiRahman", "Mac-pro"))
print(login("Reyes", "Windows"))
print(login("albert", "Linux"))
print(login("Raha", "Mac-Air"))
print(login("John", "PC"))
print(login("AbdiRahman", "VM"))
