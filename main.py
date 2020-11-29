import os
import shutil


def create_dir(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)

def move(folder,file):
    shutil.move(f'{os.getcwd()}/{file}',f'{folder}/{file}')

files = os.listdir()
print(files)

images = ['.png','.jpg','.jpeg']
docs = ['.ppt','.pdf','.txt','.csv']


for file in files:
    if (os.path.splitext(file)[1]).lower() in images:
        move('Images',file)

    elif (os.path.splitext(file)[1]).lower() in docs:
        move('Documents',file)
    
    elif os.path.isfile(file):
        move('Others',file)


if __name__ == "__main__":
    
    create_dir('Images')
    create_dir('Documents')
    create_dir('Others')