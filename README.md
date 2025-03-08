# handle-operating-system-updates


Summary:
This Python script is designed to perform two main tasks: check the operating system (OS) update status and validate user access based on the username and login time.

Operating System Update Check: The check_os_update() function takes an OS identifier (e.g., "OS 1", "OS 3") and checks whether an update is needed for the system. If the system is "OS 1" or "OS 3," an update is needed. Otherwise, it reports that no update is necessary.

User Access Control: The check_user_access() function checks if the user is approved for access based on their username and whether the login attempt is made within organizational hours. If the username is in the approved list, it checks if the login is happening during office hours and reports the result accordingly.
