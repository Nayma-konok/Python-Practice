import FreeSimpleGUI as sg

label1=sg.Text("Email Address:")
input1=sg.Input()

label2=sg.Text("Password:")
input2=sg.Input()

button = sg.Button("Enter")

window=sg.Window("LogIn",layout=[[label1,input1],
                          [label2,input2],
                          [button]])


window.read()
window.close