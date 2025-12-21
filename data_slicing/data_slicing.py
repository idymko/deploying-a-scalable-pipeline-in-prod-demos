"""
Data Slicing 

	Download the Iris data set from the UCI Machine Learning Repository(opens in a new tab).
 	https://archive.ics.uci.edu/dataset/53/iris
	
 	Load the data using Pandas and then write a function that outputs the descriptive stats 
	for each numeric feature while the categorical variable is held fixed.
	
 	Run this function for each of the four numeric variables in the Iris data set.

	python data_slicing.py --file_name iris.zip

"""

import pandas as pd
import argparse
import logging
import zipfile
import os

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()

def load_data(args):
	try:
		# Extract the zip file
		with zipfile.ZipFile(args.file_name, 'r') as zip_ref:
			extract_path = os.path.splitext(args.file_name)[0]  # Extract to a folder with the same name as the zip file
			zip_ref.extractall(extract_path)
			logger.info(f"Extracted files to: {extract_path}")
		
		# Identify the correct data file (iris.data)
		data_file = os.path.join(extract_path, "iris.data")
		if not os.path.exists(data_file):
			raise FileNotFoundError(f"Expected data file 'iris.data' not found in {extract_path}.")
		
		# Load the data into a DataFrame
		column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
		data = pd.read_csv(data_file, header=None, names=column_names)
		logger.info("Iris dataset loaded successfully.")
		return data
	
	except Exception as e:
		logger.error(f"Error processing the zip file: {e}")
		raise

def descriptive_stats_by_class(data, auto=False):
	"""
	Output descriptive statistics for each numeric feature grouped by the 'class' column.
	"""
	if auto == False:
		print("\nDescriptive statistics grouped by class (manual)")
		for feature in ["sepal_length", "sepal_width", "petal_length", "petal_width"]:
			print(f"\nfeature: {feature}")
			for cls in data["class"].unique():
				class_data = data[feature][data["class"]==cls]
				mean = class_data.mean()
				stddev = class_data.std()
				print(f"\tclass: {cls} \t mean: {mean:.4f} \t stddev: {stddev:.4f}")
	else:
		print("\nDescriptive statistics grouped by class (pandas)")
		for feature in ["sepal_length", "sepal_width", "petal_length", "petal_width"]:
			print(f"\n{feature}")
			grouped_stats = data.groupby("class")[feature].describe()
			print(grouped_stats)
	
def go(args):
	# Load data
	data = load_data(args)
 
	# Descriptive statistics
	descriptive_stats_by_class(data)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(
		description="Download a file and upload it as an artifact to W&B", fromfile_prefix_chars="@"
	)

	parser.add_argument(
		"--file_name", 
		type=str, 
		help="Filename of Iris dataset", 
		required=False,
		default="iris.zip"
	)
 
	args = parser.parse_args()

	go(args)
