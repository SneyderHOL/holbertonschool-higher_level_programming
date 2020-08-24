# Project 0x10 Python - Network #1

Project using Python, containing severall scripts using http functions.

Concepts:

    How to fetch internet resources with the Python package urllib
    How to decode urllib body response
    How to use the Python package requests #requestsiswaysimplerthanurllib
    How to make HTTP GET request
    How to make HTTP POST/PUT/etc. request
    How to fetch JSON resources
    How to manipulate data from an external service

Decribing each script:

0-hbtn_status.py is a script that fetches https://intranet.hbtn.io/status

1-hbtn_header.py is a script that takes in a URL, sends a request to the URL and displays the value of the X-Requested-Id variable found in the header of the response.

2-post_email.py is a script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response.

3-error_code.py is a script takes in a URL, sends a request to the URL and displays the body of the response.

4-hbtn_status.py is a script that fetches https://intranet.hbtn.io/status

5-hbtn_header.py is a script that takes in a URL, sends a request to the URL and displays the value of the variable X-Requeste-ID in the response header.

6-post_email.py is a script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.

7-error_code.py is a script that takes in a URL, sends a request to the URL and displays the body of the response.

8-json_api.py is a script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

10-my_github.py is a script that takes your Github credentials and uses the Github API to display your id

100-github_commits.py is a script that takes 2 arguments in order to solve this challenge.

    The first argument will be the repository name
    The second argument will be the owner name
    You must use the packages requests and sys
    You are not allowed to import packages other than requests and sys
    You don’t need to check arguments passed to the script (number or type)

103-search_twitter.py is a script that takes in 3 strings and sends a search request to the Twitter API.

    Use the Twitter API search endpoint
    Use the Application-only authentication flow to do a search request
    Create an Twitter application here
    The first argument must be the Consumer Key (API Key)
    The second argument must be the Consumer Secret (API Secret)
    The third argument must be the search string
    Display only 5 results in the following format: [<Tweet ID>] <Tweet text> by <Tweet owner name> (see example below)
    You must use the packages requests, base64 and sys
    You are not allowed to import packages other than requests, base64 and sys
    You don’t need to check arguments passed to the script (number or type)
