from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from exercise import Exercise

class Scraper:
    XPATH_CLOSE_MODAL = '/html/body/div[2]/div/div/div/div[2]/div/div/div/button'
    XPATH_DAY = '/html/body/div[1]/div/div/main/div/div/div/div[1]/div/div[1]/h2'
    PARENT_XPATH = '../..'
    TAG_NAME_EXERCISE = 'h3'
    TAG_NAME_LIST_ITEM = 'li'
    
    def __init__(self, url, headless=True):
        self.url = url
        self.driver = self._initialize_driver(headless)
    
    def _initialize_driver(self, headless):
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def _close_modal(self):
        try:
            wait = WebDriverWait(self.driver, 30)
            close_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.XPATH_CLOSE_MODAL)))
            close_button.click()
        except Exception as e:
            print(f"Error closing modal: {e}")
            
    def _get_day(self):
        day_element = self.driver.find_element(By.XPATH, self.XPATH_DAY)
        return " ".join(day_element.text.split())
    
    def _get_exercises(self):
        exercises = []
        wait = WebDriverWait(self.driver, 30)
        exercise_elements = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, self.TAG_NAME_EXERCISE)))

        for element in exercise_elements:
            exercise_name = element.text
            exercise = Exercise(name=exercise_name)

            parent = element.find_element(By.XPATH, self.PARENT_XPATH)
            sets = parent.find_elements(By.TAG_NAME, self.TAG_NAME_LIST_ITEM)

            for set_element in sets:
                inputs = set_element.find_elements(By.TAG_NAME, 'input')
                if len(inputs) >= 2:
                    weight = inputs[0].get_attribute('value')
                    reps = inputs[1].get_attribute('placeholder')
                    exercise.add_set(weight=weight, reps=reps)

            exercises.append(exercise)
        return exercises

    def scrape(self):
        self.driver.get(self.url)
        self._close_modal()
        day = self._get_day()
        exercises = self._get_exercises()
        self.driver.quit()
        return day, exercises
