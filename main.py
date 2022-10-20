from os import error
from socket import htonl
from nbformat import write
from requests import head
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pyautogui as pg

#Agar bisa berjalan, gunakan chrome profile yg sudah verifikasi kode unik/terdaftar
#atau chrome profile yg biasa bisa untuk buka nadine

#ISI DULU , cek dengan ketik di browser chrome://version
#userdir : Profile Path tapi tanpa /Profile di paling belakang
#profile : isi Profile berapa yg paling belakang misal Profile 1
# Download chrome driver sesuai OS dan versi Chrome :https://chromedriver.chromium.org/downloads



opsi = Options()
opsi.headless = False
path = ''  #isi lokasi chromedriver
userdir = ''  #isi lokasi userdir
profile = "Profile 1"  # isi sesuai Profil
opsi.add_argument(f"--user-data-dir={userdir}")
opsi.add_argument(f'--profile-directory={profile}')
driver = webdriver.Chrome(path, options=opsi)
driver.get("https://office.kemenkeu.go.id/")
driver.find_element_by_xpath(
  '//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li/a').click()
time.sleep(2)
driver.find_element_by_xpath('//button[@class="login100-form-btn"]').click()
n = 1000  # berapa kali 15xn ND, tiap 15 nd di refresh agar muncul
for i in range(0, n):
  driver.get("https://office.kemenkeu.go.id/nadine/mejaku")
  time.sleep(1)
  for item in range(1, 16):
    ac = ActionChains(driver)
    nd = '//div[@class="nd-list-item"][1]'
    wait = WebDriverWait(driver, 10)
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.XPATH, nd)))
    el = driver.find_element_by_xpath(nd).click()
    time.sleep(1)
    arsip = '//button[@class="mat-focus-indicator js-test-arsipkan-button mat-raised-button mat-button-base mat-accent ng-star-inserted"][1]'
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, arsip)))
    driver.find_element_by_xpath(arsip).click()
    driver.find_element_by_xpath(
      '//input[@placeholder="Alasan Mengarsipkan"]').send_keys('Arsipkan')
    time.sleep(1)
    arsipkan = '//button[@tabindex="2"]'
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, arsipkan)))
    driver.find_element_by_xpath(arsipkan).click()
