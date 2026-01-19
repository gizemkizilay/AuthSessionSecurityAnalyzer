# src/test_main.py
import requests

def test_connection():
    try:
        response = requests.get("https://www.google.com")
        if response.status_code == 200:
            print("[TEST PASSED] Internet baglantisi ve requests calisiyor.")
        else:
            print("[TEST FAILED] Siteye ulasilamadi.")
    except Exception as e:
        print(f"[TEST ERROR] Hata: {e}")

if __name__ == "__main__":
    test_connection()
