import argparse
parser = argparse.ArgumentParser(description='A program that takes an input file, and writes it to either the console or a to an output file')

if __name__ == '__main__':
    parser.add_argument('inputFile', help='Name of input file (including file-extension). Must be in the exact same directory as this file.')
    parser.add_argument('--o','--outputFile', help='Name of the output file.')
    args = parser.parse_args()

    
    with open(args.inputFile,'r') as file_object:
        inputFileText = file_object.read()

    if args.outputFile:
        with open(args.outputFile, 'w') as file_object:
            file_object.write(inputFileText)

    else:
        print(inputFileText)