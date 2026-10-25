from ingradiens import get_type

def can_add(inv, name, max_slots, stack_size):
    try:
        for slot in inv:
            if slot["name"] == name and slot["count"] < stack_size:
                return True
        return len(inv) < max_slots
    except Exception as e:
        print("Помилка can_add:", e)
        return False

def add_item(inv, name, amount, max_slots, stack_size):
    try:
        for slot in inv:
            if amount == 0:
                break
            if slot["name"] == name and slot["count"] < stack_size:
                put = min(stack_size - slot["count"], amount)
                slot["count"] += put
                amount -= put
        while amount > 0 and len(inv) < max_slots:
            put = min(stack_size, amount)
            inv.append({"name": name, "count": put})
            amount -= put
    except Exception as e:
        print("Помилка додавання предмета:", e)
    return amount

def count_item(inv, name):
    total = 0
    try:
        for slot in inv:
            if slot["name"] == name:
                total += slot["count"]
    except Exception as e:
        print("Помилка підрахунку:", e)
    return total
def remove_item(inv, name, amount):
    try:
        if count_item(inv, name) < amount:
            return False
        i = 0
        while i < len(inv) and amount > 0:
            if inv[i]["name"] == name:
                take = min(inv[i]["count"], amount)
                inv[i]["count"] -= take
                amount -= take
                if inv[i]["count"] == 0:
                    inv.pop(i)
                    continue
            i += 1
        return True
    except Exception as e:
        print("Помилка видалення предмета:", e)
        return False

def count_type(inv, item_type):
    total = 0
    try:
        for slot in inv:
            if get_type(slot["name"]) == item_type:
                total += slot["count"]
    except Exception as e:
        print("Помилка підрахунку типу:", e)
    return total

def remove_by_type(inv, item_type):
    try:
        for slot in inv:
            if get_type(slot["name"]) == item_type:
                return remove_item(inv, slot["name"], 1)
        return False
    except Exception as e:
        print("Помилка remove_by_type:", e)
        return False

def print_inventory(inv, title, max_slots):
    try:
        print("--- " + title + " (" + str(len(inv)) + "/" + str(max_slots) + " слотів) ---")
        if len(inv) == 0:
            print("  порожньо")
        for i in range(len(inv)):
            print("  " + str(i + 1) + ". " + inv[i]["name"] + " x" + str(inv[i]["count"]))
    except Exception as e:
        print("Помилка виводу інвентаря:", e)