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

#empty lists to be constructed from run of for loop
fileNamesList = []
fileLengthList = []

#for loop to iterate over each file in directory
for name in glob.glob(pattern):
    #function to return size of file
    size = os.path.getsize(name)
    #function to return simple name of file without directory names
    simpleName = os.path.basename(name)
    #if statement to test that file size is greater than 0
    if size > 0:
        #if file size greater than 0 print the simple file name + file size
        simpleName = os.path.basename(name)
        fileNamesList.append(simpleName)
        fileLengthList.append(size)
        print(simpleName + " (" + str(size) + "B)")

print("\n")

print(fileNamesList)
print(fileLengthList)

print("\n")
# Convert lists to dictionary
dict = {fileNamesList[element]: fileLengthList[element] for element in range(len(fileNamesList))}

# Printing resultant dictionary
print(dict)
