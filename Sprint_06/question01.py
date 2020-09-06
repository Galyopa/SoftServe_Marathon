"""
Create function find(file, key)
This function parses json-file and returns all unique values of the key.

1.json:
[{"name": "user_1”, "password": "pass_1”},
{"name": "user_2”, "password": ["pass_1", "qwerty“]} ]
find("1.json", "password") returns ["pass_1", "qwerty"]

2.json:
[{"name": "user_1”, "credentials": {"username": "user_user”, "password": "1234qweQWE"}}, {"name": "user_2”, "password": ["pass_1 ", "qwerty "]}]
find("2.json", "password") returns ["1234qweQWE", "pass_1", "qwerty"]

3.json:
{"name": "user_1","credentials": {"username": "user_user","password": "1234qweQWE"}}
find("3.json", "password") returns ["1234qweQWE"]
"""
import json


def find(file, key):
    result = []

    def handle_dict(data):
        if key in data.keys():
            result.extend(data[key]) if isinstance(data[key], list) else result.append(data[key])

    with open(file) as f:
        json.load(f, object_hook=handle_dict)
    return list(set(result))


# def find_all(data, key):
#     result = []
#
#     def find_in_dict(data, key):
#         for k, v in data.items():
#             if k == key:
#                 result.extend(v) if isinstance(v, list) else result.append(v)
#             else:
#                 find_data(v, key)
#
#     def find_data(data, key):
#         if isinstance(data, list):
#             for elem in data:
#                 find_data(elem, key)
#         if isinstance(data, dict):
#             find_in_dict(data, key)
#
#     find_data(data, key)
#     return set(result)
#
#
# def find(file, key):
#     with open(file) as f:
#         data = json.load(f)
#     return list(find_all(data, key))

"""__________________________________________________________________"""
# def find(file, key):
#     with open(file) as f:
#         data = json.load(f)
#     password = []
#     if isinstance(data, list):
#         for element in data:
#             if isinstance(element, dict):
#                 for r, v in element.items():
#                     if isinstance(v, dict):
#                         u = v.get(key)
#                         password.append(u)
#                 s = element.get(key)
#                 if isinstance(s, list):
#                     for i in s:
#                         password.append(i)
#                 elif isinstance(s, dict):
#                     k = s.get(key)
#                     if k:
#                         password.append(k)
#                 elif s:
#                     password.append(s)
#     elif isinstance(data, dict):
#         p = data.get(key)
#         if isinstance(p,list):
#             for i in p:
#                 password.append(i)
#         else:
#             password.append(p)
#     answer = set(password)
#     return list(answer)


print(find("/Users/denisgalyopa/IT/Projects/Softserve_marafon/Sprint_06/q1/1.json", "password"))
print(find("/Users/denisgalyopa/IT/Projects/Softserve_marafon/Sprint_06/q1/2.json", "password"))
print(find("/Users/denisgalyopa/IT/Projects/Softserve_marafon/Sprint_06/q1/3.json", "password"))
print(find("/Users/denisgalyopa/IT/Projects/Softserve_marafon/Sprint_06/q1/4.json", "password"))
print(find("/Users/denisgalyopa/IT/Projects/Softserve_marafon/Sprint_06/q1/one_user_array_pass.json", "password"))
print(find("/Users/denisgalyopa/IT/Projects/Softserve_marafon/Sprint_06/q1/one_user_one_pass.json", "password"))
