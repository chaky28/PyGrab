from re import search, sub, findall


def regex_transform(data, transformation):
    res = data

    for val in transformation.get("value"):
        sel = val.get("selection")

        handling = val.get("handling")
        h_type = handling.get("type")
        h_value = handling.get("value")

        if h_type == "return":
            sel_result = search(sel, res)
            res = regex_return(h_value, sel_result)
        if h_type == "replace":
            return regex_replace(h_value, sel, data)

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


def regex_replace(h_value, sel, data):
    return sub(sel, sub(r"\$(\d+)", r"\\\1", h_value), data)
