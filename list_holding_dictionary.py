def search_dictionaries_by_key(list_of_dictionaries, key_name):
    """
    Searches a list of dictionaries for dictionaries containing a specific key.

    Args:
        list_of_dictionaries: A list of dictionary objects.
        key_name: The name of the key to search for (string).

    Returns:
        A list of dictionaries that contain the specified key.
    """
    found_dictionaries = []
    for dictionary in list_of_dictionaries:
        if key_name in dictionary:
            found_dictionaries.append(dictionary)
    return found_dictionaries

# Example usage:
my_list = [
    {'a': 1, 'x': 2, 'c': 3},
    {'d': 4, 'e': 5, 'f': 6},
    {'g': 7, 'x': 8, 'i': 9},
    {'j': 10, 'k': 11, 'l': 12}
]

key_to_find = 'x'
result = search_dictionaries_by_key(my_list, key_to_find)
print(f"Dictionaries containing the key '{key_to_find}':")
for dictionary in result:
    print(dictionary)
