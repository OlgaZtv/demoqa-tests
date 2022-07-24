import demoqa_tests
import os
from pathlib import Path


def resourse(path):
    file_path = str(Path(demoqa_tests.__file__)
                    .parent
                    .parent
                    .joinpath(f'resources/{path}'))
    return os.path.abspath(file_path)
