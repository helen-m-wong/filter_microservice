Communication Contract

The microservice filters data provided in the “expenses.json” file and writes the filtered data to the “filtered_expenses.json” file. To request data from the microservice, you should have your program write all the expenses data to the “expenses.json” file in the format:

{
“filter”: “CATEGORY”,
“data”: [expenses data goes here]
}

Then run the filter_microservice.py program. You can run it by entering into the terminal “python3 filter_microservice.py.” To receive data from the microservice, you should have your program pull the filtered data from the “filtered_expenses.json” file. 

UML Sequence Diagram:

<img width="625" alt="Screen Shot 2023-07-31 at 10 24 26 PM" src="https://github.com/helen-m-wong/filter_microservice/assets/108026042/0c496926-9bdb-4255-a263-c7c079a939c1">
