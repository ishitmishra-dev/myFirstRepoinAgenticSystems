def calculate_average(scores):
    return sum(scores) / len(scores)


def has_admin_access(roles):
    return "admin" in roles


def main():
    users = [
        {
            "name": "Alice",
            "scores": [80, 85, 90, 75],
            "roles": {"admin", "editor"}
        },
        {
            "name": "Bob",
            "scores": [60, 70, 65, 68],
            "roles": {"viewer"}
        },
        {
            "name": "Charlie",
            "scores": [88, 92, 84, 86],
            "roles": {"editor", "viewer"}
        }
    ]

    for user in users:
        name = user["name"]
        scores = user["scores"]
        roles = user["roles"]

        average = calculate_average(scores)
        admin_access = has_admin_access(roles)

        user_summary = (name, average, admin_access)

        print("Name:", user_summary[0])
        print("Average Score:", user_summary[1])
        print("Admin Access:", user_summary[2])
        print("-" * 30)


main()
