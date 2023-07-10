# Python 3 code to rename multiple
# files in a directory or folder

# importing os module
import os


# Function to rename multiple files
def main():
    folder = "/home/anirudh.chawla/Downloads/FaceRecognition-GUI-APP (1)/FaceRecognition-GUI-APP/data/anirudh"
    for i in range(0,len(os.listdir(folder))):
        print(f"count {i}")
        print(f"count {os.listdir(folder)[i]}")
        dst = f"{str(i)}anirudh.jpg"
        src = f"{folder}/{os.listdir(folder)[i]}"  # foldername/filename, if .py file is outside folder
        dst = f"{folder}/{dst}"

        # rename() function will
        # rename all the files
        print(f"source {src}")
        print(f"dest {dst}")
        os.rename(src, dst)


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
