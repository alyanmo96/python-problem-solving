#    Returns the number of lightsabers owned by a person.

def how_many_light_sabers_do_you_own(name="Anyone else"):
    if name == "Zach":    # If the name is "Zach", he owns 18 lightsabers

        return 18

    else:        # Anyone else owns 0

        return 0


# Example usage
print(how_many_light_sabers_do_you_own("Zach"))   # Output: 18
print(how_many_light_sabers_do_you_own())         # Output: 0
print(how_many_light_sabers_do_you_own("John"))   # Output: 0