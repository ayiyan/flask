
from apiframework.views.blueprint import apigroup_bp
from flask_cors import CORS
from flask import  Flask
import argparse
import sys
# sys.path.append('./apiframework')

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})

app.register_blueprint(apigroup_bp)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("-p", "--port", type=int, help="server port", default=8000)
    args = parser.parse_args()
    port = int(args.port)
    app.run(host='0.0.0.0', port=port, debug=False, threaded=False)