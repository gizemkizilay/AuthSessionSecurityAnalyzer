# research.chatgpt.result

**Özet**  
Auth Session Security Analyzer, web uygulamalarının oturum yönetimi ve yetkilendirme kontrollerini otomatik veya yarı-otomatik olarak test eden araçları tanımlar. Araçlar session ID, cookie, JWT ve CSRF token akışlarını analiz ederek session hijacking, session fixation, IDOR ve privilege escalation gibi zafiyetleri tespit eder.

---

## 1. Temel Çalışma Prensipleri
- **Trafik yakalama ve çıkarım:** HTTP/HTTPS trafiği proxy veya tarayıcı entegrasyonu ile yakalanır; session öğeleri otomatik tespit edilir.  
- **Replay ve role-swap testleri:** Aynı istekler farklı rollerle tekrar edilerek yatay/dikey yetki atlama senaryoları denenir.  
- **Parametre manipülasyonu ve fuzzing:** ID parametreleri, tokenler ve cookie değerleri değiştirilerek mantık hataları aranır.  
- **Oturum yaşam döngüsü analizi:** Oturum oluşturma, yenileme, sonlandırma ve timeout davranışları test edilir.  
- **Raporlama:** Bulgular kategori, risk seviyesi, yeniden üretme adımları ve öneriler ile raporlanır.

---

## 2. En İyi Uygulamalar ve Endüstri Standartları
- **Token güvenliği:** Yüksek entropili, tahmin edilemez tokenler; rotate on auth.  
- **TLS zorunluluğu:** Tüm oturum verileri yalnızca HTTPS üzerinden iletilmeli.  
- **Cookie flag’leri:** `Secure`, `HttpOnly`, `SameSite` ve `_Host-`/`_Secure-` önekleri kullanılmalı.  
- **Timeout ve re-authentication:** Idle/absolute timeout; kritik işlemler için yeniden kimlik doğrulama.  
- **MFA ve least privilege:** Kritik roller için çok faktörlü kimlik doğrulama; roller en az ayrıcalık prensibine göre tanımlanmalı.  
- **Standartlar:** OWASP Session Management Cheat Sheet, OWASP ASVS, OWASP Top 10, NIST SP 800-63B.

---

## 3. Benzer Açık Kaynak Projeler ve Rakipler
- **Burp Suite + eklentiler (AuthMatrix, Auth Analyzer)** — Yetkilendirme testleri için yaygın kullanılan araçlar.  
- **OWASP ZAP** — Açık kaynak web uygulama güvenlik tarayıcısı; scripting ile özelleştirilebilir.  
- **JWT Tool** — JWT analiz ve manipülasyon araçları.  
- **Çeşitli GitHub scriptleri** — Session/authorization test scriptleri ve örnek otomasyonlar.

---

## 4. Kritik Yapılandırma Dosyaları ve Parametreler
- **config.yaml / config.json**: `target_base_url`, `session_cookie_name`, `csrf_token_param`, `roles`, `timeout`, `replay_rules`, `fuzzing` parametreleri.  
- **specs/**: IDOR, CSRF, role-swap gibi test senaryoları.  
- **logging.conf**: Hassas verilerin maskelenmesi ve log seviyeleri.  
- **reports/**: Findings JSON/Markdown/PDF çıktıları.

**Örnek config.yaml**
```yaml
target_base_url: "https://staging.example.com"
session_cookie_name: "SESSIONID"
csrf_token_param: "csrf_token"
roles:
  - admin
  - user
  - guest
timeout:
  idle_seconds: 1800
  absolute_seconds: 86400
replay_rules:
  allow_replay_on_different_role: true
fuzzing:
  id_entropy_threshold: 40
  max_bruteforce_attempts: 1000
logging:
  mask_session_tokens: true
  log_level: INFO
