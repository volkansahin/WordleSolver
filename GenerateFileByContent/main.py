import re
import os


def create_files(dir_name, file_name, file_content):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    file_name= "".join(x for x in file_name if x.isalnum() or x == ' ' or x == '.').strip()
    file_path = os.path.join(dir_name, file_name + ".md")
    with open(file_path, "w+") as f:
        f.write(file_content)


def parse_topics(str_content):
    reg_str = r"(?<=\#\s)(.+)([^#]*)"
    x = re.findall(reg_str, str_content)
    return x


for d in os.listdir():
    if d.endswith(".md"):
        content = open(d, "r").read()
        list_title_content = parse_topics(content)
        for title, content in list_title_content:
            create_files(d.split('.')[0], title, content)
