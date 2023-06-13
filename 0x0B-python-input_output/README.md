## 0x0B. Python - Input/Output

**0. Read file** `[0-read_file.py]` >> Function that reads a text file (`UTF8`) and prints it to stdout.

**1. Write to a file** `[1-write_file.py]` >> Function that writes a string to a text file (`UTF8`) using the `with` statement and returns the number of characters written. Creates the file if it does not already exist, else it overwrites the content of the file if it already does exist.

**2. Append to a file** `[2-append_write.py]` >> Function that appends a string at the end of a text file (`UTF8`) using the `with` statement and returns the number of characters added. Creates the file if it does not already exist.

**3. To JSON string** `[3-to_json_string.py]` >> Function that returns the JSON representation of an object (string).

**4. From JSON string to Object** `[4-from_json_string.py]` >> Function that returns an object (Python data structure) represented by a JSON string.

**5. Save Object to a file** `[5-save_to_json_file.py]` >> Function that writes an Object to a text file, using a JSON representation and that makes use of the `with` statement.

**6. Create object from a JSON file** `[6-load_from_json_file.py]` >> Function that creates an Object from a “JSON file” making use of the `with` statement.

**7. Load, add, save** `[7-add_item.py]` >> Script that adds all arguments to a Python list, and then saves them to a file. The script makes use of the `save_to_json_file` function from `5-save_to_json_file.py` script and the `load_from_json_file` function from `6-load_from_json_file.py` script.

**8. Class to JSON** `[8-class_to_json.py]` >> Function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object. `obj` is an instance of a Class which has all its attributes as serializable (list, dictionary, string, integer and boolean).

**9. Student to JSON** `[9-student.py]` >> Class `Student` that defines a student by public instance attributes `first_name`, `last_name` and `age`, and which has instantiation with `def __init__(self, first_name, last_name, age):` and has a public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`).

**10. Student to JSON with filter** `[10-student.py]` >> Class `Student` based on `9-student.py` that defines a student by public instance attributes `first_name`, `last_name` and `age`, and which has instantiation with `def __init__(self, first_name, last_name, age):` and has a public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`); where if `attrs` is a list of strings only attribute names contained in this list will be retrieved, otherwise, all attributes will be retrieved.

**11. Student to disk and reload** `[11-student.py]` >> Class `Student` based on `10-student.py` that defines a student by public instance attributes `first_name`, `last_name` and `age`, and which has instantiation with `def __init__(self, first_name, last_name, age):` and has a public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`); where if `attrs` is a list of strings only attribute names contained in this list will be retrieved, otherwise, all attributes will be retrieved. Also has public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance, with `json` assumed to always be a dictionary, a dictionary key being the public attribute name and a dictionary value being the value of the public attribute.

**12. Pascal's Triangle** `[12-pascal_triangle.py]` >> Function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`. The function returns an empty list if `n <= 0` and `n` is assumed to always be an integer.

**13. Search and update** `[100-append_after.py]` >> Function that inserts a line of text to a file using the `with` statement, after each line containing a specific string, as shown in the provided example.

**14. Log parsing** `[101-stats.py]` >> Script that reads `stdin` line by line with the input format `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`, and computes metrics. Prints these statistics since the beginning after each 10 lines and after a keyboard interruption (`CTRL + C`):
- Total file size: `File size: <total size>`
- where is the sum of all previous
- Number of lines by status code:
	- possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500`
	- if a status code doesn’t appear, doesn’t print anything for this status code
	- format: `<status code>: <number>`
	- status codes are printed in ascending order
