import os

from dotenv import dotenv_values


def path_to_file(file):
    env_path = os.path.dirname(os.path.realpath(__file__))
    path = None
    for root, dirs, files in os.walk(env_path):
        for name in files:
            if name == file:
                path = (os.path.abspath(os.path.join(root, name)))

    return path


def get_env_values() -> dict:
    default_env = dotenv_values(path_to_file('env.env'))
    env_type = default_env['ENV']

    if env_type == 'PROD':
        print('============ ENV PROD ===========')
        env_values = dotenv_values(path_to_file('.env.prod'))
    elif env_type == 'HOMOLOG':
        print('============ ENV HOMOLOG ===========')
        env_values = dotenv_values(path_to_file('.env.homolog'))
    elif env_type == 'DEV':
        print('============ ENV DEV ===========')
        env_values = dotenv_values(path_to_file('.env.dev'))
    return env_values


ENV = get_env_values()
print(ENV['DB_HOST'])
