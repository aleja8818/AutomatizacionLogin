from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

servicio = Service(ChromeDriverManager().install())  
controlador = webdriver.Chrome(service=servicio)

try:
    controlador.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    controlador.maximize_window()
    time.sleep(3)

    nombre_usuario = controlador.find_element(By.NAME, "username")
    contraseña = controlador.find_element(By.NAME, "password")

    time.sleep(3)

    nombre_usuario.send_keys("NoAdmin")  
    time.sleep(3)
    contraseña.send_keys("000000")
    
    time.sleep(3)  

    boton_login = controlador.find_element(By.XPATH, "//button[@type='submit']")
    boton_login.click()

    time.sleep(3)

    mensaje_error = WebDriverWait(controlador, 3).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='oxd-text oxd-text--p oxd-input-field-error-message']")))
    
    
    print("Mensaje de error capturado:", mensaje_error.text)

except Exception as e:
    print("Ocurrió un error:", e)
finally:
    print("El navegador se mantendrá abierto.")