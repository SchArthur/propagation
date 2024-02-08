
def readini(file : str) -> dict:
    """
    Returns a dictionnary of all namespaces and their values in the target ini file.
    """
    with open(file, "r") as f:
        content = f.readlines()
        returned_values = {}
        for i in range(len(content)):
            x = content[i].split(":")
            returned_values[x[0]]=x[1].rstrip()
    return returned_values