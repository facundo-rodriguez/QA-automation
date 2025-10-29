from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .utils import *

def test_login():
    
    try:

        driver=loguin()
        assert "inventory.html" in driver.current_url, "error! no se redireccionó a la página de inventario falló"
        
        title=driver.title
        print("title:", title)
        assert title=="Swag Labs", "error! el título de la página es incorrecto"

    except Exception as e:
        print(f"falló la prueba: {e}")
        raise
    
    finally:
        print("test loguin finalizado")    
        driver.quit()


    

def test_find_elements():
    
    try:
        driver=loguin()

        #se espera que los  los productos en la página de inventario esten visibles
        products = WebDriverWait(driver, 10).until(
            #EC.visibility_of_element_located((By.CSS_SELECTOR, ".inventory_list"))#inventory_item
            EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
        )

        #se buscan los productos en la página de inventario
        #products = driver.find_elements(By.CLASS_NAME, "inventory_item")
       
        assert len(products) >0, f"error! no hay productos"
        print( products[0].text )

        menu=driver.find_elements(By.ID, "react-burger-menu-btn")
        assert len(menu) >0, f"error! no hay menú"

        filter=driver.find_elements(By.CLASS_NAME, "product_sort_container")
        assert len(filter) >0, f"error! no hay filtro"

        carrito=driver.find_elements(By.CLASS_NAME, "shopping_cart_link")
        assert len(carrito) >0, f"error! no hay carrito"
    
    finally:
        print("test find_elements finalizado")    
        driver.quit()


def test_carrito():
  
    try:
        
        driver=loguin()
        
        # Obtener el nombre del primer producto para validarlo después
        product= driver.find_element(By.CLASS_NAME, "inventory_item_name")
        product_name = product.text
        print(f"Producto seleccionado: {product_name}")
        
        # Añadir el primer producto al carrito
        add_product = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")#driver.find_element(By.XPATH, "//button[contains(@data-test, 'add-to-cart')]")
        add_product.click()
        
        # Verificar que el contador del carrito se incremente
        badge = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        assert int(badge.text) >= 1, f"El contador del carrito es {badge.text}"
        print("Producto añadido al carrito")
        
        # Navegar al carrito
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        # espera que la URL actual del navegador contenga el texto "cart.html"
        WebDriverWait(driver, 10).until(
            EC.url_contains("cart.html")
        )
        
        # Verificar que esté el producto añadido y que sea el mismo que añadimos
        items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(items) == 1, f"Debería haber 1 producto en el carrito, pero hay {len(items)}"
        
        
        item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        assert item_name == product_name, f"El producto en el carrito ({item_name}) no coincide con el añadido ({product_name})"
        
    except Exception as e:
        print(f"falló la prueba: {e}")
        raise
    
    finally:
        print("test carrito finalizado")    
        driver.quit()