import os
import shutil
import uuid

from contextlib import contextmanager

@contextmanager
def temp_folder():
    path = "/tmp/{}".format(uuid.uuid4(), exist_ok=True)
    os.makedirs(path)
    
    try:
        yield path
    finally:
        shutil.rmtree(path)

@contextmanager
def temp_file():
    path = "/tmp/{}".format(uuid.uuid4())
    os.makedirs("/tmp", exist_ok=True)

    try:
        yield path
    finally:
        os.remove(path)