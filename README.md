# QBLib

QBLib is an SQL query construction library for Python. QBLib was developped to serve as a "no-bells-and-whistles" solution for developpers to dynamically build and integrate SQL queries within their code.


## Getting Started

These instructions will get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The only dependency is Python 2.x

### Installing

Options to install the QBLib package:
* Clone the repository: git clone https://github.com/mkrahal/QBLib  
* Download the zip: https://github.com/mkrahal/QBLib

## Basic Usage and Examples

### First Steps

Import QBLib into your python module.

```
import QBLib
```

### Building SQL Queries

Build an SQL query to create a table using the creation_tools() class:

```
# Create an instance of the creation_tools() class
i = QBLib.creation_tools()

# Define the table name and the column-names / data-structure dictionary
table_name = "city_table"
column_and_datatype_dict = {"ID": ["INTEGER"], "CITY": ["VARCHAR": 10], "STATE": ["VARCHAR": 2], "POPULATION": ["INTEGER"]}

# Use the create_table() method to build your SQL Query
i.create_table(table_name, column_and_datatype_dict)
 
```

Build an SQL query to insert data into a table using the editing_tools() class:

```
# Create an instance of the editing_tools() class
i = QBLib.editing_tools()

# Define the table name and the column-names / column-value dictionary
table_name = "city_table"
column_and_value_dict = {"ID": 13, "CITY": "Miami", "STATE": "FL", "POPULATION": 430332}

# Use the insert_data() method to build your SQL query
i.insert_data(table_name, column_and_value_dict)
 
```

Build an SQL query to search for data in a table using the processing_tools() class:

```
# Create an instance of the processing_tools() class
i = QBLib.processing_tools()

# Define the table name, pattern to search for, column to search, and the match type (exact or approximate).
table_name = "city_table"
search_pattern = "FL" 
match_column = "STATE"
match_exact = True

# Use the find_row() method to build your SQL query
i.find_row(table_name, search_pattern, match_column, match_exact)
 
```

### Full List of Classes and Methods

==> creation_tools()
       |- create_table()
       |- add_columns()
       |- define_index_col()
       |- define_primary_key()

==> editing_tools()
       |- insert_data()
       |- import_csv()
       |- export_csv()
       |- delete_row()
       |- delete_columns()

==> processing_tools()
       |- find_row()
       |- find_in_col()
       |- find_greater()
       |- find_lesser()
       |- table_join
       |- count_records()
       |- get_max()
       |- get_min() 

For further details on the usage and applications of these classes/methods please refer to the documentation.


## Built With

* Python 2.7


## Contributing

Please read [CONTRIBUTING.md](contributing.md) for details on the code of conduct, and the process for submitting pull requests.


## Authors

* **MK Rahal** - *Initial Development* - [mkrahal](https://github.com/mkrahal)


## License

This project is licensed under the MIT License - see the [LICENSE.txt](license.txt) file for details


## Acknowledgments

* Special thanks to Mark Lutz.
