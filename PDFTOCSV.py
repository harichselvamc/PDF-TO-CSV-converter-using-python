import csv
import PyPDF2

# Open the PDF file in read-binary mode
pdf_file = open('example.pdf', 'rb') # name of the PDF file with .pdf extension

# Create a PDF reader object
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# Get the first page of the PDF
page = pdf_reader.getPage(0)

# Extract the text from the page
text = page.extractText()

# Split the text into lines
lines = text.split('\n')

# Create a CSV file in write mode
csv_file = open('example.csv', 'w', newline='')

# Create a CSV writer object
csv_writer = csv.writer(csv_file)

# Write the lines to the CSV file
for line in lines:
    # Split the line into columns based on whitespace
    columns = line.split()
    # Write the columns to the CSV file
    csv_writer.writerow(columns)

# Close the PDF file and the CSV file
pdf_file.close()
csv_file.close()
