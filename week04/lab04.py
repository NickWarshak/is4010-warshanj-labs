def find_common_elements(list1, list2):
    """Find the common elements between two lists using set intersection."""
    # Converting to sets allows us to perform an intersection
    # This is highly optimized in CPython
    return list(set(list1) & set(list2))

def build_user_index(users):
    """
    Transforms the list into a dictionary for O(1) lookups.
    Key: username, Value: full profile dict
    """
    return {user['name']: user for user in users}

def find_user_by_name(users, name):
    """Find a user's profile by name from a list of user data."""
    for user in users:
        if user['name'] == name:
            return user
    return None

def get_list_of_even_numbers(numbers):
    """Filters for even numbers while maintaining original sensor sequence."""
    # We use the modulo operator (%) to check if the remainder is 0
    return [num for num in numbers if num % 2 == 0]
