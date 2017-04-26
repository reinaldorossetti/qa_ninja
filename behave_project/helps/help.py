


def open(file_path, string):

    with open(file_path) as file:
        data = file.readlines()

    with open(file_path,"w") as test:
        test.write("{}{}".format(data, string))

