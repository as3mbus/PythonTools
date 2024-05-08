import csv;
import os;
import pandas as pd;

# current working directory
current_dir = os.getcwd()

# relative path to the directory
relative_path = "Input"

# combine current working directory with relative path
directory = os.path.join(current_dir, relative_path)

print(directory)

# get a list of all files in the directory
files = os.listdir(directory)

print(files)

combined_csv = pd.DataFrame()

# loop through the list and print the file names
for file in files:
    print(directory+file)
    # with open(os.path.join(directory,file), newline='') as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         print(row)


    # with open(directory+file, 'w', newline='') as finalFile:
        # print(finalFile)

    df = pd.read_csv(os.path.join(directory,file))
    # append to combined_csv
    combined_csv = combined_csv.append(df)

# write combined data to new csv file
combined_csv.to_csv('1_combined_csv.csv', index=False)

# cleanDf = combined_csv[["Technology Name / Topics","Description","Tags","Project Leads / Owner", "🏑 Quest"]]

# cleanDf = combined_csv.drop_duplicates()

# if you want to merge duplicate entries with specific column, you can use

cleanDf = combined_csv.groupby(['Technology Name / Topics']).sum()
cleanDf = cleanDf.reset_index()

# write the cleaned data to a new csv file
cleanDf.to_csv('2_cleaned_file.csv', index=False)


# with open('output.csv', 'w', newline='') as finalFile:
    # writer = csv.writer(finalFile)
    # writer.writerow("Stuff")