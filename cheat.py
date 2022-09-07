from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

URL = "https://flippybitandtheattackofthehexadecimalsfrombase16.com"
DRIVER_PATH = '/snap/bin/chromium.chromedriver'


def main():
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get(URL)
    time.sleep(5)

    action = ActionChains(driver)
    action.send_keys(Keys.SPACE).perform()
    WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.ID, 'enemy-1')))
    time.sleep(2)
    
    for i in range(1, 1000):    
        hexNumber = getHexEnemy(i, driver)
        answer = str(bin(int(hexNumber, 16)))[2:]
        placement = 8
        for index in reversed(range(0, len(answer))):
            placement -= 1
            print(answer[index], index)
            pressBit(placement, answer, index, action)

        print("this is Hex:{} this is binary: {}".format(hexNumber, answer))


def pressBit(place, answer, index, action):
    match place:
            case 0:
                pressButton(answer[index],'1', action)
            case 1:
                pressButton(answer[index],'2', action)
            case 2:
                pressButton(answer[index],'3', action)
            case 3:
                pressButton(answer[index],'4', action)
            case 4:
                pressButton(answer[index],'5', action)
            case 5:
                pressButton(answer[index],'6', action)
            case 6:
                pressButton(answer[index],'7', action)
            case 7:
                pressButton(answer[index],'8', action)
            case _:
                pass


def getHexEnemy(i, driver):
    enemyClassName = 'enemy-{}'.format(i)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, enemyClassName)))
    return driver.find_element(By.ID,enemyClassName).text


def pressButton(bit, number, action):
    if bit == '1':
        action.send_keys(number).perform()



if __name__ == '__main__':
    main()