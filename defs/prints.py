from data import users, cards


# for checking
def print_users(users, data_type):
    user_info = []
    for user in users:
        if data_type == "user":
            user_info.append(
                f'{data_type}:{user["id"]} {user["username"]} {user["password"]}'
            )
        else:
            user_info.append(
                f'{data_type}:{user["id"]} {user["username"]} {user["cardname"]}'
            )
    for info in user_info:
        print(info)


def checks():
    print_users(users, "user")
    print_users(cards, "card")
