"""
In this exercise we will track data using a local "remote" and explore the fundamentals of DVC.

Set up
- Create a conda environment with DVC installed.
- Initialize DVC and Git using dvc init and git init, respectively.

Create Local Remote
- Create a folder outside of your current working directory and set it as your local "remote" storage.

Track files in DVC
- In Python, write a (simple) function that creates a list of identifiers (e.g. 1 to 10) and save it as a csv.
- Track that file using DVC and push it to your local remote.
- Re-run your code but now double the number of identifiers. Now track and push the newly updated csv file.
- Optionally, explore the created .dvc file and what see how it changes when you update the tracked csv.
"""

import numpy as np
import csv
import sys

def create_ids(id_count: str) -> None:
    
    id_count = int(id_count)
    
    # Generate data for the array
    array_data = list(range(1, id_count))

    # Define the output CSV file name
    output_file = "dvc_exercise.csv"

    # Write the array data to the CSV file
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Number"])  # Write header row
        for number in array_data:
            writer.writerow([number])

    print(f"Data 1 to {id_count} written to {output_file}")

if __name__ == "__main__":
    
    create_ids(sys.argv[1])