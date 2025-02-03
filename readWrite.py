def read_and_write_file_with_error_handling(input_file, output_file):
    try:
        # Read the input file
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Modify the content (e.g., convert text to uppercase)
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print("File modified successfully and saved as", output_file)
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except IOError:
        print(f"Error: There was an issue reading or writing the file.")


def safe_file_read():
    filename = input("Enter the filename you want to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
        print("File content:")
        print(content)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: The file '{filename}' could not be read.")


# Run the error handling lab first to allow the user to check if the file exists
safe_file_read()

# After successful reading, you can then proceed with the read-and-write challenge
input_filename = 'input.txt'  # Replace with your input file
output_filename = 'output.txt'  # Replace with your output file
read_and_write_file_with_error_handling(input_filename, output_filename)
