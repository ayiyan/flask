from flask.views import MethodView
from flask import make_response

class TestServiceView(MethodView):
    def get(self, *args, **kwargs):
        return make_response(dict(code=200, status=True, message=123, data=456)), 200