
def createLine(newLine):
    try:
        with open('scratch.txt', 'a', encoding='utf-8') as file:
            file.write(newLine + '\n')
        print(f"Successfully added line: '{newLine}' to 'scratch.txt'.")
    except Exception as e:
        print(f"Error writing to 'scratch.txt': {e}")

def readFile():
    try:
        with open('scratch.txt', 'r', encoding='utf-8') as file:
            for line in file:
                print(line.rstrip())
    except FileNotFoundError:
        print('The file does not exist.')

def updateFile(oldLine, newLine):
    try:
        with open('scratch.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        found = False
        with open('scratch.txt', 'w', encoding='utf-8') as file:
            for line in lines:
                if line.rstrip() == oldLine:
                    file.write(newLine + '\n')
                    found = True
                    print(f"Updated line '{oldLine}' to '{newLine}'.")
                else:
                    file.write(line)
        if not found:
            print(f"Line '{oldLine}' not found.")
    except FileNotFoundError:
        print("The file does not exist.")

def removeLine(lineDelete):
    try:
        with open('scratch.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        found = False
        with open('scratch.txt', 'w', encoding='utf-8') as file:
            for line in lines:
                if line.rstrip() == lineDelete:
                    found = True
                    print(f"Deleted line '{lineDelete}'.")
                else:
                    file.write(line)
        if not found:
            print(f"Line '{lineDelete}' not found.")
    except FileNotFoundError:
        print("The file does not exist.")

def main():
    while True:
        print("\nCRUD (Create, Read, Update, and Delete)")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            line = input("Enter line to add: ")
            createLine(line)
        elif choice == '2':
            readFile()
        elif choice == '3':
            oldLine = input("Enter the line to update: ")
            newLine = input("Enter new line: ")
            updateFile(oldLine, newLine)
        elif choice == '4':
            lineDelete = input("Enter line to delete: ")
            removeLine(lineDelete)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
