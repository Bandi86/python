def t_actions(action):
    for t_action in action:
        print(f"{t_action} ft értékű tranzakció")

def full_release(action):
    release_sum = 0
    for t_action in action:
        if t_action < 0:
            release_sum += t_action
    print(f"Teljes kiadások összege: {release_sum}")
    

def income(action):
    income_sum = 0
    for t_action in action:
        if t_action > 0:
            income_sum += t_action
    print(f"Teljes bevételek összege: {income_sum}")                     