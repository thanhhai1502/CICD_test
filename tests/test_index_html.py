from playwright.sync_api import sync_playwright, expect

def test_open_index_html():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Headless cho CI
        page = browser.new_page()
        
        # # Mở file index.html cục bộ
        # page.goto("file:///F:/python_playwright/vscode/CICD_test/cubeit/index.html")
        page.goto("http://127.0.0.1:8000/")

        # Kiểm tra tiêu đề (giả sử index.html có <h1>)
        title = page.locator("h1")
        expect(title).to_have_text("Chào mừng đến với trang CI Test!")
        
        # Kiểm tra đoạn văn (giả sử có <p>)
        paragraph = page.locator("p")
        expect(paragraph).to_have_text("Đây là một trang đơn giản để kiểm tra pipeline CI.")
        
        # Đóng trình duyệt
        browser.close()

if __name__ == "__main__":
    test_open_index_html()