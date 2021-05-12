import os



if __name__ == "__main__":

    cwd = os.getcwd()
    totalFiles = 0
    totalDir = 0

    for base, dirs, files, in os.walk(cwd):
        if ".git" not in base:
            #print("Searching in : ", base)
            for d in dirs:
                totalDir += 1
            for f in files:
                totalFiles += 1

    print('Total Number of Directories', totalDir)
    print('Total number of Files', totalFiles)
