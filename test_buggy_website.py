from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Usamos WebDriverManager para instalar el ChromeDriver y obtener el path correcto
service = Service(ChromeDriverManager().install())

# Inicializamos el driver pasando el objeto Service
driver = webdriver.Chrome(service=service)

# Abre la página
driver.get("https://buggy.justtestit.org/")

# Espera explícita para que el campo de usuario sea visible antes de interactuar
wait = WebDriverWait(driver, 10)  # Espera hasta 10 segundos
username_field = wait.until(EC.visibility_of_element_located((By.ID, "user")))

# Encuentra los campos de usuario y contraseña y el botón de login
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

# Completa los campos con credenciales de prueba
username_field.send_keys("testuser")
password_field.send_keys("testpassword")
login_button.click()

# Espera un poco para que el login se procese
time.sleep(3)

# Verifica si el login fue exitoso (por ejemplo, buscando un mensaje de bienvenida)
welcome_message = driver.find_element(By.XPATH, "//h1[text()='Welcome']")
assert welcome_message.is_displayed(), "El login no fue exitoso"

# Toma una captura de pantalla como reporte
driver.save_screenshot("screenshot_login_success.png")

# Cierra el navegador después de la prueba
driver.quit()
