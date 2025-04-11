def find_dictionaries_by_value(list_of_dictionaries, target_value):
    """
    Searches a list of dictionaries for dictionaries containing a specific value
    for any key.

    Args:
        list_of_dictionaries: A list of dictionary objects.
        target_value: The value to search for (can be any data type).

    Returns:
        A list of dictionaries that contain the specified target value.
    """
    found_dictionaries = []
    for dictionary in list_of_dictionaries:
        if target_value in dictionary.values():
            found_dictionaries.append(dictionary)
    return found_dictionaries

# Example usage:
my_list = [
    {'a': 1, 'x': 2, 'c': 3},
    {'d': 4, 'e': 5, 'f': 6},
    {'g': 7, 'x': 8, 'i': 9},
    {'j': 10, 'k': 3, 'l': 12},
    {'m': 3, 'n': 14, 'o': 15},
    {'p': 'hello', 'q': 20, 'r': 3}
]

value_to_find = 3
result = find_dictionaries_by_value(my_list, value_to_find)
print(f"Dictionaries containing the value '{value_to_find}':")
for dictionary in result:
    print(dictionary)

value_to_find_string = 'hello'
result_string = find_dictionaries_by_value(my_list, value_to_find_string)
print(f"\nDictionaries containing the value '{value_to_find_string}':")
for dictionary in result_string:
    print(dictionary)
