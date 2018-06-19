import os
import os.path
import json
import re
import hashlib
import uuid


def load_app_config(config_file_path):
    '''
    load json config file, example:
    {
        "query": {
            "port": 8000,
            "env1": "${ENV1:-default_value}",
            "env2": "${ENV2:-12}"
        }
    }
    :param config_file_path:
    :return:
    '''

    def _cast_to_type(s):
        try:
            return int(s)
        except ValueError:
            try:
                return float(s)
            except ValueError:
                return s

    def _substitude_env_vars(d):
        for key in d.keys():
            v = d.get(key)
            if isinstance(v, str) or isinstance(v, unicode):
                # parse ${ENV2}
                m = re.match('\${(\w+)}', v)
                if m:
                    env_name = m.group(1)
                    env_val = os.environ.get(env_name)
                    d[key] = env_val
                else:
                    # parse: ${ENV2:-12}
                    m = re.match('\${(\w+)\:-([\w\-\/\{\}]+)}', v)
                    if m:
                        env_name = m.group(1)
                        def_val = m.group(2)
                        env_val = os.environ.get(env_name)
                        if env_val is None:
                            env_val = _cast_to_type(def_val)
                        d[key] = env_val
            elif isinstance(v, dict):
                _substitude_env_vars(v)

    if os.path.isfile(config_file_path):
        with open(config_file_path, 'r') as f:
            app_config = json.load(f)
            _substitude_env_vars(app_config)
            return app_config
    else:
        raise Exception('Configuration file not found: '.format(config_file_path))


def to_bool(val):
    if type(val) is bool:
        return val
    elif type(val) is int:
        return bool(val)
    elif type(val) is str:
        try:
            return bool(int(val))
        except Exception as e:
            return False
    elif type(val) is float:
        return bool(int(val))
    else:
        return False


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


def random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.


def touch(fname, times=None):
    """
    equivalent of touch cmd
    :param fname:
    :param times:
    :return:
    """

    with open(fname, 'a'):
        os.utime(fname, times)


def get_file_update_time_epoch(file_path):
    try:
        return int(os.stat(file_path).st_mtime)
    except Exception as err:
        return 0
