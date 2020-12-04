# Custom error pages and static files
[README_PREVIOUS.md](./README_PREVIOUS.md)

Static files - overridden favicon.
[Flask - static files][]
Error codes https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

### Handle errors
http://127.0.0.1:5000/return_error/404/ isn't handled
http://127.0.0.1:5000/abort_error/404/ is

## Assignments
* Download gif used in 404.html as "vincent404.gif" and serve it as static file in 404 handler
* Handle internal_server_error (500) with custom template


[Flask - static files]: https://flask.palletsprojects.com/en/2.1.x/tutorial/static/#static-files
