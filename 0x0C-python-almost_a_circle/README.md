## 0x0C. Python - Almost a circle

**0. If it's not tested it doesn't work** `[tests/]` >> Files, classes and methods are unit tested and PEP 8 validated.

**1. Base class** `[models/base.py, models/__init__.py]` >> Defines the first class `Base`. Also has an `__init__.py` file in a folder `models`, making it a Python package.

**2. First Rectangle** `[models/rectangle.py]` >> Defines a class `Rectangle` that inherits from `Base`.

**3. Validate attributes** `[models/rectangle.py]` >> Updates the class `Rectangle` by adding validation of all setter methods and instantiation (`id` excluded).

**4. Area first** `[models/rectangle.py]` >> Updates the class `Rectangle` by adding the public method `def area(self):` that returns the area value of the Rectangle instance.

**5. Display #0** `[models/rectangle.py]` >> Updates the class `Rectangle` by adding the public method `def display(self):` that prints in stdout the `Rectangle` instance with the character `#`.

**6. __str__** `[models/rectangle.py]` >> Updates the class `Rectangle` by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`.

**7. Display #1** `[models/rectangle.py]` >> Updates the class `Rectangle` by improving the public method `def display(self):` to print in stdout the `Rectangle` instance with the character `#` by taking care of `x` and `y`.

**8. Update #0** `[models/rectangle.py]` >> Updates the class `Rectangle` by adding the public method `def update(self, *args):` that assigns an argument to each of the provided attributes.

**9. Update #1** `[models/rectangle.py]` >> Updates the class `Rectangle` by updating the public method `def update(self, *args):` by changing the prototype to `update(self, *args, **kwargs)` that assigns a key/value argument to each of the provided attributes.

**10. And now, the Square!** `[models/square.py]` >> Defines a class `Square` that inherits from `Rectangle`.

**11. Square size** `[models/square.py]` >> Updates the class `Square` by adding the public getter and setter `size`.

**12. Square update** `[models/square.py]` >> Updates the class `Square` by adding the public method `def update(self, *args, **kwargs)` that assigns to each of the provided attributes.

**13. Rectangle instance to dictionary representation** `[models/rectangle.py]` >> Updates the class `Rectangle` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Rectangle`.

**14. Square instance to dictionary representation** `[models/square.py]` >> Updates the class `Square` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Square`.

**15. Dictionary to JSON string** `[models/base.py]` >> Updates the class `Base` by adding the static method `def to_json_string(list_dictionaries):` that returns the JSON string representation of `list_dictionaries`.

**16. JSON string to file** `[models/base.py]` >> Updates the class `Base` by adding the class method `def save_to_file(cls, list_objs):` that writes the JSON string representation of `list_objs` to a file.

**17. JSON string to dictionary** `[models/base.py]` >> Updates the class `Base` by adding the static method `def from_json_string(json_string):` that returns the list of the JSON string representation `json_string`.

**18. Dictionary to Instance** `[models/base.py]` >> Updates the class `Base` by adding the class method `def create(cls, **dictionary):` that returns an instance with all attributes already set.

**19. File to instances** `[models/base.py]` >> Updates the class `Base` by adding the class method `def load_from_file(cls):` that returns a list of instances.

**20. JSON ok, but CSV?** `[models/]` >> Updates the class `Base` by adding the class methods `def save_to_file_csv(cls, list_objs):` and `def load_from_file_csv(cls):` that serializes and deserializes in CSV.

**21. Let's draw it** `[models/base.py]` >> Updates the class `Base` by adding the static method `def draw(list_rectangles, list_squares):` that opens a window and draws all the `Rectangles` and `Squares`.
