#import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import datetime
import enums

class Booking():
    NAME: str
    SURNAME: str
    ADRESS: str
    PLZCITY: str
    STUDENTNUMBER: str
    MAIL: str
    PHONENUMBER: str
    #COURSE_ID: enums.course_id.value
    GENDER: enums.gender
    STATUS: enums.status
    DATA = {
        "NAME": "BS_F1100",
        "SURNAME": "BS_F1200", 
        "ADRESS": "BS_F1300", 
        "PLZCITY": "BS_F1400", 
        "STUDENTNUMBER": "BS_F1700",
        "MAIL": "BS_F2000", 
        "PHONENUMBER": "BS_F2100",
        }

    def __init__(self, NAME, SURNAME, ADRESS, PLZCITY, STUDENTNUMBER, MAIL, PHONENUMBER, GENDER, STATUS, COURSE_ID):
        self.NAME = NAME
        self.SURNAME = SURNAME
        self.ADRESS = ADRESS
        self.PLZCITY = PLZCITY
        self.STUDENTNUMBER = STUDENTNUMBER
        self.MAIL = MAIL
        self.PHONENUMBER = PHONENUMBER
        self.GENDER = GENDER
        self.STATUS = STATUS
        self.COURSE_ID = COURSE_ID
        
    def book(self):
        TOMORROW = datetime.date.today() + datetime.timedelta(days = 1)
        BOOKING_DAY_BUTTON = f"BS_Termin_{TOMORROW.strftime('%Y-%m-%d')}"
        PATH = "C:/chromium/chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        driver.get("https://buchung.hsz.rwth-aachen.de/angebote/aktueller_zeitraum/_Lernraumbuchung.html")
        driver.maximize_window()
        #click on chosen library
        driver.find_element(By.NAME, self.COURSE_ID).click()
        #switch tab
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        #click on chosen day
        try: 
            driver.find_element(By.NAME, BOOKING_DAY_BUTTON).click()
        except NoSuchElementException:
            print("already booked!")
        #%% fill in accessed form
        #choose gender
        driver.find_element_by_xpath("//input[@name='sex' and @value=f'{self.GENDER}']").click()
        #select status
        select = Select(driver.find_element_by_id('BS_F1600'))
        select.select_by_visible_text('StudentIn der RWTH')

        for data in self.DATA:
            input_data = driver.find_element(By.ID, data)
            input_data.send_keys(self.DATA[data])
          
        driver.execute_script("window.scrollBy(0, 300)", "")
        #accept privacy policy    
        button_datenschutz = driver.find_element(By.XPATH, "//input[@name='tnbed' and @value='1']")
        button_datenschutz.click()
        #book
        book = driver.find_element_by_xpath("//input[@class='sub' and @value='weiter zur Buchung']")
        book.submit()

uzhan = Booking("Uzhan", "Kocaman", "", "55555 Aachen", "999999", "uzhan.kocaman@rwth-aachen.de", "999999999999", enums.gender.M.value, enums.status.STUDENT_RWTH.value, enums.course_id.BIB2_0800.value)
uzhan.book()