import FreeSimpleGUI as sg
from zip_creator import make_archive

label1=sg.Text("Select file to compress:")
input1=sg.Input()
choose_button1=sg.FilesBrowse("Choose",key="files")

label2=sg.Text("Select folder to compress:")
input2=sg.Input()
choose_button2=sg.FolderBrowse("Choose",key="folder")

compress_button=sg.Button("compress")
output_label=sg.Text(key="output",text_color="black")

window=sg.Window("File Compress",layout=[[label1],[input1,choose_button1],
                                         [label2],[input2,choose_button2],
                                         [compress_button,output_label]])

while True:
    event,values=window.read()
    print(event)
    print(values)
    Filepath= values["files"].split(",")
    Folder=values["folder"]
    make_archive(Filepath,Folder)
    window["output"].update(value ="compresson completed!")


window.close
