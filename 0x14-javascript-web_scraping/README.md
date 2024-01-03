## 0x14. JavaScript - Web scraping

**0. Readme** `[0-readme.js]` >> Javascript script that reads and prints the content of a file. It takes the file's path as the first argument, and the content is read in `utf-8`. In case of occurrence of an error during the reading, the error object is printed.

**1. Write me** `[1-writeme.js]` >> Javascript script that writes a string to a file. It takes the file's path as the first argument, the string to be written into the file as the second argument, and the content is read in `utf-8`. In case of occurrence of an error during the reading, the error object is printed.

**2. Status code** `[2-statuscode.js]` >> Javascript script that displays the status code of a `GET` request in the format `code: <status code>`, using the module `request`.

**3. Star wars movie title** `[3-starwars_title.js]` >> Javascript script that uses the [Star Wars API](https://swapi-api.alx-tools.com/) with the endpoint `https://swapi-api.alx-tools.com/api/films/:id` to print the title of a Star Wars movie where the episode number matches a given integer, using the module `request`. It takes the movie ID as the first argument.

**4. Star wars Wedge Antilles** `[4-starwars_count.js]` >> Javascript script that uses the [Star Wars API](https://swapi-api.alx-tools.com/) with the endpoint `https://swapi-api.alx-tools.com/api/films/` to print the number of movies where the character "Wedge Antilles" is present, using the module `request`. The script uses Wedge Antilles' character ID (`18`), to filter the result of the API.

**5. Loripsum** `[5-request_store.js]` >> Javascript script that gets the contents of a webpage and stores them in a file, using the module `request`. It takes the URL to request as the first argument, and the file path to store the body response as the second argument.

**6. How many completed?** `[6-completed_tasks.js]` >> Javascript script that computes the number of tasks completed by user id and then prints the users with their number of completed tasks, using the module `request`. It takes the API URL `https://jsonplaceholder.typicode.com/todos` as the first argument.

**7. Who was playing in this movie?** `[100-starwars_characters.js]` >> Javascript script that uses the [Star Wars API](https://swapi-api.alx-tools.com/) to print all characters of a Star Wars movie, displaying one character name by line using the module `request`. It takes the Movie ID as the first argument.

**8. Right order** `[101-starwars_characters.js]` >> Javascript script that uses the [Star Wars API](https://swapi-api.alx-tools.com/) to print all characters of a Star Wars movie, displaying one character name by line (in the same order of the list "characters" in the `/films/` response) using the module `request`. It takes the Movie ID as the first argument.
