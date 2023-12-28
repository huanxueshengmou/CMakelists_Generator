import os

def create_cmakelists(directory, levels):
    # Check if .cpp or .c files are present in the current directory
    contains_cpp_files = any(file.endswith((
    '.cpp', '.cxx', '.cc', '.c++', '.C','.c',   # C++
    '.c',                                       # C
    '.f', '.for', '.f90',                       # Fortran
    '.java',                                    # Java
    '.cs',                                      # C#
    '.py',                                      # Python
        )) for file in os.listdir(directory))

    # If there are .cpp or .c files in the directory and CMakeLists.txt does not exist, create it
    if contains_cpp_files and not os.path.isfile(os.path.join(directory, 'CMakeLists.txt')):
        with open(os.path.join(directory, 'CMakeLists.txt'), 'w') as cmakelists:
            cmakelists.write('cmake_minimum_required(VERSION 3.10)\n\n# Add your project setup here\n')
        print(f'Created CMakeLists.txt in {directory}')
    
    # If levels is 0, it means this is the last directory we need to check
    if levels == 0:
        return

    # Recursively create CMakeLists.txt in subdirectories if they contain .cpp or .c files
    for dirpath, dirnames, filenames in os.walk(directory):
        # Skip the subdirectories if we have reached the specified level depth
        if os.path.relpath(dirpath, directory).count(os.sep) >= levels:
            continue
        for subdir in dirnames:
            create_cmakelists(os.path.join(dirpath, subdir), levels - 1)

# Main function to run the script
if __name__ == "__main__":
    directory_input = input("Enter the directory path (use . for current directory): ")
    level_input = int(input("Enter the number of levels to traverse (0 for current directory only): "))

    # Call the create_cmakelists function with the user's input
    create_cmakelists(directory_input, level_input)
