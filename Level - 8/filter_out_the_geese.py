# List of geese breeds to be filtered out
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim","Steinbacher"]

def goose_filter(birds):
    returnedlist=[]
    for n in birds:
        # If the bird is not a goose, add it to the result list
        if n not in geese:
            returnedlist.append(n)

    return returnedlist
# Example usage
print(goose_filter(["Malard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]))
# Output: ['Malard', 'Hook Bill', 'Crested', 'Blue Swedish']