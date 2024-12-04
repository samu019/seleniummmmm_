from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configura el WebDriver (asegúrate de tener el ChromeDriver o el correspondiente a tu navegador)
driver_path = "C:chromedriver_131.0.6778.87.exe"  # Reemplaza con la ruta de tu WebDriver
driver = webdriver.Chrome(driver_path)

def test_form():
    try:
        # Acceder a la página web
        driver.get("https://polyetch-form.vercel.app/")
        time.sleep(2)

        # Localizar los campos del formulario
        name_field = driver.find_element(By.NAME, "name")
        email_field = driver.find_element(By.NAME, "email")
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        # Completar el formulario
        name_field.clear()
        name_field.send_keys("Prueba Selenium")
        email_field.clear()
        email_field.send_keys("correo@prueba.com")

        # Verificar si el botón de envío está habilitado
        if submit_button.is_enabled():
            print("Formulario listo para enviar.")
            submit_button.click()
        else:
            print("Formulario no está listo.")

        time.sleep(3)  # Esperar para observar el resultado

    finally:
        # Cerrar el navegador
        driver.quit()

# Ejecutar la prueba
test_form()
