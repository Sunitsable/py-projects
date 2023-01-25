import pyautogui
pyautogui.alert('Just a notification', "Title")  # always returns "OK"
pyautogui.confirm('Asks OK or Cancel')  # returns "OK" or "Cancel"
pyautogui.prompt('Asks for a string from user')  # returns string or None
pyautogui.password('Enter password')  # returns string or None
