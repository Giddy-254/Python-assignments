# File Read & Write with Error Handling

def modify_file_content(text):
    
    return text.upper()


def main():
    # Ask the user for the input filename
    filename = input("Enter the filename to read: ")

    try:
        # Open the file for reading
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content
        modified_content = modify_file_content(content)

        # Create a new file to store modified content
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"✅ File processed successfully!")
        print(f"Modified content saved as: {new_filename}")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"❌ Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
