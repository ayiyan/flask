from flask.blueprints import Blueprint
from apiframework.views.api.test_service_view import TestServiceView


apigroup_bp = Blueprint('apigroup',__name__,url_prefix='/api/v1/')

# apigroup_bp.add_url_rule('<string:dc_id>/test_service_register',view_func=TestServiceView)
apigroup_bp.add_url_rule('bbb',view_func=TestServiceView.as_view('TestServiceView'))