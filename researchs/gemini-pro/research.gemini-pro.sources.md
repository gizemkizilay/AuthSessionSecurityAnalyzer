# Referanslar ve Kaynaklar

Bu araştırmada kullanılan temel standartlar ve dokümantasyon kaynakları aşağıdadır:

## Endüstri Standartları
* **OWASP ASVS (Application Security Verification Standard):** V3. Session Management Verification Requirements.
    * *Kullanım:* Oturum yönetiminin doğrulama kriterleri için temel alındı.
* **NIST SP 800-63B (Digital Identity Guidelines):** Authentication and Lifecycle Management.
    * *Kullanım:* Oturum ömrü (timeout) ve şifreleme standartları için referans alındı.
* **FIPS 140-2 (Security Requirements for Cryptographic Modules):**
    * *Kullanım:* Entropi analizindeki istatistiksel testlerin (Monobit, Poker vb.) dayanağıdır.

## Araç Dokümantasyonları
* **PortSwigger Web Security Academy:**
    * *Konu:* Session Management Vulnerabilities & Burp Sequencer Documentation.
* **OWASP ZAP Documentation:**
    * *Konu:* Session Management & Context Configuration.

## Teknik Dokümantasyonlar (Dil Bazlı)
* **PHP Manual:** Session Configuration Options (`php.ini`).
* **Express.js:** `express-session` middleware documentation.
* **Spring Security:** Session Management Architecture.
