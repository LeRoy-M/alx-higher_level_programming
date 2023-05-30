## 0x06. Python - Classes and Objects

**0. My first square** `[0-square.py]` >> Defines an empty class `Square` that defines a square.

**1. Square with size** `[1-square.py]` >> Defines a class `Square` that defines a square (based on `0-square.py`) with a private instance attribute named `size`, that has no type/ value verification instantion.

**2. Size validation** `[2-square.py]` >> Defines a class `Square` that defines a square (based on `1-square.py`) with a private instance attribute named `size`, that has optional `size: def __init__(self, size=0):` instantion. 

**3. Area of a square** `[3-square.py]` >> Defines a class `Square` that defines a square (based on `2-square.py`) with a private instance attribu    te named `size`, that has optional `size: def __init__(self, size=0):` instantion, and public instance method `def area(self):` that returns the current square area.

**4. Access and update private attribute** `[4-square.py]` >> Defines a class `Square` that defines a square (based on `3-square.py`) with a private instance attribute named `size`, that has optional `size: def __init__(self, size=0):` instantion, and public instance method `def area(self):` that returns the current square area.

**5. Printing a square** `[5-square.py]` >> Defines a class `Square` that defines a square (based on `4-square.py`) with a private instance attribute named `size`, that has optional `size: def __init__(self, size=0):` instantion, and public instance method `def area(self):` that returns the current square area, plus public instance method `def my_print(self):` that prints in stdout the square with the character `#`.

**6. Coordinates of a square** `[6-square.py]` >> Defines a class `Square` that defines a square (based on `5-square.py`) with a private instance attribute named `size` and `position`, that has optional `size` and optional `position: def __init__(self, size=0, position=(0, 0)):` instantion, and public instance method `def area(self):` that returns the current square area, plus public instance method `def my_print(self):` that prints in stdout the square with the character `#`.

**7. Singly linked list** `[100-singly_linked_list.py]` >> Defines a class `Node` that defines a node of a singly linked list by private instance attribute `data` and `next_node`, where `data` and `next_node` have instantiation with `100-singly_linked_list.py`. Also has a printable class `SinglyLinkedList` that defines a singly linked list by private instance attribute `head`, simple instantiation `def __init__(self):`, and public instance method `def sorted_insert(self, value):` that inserts a new `Node` into the correct sorted position in the list (increasing order).

**8. Print Square instance** `[101-square.py]` >> Defines a class `Square` that defines a square (based on `6-square.py`) with a private instance attribute named `size` and `position`, that has optional `size` and optional `position: def __init__(self, size=0, position=(0, 0)):` instantion, and public instance method `def area(self):` that returns the current square area, plus public instance method `def my_print(self):` that prints in stdout the square with the character `#`. Printing a `Square` instance has the same behaviour as `my_print()`.

**9. Compare 2 squares** `[102-square.py]` >> Defines a class `Square` that defines a square (based on `4-square.py`) with a private instance attribute named `size`, instantiated with `size: def __init__(self, size=0):`. It has a public instance method `def area(self):` that returns the current square area, and an instance can answer to comparators `==`, `!=`, `>`, `>=`, `<` and `<=` based on the square area.

**10. ByteCode -> Python #5** `[103-magic_class.py]` >> Python class MagicClass that does exactly the same as the provided Python bytecode.
