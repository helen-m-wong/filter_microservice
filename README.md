Communication Contract

The microservice filters data provided in the “expenses.json” file and writes the filtered data to the “filtered_expenses.json” file. To request data from the microservice, you should have your program write all the expenses data to the “expenses.json” file in the format:

{
“filter”: “CATEGORY”,
“data”: [expenses data goes here]
}

Then run the filter_microservice.py program. You can run it by entering into the terminal “python3 filter_microservice.py.” To receive data from the microservice, you should have your program pull the filtered data from the “filtered_expenses.json” file. 
