import subprocess
import os
from binah.config import Config

import pyautogui as pag

def start_dofbot(config: Config) -> None:
    """
    Starts the Dofbot.exe application located in the same directory tree as this script.
    """
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to Dofbot.exe
    dofbot_path = os.path.join(current_dir, "../../../", "Dofbot.exe")
    
    # Check if the file exists
    if not os.path.isfile(dofbot_path):
        raise FileNotFoundError(f"Dofbot.exe not found at {dofbot_path}")
    
    # Start the application
    try:
        subprocess.Popen([dofbot_path], shell=True)
        print(f"Dofbot.exe started successfully from {dofbot_path}")

        # wait 5 seconds for the app to open
        pag.sleep(5)

        connect_coodinate = config.dofbot_app_connect_button_coodinate
        pag.moveTo(connect_coodinate[0], connect_coodinate[1])
        pag.click()
        print("Clicked on the connect button.")

        check_network_coodinate = config.dofbot_check_network_coodinate
        pag.moveTo(check_network_coodinate[0], check_network_coodinate[1])
        pag.click()
        print("Clicked on the check network button.")

        ip_input_coodinate = config.dofbot_app_ip_input_coodinate
        pag.moveTo(ip_input_coodinate[0], ip_input_coodinate[1])
        pag.click()
        for _ in range(15):
            pag.press('right')
        for _ in range(15):
            pag.press('backspace')
        pag.write(config.dofbot_ip, interval=0.1)
        print(f"Entered IP address: {config.dofbot_ip}")

        port_input_coodinate = config.dofbot_app_port_input_coodinate
        pag.moveTo(port_input_coodinate[0], port_input_coodinate[1])
        pag.click()
        for _ in range(5):
            pag.press('right')
        for _ in range(5):
            pag.press('backspace')
        pag.write(str(config.dofbot_port), interval=0.1)
        print(f"Entered port: {config.dofbot_port}")

        connect_submit_coodinate = config.dofbot_app_connect_submit_button_coodinate
        pag.moveTo(connect_submit_coodinate[0], connect_submit_coodinate[1])
        pag.click()
        print("Clicked on the connect submit button.")

        use_coodinate = config.dofbot_app_use_coodinate
        pag.moveTo(use_coodinate[0], use_coodinate[1])
        pag.click()
        print("Clicked on the use button.")
    except Exception as e:
        print(f"Failed to start Dofbot.exe: {e}")