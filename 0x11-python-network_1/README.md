## 0x11. Python - Network #1

**0. What's my status? #0** `[0-hbtn_status.py]` >> Python script that fetches `https://alx-intranet.hbtn.io/status`, using the `urllib` package.

**1. Response header value #0** `[1-hbtn_header.py]` >> Python script that takes in a URL, sends a request to the URL, and displays the value of the `X-Request-Id` variable found in the header of the response, using the `urllib` and `sys` packages.

**2. POST an email #0** `[2-post_email.py]` >> Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`), using the `urllib` and `sys` packages.

**3. Error code #0** `[3-error_code.py]` >> Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8), using the `urllib` and `sys` packages.

**4. What's my status? #1** `[4-hbtn_status.py]` >> Python script that fetches `https://alx-intranet.hbtn.io/status`, using the `requests` package.

**5. Response header value #1** `[5-hbtn_header.py]` >> Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header, using the `requests` and `sys` packages.

**6. POST an email #1** `[6-post_email.py]` >> Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response, using the `requests` and `sys` packages.

**7. Error code #1** `[7-error_code.py]` >> Python script that takes in a URL, sends a request to the URL and displays the body of the response, using the `requests` and `sys` packages. If the HTTP status code is greater than or equal to 400, prints `Error code: <HTTP_status_code>`.

**8. Search API** `[8-json_api.py]` >> Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter, using the `requests` and `sys` packages. The letter sent is in variable `q`, which is set to `q=""` if no argument is given. If the response body is properly JSON formatted and not empty, displays the `id` and `name` like so => `[<id>] <name>`; otherwise displays `Not a valid JSON` if the JSON is invalid, and `No result` if the JSON is empty.

**9. My GitHub!** `[10-my_github.py]` >> Python script that takes ones GitHub credentials (username and password) and uses the [GitHub API][link] to display their `id`, using the `requests` and `sys` packages. The first argument is the `username` and the second is the `password` (which is a PAT in some cases).

[link]: https://docs.github.com/en/rest/users?apiVersion=2022-11-28

**10. Time for an interview!** `[100-github_commits.py]` >> Python script that takes two (2) arguments in order to solve the challenge posed below, using the `requests` and `sys` packages.

> The Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges, like this one:
```
Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
```
