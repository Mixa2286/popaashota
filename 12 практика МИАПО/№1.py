def get_access_level(role):
    access_levels = {"admin": 10,"manager": 5,"user": 1}
    return access_levels.get(role, 0)

print(get_access_level("user"))