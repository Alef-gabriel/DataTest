import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shell import unzip

DOWNLOAD_URL = "https://receita.economia.gov.br/orientacao/tributaria/cadastros/cadastro-nacional-de-pessoas-juridicas-cnpj/dados-publicos-cnpj"
download_dir =  "D:\\zips"
driver_path = "./exe/chromedriver.exe"

def enable_download(driver):
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    driver.execute("send_command", params)

def setting_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    return chrome_options;

def isFileDownloaded(path):
    file_path = download_dir+path
    while not os.path.exists(file_path):
        time.sleep(1)
    if os.path.isfile(file_path):
        print("File Downloaded successfully..")


driver = webdriver.Chrome(executable_path=driver_path,options=setting_chrome_options())
enable_download(driver)
driver.get(DOWNLOAD_URL)
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div/div[3]/div[1]/div/div[5]/div/p[3]/a").click()
isFileDownloaded("\DADOS_ABERTOS_CNPJ_01.zip")
driver.get(DOWNLOAD_URL)
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div/div[3]/div[1]/div/div[5]/div/p[4]/a/span").click()
isFileDownloaded("\DADOS_ABERTOS_CNPJ_02.zip")
unzip("D:/zips", "D:/")

