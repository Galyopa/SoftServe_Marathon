"""
Create context manager class SerializeManager with attributes filename and type for serializing python object to different formats.
For defining format create enum FileType with values JSON, BYTE. Create function serialize(object, filename, fileType).
This function should serialize object to filename according to type.
For example:
if user_dict = { 'name': 'Roman', 'id': 8}
then
serialize(user_dict, "2", FileType.BYTE) -> creates file with name "2" and this file will contain user_dict as byte array
serialize("String", "string.json", FileType.JSON) -> creates file with name "string.json" and text "String"
"""
import json
import pickle
from enum import Enum


class FileType(Enum):
    JSON = 'json'
    BYTE = 'byte'


class SerializeManager:

    def __init__(self, filename, type):
        self.filename = filename
        self.type = type

    def __enter__(self):
        if self.type == FileType.JSON:
            self.file = open(self.filename, 'w')
        else:
            self.file = open(self.filename, 'wb')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


def serialize(object, filename, fileType):
    with SerializeManager(filename, fileType) as f:
        if fileType == FileType.JSON:
            json.dump(object, f)
        else:
            pickle.dump(object, f)
