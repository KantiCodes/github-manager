import PySimpleGUI as sg
from app import github_api

if __name__ == '__main__':
    sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('This is a simple tool to add a person with specific username to specific team')],
              [sg.Text('Enter github user'), sg.InputText(default_text='github_api username'), sg.Button('save user')],
              [sg.Text('Enter the team name'), sg.InputText     (default_text='github_team'), sg.Button('save team')],
              [sg.Button('Ok'), sg.Button('cancel')]]

    # Create the Window
    window = sg.Window('Github team controller', layout)
    user_id, team_id = None, None
    # Event Loop to process "events" and get the "values" of the inputs
    while True:

        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'cancel':  # if user closes window or clicks cancel
            break
        if event == 'Ok':
            print('You entered ', values[0])

            if user_id and team_id:
                sg.popup(github_api.invite_user(user_id, [team_id, ]))

            else:
                sg.popup('provide correct username and team name')

        if event == 'save user':
            user_id = github_api.get_user_id(values[0])
            if user_id:
                sg.popup(f"id : {user_id}")
            else:
                sg.popup('incorrect github username')
        if event == 'save team':
            #print(f"this is the name of the team: {values[1]}")
            team_id = github_api.get_team_id(values[1])
            sg.popup(f"id : {team_id}")
            print(team_id)

    window.close()
