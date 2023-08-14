import json 
import time

while True:

    time.sleep(0.5)
    
    # Opens JSON file
    expenses_json = open('expenses.json')
    # Returns JSON object as a dictionary
    expenses_list = json.load(expenses_json)
    # Retrieves expenses data
    expenses_data = expenses_list["data"]
    # Retrieves filter category
    filter = expenses_list["filter"]
    filtered_list = []

    # Adds expenses to filtered list
    for expense in expenses_data:
        if expense["category"] == filter:
            filtered_list.append(expense)

    # Converts filtered list to JSON object
    filtered_json = json.dumps(filtered_list)
    # Opens JSON file and writes filtered JSON object to file
    with open("filtered_expenses.json", "w") as outfile:
        outfile.write(filtered_json)