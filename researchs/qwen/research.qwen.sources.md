# Auth Session Security Analyzer – Kaynaklar ve Referanslar

Bu belge, `research.felo.qwen.md` kapsamında yürütülen teknik araştırmada kullanılan resmi standartlar, güvenlik kılavuzları ve açık kaynak dokümantasyonlarını içermektedir. Tüm kaynaklar 2026 itibarıyla geçerli ve erişilebilir durumdadır.

---

## 1. Güvenlik Kılavuzları ve Cheat Sheet’ler

- **OWASP Session Management Cheat Sheet**  
  → [https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)  
  *Oturum güvenliği için en kapsamlı topluluk kaynağı.*

- **OWASP Top 10:2021 – A07: Identification and Authentication Failures**  
  → [https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/](https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/)  
  *Kimlik doğrulama zafiyetlerinin risk sınıflandırması.*

- **OWASP Web Security Testing Guide (WSTG) – Session Management Testing**  
  → [https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing)  
  *Oturum test metodolojileri.*

---

## 2. Resmi Standartlar ve Düzenlemeler

- **NIST Special Publication 800-63B: Digital Identity Guidelines**  
  → [https://pages.nist.gov/800-63-3/sp800-63b.html](https://pages.nist.gov/800-63-3/sp800-63b.html)  
  *Kimlik doğrulama, oturum süresi ve MFA politikaları.*

- **PCI DSS v4.0 – Requirement 8: User Access and Authentication**  
  → [https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Standard/PCI-DSS-v4_0.pdf](https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Standard/PCI-DSS-v4_0.pdf)  
  *Özellikle ödeme sistemlerinde oturum güvenliği gereklilikleri.*

- **ISO/IEC 27001:2022 & ISO/IEC 27002:2022**  
  → Kontrol maddeleri: A.9.4.2 (Oturum yönetimi), A.10.1 (Kriptografi)  
  *Kurumsal bilgi güvenliği çerçevesi.*

---

## 3. Teknik Protokoller ve RFC’ler

- **RFC 6265 – HTTP State Management Mechanism (Cookies)**  
  → [https://datatracker.ietf.org/doc/html/rfc6265](https://datatracker.ietf.org/doc/html/rfc6265)  
  *Cookie özniteliklerinin (Secure, HttpOnly, SameSite) teknik temeli.*

- **RFC 7519 – JSON Web Token (JWT)**  
  → [https://datatracker.ietf.org/doc/html/rfc7519](https://datatracker.ietf.org/doc/html/rfc7519)  
  *Token yapısı, imzalama ve geçerlilik süresi.*

- **RFC 6749 – OAuth 2.0 Authorization Framework**  
  → [https://datatracker.ietf.org/doc/html/rfc6749](https://datatracker.ietf.org/doc/html/rfc6749)  
  *Modern oturum akışlarında kullanılan yetkilendirme protokolü.*

---

## 4. Açık Kaynak Projeler ve Dokümantasyonlar

- **OWASP ZAP Documentation – Session Handling Rules**  
  → [https://www.zaproxy.org/docs/desktop/start/features/sessionhandling/](https://www.zaproxy.org/docs/desktop/start/features/sessionhandling/)  
  *Otomatik oturum analizi ve test senaryoları.*

- **ModSecurity Core Rule Set (CRS) – Session Fixation Rules**  
  → [https://coreruleset.org](https://coreruleset.org)  
  *WAF düzeyinde oturum saldırısı engelleme kuralları.*

- **Mozilla HTTP Observatory**  
  → [https://observatory.mozilla.org](https://observatory.mozilla.org)  
  *Cookie ve güvenlik başlıkları için otomatik değerlendirme aracı.*

---

## 5. Ticari Platform Belgeleri (Referans Amaçlı)

- **Okta: Session Management Best Practices**  
  → [https://help.okta.com/en-us/Content/Topics/Security/identity-protection/session-management.htm](https://help.okta.com/en-us/Content/Topics/Security/identity-protection/session-management.htm)

- **Akamai Identity Cloud: Session Security**  
  → [https://developer.akamai.com/legacy/identity-cloud/security/session-security](https://developer.akamai.com/legacy/identity-cloud/security/session-security)

> ⚠️ Not: Ticari platform belgeleri yalnızca endüstri uygulamalarını anlamak amacıyla referans alınmıştır; açık kaynak alternatifler tercih edilmelidir.

---

## Güncelleme Tarihi
**18 Ocak 2026**

Tüm bağlantılar bu tarihte test edilmiş ve erişilebilir durumdadır.
