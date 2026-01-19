# Auth Session Security Analyzer: Teknik Araştırma Raporu

Bu rapor, modern web uygulamalarında oturum güvenliği analizinin nasıl yapıldığını, kullanılan araçların (özellikle Burp Suite Auth Analyzer ve Sequencer) çalışma prensiplerini ve kritik güvenlik parametrelerini incelemektedir.

## 1. Temel Çalışma Prensipleri

Auth Session Security Analyzer araçları temel olarak iki ana kategoride çalışır: **Entropi Analizi** ve **Yetkilendirme (Authorization) Doğrulaması**.

### A. İstatistiksel Entropi Analizi (Token Randomness)
Oturum kimliklerinin (Session ID) veya CSRF tokenlarının tahmin edilebilirliğini ölçer.
* **Veri Toplama:** Araç, hedef uygulamadan binlerce (örneğin 20.000 adet) örnek token toplar.
* **Bit Seviyesi Analizi:** Her bir token'ı bit dizilerine dönüştürür.
* **FIPS 140-2 Testleri:** NIST standartlarına uygun istatistiksel testler (Monobit, Poker, Runs, Long Runs) uygular.
* **Sonuç:** Token'ın rastgelelik kalitesini (Effective Entropy) bit cinsinden raporlar. Eğer entropi düşükse, saldırganın bir sonraki token'ı tahmin etmesi (Brute-force/Prediction) mümkündür.

### B. Otomatik Yetki Karşılaştırması (Privilege Escalation)
Burp Suite'in "Auth Analyzer" eklentisi gibi araçlar bu prensiple çalışır:
1. **Oturum Tanımlama:** Farklı yetki seviyelerine sahip kullanıcılar (örn: Admin, Standart Kullanıcı, Anonim) tanımlanır.
2. **Trafik Kopyalama:** "Admin" kullanıcısı ile yapılan her istek, arka planda otomatik olarak "Standart" ve "Anonim" kullanıcıların oturum çerezleri (cookies) ile tekrar edilir.
3. **Diff Analizi:** Yanıtlar (HTTP Status Code, Response Length, Body) karşılaştırılarak, düşük yetkili kullanıcının erişmemesi gereken bir kaynağa erişip erişemediği (IDOR/BOLA zafiyetleri) tespit edilir.

---

## 2. En İyi Uygulama Yöntemleri (Best Practices) ve Standartlar

Endüstri standartları büyük ölçüde **OWASP ASVS** ve **NIST SP 800-63B** dokümanlarına dayanır.

| Kategori | Standart / En İyi Uygulama |
| :--- | :--- |
| **Entropi** | Oturum anahtarları en az **128-bit** entropiye sahip olmalıdır. (Örn: MD5 yerine SHA-256 veya CSPRNG kullanımı). |
| **Ömür (Lifecycle)** | Oturumlar "Idle Timeout" (örn. 15-30 dk) ve "Absolute Timeout" (örn. 8-24 saat) sınırlarına sahip olmalıdır. |
| **Yenileme** | Kullanıcı giriş yaptığında (Login) veya yetki seviyesi değiştiğinde Session ID mutlaka yenilenmelidir (**Session Regeneration**). |
| **Taşıma** | Oturum bilgileri asla URL parametrelerinde taşınmamalı, sadece HTTP Header (Cookie) veya Body içinde iletilmelidir. |
| **Bayraklar** | Çerezler için `Secure`, `HttpOnly` ve `SameSite=Strict/Lax` bayrakları zorunlu tutulmalıdır. |

---

## 3. Benzer Açık Kaynak Projeler ve Rakipler

Bu alandaki araçlar genellikle "Dynamic Application Security Testing" (DAST) ve "Proxy" araçlarının alt modülleri olarak bulunur.

1. **Burp Suite (PortSwigger):**
    * **Sequencer:** Token rastgeleliğini ölçmek için endüstri lideri araçtır.
    * **Auth Analyzer (Extension):** Yetki yükseltme (Privilege Escalation) testleri için en popüler eklentidir.
    * **AuthMatrix:** Matris tabanlı yetki kontrolleri için kullanılan bir başka güçlü eklentidir.

2. **OWASP ZAP (Zed Attack Proxy):**
    * **Session Management:** Otomatik oturum yönetimi algılama ve test etme özelliklerine sahiptir. Açık kaynaklı ve ücretsiz en güçlü rakiptir.

3. **Diğerleri:**
    * **Acunetix & Netsparker:** Otomatik tarayıcılar (Scanner) içinde gömülü modül olarak bu analizleri yapar.
    * **Yaso (Yet Another Session Overview):** Spesifik oturum analizleri için kullanılan daha küçük çaplı GitHub projeleri.

---

## 4. Kritik Yapılandırma Dosyaları ve Parametreleri

Bir güvenlik analisti, analiz sırasında hem analiz aracının hem de hedef sistemin yapılandırmasına odaklanır.

### A. Hedef Sistem Yapılandırmaları (Örnekler)
Analiz sonucunda düzeltilmesi gereken kritik dosyalar şunlardır:

* **PHP (`php.ini`):**
    ```ini
    session.cookie_httponly = 1  ; JavaScript erişimini engeller
    session.cookie_secure = 1    ; Sadece HTTPS üzerinden iletim
    session.use_strict_mode = 1  ; Session Fixation engelleme
    session.entropy_length = 32  ; Token uzunluğu
    ```

* **Java / Spring Security:**
    `WebSecurityConfigurerAdapter` içinde `http.sessionManagement()` ayarları (Session Fixation koruması, Concurrency limitleri).

* **Node.js (Express-session):**
    ```javascript
    app.use(session({
      secret: 'cok-gizli-anahtar', // Zayıf/tahmin edilebilir olmamalı
      cookie: { secure: true, httpOnly: true, sameSite: 'strict' },
      resave: false
    }))
    ```

### B. Analiz Aracı Yapılandırması (Burp Sequencer)
* **Sample Size:** Güvenilir bir istatistiksel analiz için en az **20.000 token** toplanmalıdır.
* **Significance Level:** Genellikle %1 veya %5 olarak ayarlanır; sapmaların rastlantısal olup olmadığını belirler.

---

## 5. Güvenlik Açısından Dikkat Edilmesi Gereken Kritik Noktalar

Analiz sırasında aşağıdaki zafiyet türlerine (Vulnerabilities) odaklanılır:

1. **Session Fixation (Oturum Sabitleme):** Saldırganın belirlediği bir Session ID'nin kurban tarafından kullanılmaya zorlanması.
2. **Yetersiz Entropi:** Token'ların tarih, zaman damgası veya kullanıcı adına bağlı olarak tahmin edilebilir şekilde üretilmesi.
3. **XSS ile Token Çalma:** `HttpOnly` bayrağı eksikse, basit bir XSS saldırısı ile oturum ele geçirilebilir.
4. **JWT (JSON Web Token) Zafiyetleri:** `None` algoritması kabulü veya imza doğrulama eksiklikleri.
5. **Loglama Hataları:** Session ID'lerin URL'de veya log dosyalarında açık metin olarak saklanması.
