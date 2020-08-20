import os

if __name__ == "__main__":
    arr = os.listdir(".")

    for filename in arr:
        if "_" in filename:
            os.rename(filename, filename.replace("_", " "))
            print("Replaced " + filename, " with " + filename.replace("_", " "))
