import sys
import glob
import os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')

#for loop to iterate over each file in directory
for name in glob.glob(pattern):
    #function to return size of file
    size = os.path.getsize(name)
    #function to return simple name of file without directory names
    simpleName = os.path.basename(name)
    #if statement to test that file size is greater than 0
    if size > 0:
        #if file size greater than 0 print the simple file name + file size (basic)
        # print(simplename)
        # print(os.path.getsize(name))

        # Extension to add the file size in brackets on the same line after the filename
        print(simpleName + " (" + str(size) + "B)")

print("\n\n\n\n---------------------------------------------------------------------------------------------------------\n\n\n\n")


# List Extension
# 1) Turn the file names into a list + the file sizes into a separate list
fileNamesList = []
fileLengthList = []
for name in glob.glob(pattern):
    #function to return size of file
    size = os.path.getsize(name)
    #function to return simple name of file without directory names
    if size > 0:
        simpleName = os.path.basename(name)
        fileNamesList.append(simpleName)
        fileLengthList.append(size)
print(fileNamesList)
print(fileLengthList)
# print(len(fileNamesList)) - NO LONGER NEEDED - USED TO TEST LENGTH OF LIST AND CONFIRM FILES SIZES LESS THAN 0 DELETED
# print(len(fileLengthList)) - NO LONGER NEEDED - USED TO TEST LENGTH OF LIST AND CONFIRM FILES SIZES LESS THAN 0 DELETED

print("\n\n\n\n---------------------------------------------------------------------------------------------------------\n\n\n\n")

# Dictionary Extension to convert lists to dictionary
dict = {fileNamesList[element]: fileLengthList[element] for element in range(len(fileNamesList))}

# Printing resultant dictionary
print(dict)