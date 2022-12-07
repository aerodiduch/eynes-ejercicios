from random import randint
import uuid


def generate_mock_data(min_age: int, max_age: int, quantity: int) -> list:
    '''Generate user mock data entries with a random age in range of min_age and max_age
    and returns a list of dicts.

    Args:
        min_age (int): Minimum age
        max_age (int): Maximum age
        quantity (int): Quantity of registries to generate.

    Returns:
        list: List of dicts containing user data
    '''
    data = []
    for i in range(quantity):
        user_data = {
            'user_id': uuid.uuid1(),
            'age': randint(min_age, max_age)
        }
        data.append(user_data)
    return data

def sort_data(data: list) -> list:
    '''Function that receives an unsorted list of dicts and sorts it by age.

    Args:
        data (list): Unsorted list containing dicts with user data

    Returns:
        list: Sorted list in descending order (oldest to youngest)
    '''
    sorted_data  = sorted(data, key=lambda item: item['age'], reverse=True) 
    print(f"oldest person. id -> {sorted_data[0]['user_id']}, age -> {sorted_data[0]['age']}")
    print(f"youngest person. id -> {sorted_data[-1]['user_id']}, age -> {sorted_data[-1]['age']}")
    return sorted_data

if __name__ == '__main__':
    mock_data = generate_mock_data(10, 100, 10)
    sort_data(mock_data)
