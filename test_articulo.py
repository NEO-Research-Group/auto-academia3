# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestArticulo():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
    # Test name: articulo
    # Step # | name | target | value
    # 1 | open | /Academia3/solicitudes | 
    self.driver.get("https://srv.aneca.es/Academia3/solicitudes")
    # 2 | setWindowSize | 1200x831 | 
    self.driver.set_window_size(1200, 831)
    # 4 | waitForElementPresent | css=#nuevaPublicacionIdxId | 30000
    WebDriverWait(self.driver, 60).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#nuevaPublicacionIdxId")))
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_articulo(self, record, pos):
    # 4 | waitForElementPresent | css=#nuevaPublicacionIdxId | 30000
    WebDriverWait(self.driver, 60).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#nuevaPublicacionIdxId")))
    time.sleep(1)
    # 5 | click | css=#nuevaPublicacionIdxId > label | 
    self.driver.find_element(By.CSS_SELECTOR, "#nuevaPublicacionIdxId > label").click()

    WebDriverWait(self.driver, 60).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#autoresFilter")))
    time.sleep(1)
    for author in record['author']:
      # 6 | type | id=autoresFilter | Chrisitan
      self.driver.find_element(By.ID, "autoresFilter").send_keys(author)
      # 7 | sendKeys | id=autoresFilter | ${KEY_ENTER}
      self.driver.find_element(By.ID, "autoresFilter").send_keys(Keys.ENTER)


    self.driver.find_element(By.ID, "posicionSolicitanteTextId").send_keys(str(pos))
    #time.sleep(1)
    # 13 | type | css=#claveLabelid + div input | Artículo
    self.driver.find_element(By.CSS_SELECTOR, "#claveLabelid + div input").send_keys("Artículo")
    time.sleep(1)
    # 14 | sendKeys | css=#claveLabelid + div input | ${KEY_ENTER}
    self.driver.find_element(By.CSS_SELECTOR, "#claveLabelid + div input").send_keys(Keys.ENTER)
    time.sleep(1)
    # 15 | type | id=tituloTextId | Hola
    self.driver.find_element(By.ID, "tituloTextId").send_keys(record['title'])
    #time.sleep(1)
    # 16 | type | id=nombreRevistaTextId | Expoert
    self.driver.find_element(By.ID, "nombreRevistaTextId").send_keys(record['journal'])
    #time.sleep(1)
    # 17 | type | id=volumenTextId | 161
    self.driver.find_element(By.ID, "volumenTextId").send_keys(record['volume'])
    #time.sleep(1)
    # 18 | type | id=annioPublicacionTextId | 2020
    self.driver.find_element(By.ID, "annioPublicacionTextId").send_keys(record['year'])
    #time.sleep(1)
    # 19 | click | id=saveBtn | 
    self.driver.find_element(By.ID, "saveBtn").click()
    time.sleep(3)
  
