## 0x10. Python - Network #0

**0. cURL body size** `[0-body_size.sh]` >> Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response in bytes, using `curl`.

**1. cURL to the end** `[1-body.sh]` >> Bash script that takes in a URL, sends a `GET` request to the URL, and displays the body of the response if the status code response is `200`, using `curl`.

**2. cURL Method** `[2-delete.sh]` >> Bash script that sends a `DELETE` request to the URL passed as the first argument and displays the body of the response, using `curl`.

**3. cURL only methods** `[3-methods.sh]` >> Bash script that takes in a URL and displays all HTTP methods the server will accept, with `curl`.

**4. cURL headers** `[4-header.sh]` >> Bash script that takes in a URL as an argument together with a header variable `X-School-User-Id` of value `98`, sends a `GET` request to the URL, and displays the body of the response, using `curl`.

**5. cURL POST parameters** `[5-post_params.sh]` >> Bash script that takes in a URL together with variables `email` and `subject` with values `test@gmail.com` and `I will always be here for PLD` respectively, sends a `POST` request to the passed URL, and displays the body of the response, using `curl`.

**6. Find a peak** `[6-peak.py, 6-peak.txt]` >> Script that prints 3 lines using `console.log()` (like in `1-multi_languages.js`), but by using an array of string and a loop.

**7. Only status code** `[100-status_code.sh]` >> Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response, using `curl`.

**8. cURL a JSON file** `[101-post_json.sh]` >> Bash script that sends a JSON `POST` request to a URL passed as the first argument, and displays the body of the response, using `curl`. The script sends a `POST` request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request.

**9. Catch me if you can!** `[102-catch_me.sh]` >> Bash script that makes a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message containing `You got me!`, in the body of the response, using `curl`.
