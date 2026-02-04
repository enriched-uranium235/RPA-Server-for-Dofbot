# RPA for Dofbot Automatic Control

<span style="color: red; ">This tool is under development. Operation is not guaranteed.</span>

This tool is an RPA server being developed to control Yahboom's Dofbot from an AI agent.

## Operating Environment
- Windows 10
- Windows 11

## How to Use
- Download the source code from Github to your local PC.

```
git clone https://github.com/enriched-uranium235/RPA-Server-for-Dofbot
```

- Create a Python virtual environment with the following command:

```
python -m venv .venv
```

- Enter the virtual environment:

```
.venv\Scripts\activate
```

- Install the dependent libraries listed in requirements.txt into the virtual environment:

```
pip install -r requirements.txt
```

- Access Yahboom's official website (http://www.yahboom.net/study/Dofbot-Pi) and download the control application for your Dofbot. The tool uses the content from YahboomArmEn.zip, which can be found in the PC Software link under Download in the left menu.

- After extracting the downloaded zip file, launch Dofbot.exe inside to confirm that you can connect to the robot arm, then copy 3DS, Video, Dofbot.exe, and config.ini under DofbotAutoControl.

Directory tree after copying necessary files:
```
DofbotAutoControl
  ├ .venv
  ├ 3DS
  ├ operate_recorder
  ├ server
  ├ Video
  ├ .gitignore
  ├ config.ini
  ├ Dofbot.exe
  ├ README.en.md
  ├ README.md
  └ requirements.txt
```

- Double-click Dofbot.exe to launch it, then use the following command in the virtual environment to output and investigate the coordinate information needed for automatic application control:
```
python operate_recorder/record.py
```

- Required coordinate information:
  - Coordinates of the Connect button
  - Coordinates of the Network radio button
  - Coordinates of the Host Address input field
  - Coordinates of the Communication input field
  - Coordinates of the Connect button in the Communication Configuration dialog
  - Coordinates to bring the Dofbot control app to the foreground (needed to bring the control app back to the front when Edge browser is displayed upon successful connection)
  - Coordinates of ControlDofbot1~6

- Enter the necessary information in config.toml:
```
[dofbot]
min_servo1=0
max_servo1=180
min_servo2=0
max_servo2=180
min_servo3=0
max_servo3=180
min_servo4=0
max_servo4=180
min_servo5=0
max_servo5=180
min_servo6=0
max_servo6=180
dofbot_ip="127.0.0.1"
dofbot_port=6000
dofbot_app_connect_button_coodinate=[0, 0]
dofbot_check_network_coodinate=[0, 0]
dofbot_app_ip_input_coodinate=[0, 0]
dofbot_app_port_input_coodinate=[0, 0]
dofbot_app_connect_submit_button_coodinate=[0, 0]
dofbot_app_use_coodinate=[0, 0]
dofbot_app_servo1_scroll_coodinate=[0, 0]
dofbot_app_servo2_scroll_coodinate=[0, 0]
dofbot_app_servo3_scroll_coodinate=[0, 0]
dofbot_app_servo4_scroll_coodinate=[0, 0]
dofbot_app_servo5_scroll_coodinate=[0, 0]
dofbot_app_servo6_scroll_coodinate=[0, 0]
```

  - min_servo1, ... , max_servo6 represent the minimum and maximum values that can be set for each servo angle of the arm. If the arm is placed in a high location such as on top of a bookshelf, it is recommended to fix min_servo1 and max_servo1 to 90 and not move it.
  - dofbot_ip: Enter the IP address of the Dofbot you want to control.
  - dofbot_port: Enter the port number of the Dofbot you want to control.
  - dofbot_app_connect_button_coodinate is required to open the IP address and port number configuration screen of the Dofbot control app that starts automatically after launching the tool.
  - dofbot_check_network_coodinate is the coordinate required to set the IP address and port number after the configuration screen is opened.
  - dofbot_app_ip_input_coodinate is the coordinate required to enter the IP address of the Dofbot to connect to.
  - dofbot_app_port_input_coodinate is the coordinate required to enter the port number of the Dofbot to connect to.
  - dofbot_app_connect_submit_button_coodinate is required to press the Connect button to save the settings after entering the IP address and port number.
  - dofbot_app_use_coodinate: When the connection to Dofbot is successful, the settings dialog will close automatically, but since the Edge browser will be displayed in the foreground, please prepare coordinates other than where the Edge browser is displayed to bring the control app back to the foreground.
  - dofbot_app_servo1_scroll_coodinate ~ dofbot_app_servo6_scroll_coodinate are the coordinates required to control each servo of the Dofbot.

- After completing the config.toml settings, start the server with the following command in the virtual environment:
```
python server/sephiroth/kether/main.py
```

- If the server starts at http://localhost:6001 and the Dofbot control app is in the foreground on your local PC, you can control the robot arm by sending curl commands from other devices on the same network environment or by sending requests from Postman on other devices as follows:

```sh
curl -X POST http://(IP address of the PC running the server):6001/api/v1/controller \
    -H "Content-Type: application/json" \
    -d '{"servo1": 0, "servo2": 0, "servo3": 0, "servo4": 0, "servo5": 0, "servo6": 0}'
```
