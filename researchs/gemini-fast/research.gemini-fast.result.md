# Teknik Araştırma Raporu: Auth Session Security Analyzer

## 1. Temel Çalışma Prensipleri
Auth Session Security Analyzer, bir uygulamanın kimlik doğrulama sonrası oluşturduğu oturum (session) mekanizmasının güvenliğini denetleyen bir sistemdir.

* **Oturum Yaşam Döngüsü İzleme:** Kullanıcı giriş yaptığı anda benzersiz bir Session ID (SID) veya JWT oluşturulur. Sistem, bu anahtarın ne kadar süre aktif kaldığını ve sunucu tarafında nasıl sonlandırıldığını denetler.
* **Bağlamsal Doğrulama (Contextual Validation):** Oturumun başladığı IP adresi, User-Agent bilgisi ve coğrafi konum verileri kaydedilir. Anormal değişimlerde (Session Hijacking şüphesi) alarm tetiklenir.
* **Entropi Analizi:** Oluşturulan oturum kimliklerinin tahmin edilebilir olup olmadığını ölçer. Zayıf rastgelelik, "Session Prediction" saldırılarına yol açar.


## 2. En İyi Uygulama Yöntemleri (Best Practices)
* **Çerez Güvenlik Bayrakları:** Tüm oturum çerezleri `HttpOnly` (XSS koruması), `Secure` (Sadece HTTPS) ve `SameSite=Strict/Lax` (CSRF koruması) bayraklarına sahip olmalıdır.
* **Oturum Rotasyonu:** Ayrıcalık yükseltme (login vb.) işlemlerinden sonra mevcut SID imha edilmeli ve yenisi oluşturulmalıdır.
* **Atıl Oturum Zaman Aşımı:** Kullanıcı pasif kaldığında oturumun 15-30 dakika içinde otomatik olarak sonlandırılması bir endüstri standardıdır.

## 3. Benzer Açık Kaynak Projeler ve Rakipler
| Proje / Ürün | Tür | Öne Çıkan Özelliği |
| :--- | :--- | :--- |
| **OWASP ZAP** | Açık Kaynak | Dinamik oturum güvenliği taraması (DAST). |
| **Keycloak** | Açık Kaynak | Gelişmiş IAM ve yerleşik oturum yönetimi. |
| **SuperTokens** | Açık Kaynak/SaaS | Oturum rotasyonu ve hırsızlık tespiti odaklı mimari. |
| **Authelia** | Açık Kaynak | Reverse Proxy katmanında merkezi oturum kontrolü. |

## 4. Kritik Yapılandırma Parametreleri
* `session.cookie_lifetime`: Çerezin istemci tarafındaki ömrü.
* `session.gc_maxlifetime`: Sunucu tarafındaki oturum verisi silinme süresi.
* `max_concurrent_sessions`: Aynı anda aktif olabilecek maksimum cihaz sayısı.

## 5. Güvenlik Açısından Kritik Noktalar
1.  **Session Fixation:** Saldırganın belirlediği SID'nin kurban tarafından kullanılması.
2.  **Insecure Storage:** Oturum verilerinin tarayıcıda `localStorage` gibi güvensiz alanlarda saklanması.
3.  **Lack of Server-Side Invalidation:** Logout işleminde oturumun sunucu tarafında (Redis/DB) silinmemesi.
