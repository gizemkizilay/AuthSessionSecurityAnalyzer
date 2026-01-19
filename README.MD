# Auth Session Security Analyzer 🛡️
 
## 🎯 Proje Amacı
 
Bu proje, web uygulamalarındaki **Oturum Yönetimi (Session Management)** mekanizmalarını güvenlik testlerinden geçirmek amacıyla tasarlanmış bir analiz aracıdır. Modern web uygulamalarında kimlik doğrulama sonrası oluşan oturumların (Session ID, Token, Cookie) güvenliğini otomatik veya yarı-otomatik olarak denetlemeyi hedefler.
 
## 🚀 Beklenen Özellikler
 
Bu araç, aşağıdaki güvenlik zafiyetlerini tespit etmek için modüler testler içerir:
 
* **🕵️‍♂️ Oturum Çalma (Session Hijacking):**

    * Session ID'lerin tahmin edilebilirliğinin (Entropy analizi) test edilmesi.

    * XSS (Cross-Site Scripting) senaryolarına karşı oturum anahtarlarının dayanıklılığının analizi.
 
* **🍪 Cookie Güvenliği Denetimi:**

    * Kritik güvenlik bayraklarının (`HttpOnly`, `Secure`, `SameSite`) doğru yapılandırılıp yapılandırılmadığının kontrolü.

    * Cookie ömrü ve kapsam (Domain/Path) analizi.
 
* **⏱️ Timeout (Zaman Aşımı) Analizi:**

    * Oturumun eylemsizlik (idle) süresi ve mutlak zaman aşımı (absolute timeout) sürelerinin güvenli aralıkta olup olmadığının tespiti.
 
* **🆙 Yetki Yükseltme (Privilege Escalation):**

    * Farklı yetki seviyelerindeki kullanıcılar (Admin vs User) arasındaki izolasyonun testi.

    * IDOR (Insecure Direct Object References) tabanlı oturum manipülasyonu denemeleri.
 
## 🛠️ Teknik Odak ve Metodoloji
 
Proje, **OWASP Session Management** standartlarını temel alır ve aşağıdaki protokoller üzerinde çalışır:
 
* **Protokoller:** HTTP Cookies, JSON Web Tokens (JWT)

* **Standartlar:** OWASP ASVS (Application Security Verification Standard)

* **Analiz Yöntemi:** Black-box testing (Siyah kutu testi)
 
## 📂 Proje Yapısı
 


Auth-Session-Security-Analyzer/

├── docs/          # Araştırma notları ve teknik dökümanlar

├── src/           # Analiz aracının kaynak kodları (Geliştirme aşamasında)

├── tests/         # Test senaryoları

└── README.md      # Proje dökümantasyonu
 
# 🛡️ Auth Session Security Analyzer
 
## 📋 Proje Hakkında

Bu proje, web tabanlı uygulamalarda kritik öneme sahip olan **Oturum Yönetimi (Session Management)** süreçlerini denetleyen bir güvenlik analiz aracıdır. **SecOps** ve **Web Pentesting** süreçlerine katkı sağlamak amacıyla geliştirilen bu araç; oturum çalma, yetki karmaşası ve güvensiz çerez yapılandırmaları gibi zafiyetleri otomatik olarak tespit etmeyi hedefler.
 
## ✨ Temel Yetenekler

Geliştirme süreci tamamlandığında araç şu analizleri gerçekleştirecektir:
 
* 🕵️‍♂️ **Session Hijacking Analizi:** Oturum kimliklerinin (Session ID) tahmin edilebilirliği ve XSS kaynaklı sızıntı risklerinin testi.

* 🍪 **Cookie Konfigürasyon Denetimi:** Çerezlerdeki `HttpOnly`, `Secure` ve `SameSite` gibi güvenlik parametrelerinin doğrulanması.

* ⏳ **Zaman Aşımı (Timeout) Kontrolü:** Oturumun eylemsizlik (idle) ve mutlak sonlanma sürelerinin güvenlik standartlarına uygunluğunun analizi.

* 🔐 **Yetki İzolasyon Testleri:** Kullanıcılar arası yetki geçişi ve **IDOR** (Insecure Direct Object References) zafiyetlerinin taranması.

* 🔑 **JWT Güvenliği:** JSON Web Token yapısındaki imza ve algoritma zafiyetlerinin incelenmesi.
 
## ⚙️ Teknik Altyapı

Proje, **OWASP Session Management** standartları referans alınarak geliştirilmektedir.
 
* **Yazılım Dili:** Python 🐍

* **Temel Kütüphaneler:** `Requests`, `PyJWT`, `Selenium` (veya alternatif otomasyon araçları)

* **Metodoloji:** Black-box Testing
 
---

### 🎓 Ders ve Öğrenci Bilgileri

Bu proje, **İleri Sızma Testi** dersi kapsamında geliştirilmekte olan bir dönem ödevidir.
 
* **Geliştirici:** Gizem Kızılay

* **Öğrenci No:** 2420191015
 

