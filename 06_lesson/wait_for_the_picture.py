from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

WebDriverWait(driver, 15).until(
    EC.invisibility_of_element_located((By.ID, "spinner"))
)

third_image = driver.find_element(By.ID, "award")

image_src = third_image.get_attribute("src")

print("SRC третьей картинки:", image_src)

driver.quit()