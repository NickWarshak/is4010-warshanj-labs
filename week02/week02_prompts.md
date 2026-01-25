# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

**My Prompt:**
> I am working on a python lab and specifically am tasked with debugging this code:
> 
> ```python
> def sum_of_evens(numbers):
>     total = 0
>     for num in numbers:
>         if num % 2 == 1:  # This line has a bug!
>             total += num
>     return total
> ```
> Act as a senior developer and fix the bug where is sums odd numbers instead of even ones. Give me a code block with an explanation about any changes built inside of the code.

**AI's Corrected Code:**
```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        # BUG FIX: Changed 'num % 2 == 1' to 'num % 2 == 0'
        # An even number is any integer that is exactly divisible by 2, 
        # meaning the remainder (modulo) must be zero.
        if num % 2 == 0:
            total += num
            
   return total
```

**What I learned:** The original code used `num % 2 == 1`, which identifies odd numbers. By switching the condition to `num % 2 == 0`, I was able to identify even numbers instead.


## Problem 2: Refactoring

**My Prompt:**
> Hello, I am working on a new problem in a coding class and could use some assistance. The code ive been tasked with fixing is written down below this intro message. My, and your, general task is to clean the code up so it is less confusing and more pythonic. Act as a developer and treat me as your supervisor who will be reviewing your code for clarity. Return only the code block with comments about any changes made on the inside of the code block.

Code:
def get_names_of_adults(users):

    """Given a list of user dictionaries, returns a list of names of users

    who are 18 or older.



    Parameters

    ----------

    users : list of dict

        List of user dictionaries with 'name' and 'age' keys.



    Returns

    -------

    list of str

        Names of users who are 18 or older.

    """

    results = []

    for i in range(len(users)):

        if users[i]['age'] >= 18:

            results.append(users[i]['name'])

    return results



**AI's Corrected Code:**
```python
def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    # REFACTOR: Replaced manual indexing (range(len(users))) with a List Comprehension.
    # This is more "Pythonic" as it is more readable, concise, and faster.
    # We iterate directly over the user objects rather than tracking an index 'i'.
    return [user['name'] for user in users if user['age'] >= 18]

    # OLD LOGIC FOR REFERENCE:
    # results = []
    # for i in range(len(users)):  <-- Unnecessary indexing
    #     if users[i]['age'] >= 18:
    #         results.append(users[i]['name'])
    # return results
```

**What I learned:** I learned that being pythonic in many ways means making your code readable to someone else or to yourself if you revisit the code later. It can also mean using shortened functions to boost effiency. I think a good example is _variable_ +=1 rather than _variable_ = _variable_ + 1. 

## Problem 3: Documenting

**My Prompt:**
> Now we are on to the last problem in which you, as a senior developer, must write a professional NumPy-style docstring for this function. The code you have been tasked with fixing has been copied below. Again, return just the fixed code block with comments embedded inside the code explaining changes.



def calculate_area(length, width):

    if length <= 0 or width <= 0:

        raise ValueError("Length and width must be positive numbers.")

    return length * width



**AI's Corrected Code:**
```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters
    ----------
    length : int or float
        The linear length of the rectangle. Must be a positive value.
    width : int or float
        The linear width of the rectangle. Must be a positive value.

    Returns
    -------
    area : int or float
        The calculated area (length * width).

    Raises
    ------
    ValueError
        If either length or width is less than or equal to zero.
    """
    # REFACTOR: Added a standard NumPy-style docstring above to document 
    # types, return values, and potential exceptions for better maintainability.
    
    if length <= 0 or width <= 0:
        # VALIDATION: Keeping the existing guard clause to ensure 
        # geometric calculations remain mathematically valid.
        raise ValueError("Length and width must be positive numbers.")
        
    return length * width
```

**What I learned:** I learned ow to use a numby docstring for a specific function. I also learned that it is important to raise value errors for invalid inputs.

