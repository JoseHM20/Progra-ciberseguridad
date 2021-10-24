import pyautogui
import time

# Participante:
# Jose Luis Hernandez Meza

def Form():
    # Answer question 1
    heroes = input("Marvel or DC")
    if heroes == "Marvel":
        pyautogui.moveTo(750, 430)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
    elif heroes == "DC":
        pyautogui.moveTo(750, 455)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
    else:
        print("I select both heroes")
        pyautogui.moveTo(750, 485)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
    
    # Answer question
    pyautogui.moveTo(750, 620)
    time.sleep(1)
    pyautogui.click()
    phrase = input("Write the phrase to be used: ")
    time.sleep(1)
    pyautogui.write(phrase, interval = 0.2)
    
    # Answer question 3
    pyautogui.moveTo(750, 715)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

    hour = input("Time to eat cake (10, 11, 12...): ")
    if hour == "9":
        pyautogui.moveTo(750, 760)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
    elif hour == "10":
        pyautogui.moveTo(750, 800)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
    elif hour == "11":
        pyautogui.moveTo(750, 815)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
    elif hour == "11":
        pyautogui.moveTo(750, 830)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
    elif hour == "12":
        pyautogui.moveTo(750, 845)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
    else:
        print("This time is not yet loaded in the script.")

    # Answer question 4
    pyautogui.moveTo(750, 800)
    time.sleep(1)
    mail = input("Write a fake email: ")
    pyautogui.click()
    pyautogui.write(mail, interval = 0.2)
    
    confirm = input("Write 'y' to confirm your answers: ")

    if confirm == "y":
        print("Sending answers...")
        time.sleep(2)
        # Send form
        pyautogui.moveTo(750, 870)
        time.sleep(1)
        pyautogui.click()
    else:
        print("You have not selected any answer, so it will be taken as confirmation.")

if __name__ == "__main__":
    # Running Google Chrome
    pyautogui.hotkey("win", "r")
    time.sleep(2)
    pyautogui.write('chrome.exe "https://forms.office.com/pages/responsepage.aspx?id=EZDKymp73kSGHwlaLKiDt4wXC_YfIWlGrUcWrbkA4-NUOVNHMk5FT1k3VVJRRVpKUVlJSElIVE02TC4u"', interval = 0.2)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(5)

    # Executing first form
    Form()

    # Send another form
    other = input("Do you want to send another form? (y/n): ")

    if other == "y":
        pyautogui.moveTo(750, 460)
        time.sleep(1)
        Form()
    elif other == "n":
        print("Closing process...")
        exit()
    else:
        print("No valid answer was selected")
        exit()