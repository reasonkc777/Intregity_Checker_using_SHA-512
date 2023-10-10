File Integrity Checker in Python
 
Overview

The file integrity checker is a Python program that allows users to verify the consistency and integrity of two files using SHA-512. This tool is designed to provide graphical user interfaces (GUI) to help users verify the integrity of files.

Prerequisites

Before using this application, ensure that you have the following prerequisites in place:
- Python 3 installed on your system.

Usage

Follow the steps below to use the File Integrity Checker:
1. Download the Application: Clone or download this repository to your local machine.
   
3. Run the Application: Open a terminal or command prompt and navigate to the directory containing the script.

5. Execute the Script: Run the script using the following command:
python file_integrity_checker.py

7. Launch the GUI: The GUI application will pop up on your screen.
   
9. Initiate the Check: To start the integrity check, click on the “Check Integrity” button.
    
11. Select Files: You can choose the first file you want to check in the file dialog that appears. Click "Open" after selecting the file.
    
13. Select Second File: You will be prompted to choose the second file for comparison in a new file dialog that will open. After making your choice, click "Open".
    
15. Integrity Check: The application will compute the SHA-512 hashes of the two chosen files and contrast them to check for consistency.
    
17. View Results: The GUI will reveal the integrity check's outcome. It will display "Files match" in green if the files are identical. If they do, "Files differ" will appear in red.
   
Customization

This program can be modified to fit particular needs. You have the freedom to change the code to change how the GUI appears, add new features, or change the integrity check hashing algorithm.
