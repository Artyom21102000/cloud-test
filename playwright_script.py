from playwright.sync_api import sync_playwright

def run_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # Открываем веб-страницу
        page.goto("https://example.com")
        
        # Проверяем, что заголовок страницы содержит слово "Example"
        assert "Example" in page.title()
        
        # Находим элемент по CSS-селектору, содержащему текст "More information" и кликаем по нему
        page.locator("text=More information").click()
        
        # Проверяем, что по клику произошло перенаправление на страницу с URL "https://www.iana.org/help/example-domains"
        assert page.url == "https://www.iana.org/help/example-domains"
        
        browser.close()

if __name__ == "__main__":
    run_playwright()
