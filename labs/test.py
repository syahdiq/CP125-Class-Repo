def archive_inactive_user(users):
    inactive = []
    for element in users:
        if element["status"] == "inactive":
            inactive.append(element["id"])
    return inactive
users = ("id" == "m40", "status" == "inactive")

