import requests

def analyze_cookies(url):
    print(f"--- {url} Analiz Ediliyor ---")
    try:
        response = requests.get(url)
        cookies = response.cookies

        if not cookies:
            print("[-] Hiç cookie bulunamadı.")
            return

        for cookie in cookies:
            print(f"\n[+] Cookie İsmi: {cookie.name}")
            # HttpOnly Kontrolü
            if cookie.has_nonstandard_attr('HttpOnly') or cookie.rest.get('HttpOnly'):
                print("    [SAFE] HttpOnly flag mevcut.")
            else:
                print("    [VULN] HttpOnly flag eksik! (XSS riski)")

            # Secure Kontrolü
            if cookie.secure:
                print("    [SAFE] Secure flag mevcut.")
            else:
                print("    [VULN] Secure flag eksik! (MITM riski)")

    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    target_url = input("Analiz edilecek URL'yi girin (örn: https://google.com): ")
    analyze_cookies(target_url)
