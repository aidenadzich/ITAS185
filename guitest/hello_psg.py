
import PySimpleGUI as sg

layout = [[sg.Text("Hello World!")], [sg.Button("CLOSE")]]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "CLOSE" or event == sg.WIN_CLOSED:
        break

window.close()