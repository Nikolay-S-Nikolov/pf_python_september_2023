def collect(journal_list: list, collect_item: str):
    if collect_item not in journal_list:
        journal_list.append(collect_item)
    return journal_list


def drop(journal_list: list, drop_item: str):
    if drop_item in journal_list:
        journal_list.remove(drop_item)
    return journal_list


def combine_item(journal_list: list, comb_item: str):
    old_item, new_item = comb_item.split(":")
    if old_item in journal_list:
        idx_add = journal_list.index(old_item) + 1
        journal_list.insert(idx_add, new_item)
    return journal_list


def renew(journal_list: list, renew_item: str):
    if renew_item in journal_list:
        idx_renew = journal_list.index(renew_item)
        last_item = journal_list.pop(idx_renew)
        journal_list.append(last_item)
    return journal_list


journal = input().split(", ")
command = input()

while command != "Craft!":
    action, item = command.split(" - ")
    if action == "Collect":
        journal = collect(journal, item)
    elif action == "Drop":
        journal = drop(journal, item)
    elif action == "Combine Items":
        journal = combine_item(journal, item)
    elif action == "Renew":
        journal = renew(journal, item)
    command = input()
print(*journal, sep=", ")
