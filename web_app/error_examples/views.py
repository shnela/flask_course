from flask import render_template, abort

from . import bp

@bp.route('/return_error/<int:response_code>/')
def return_response_with_code(response_code):
    return f'Return {response_code}', response_code


@bp.route('/abort_error/<int:response_code>/')
def abort_response_with_code(response_code):
    abort(response_code)


@bp.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404
