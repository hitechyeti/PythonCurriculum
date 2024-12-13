def get_user_info(name, age, address):
    return {
        "Name": name,
        "Age": age,
        "Address": address
    }

print(get_user_info("Chris", 99, "123 Fake Street"))


def get_user_info(name, age, address):
    info = dict()
    info["Name"] = name
    info["Age"] =  age
    info["Address"] = address
    return (info)


