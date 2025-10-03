import zipfile
import pathlib

def extract_archive(ArchivePath,dest_dir):
    with zipfile.ZipFile(ArchivePath,"r") as archive:
        archive.extractall(dest_dir)



if __name__ == "__main__":
    extract_archive("dest\compressed.zip",
                    "practice5\extractfile")