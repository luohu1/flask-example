# coding: utf-8


def bad_request(e):
    return 'Bad request!', 400


def not_found(e):
    return 'Not found!', 404


ERROR_MAPPING = {
    400: bad_request,
    404: not_found,
}


def register_error_handlers(app):
    for code, handler in ERROR_MAPPING.items():
        app.register_error_handler(code, handler)
