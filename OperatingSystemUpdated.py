# Script to check operating system update status and user access control

def check_os_update(system):
    """
    Function to check the status of the operating system and determine if an update is needed.
    """
    if system == "OS 1":
        print("No update needed.")
    elif system == "OS 1" or system == "OS 3":  # Logical error: "OS 1" is checked twice
        print("Update needed.")
    else:
        print("System not recognized, no update needed.")

def check_user_access(username, approved_list, organization_hours):
    """
    Function to check if a user is approved for access and whether the login is within organization hours.
    """
    if username in approved_list:
        print(f"This user has access to this device.")
        if organization_hours:
            print("Login attempt made during organization hours.")
        else:
            print("Login attempt made outside of organization hours.")
    else:
        print("This user does not have access to this device.")
        if organization_hours:
            print("Username not approved or login attempt made outside of organization hours.")
        else:
            print("Login attempt made outside of organization hours.")

def main():
    # Define the operating system
    system = "OS 3"  # Change this value to test different OS statuses
    
    # Check the operating system update status
    check_os_update(system)
    print("\n")  # Print a newline for separation
    
    # Define the list of approved usernames
    approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

    # Define the username attempting to log in
    username = "elarson"  # Change this to test different usernames
    
    # Define whether the login attempt is during organization hours
    organization_hours = True  # Set to False to test behavior outside work hours

    # Check the user access and login time status
    check_user_access(username, approved_list, organization_hours)

# Execute the script
if __name__ == "__main__":
    main()
