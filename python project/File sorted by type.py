import os
import shutil
folder=input("Enter a folder path:")
pdf_folder= os.path.join(folder,"PDFs")
image_folder=os.path.join(folder,"Image")
text_folder=os.path.join(folder,"Textfile")
other_folder=os.path.join(folder,"others")
os.makedirs(pdf_folder,exist_ok=True)
os.makedirs(image_folder,exist_ok=True)
os.makedirs(text_folder,exist_ok=True)
os.makedirs(other_folder,exist_ok=True)
for file in os.listdir(folder):
    file_path=os.path.join(folder,file)
    if os.path.isdir(file_path):
        continue
    extension=os.path.spiltext(file)[1].lower()
    if extension==".pdf":
        shutil.move(file_path,pdf_folder)
    elif extension==[".jpg",".jpeg",".png"]:
        shutil.move(file.path,image_folder)
    elif extension==".txt":
        shutil.move(file_path,text_folder)
    else:
        shutil.move(file_path,other_folder)
print("Files sorted successfully")