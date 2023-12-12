from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from tools import open_json_by_path


def create_chromium_driver():
  # main.py, line 6-16
  options = Options()
  options.add_argument("--headless")
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-gpu")
  options.add_argument("--window-size=1920x1080")

  driver = webdriver.Chrome(options=options)


  return driver



def get_available_filters(driver, base_url, filter_div_id):
  driver.get(base_url)
  filter_div = driver.find_element(By.ID, filter_div_id)
  list_items = filter_div.find_elements(By.TAG_NAME, 'li')
  links = [item.find_element(By.TAG_NAME, 'a') for item in list_items]
  filters = {link.text: link.get_attribute('href') for link in links}
  return filters



def apply_filter(driver, filter_url):
  driver.get(filter_url)
  # Potentially further actions can be taken on the filtered page


if __name__ == "__main__":
  base_url = "https://www.normattiva.it/"
  anno = open_json_by_path(
      "indice/anno.json")  # This should return a dictionary
  driver = create_chromium_driver()

  # Let's assume the value we're appending to the base URL is from a key 'year' in the dictionary
  year_url = base_url+anno['2023']

  available_filters = get_available_filters(driver, year_url,
                                            'collapseEmettitore')
  
  # Now you can interact with the CLI or otherwise to select and apply a filter
  print(type(available_filters))
  driver.quit()
