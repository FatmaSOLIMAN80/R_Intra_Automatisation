from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialiser le webdriver
driver = webdriver.Chrome()

#Aggrandir la fenêtre
driver.maximize_window()

# Initialiser le webdriver
driver.get("https://videotron.com/")

# Utilisation de explicity wait
wait = WebDriverWait(driver,10)

#localiser les images
localisation_image=wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))

# 2- Trouver le nombre d'images sur tout le site
images = driver.find_elements(By.TAG_NAME,"img")
print("Nombre d’images sur le site: ", len(images))

# 3- Afficher la valeur de l’attribut « alt » des images du site
for image in images:
    print(image.get_attribute('alt'))

# 4- Trouver le nombre de liens sur tout le site
liens = driver.find_elements(By.TAG_NAME,"a")
print("Nombre de liens sur le site: ", len(liens))

# 5- Trouver le nombre de liens dans la section « footer » du site
footer = driver.find_element(By.TAG_NAME,"footer")
footer_liens = footer.find_elements(By.TAG_NAME,"a")
print("Nombre de liens dans le footer: ", len(footer_liens)) #//footer//a

# 6- Récupérer la valeur de l’attribut « href » de chaque lien dans le footer et les mettre dans une liste
footer_hrefs = []
for lien in footer_liens:
    href = lien.get_attribute("href")
    footer_hrefs.append(href)
    print("l’attribut « href » de chaque lien dans le footer: ", href)

#affihcer le nombre de hrefs
print("Nombre de 'href' dans le footer: ", len(footer_hrefs))

#Fermer le navigateur
driver.quit()
