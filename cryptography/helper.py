import os

CURRENTLY_PATH = '../'


def path_to_file(file):
    path = None
    for root, dirs, files in os.walk(CURRENTLY_PATH):
        for name in files:
            if name == file:
                path = (os.path.abspath(os.path.join(root, name)))

    return path
