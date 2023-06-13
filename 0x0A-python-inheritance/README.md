## 0x0A. Python - Inheritance

**0. Lookup** `[0-lookup.py]` >> Function that returns the list of available attributes and methods of an object.

**1. My list** `[1-my_list.py, tests/1-my_list.txt]` >> Class `MyList` that inherits from `list`.

**2. Exact same object** `[2-is_same_class.py]` >> Function that returns `True` if the object is exactly an instance of the specified class; otherwise `False`.

**3. Same class or inherit from** `[3-is_kind_of_class.py]` >> Function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise `False`.

**4. Only sub class of** `[4-inherits_from.py]` >> Function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise `False`.

**5. Geometry module** `[5-base_geometry.py]` >> An empty class `BaseGeometry`.

**6. Improve Geometry** `[6-base_geometry.py]` >> Class `BaseGeometry` (based on `5-base_geometry.py`), with public instance method `def area(self):` that raises an `Exception` with the message `area() is not implemented`.

**7. Integer validator** `[7-base_geometry.py, tests/7-base_geometry.txt]` >> Class `BaseGeometry` (based on `5-base_geometry.py`), with public instance method `def area(self):` that raises an `Exception` with the message `area() is not implemented`, and public instance method `def integer_validator(self, name, value):` that validates `value`. `name` is assumed to always be a string, and if `value` is not an integer raises a `TypeError` exception with the message `<name> must be an integer`, else if `value` is less or equal to 0 raises a `ValueError` exception with the message `<name> must be greater than 0`.

**8. Rectangle** `[8-rectangle.py]` >> Class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`), with instantiation for `width` and `height` in prototype `def __init__(self, width, height):`. `width` and `height` are private with no getter or setter methods defined, and must be positive integers validated by `integer_validator`.

**9. Full rectangle** `[9-rectangle.py]` >> Class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`) (based on `8-rectangle.py`), with instantiation for `width` and `height` in prototype `def __init__(self, width, height):`. `width` and `height` are private with no getter or setter methods defined, and must be positive integers validated by `integer_validator`. Implements the `area()` method. `print()` prints and `str()` returns `[Rectangle] <width>/<height>` as the rectangle description.

**10. Square #1** `[10-square.py]` >> Class `Square` that inherits from `Rectangle` (`9-rectangle.py`). Instantiated with `size: def __init__(self, size):`, where `size` is private with no getter and setter methods defined, and is a positive integer validated by `integer_validator`. Implements the `area()` method.

**11. Square #2** `[11-square.py]` >> Class `Square` that inherits from `Rectangle` (`9-rectangle.py`) (based on `10-square.py`). Instantiated with `size: def __init__(self, size):`, where `size` is private with no getter and setter methods defined, and is a positive integer validated by `integer_validator`. Implements the `area()` method. `print()` prints and `str()` returns `[Square] <width>/<height>` as the square description.

**12. My integer** `[100-my_int.py]` >> Class `MyInt` that inherits from `int`. This class is a rebel, and its `==` and `!=` operators inverted.

**13. Can I?** `[101-add_attribute.py]` >> Function that adds a new attribute to an object if it’s possible. Raises a `TypeError` exception, with the message `can't add new attribute` if the object can’t have new attribute.
