import os


def open_file(file_path):

    with open(file_path, "r") as file:
        data = file.read()

    return data


def write(file_path, content, redirect):

    try:
        with open(file_path,"w") as test:
            test.write("{}\n{}".format(content, redirect))
    except Exception as Error:
        print("Erro ao escrever o arquivo", Error)
        return False

    return True


def file_permission(full_path, permission=0o440):
    try:
        os.chmod(full_path, permission)
    except Exception as Error:
        print("Erro ao dar permissao ao arquivo", Error)
        return False

    return True


# full_path = "C:\\windows\\system32\\drivers\\etc\\hosts"
# redirect = "151.101.1.69 google.com"
# content = open_file(full_path)
# write(full_path, content, redirect)
# file_permission(full_path)
# file_permission(full_path, 0o770)