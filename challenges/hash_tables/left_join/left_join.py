
def left_join(h1, h2):
    """Function that left joins two hashtables.
    """
    output = []

    for el in h1.hashtable:
        if el:
            for key_value in el:
                output.append(key_value)

    for key_value in output:
        key_value.append(h2._get(key_value[0]))

    return output
