import json

def search_by_id(json_data, item_id):
    item_info = json_data.get(item_id)
    if item_info:
        fr_name = item_info.get("fr", "Name not found for French language")
        return fr_name
    return None

def search_by_name(json_data, fr_name):
    for item_id, item_info in json_data.items():
        if item_info.get("fr") == fr_name:
            return item_id, item_info
    return None, None

def main():
    # Load JSON data from file
    with open('items_id.json', 'r') as file:
        json_data = json.load(file)

    # Search by ID
    # search_id = "41429"
    # item_fr_name = search_by_id(json_data, search_id)
    # if item_fr_name:
    #     print(f"Item found with ID {search_id} (French name): {item_fr_name}")
    # else:
    #     print(f"No item found with ID {search_id}")

    # # Search by name
    # search_name = "Imitation de station de stockage magitek"
    # item_id, item_info = search_by_name(json_data, search_name)
    # if item_info:
    #     print(f"Item found with name '{search_name}': ID {item_id}")
    # else:
    #     print(f"No item found with name '{search_name}'")

if __name__ == "__main__":
    main()
