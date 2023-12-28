import os
import tkinter as tk
from tkinter import filedialog, simpledialog

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

    # Create CMakeLists.txt if .cpp or .c files are found and CMakeLists.txt does not already exist
    if contains_cpp_files and not os.path.isfile(os.path.join(directory, 'CMakeLists.txt')):
        with open(os.path.join(directory, 'CMakeLists.txt'), 'w') as cmakelists:
            cmakelists.write('cmake_minimum_required(VERSION 3.10)\n\n# Add your project setup here\n')
        print(f'Created CMakeLists.txt in {directory}')
    
    # Stop recursion if the specified level is reached
    if levels == 0:
        return

    # Recursively create CMakeLists.txt in subdirectories if they contain .cpp or .c files
    for dirpath, dirnames, filenames in os.walk(directory):
        # Skip subdirectories deeper than the specified level
        if os.path.relpath(dirpath, directory).count(os.sep) >= levels:
            continue
        for subdir in dirnames:
            create_cmakelists(os.path.join(dirpath, subdir), levels - 1)

def gui_create_cmakelists():
    directory = filedialog.askdirectory()
    if directory:  # Ensure that the user didn't cancel directory selection
        levels = simpledialog.askinteger("Input Level", "Enter the number of levels to traverse (0 for the current directory only):")
        if levels is not None:  # Ensure that the user entered a number
            create_cmakelists(directory, levels)

# Create the main window
root = tk.Tk()
root.title("CMakeLists Creator")

# Create a label and button for directory selection and function execution
label = tk.Label(root, text="Select a directory and enter the number of levels", padx=10, pady=10)
label.pack()

create_button = tk.Button(root, text="Create CMakeLists", command=gui_create_cmakelists, padx=20, pady=5)
create_button.pack()

# Run the event loop
root.mainloop()
