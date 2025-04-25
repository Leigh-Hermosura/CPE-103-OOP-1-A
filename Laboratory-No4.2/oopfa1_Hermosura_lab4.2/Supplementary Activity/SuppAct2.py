for i in range(3):
    username = input("Please enter your name: ")
    nameLength = len(username)
    if nameLength >= 3:
        startIndex = (nameLength // 2) - 1
        endIndex = startIndex + 3
        middle = username[startIndex:endIndex]
        print(middle)
    else:
        print("Your name is too short to extract 3 middle characters.")