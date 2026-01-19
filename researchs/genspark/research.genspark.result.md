# Auth Session Security Analyzer — Teknik Araştırma Raporu

> **Kapsam Notu:** “Auth Session Security Analyzer” ifadesi, kamuya açık kaynaklarda tekil bir ürün/proje adı olarak doğrulanamazsa, rapor “oturum (session) güvenliğini analiz eden yaklaşım ve araçlar” kategorisi üzerinden ilerler.

## İçindekiler
1. [Kavramın Tanımı ve Kapsamı](#kavramın-tanımı-ve-kapsamı)
2. [1. Temel Çalışma Prensipleri](#1-temel-çalışma-prensipleri)
3. [2. Best Practices ve Endüstri Standartları](#2-best-practices-ve-endüstri-standartları)
4. [3. Açık Kaynak Projeler ve Rakipler](#3-açık-kaynak-projeler-ve-rakipler)
5. [4. Kritik Yapılandırmalar ve Parametreler](#4-kritik-yapılandırmalar-ve-parametreler)
6. [5. Güvenlikte Kritik Noktalar (Threat Model)](#5-güvenlikte-kritik-noktalar-threat-model)
7. [Kontrol Listesi](#kontrol-listesi)
8. [Anti-pattern’ler](#anti-patternler)
9. [Örnek Konfig Parçaları](#örnek-konfig-parçaları)
10. [Kaynakça](#kaynakça)

---

## Kavramın Tanımı ve Kapsamı
- AuthN/AuthZ ve session yönetiminin ilişkisi
- Cookie tabanlı session vs token tabanlı session
- Web, API, SPA, mobil ve SSO senaryoları
- Saldırı yüzeyi: istemci, ağ, reverse proxy, sunucu, veri deposu

---

## 1. Temel Çalışma Prensipleri
### 1.1 HTTP stateless → Session state nasıl kurulur?
### 1.2 Session ID özellikleri: entropy, CSPRNG, tahmin edilemezlik
### 1.3 Session lifecycle: create / rotate / expire / revoke
### 1.4 Cookie mekanikleri ve cookie attribute’ları
### 1.5 CSRF-SameSite ilişkisi
### 1.6 Token tabanlı oturumlar (JWT/opaque) ve riskleri
### 1.7 OAuth2/OIDC’de oturum: access/refresh, rotation, audience/issuer

---

## 2. Best Practices ve Endüstri Standartları
### 2.1 OWASP Session Management rehberi ile uyum
### 2.2 OWASP ASVS: doğrulama kontrolleri nasıl okunur/uygulanır?
### 2.3 IETF standartları: Cookies (RFC 6265), OAuth2 (RFC 6749), JWT BCP (RFC 8725)
### 2.4 Uygulama düzeyi kontroller
### 2.5 Altyapı ve edge kontrolleri (TLS/HSTS, proxy trust, rate limit)
### 2.6 İzleme/denetim: loglama, alarm üretimi, anomali tespiti

---

## 3. Açık Kaynak Projeler ve Rakipler
> Tablo: Araç / Tür / Güçlü Yön / Zayıf Yön / En iyi kullanım

- DAST (örn. OWASP ZAP)
- Proxy tabanlı test (örn. Burp Suite - ticari; referans amaçlı)
- SAST & pattern scanning (örn. Semgrep)
- Nuclei template yaklaşımı
- IAM/SSO (örn. Keycloak gibi) ve denetim noktaları

---

## 4. Kritik Yapılandırmalar ve Parametreler
### 4.1 Cookie ayarları (Secure, HttpOnly, SameSite, Domain, Path, Max-Age/Expires)
### 4.2 Session timeouts (idle/absolute/renewal)
### 4.3 Session store (Redis/DB) güvenliği
### 4.4 JWT doğrulama parametreleri (iss/aud/alg allowlist/jwks/kid)
### 4.5 Reverse proxy & LB güven modeli (trusted proxies)
### 4.6 CORS/CSP/CSRF parametreleri

---

## 5. Güvenlikte Kritik Noktalar (Threat Model)
Her başlık için format:
- **Saldırı**
- **Etkisi**
- **Tespit**
- **Önleme / Mitigasyon**
- **Test stratejisi** (DAST/SAST/manual)

Kapsanacak tehditler:
- Session fixation
- Session hijacking
- CSRF
- JWT alg confusion / “none” / key injection / SSRF vektörleri
- Refresh token replay
- OAuth redirect_uri manipülasyonu / open redirector
- Mixed content / TLS downgrade
- Cache ve log sızıntıları

---

## Kontrol Listesi
- (10–25 madde; uygulama+altyapı+izleme)

---

## Anti-pattern’ler
- (En az 8 madde; örn. localStorage’da access token, SameSite=None + Secure yok, alg allowlist yok, cookie domain geniş, vs.)

---

## Örnek Konfig Parçaları
> Kısa snippet’ler:
1) Set-Cookie örnekleri (güvenli bayraklarla)
2) JWT validation pseudocode (iss/aud/alg allowlist/jwks/kid)
3) Reverse proxy trusted headers örneği (örn. Nginx/Ingress notları)

---

## Kaynakça
- Zorunlu kaynaklar + ek referanslar (tam URL)
