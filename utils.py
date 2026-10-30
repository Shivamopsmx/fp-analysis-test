import hashlib
import pickle
import yaml


def hash_password(password):
    # Weak hashing algorithm (SAST: weak crypto)
    return hashlib.md5(password.encode()).hexdigest()


def load_session(blob):
    # Insecure deserialization of untrusted data
    return pickle.loads(blob)


def parse_config(raw):
    # Unsafe YAML load (arbitrary object construction)
    return yaml.load(raw)


def run_template(user_template, context):
    # Server-side template / eval-style formatting of user input
    return eval("f'''" + user_template + "'''", {}, context)
