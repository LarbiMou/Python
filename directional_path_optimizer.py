# Lab 12 Solution Code 4/24/25
# This module contains a funcrtion dirReduc that recieves an list
# With a set of directions. If two direxrions in a row are opposite each other
# Then those directions are removed from the list. After all directions are
# Reduced the resulting list (which might be emoty) is returned

def dirReduc(list_of_dirs):
    list_index = 0
    while list_index < len(list_of_dirs)-1:
        opposite = False
        if list_of_dirs[list_index]=="NORTH" and list_of_dirs[list_index+1]=="SOUTH":
            opposite = True
        elif list_of_dirs[list_index]=="SOUTH" and list_of_dirs[list_index+1]=="NORTH":
            opposite = True
        elif list_of_dirs[list_index]=="EAST" and list_of_dirs[list_index+1]=="WEST":
            opposite = True
        elif list_of_dirs[list_index]=="WEST" and list_of_dirs[list_index+1]=="EAST":
            opposite = True

        if opposite:
            list_of_dirs.pop(list_index+1)
            list_of_dirs.pop(list_index)
            list_index=0
        else:
            list_index=list_index+1

            

    return list_of_dirs # At end of function, return reduced list
