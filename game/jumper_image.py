#Image printer
#End the game

#Alexander

class Jumper_image:
    incorrect = 0
    print("   ___   ")
    print("  /___\  ")
    print("  \   /  ")
    print("   \ /   ")
    print("    O    ")
    print("   /|\   ")
    print("   / \   ")
    print("         ")
    print("^^^^^^^^^")

    if incorrect <= 0:
        print("   ___   ")
        print("  /___\  ")
        print("  \   /  ")
        print("   \ /   ")
        print("    O    ")
        print("   /|\   ")
        print("   / \   ")
        print("         ")
        print("^^^^^^^^^") 

    elif incorrect == 1:
        print("  /___\  ")
        print("  \   /  ")
        print("   \ /   ")
        print("    O    ")
        print("   /|\   ")
        print("   / \   ")
        print("         ")
        print("^^^^^^^^^")

    elif incorrect == 2:    
        print("  \   /  ")
        print("   \ /   ")
        print("    O    ")
        print("   /|\   ")
        print("   / \   ")
        print("         ")
        print("^^^^^^^^^")

    elif incorrect == 3:
        print("   \ /   ")
        print("    O    ")
        print("   /|\   ")
        print("   / \   ")
        print("         ")
        print("^^^^^^^^^")

    elif incorrect == 4:
        print("    O    ")
        print("   /|\   ")
        print("   / \   ")
        print("         ")
        print("^^^^^^^^^")

    elif incorrect >= 5:
        print("    X    ")
        print("   /|\   ")
        print("   / \   ")
        print("         ")
        print("^^^^^^^^^")
        exit()

