# scraper.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from exercise import Exercise

class Scraper:
    def __init__(self, url, headless=True):
        self.url = url
        self.driver = self.initialize_driver(headless)
    
    def initialize_driver(self, headless):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        if headless:
            chrome_options.add_argument("--headless")  # Run headless for faster execution
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def close_modal(self):
        try:
            wait = WebDriverWait(self.driver, 30)
            close_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div/button'))
            )
            close_button.click()
        except Exception as e:
            print("Error closing modal:", e)
            
    def get_day(self):
        day = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div/div/div[1]/div/div[1]/h2')
        s = " ".join(day.text.split())
        return s
    
    def get_exercises(self):
        exercises = []

        wait = WebDriverWait(self.driver, 30)
        exercise_elements = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'h3')))

        for element in exercise_elements:
            exercise_name = element.text
            exercise = Exercise(name=exercise_name)  # Create a new Exercise object with the name

            parent = element.find_element(By.XPATH, '../..')
            sets = parent.find_elements(By.TAG_NAME, 'li')

            for set_element in sets:
                inputs = set_element.find_elements(By.TAG_NAME, 'input')
                if len(inputs) >= 2:
                    weight = inputs[0].get_attribute('value')
                    reps = inputs[1].get_attribute('placeholder')
                    exercise.add_set(weight=weight, reps=reps)  # Add the set to the current exercise

            exercises.append(exercise)  # Append the fully populated exercise to the list

        return exercises
    

    def scrape(self):
        data = []
        self.driver.get(self.url)
        self.close_modal()
        day = self.get_day()
        exercises = self.get_exercises()
        data = [day, exercises]
        self.driver.quit()
        return data