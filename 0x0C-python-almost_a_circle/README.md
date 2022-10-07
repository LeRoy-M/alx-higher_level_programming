0. If it's not tested it doesn't work [tests/] >> All files, classes and methods to be unit tested and be PEP8 validated 
1. Base class [models/base.py, models/__init__.py] >> The first class 'Base'
2. First Rectangle [models/rectangle.py] >> Class 'Rectangle' that inherits from 'Base'
3. Validate attributes [models/rectangle.py] >> Class 'Rectangle' updated by adding validation of all setter methods and instantiation ('id' excluded)
4. Area first [models/rectangle.py] >> Class 'Rectangle' updated by adding the public method 'def area(self):' that returns the area value of the 'Rectangle' instance
5. Display #0 [models/rectangle.py] >> Class 'Rectangle' updated by adding the public method 'def display(self):' that prints in stdout the 'Rectangle' instance with the character '#'
6. __str__ [models/rectangle.py] >> Class 'Rectangle' updated by overriding the '__str__' method so that it returns '[Rectangle] (<id>) <x>/<y> - <width>/<height>'
7. Display #1 [models/rectangle.py] >> Class 'Rectangle' updated by improving the public method 'def display(self):' to print in stdout the 'Rectangle' instance with the character '#'
8. Update #0 [models/rectangle.py] >> Class 'Rectangle' updated by adding the public method 'def update(self, *args):' that assigns an argument to each attribute
9. Update #1 [models/rectangle.py] >> Class 'Rectangle' updated by updating the public method 'def update(self, *args):' by changing the prototype to 'update(self, *args, **kwargs)' that assigns a key/value argument to attributes
10. And now, the Square! [models/square.py] >> Class 'Square' that inherits from 'Rectangle'
11. Square size [models/square.py] >> Class 'Square' updated by adding the public getter and setter 'size'
12. Square update [models/square.py] >> Class 'Square' updated by adding the public method 'def update(self, *args, **kwargs)' that assigns attributes
13. Rectangle instance to dictionary representation [models/rectangle.py] >> Class 'Rectangle' updated by adding the public method 'def to_dictionary(self):' that returns the dictionary representation of a 'Rectangle'
14. Square instance to dictionary representation [models/square.py] >> Class 'Rectangle' updated by adding the public method 'def to_dictionary(self):' that returns the dictionary representation of a 'Square'
15. Dictionary to JSON string [models/base.py] >> Class 'Base' updated by adding the static method 'def to_json_string(list_dictionaries):' that returns the JSON string representation of 'list_dictionaries'
16. JSON string to file [models/base.py] >> Class 'Base' updated by adding the class method 'def save_to_file(cls, list_objs):' that writes the JSON string representation of 'list_objs' to a file
17. JSON string to dictionary [models/base.py] >> Class 'Base' updated by adding the static method 'def from_json_string(json_string):' that returns the list of the JSON string representation 'json_string'
18. Dictionary to Instance [models/base.py] >> Class 'Base' updated by adding the class method 'def create(cls, **dictionary):' that returns an instance with all attributes already set
19. File to instances [models/base.py] >> Class 'Base' updated by adding the class method 'def load_from_file(cls):' that returns a list of instances
20. JSON ok, but CSV? [models/] >> Class 'Base' updated by adding the class methods 'def save_to_file_csv(cls, list_objs):' and 'def load_from_file_csv(cls):' that serializes and deserializes in CSV
21. Let's draw it [models/base.py] >> Class 'Base' updated by adding the static method 'def draw(list_rectangles, list_squares):'  that opens a window and draws all the 'Rectangles' and 'Squares'
