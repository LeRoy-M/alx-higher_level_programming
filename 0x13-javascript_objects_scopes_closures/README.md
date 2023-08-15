## 0x13. JavaScript - Objects, Scopes and Closures

**0. Rectangle #0** `[0-rectangle.js]` >> Defines an empty class `Rectangle` that defines a rectangle, using the `class` notation.

**1. Rectangle #1** `[1-rectangle.js]` >> Defines a class `Rectangle` that defines a rectangle, using the `class` notation. The constructor takes 2 arguments, `w` and `h`, and initializes the instance attributes `width` and `height` respectively.

**2. Rectangle #2** `[2-rectangle.js]` >> Defines a class `Rectangle` that defines a rectangle, using the `class` notation. The constructor takes 2 arguments, `w` and `h`, and initializes the instance attributes `width` and `height` respectively. Creates an empty object if either `w` or `h` is equals to zero, or not a positive integer.

**3. Rectangle #3** `[3-rectangle.js]` >> Defines a class `Rectangle` that defines a rectangle, using the `class` notation. The constructor takes 2 arguments, `w` and `h`, and initializes the instance attributes `width` and `height` respectively. Creates an empty object if either `w` or `h` is equals to zero, or not a positive integer. Also defines an instance method called `print()` that prints the rectangle using the character `X`.

**4. Rectangle #4** `[4-rectangle.js]` >> Defines a class `Rectangle` that defines a rectangle, using the `class` notation. The constructor takes 2 arguments, `w` and `h`, and initializes the instance attributes `width` and `height` respectively. Creates an empty object if either `w` or `h` is equals to zero, or not a positive integer. Also defines an instance method called `print()` that prints the rectangle using the character `X`, an instance method called `rotate()` that exchanges the `width` and the `height` of the rectangle, and another instance method called `double()` that multiples the `width` and the `height` of the rectangle by 2.

**5. Square #0** `[5-square.js]` >> Defines a class `Square` that defines a square and inherits from `Rectangle` of `4-rectangle.js`, using the `class` notation and `extends` as well. The constructor takes 1 argument `size` and the constructor of `Rectangle` uses `super()`.

**6. Square #1** `[6-square.js]` >> Defines a class `Square` that defines a square and inherits from `Square` of `5-square.js`, using the `class` notation and `extends` as well. Defines an instance method called `charPrint(c)` that prints the rectangle using the character `c`, or the character `X` if `c` is undefined.

**7. Occurrences** `[7-occurrences.js]` >> Function with prototype `exports.nbOccurences = function (list, searchElement)` that returns the number of occurrences in a list.

**8. Esrever** `[8-esrever.js]` >> Function with prototype `exports.esrever = function (list)` that returns the reversed version of a list.

**9. Log me** `[9-logme.js]` >> Function with prototype `exports.logMe = function (item)` that prints the number of arguments already printed and the new argument value, with output format `<number arguments already printed>: <current argument value>`.

**10. Number conversion** `[10-converter.js]` >> Function with prototype `exports.converter = function (base)` that converts a number from base 10 to another base passed as argument.

**11. Factor index** `[100-map.js]` >> Script that imports an array `list` from the file `100-data.js` and computes a new array using `map`, with each value in the new list equal to the value of the initial list multipled by the index in the list, then prints both the initial list and the new list.

**12. Sorted occurences** `[101-sorted.js]` >> Script that imports a dictionary of occurrences `dict` from the file `101-data.js` by user id and computes a dictionary of user ids by occurrence, creating a new dictionary with keys as number of occurrences and values as the list of user ids, then prints the new dictionary at the end.

**13. Concat files** `[102-concat.js]` >> Script that concats 2 files, where the first argument is the file path of the first source file, the second argument is the file path of the second source file, and the third argument is the file path of the destination.
