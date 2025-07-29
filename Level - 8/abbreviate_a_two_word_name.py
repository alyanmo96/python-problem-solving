#    Converts a full name into initials separated by a dot.

def abbrev_name(name):
    abbs=[]
    name_list = name.split()
    for abb in name_list:
        abbs.append(abb[0].upper())

    return ".".join(abbs)


# Example usage
print(abbrev_name("John Mike"))  # Output: J.M
print(abbrev_name("john mike"))  # Output: J.M