""" In user.json file we have information about users in format [{“id”: 1, “name”: “userName”, “department_id”: 1}, ...],

in file department.json are information about departments in format: [{“id”: 1, “name”: “departmentName”}, ...].

Function user_with_department(csv_file, user_json, department_json) should read from json files information and create csv file in format:

header line - user, department

next lines :  <userName>, <departmentName>

If file department.json doesn't contain department with department_id from user.json we generate DepartmentName exception.

Create appropriate json-schemas for user and department.

If schema for user or department doesn't satisfy formats described above we should generate InvalidInstanceError exception

To validate instances create function validate_json(data, schema) """
import csv
import json


class DepartmentName(Exception):
    def __init__(self, err_id):
        self.err_msg = f"Department with id {err_id} doesn't exist"

    def __str__(self):
        return repr(self.err_msg)


class InvalidInstanceError(Exception):
    def __init__(self, schema):
        self.err_msg = f" Error in {schema} schema"

    def __str__(self):
        return repr(self.err_msg)


studentSchema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
            "department_id": {"type": "number"}
        },
        "required": ["department_id", "name"]
    }
}

departmentSchema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type", "string"}
        },
        "required": ["id", "name"]
    }
}


def user_with_department(user_department_csv, user_json, department_json):
    with open(user_json) as f:
        user_list = json.load(f)
        if not validate(user_list, studentSchema):
            raise InvalidInstanceError("Error in user schema")

    with open(department_json) as f:
        department_list = json.load(f)
        if not validate(department_list, departmentSchema):
            raise InvalidInstanceError("Error in department schema")

    id_name_dict = dict((element['id'], element['name']) for element in department_list)

    user_with_dep = []
    for element in user_list:
        try:
            user_with_dep.append({"name": element["name"], "department": id_name_dict[element["department_id"]]})
        except Exception:
            raise DepartmentName(f'{element["department_id"]}')

    with open(user_department_csv, "wt") as f:
        writer = csv.DictWriter(f, fieldnames=["name", 'department'])
        writer.writeheader()
        writer.writerows(user_with_dep)


