import json

def reading_json_file(filename):
    """
    Reads files
    """
    with open(filename, 'r', encoding = 'utf-8') as file:
        result = json.load(file)
    return result

# if __name__ == '__main__':
#     print(reading_json_file('test_json_1.json'))