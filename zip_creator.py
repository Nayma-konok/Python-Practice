import zipfile
import pathlib

def make_archive(Filepath,dest_dir):  #destination directory
    dest_path=pathlib.Path(dest_dir ,"compressed.zip")
    with zipfile.ZipFile(dest_path,"w") as archive:
        for file in Filepath:
            file=pathlib.Path(file)
            archive.write(file,arcname=file.name)



if __name__ == "__main__":
    make_archive(Filepath=["set.py","function.py"],dest_dir="dest")