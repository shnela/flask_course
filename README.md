# Application context, request context and `url_for`

[README_PREV.md](./README_PREV.md)

## Context
* Just show request for `index` endpoint
* [The Application Context][]
* [The Request Context][]

## Url_for
[flask.url_for]


## Test context
```bash
python -m auxiliary_code.url_for_and_context
```

## Assignment
* Override `index`'s user_info with `name` and `age` passed as request get argument.
```python
request.args.get(<key>, <default>)
```
If no such parameter, keep default values.
Use `request.args`.
  * For http://127.0.0.1:5000/?username=chris&age=10 view should render "Hello chris (10)!"
  * For http://127.0.0.1:5000/?age=10 view should render "Hello Mike (10)!"
  * For http://127.0.0.1:5000/?dummy_arg=fasada view should render "Hello Mike (42)!"
  
* Replace all static href from `base.html` with urls rendered with `url_for`

[The Application Context]: https://flask.palletsprojects.com/en/2.1.x/appcontext/
[The Request Context]: https://flask.palletsprojects.com/en/2.1.x/reqcontext/
[flask.url_for]: https://flask.palletsprojects.com/en/2.1.x/api/?highlight=url_for#flask.url_for