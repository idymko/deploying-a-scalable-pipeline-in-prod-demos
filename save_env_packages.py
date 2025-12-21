if __name__ == "__main__":
    # Read the requirements file
    with open("requirements.txt", "r") as file:
        lines = file.readlines()

    # Filter lines that contain "=="
    filtered_lines = [line for line in lines if "==" in line]

    # Write the filtered lines back to the file
    with open("requirements1.txt", "w") as file:
        file.writelines(filtered_lines)