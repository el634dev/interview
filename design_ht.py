"""
Design a hash function from scratch

Lookup: O(1) average, O(n) worst-case.
Insertion: O(1) average, O(n) worst-case.
Deletion: O(1) average, O(n) worst-case.

Worst case meaning there is a collison
Space complexity for hash sets is O(n)
"""

def simple_hash(input_string):
    """
    Desc: Calculates the sum of the Unicode values of the characters in a string and then applies modulus 10. 
    This straightforward function converts any string into a hash value between 0 and 9
    Time Complexity: O(1)
    """
    summation = sum(ord(ch) for ch in input_string) # O(1)
    return summation % 10  # We limit our hash range from 0 to 9, O(1)

print(simple_hash('Hello'))  # outputs: 0
print(simple_hash('world'))  # outputs: 2

# ---------------
# Define a set
student_ids = set()
hash_set = set()

# -------------------
# Add elements
student_ids.add(123)
student_ids.add(456)
student_ids.add(789)

# -------------------
# Adding elements to the set
hash_set.add("element1")
hash_set.add("element1")

# -------------------
# Check the content of the set
print(hash_set)  # Output: {'element1'}

# -------------------
# Check existence
# O(1) because of the in operator
print(456 in student_ids)  # Outputs: True
print(111 in student_ids)  # Outputs: False

# -------------------
# Grocery list
grocery_list = set()

# Adding items
grocery_list.add('Milk')
grocery_list.add('Cheese')
grocery_list.add('Bread')

# -------------------
# Checking existence
print('Milk' in grocery_list)  # Outputs: True
print('Butter' in grocery_list)  # Outputs: False

# -------------------
# Add a new item
grocery_list.add('Butter')
print('Butter' in grocery_list)  # Outputs: True

# -------------------
# Try removing an item
grocery_list.remove('Bread')
print('Bread' in grocery_list)  # Outputs: False

# -------------------
# Clear the grocery list
grocery_list.clear()
print(grocery_list)  # Outputs: set()

# -------------------
# Create a new list and make a copy of it
new_list = set(['Eggs', 'Jam', 'Ham'])
copied_list = new_list.copy()

print(new_list)  # Outputs: {'Eggs', 'Ham', 'Jam'}
print(copied_list)  # Outputs: {'Eggs', 'Ham', 'Jam'}

# -------------------
# Modifying the copied list won't affect the original list
copied_list.remove('Ham')
print(new_list)  # Outputs: {'Eggs', 'Ham', 'Jam'}
print(copied_list)  # Outputs: {'Eggs', 'Jam'}

# ------------------------
# Importing the necessary libraries
import time

# Define a function to demonstrate the operation and time complexity of a hash set
def hash_set_operations():
    # Create a hash set and a list
    hash_set = set()  # O(1)
    list_data = [] # O(1)

    # Setting the range for the data elements
    data_range = 10**7 # O(1)

    # Adding elements to the hash set and the list
    for i in range(data_range): # O(n)
        hash_set.add(i) # O(1)
        list_data.append(i) # O(1)

    # Define a test element (which is out of the data range and thus is not present in both the list and set)
    test_element = data_range + 1 # O(1)

    # Start the clock and check for the presence of the test elements in the set
    start_time = time.time() # O(1)
    print("Hash Set Test Result:", test_element in hash_set) # O(1)
    print("Searching in the Hash Set Took:", time.time() - start_time) # O(1)

    # Start the clock and check for the presence of the test elements in the list
    start_time = time.time() # O(1)
    print("List Test Result:", test_element in list_data) # O(1)
    print("Searching in the List Took:", time.time() - start_time) # O(1)

# Call the function
hash_set_operations()
