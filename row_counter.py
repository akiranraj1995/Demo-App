import streamlit as st
import time
import os
import glob
import pandas as pd

# Set up the input folder path
input_folder = "streaming_data"

# Define a function to count the number of rows in a CSV file
def count_rows(file_path):
    df = pd.read_csv(file_path)
    return len(df)

# Define the Streamlit app
def app():
    # Set the page title
    st.set_page_config(page_title="Sensor Data Overview")

    # Display the title and description
    st.title("Total Number of Records")
    st.write("This app counts the number of rows in new CSV files in the input folder.")

    # Keep track of the filenames of the previously processed files
    processed_files = set()

    # Keep track of the total number of rows
    total_rows = 0

    # Continuously monitor the input folder for new CSV files and update the row count
    while True:
        # Get the list of CSV files in the input folder
        file_list = glob.glob(os.path.join(input_folder, "*.csv"))

        # Filter out the previously processed files
        new_files = [file_path for file_path in file_list if file_path not in processed_files]

        # If there are new files, count the rows and update the total count
        if new_files:
            for file_path in new_files:
                rows = count_rows(file_path)
                st.write(f"New file detected: {file_path}")
                st.write(f"Number of rows in file: {rows}")
                total_rows += rows
            st.write(f"Total number of rows: {total_rows}")

            # Add the filenames of the newly processed files to the set
            processed_files.update(new_files)

        # Wait for 10 seconds before checking for new files again
        time.sleep(10)

# Run the app
if __name__ == "__main__":
    app()
