"""
Implement function parse_user(output_file, *input_files) for creating file that will contain
only unique records (unique by key "name") by merging information from all input_files argument
(if we find user with already existing name from previous file we should ignore it).


If the function cannot find input files we need to log information with error level

root - ERROR - File <file name> doesn't exists

For example:
user1.json :
[{"name": "Bob1", "rate": 1, “languages": ["English"]},
{"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
]

user2.json :
[{"name": "Bob1", "rate": 25, “languages": ["French"]},
{"name": "Bob3", "rate": 78, "languages": ["Germany"]}
]

If we execute parse_user(user3.json, user1.json, user2.json)
then file user3.json should contain information:
[{"name": "Bob1", "rate": 1, “languages": ["English"]},
{"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
{"name": "Bob3", "rate": 78, "languages": ["Germany"]}
]

"""
import json
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def parse_user(output_file, *input_files):
    lines = []
    for file in input_files:
        try:
            with open(file) as f:
                lines.extend(json.load(f))
        except FileNotFoundError:
            logging.error(f'File{file} doesn\'t exist')
    print(lines)
    output_data = []
    for line in lines:
        if 'name' in line.keys():
            if line['name'] not in [element['name'] for element in output_data]:
                output_data.append(line)
    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=2)


parse_user("/Users/denisgalyopa/IT/Projects/Softserve_marafon/Sprint_06/q2/user4.json",
           "/Users/denisgalyopa/IT/Projects/Softserve_marafon/Sprint_06/q2/user1.json",
           "/Users/denisgalyopa/IT/Projects/Softserve_marafon/Sprint_06/q2/user2.json")
