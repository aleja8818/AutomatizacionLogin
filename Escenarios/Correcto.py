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
    contrasena = controlador.find_element(By.NAME, "password")

    time.sleep(3)

    nombre_usuario.send_keys("Admin") 
    time.sleep(3)
    contrasena.send_keys("admin123")  

    time.sleep(3)

    boton_login = controlador.find_element(By.XPATH, "//button[@type='submit']")
    boton_login.click()

    time.sleep(3)

    WebDriverWait(controlador, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Admin']"))
    )
    print("Inicio de sesión exitoso, estamos en el Dashboard")
    
    menu_admin = controlador.find_element(By.XPATH, "//span[text()='Admin']")
    menu_admin.click()
    print("Acceso a la opción Admin exitoso.")

    print("La página se mantendrá abierta en la opción Admin.")

    time.sleep(8) 

except Exception as e:
    print("Ocurrió un error:", e)

