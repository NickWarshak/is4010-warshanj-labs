# Messy script to be refactored
users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False}
]

def calculate_average_age(users):
    """
    Calculate the average age of users from a list of dictionaries.

    Parameters
    ----------
    users : list
        A list of dictionaries where each dictionary represents a user.

    Returns
    -------
    float
        The average age of users with valid integer ages, or 0.0 if empty.
    """
    total_age = 0
    user_count_for_age = 0
    
    try:
        for user in users:
            age = user.get("age")
            if isinstance(age, int):
                total_age += age
                user_count_for_age += 1
        
        return total_age / user_count_for_age
    
    except ZeroDivisionError:
        print("error: cannot calculate average age of an empty list.")
        return 0.0
    except Exception as e:
        print(f"an unexpected error occurred: {e}")
        return 0.0

def get_active_user_emails(users):
    """
    Retrieve a list of emails for all active users.

    Parameters
    ----------
    users : list
        A list of dictionaries where each dictionary represents a user.

    Returns
    -------
    list
        A list of strings containing the emails of active users.
    """
    active_user_emails = []
    try:
        for user in users:
            if user.get("is_active") and user.get("email"):
                active_user_emails.append(user["email"])
        return active_user_emails
    except Exception as e:
        print(f"error processing emails: {e}")
        return []

if __name__ == '__main__':
    avg_age = calculate_average_age(users)
    print(f"average user age: {avg_age:.2f}")

    active_emails = get_active_user_emails(users)
    print(f"active user emails: {active_emails}")