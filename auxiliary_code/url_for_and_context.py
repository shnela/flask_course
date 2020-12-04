from flask import url_for, request

from main import app


def obtain_value():
    d = {'a': 1, 'b': 2}
    print(d['a'])
    # print(d['c'])
    print(d.get('a'))
    print(d.get('c'))
    print(d.get('a', 42))
    print(d.get('c', 42))


def display_request():
    with app.test_request_context():
        print(request)


def display_urls():
    with app.test_request_context():
        print(url_for('index'))
        print(url_for('index', username='Joe'))
        print(url_for('index', username='Joe', other_get_arg='Mike'))
        print(url_for('profile', username='Joe', amount=2))
        print(url_for('profile', username='Joe', amount=2, _external=True))


if __name__ == '__main__':
    obtain_value()
    display_request()
    display_urls()
