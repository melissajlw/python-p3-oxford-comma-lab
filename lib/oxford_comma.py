def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    
    tmp = ""
    for item in items:
        if item != items[-1]:
            tmp +=  f"{item}, "
        else:
            tmp += f"and {item}"
    return tmp
