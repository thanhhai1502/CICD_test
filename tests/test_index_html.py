from playwright.sync_api import sync_playwright, expect

def test_index_html():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Headless để chạy trên CI
        page = browser.new_page()
        
        # Mở file index.html (dùng file:// protocol để truy cập file cục bộ)
        page.goto("CICD_test\cubeit\index.html")
        
        # Kiểm tra tiêu đề
        title = page.locator("h1")
        expect(title).to_have_text("Chào mừng đến với trang CI Test!")
        
        # Kiểm tra đoạn văn
        paragraph = page.locator("p")
        expect(paragraph).to_have_text("Đây là một trang đơn giản để kiểm tra pipeline CI.")
        
        # Đóng trình duyệt
        browser.close()

if __name__ == "__main__":
    test_index_html()