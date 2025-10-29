
def setup_driver(): 
    """Configura y devuelve una instancia del WebDriver de Chrome.""" 
    from selenium import webdriver 
    
    driver = webdriver.Chrome() 
     
    return driver 



def loguin(username=None, password=None):
    """Realiza el proceso de login en la página de saucedemo.com."""
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    try:
        driver = setup_driver()
        driver.get("https://www.saucedemo.com/")

        #se espera que el formulario de login sea visible
        input_username = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )

        #se escriben credenciales válidas
        input_username.send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        

        #se hace click en el botón de login
        driver.find_element(By.ID, "login-button").click()

        #verifica que la URL sea la esperada después del login
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://www.saucedemo.com/inventory.html")
        )

        return driver
        #assert "inventory.html" in driver.current_url, "error! no se la redirección a la página de inventario falló"

    except Exception as e:
        print(f"falló la prueba: {e}")
        raise


