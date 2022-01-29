import re
import os


def create_files(dir_name,file_name):
    f = open(file_name, "r")
    content = f.read()
    f.close()

    reg_str = "(?<=\\(#)[^\\)]*"
    x = re.findall(reg_str, content)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    for topic in x:
        topic = topic.replace("-"," ").title().replace(" ","_", 1)
        name = "./{0}/{1}.md".format(dir_name,topic)
        if not os.path.exists(name) :
            print("created:"+name)
            f = open(name, "a")
            f.close()


for d in os.listdir():
    if d.endswith(".txt"):
        dir_name,file_name = d.split("_")
        create_files(dir_name,file_name)





