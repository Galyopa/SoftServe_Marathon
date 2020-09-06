""" Class Student has attributes full_name:str, avg_rank: float, courses: list
Class Group has attributes title: str, students: list.

Make both classes JSON serializable.

Json-files represent information about student (students).

Create methods:

Student.from_json(json_file) that return Student instance from attributes from json-file;

Group.serialize_to_json(list_of_groups, filename)

Group.create_group_from_file(students_file)

Parse given files, create instances of Student class and create instances of Group class (title for group is name of json-file without extension)."""

import json


class Student:
    def __init__(self, full_name, avg_rank, courses):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    def __str__(self):
        return f'{self.full_name} ({self.avg_rank}):{self.courses}'

    def __repr__(self):
        return f'"{self.full_name} ({self.avg_rank}):{self.courses}"'

    @classmethod
    def from_json(cls, json_file):
        with open(json_file) as f:
            data = json.load(f)
            return cls(data['full_name'], data['avg_rank'], data['courses'])


class Group:

    def __init__(self, title, students):
        self.title = title
        self.students = students

    def __repr__(self):
        return f'{self.title}: {self.students}'

    @classmethod
    def create_group_from_file(cls, students_file):
        with open(students_file) as f:
            data = json.load(f)
            if isinstance(data, list):
                return cls(f.name.split('.')[0], [Student(**i) for i in data])
            return cls(f.name.split('.')[0], [(Student(**data))])

    @staticmethod
    def serialize_to_json(list_of_groups, file_name):
        with open(file_name, 'w') as f:
            json.dump(list_of_groups, f, default=lambda groups: groups.__dict__)
