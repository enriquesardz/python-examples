user_input = int(input("Number of blocks:"))

def get_height(blocks):
    height = 0
    total = 0
    prev = 1
    while(True):
        total += prev
        prev += 1
        if (total <= blocks):
            height += 1
            print("#" * (prev-1))
        else:
            break
        
    return height
print("Height: ", get_height(user_input))
print("Bobo putio 1 maseter")