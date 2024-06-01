from re import search, sub, findall


def regex_transform(data, transformation):
    res = data

    for val in transformation.get("value"):
        sel = val.get("selection")
        sel_result = search(sel, res)

        handling = val.get("handling")
        if handling.get("type") == "return":
            res = regex_return(handling.get("value"), sel_result)

    return res


def regex_return(h_value, sel_result):
    if "$" not in h_value:
        return h_value

    placeholders = findall(r"(\$\d+)", h_value)
    result = h_value

    for placeholder in placeholders:
        group = int(placeholder.split("$")[1])
        result = result.replace(placeholder, "" if not sel_result else sel_result.group(group))

    return result
