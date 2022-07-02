# Flask-WTF

[README_PREV.md](./README_PREV.md)

## New requirements
* [Flask-WTF][]
* Already placed in `requirements.txt`
  * pyCharm will  install automatically
  * for console or other IDE `$ pip install -r requirements.txt`

### Flask-WTF is based on WTF-Forms
[WTF-Forms][]

### `__init__.py` is updated
* [WTF-Forms - Basic fields][]
* [WTF-Forms - Built-in validators][]

## Prerequisite 
SECRET_KEY required (https://pinetools.com/random-string-generator)
Add it in pyCharm config run.

## Session example
[Session]

How we store form info in session.

## Assignment
1. Add new link in navbar, link should point to `login` view.
2. Add new field in form - `age` and save value in `session`.
This field should be positive integer, so IntegerField and NumberRange should be used.
If `age` isn't present in session - display 0.
Test form with missing data, negative values and strings instead of int.
After sending ('user1', 43), we should be redirected to `index` which will display "Hello fasada (32)!"


## Integration Flask-WTF with Flask-Bootstrap
We're using [Flask-WTF - Creating Forms][] for generating `LoginForm` in `main.py`.  
We're struggling with displaying it in `login.html`.

Let's integrate `Flask-WTF` with [Bootstrap-flask integration][]

### Why?
#### More beautiful
[Bootstrap forms][] - looks nice

#### Simpler to use in html
```html
<form method="POST">
  {{ wtf.render_form(form) }}
</form>
```

But first [Bootstrap-flask WTF macros][] is required.
```html
{% import 'bootstrap5/form.html' as wtf %}
```
Add it to `base.html`

## Assignments
* Display name of logged in user in bottom left corner, or 'Unknown'
* Implement logout view which will remove `name` and `age` keys from session
Then link new view to "Log out" button in right top corner.
This should be simple GET function (no form required)
(use `del`)

[Flask-WTF]: https://flask-wtf.readthedocs.io/en/1.0.x/
[WTF-Forms]: https://wtforms.readthedocs.io/en/3.0.x/
[WTF-Forms - Basic fields]: https://wtforms.readthedocs.io/en/3.0.x/fields/#basic-fields
[WTF-Forms - Built-in validators]: https://wtforms.readthedocs.io/en/3.0.x/validators/#built-in-validators
[Flask-WTF - Creating Forms]: https://flask-wtf.readthedocs.io/en/1.0.x/quickstart.html#creating-forms
[Bootstrap-flask integration]: https://bootstrap-flask.readthedocs.io/en/stable/basic/
[Bootstrap forms]: https://getbootstrap.com/docs/5.2/forms/overview/
[Bootstrap-flask WTF macros]: https://bootstrap-flask.readthedocs.io/en/stable/macros/
[Session]: https://flask.palletsprojects.com/en/2.1.x/api/#flask.session