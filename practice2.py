import FreeSimpleGUI as sg

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input()

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input()

button = sg.Button("Convert")

window = sg.Window("Convertor",
                   layout=[[feet_label],[feet_input],
                           [inches_label],[inches_input],
                           [button]])

event, values = window.read()
if event == "Convert":
    try:
        feet = float(values[0])      # get feet input
        inches = float(values[1])    # get inches input
        total_inches = feet * 12 + inches
        print(f"{feet} feet and {inches} inches = {total_inches} inches")
    except ValueError:
        print("Please enter valid numbers!")

window.close()
