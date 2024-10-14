# File Creation
# Create a new text file named "my_file.txt" in write mode ('w')
with open("my_file.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is my first line of text.\n")
    file.write("The answer to life is 42.\n")

# File Reading and Display
# Read the contents of "my_file.txt" and display them on the console
with open("my_file.txt", "r") as file:
    content = file.read()
    print("Contents of my_file.txt:")
    print(content)

# File Appending
# Open "my_file.txt" in append mode ('a') and append three additional lines
with open("my_file.txt", "a") as file:
    file.write("Appending a new line 1.\n")
    file.write("Appending a new line 2.\n")
    file.write("Appending a new line 3.\n")

# Optional: Display updated content
with open("my_file.txt", "r") as file:
    updated_content = file.read()
    print("Updated contents of my_file.txt:")
    print(updated_content)
