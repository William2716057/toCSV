import csv

def CSVconvert(input, output):
    # Open input file to read
    with open(input, 'r') as f:
        # Read each line
        lines = f.readlines()

    # Write each word as a separate row in the CSV
    data = [[word.strip()] for line in lines for word in line.split()]

    # Write to CSV
    with open(output, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write each row
        writer.writerows(data)

inputFile = 'input.txt'
outputFile = 'output.csv'
CSVconvert(inputFile, outputFile)