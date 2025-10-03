import FreeSimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("LightGreen")

label1=sg.Text("Select Archive")
input1=sg.Input()
choose_button1=sg.FileBrowse("Choose",key="archive")


label2=sg.Text("Select Dest_dir")
input2=sg.Input()
choose_button2=sg.FolderBrowse("Choose",key="folder")

extract_button=sg.Button("Extract")
output_label=sg.Text(key="output",text_color="Green")

window=sg.Window("Archive Extracror",layout=[[label1,input1,choose_button1],
                                             [label2,input2,choose_button2],
                                             [extract_button,output_label]])
while True:
    event,values=window.read()
    print(event, values)
    ArchivePath= values["archive"]
    dest_dir= values["folder"]
    extract_archive(ArchivePath,dest_dir)
    window["output"].update(value ="Extraction Completed!")


window.close()