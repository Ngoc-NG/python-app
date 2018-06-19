import sys
import os
import argparse

from flask import Flask, jsonify
from flask import request

# fix app root
app_root = os.getcwd()
sys.path.append(app_root)

from app.config import app_ip, app_version
from app.logger import get_logger

log = get_logger(__name__)
flask_app = Flask(__name__)
log.info('app root dir: {}'.format(app_root))


@flask_app.errorhandler(404)
def not_found(error):
    return json_error(Exception('endpoint not found'), http_code=404)


@flask_app.route('/api/v1/version', methods=['GET'])
def get_version():
    return jsonify({'version': app_version})


@flask_app.route('/api/v1/test', methods=['GET'])
def get_models():
    query_attrs = request.args.to_dict()
    try:
        return jsonify({'request_attr': query_attrs})
    except Exception as ex:
        return json_error(ex, http_code=500)


def json_error(msg, http_code=400):
    log.exception(msg)
    try:
        err = {'error': str(msg), 'exception': type(msg).__name__}
        return jsonify(err), http_code
    except:
        return jsonify({'exception': 'internal error'}), 500


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--port', default=None, type=int, help='rest port')
    args = arg_parser.parse_args()
    if args.port is not None:
        log.info('http port was provided as argument: {}'.format(args.port))
        flask_app.run(host=app_ip, port=args.port, debug=True)
    else:
        # do not provide port when run with gunicorn
        flask_app.run()
