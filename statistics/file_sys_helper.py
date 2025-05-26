from pathlib import Path


class FileSysHelper:
    """
    FileSysHelper class is used to handle file system operations.
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def file_exists(self):
        path = Path(self.file_path)
        return path.exists()

    def create_file(self):
        with open(self.file_path, 'w', newline=''):
            pass
