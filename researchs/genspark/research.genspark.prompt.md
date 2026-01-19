# Prompt — Auth Session Security Analyzer (Teknik Araştırma)

## Rol
Kıdemli Uygulama Güvenliği (AppSec) / Kimlik & Erişim Yönetimi (IAM) danışmanı ve teknik araştırmacı gibi davran. Çıktıyı **Türkçe**, **teknik derinliği yüksek**, pratikte uygulanabilir ve **kaynaklı** bir Markdown raporu olarak üret.

## Amaç
“Auth Session Security Analyzer” konusunu iki eksende ele al:
1) Eğer bu isimde **spesifik bir ürün/proje** bulunabiliyorsa onu merkeze al.
2) Bulunamıyorsa (veya belirsizse) bunu bir **kategori** olarak değerlendir: “kimlik doğrulama (AuthN) / yetkilendirme (AuthZ) ve oturum (session) yönetimi güvenliğini analiz eden araçlar, yöntemler ve kontroller”.

> Not: Web araştırmasında `"Auth Session Security Analyzer"` ifadesi ile belirgin bir ürün/proje bulunamayabilir. Bu durumda raporu “oturum güvenliği analiz yaklaşımı” kategorisi olarak kurgula.

## Çıktı Formatı (Zorunlu)
- Tek bir **Markdown rapor** üret.
- Başlıklar net, hiyerarşik olsun (H1/H2/H3).
- Her önemli iddiayı/detayı **kaynak linki** ile destekle (paragraf sonunda).
- Rapor sonunda “**Kontrol Listesi**” ve “**Örnek Konfig Parçaları**” bölümü olsun.
- Gerektiğinde tablolar kullan (karşılaştırma için).
- “Varsayım yaptığın” yerleri açıkça belirt.

## Kapsam: Cevaplanacak Sorular
Aşağıdaki 5 başlığın her birini ayrı bölüm yap ve teknik düzeyde detaylandır:

### 1) Temel Çalışma Prensipleri
- HTTP’nin stateless doğası ve session kavramı
- Session ID üretimi, entropy, CSPRNG, yaşam döngüsü (create/renew/invalidate)
- Session fixation vs session hijacking vs replay
- Cookie güvenlik bayrakları (Secure, HttpOnly, SameSite) ve scope (Domain/Path)
- CSRF ilişkisi; SameSite ve CSRF token etkileşimi
- Token tabanlı model: access token / refresh token / rotation
- JWT’de signature validation, alg confusion, typ, iss/aud doğrulaması, key rotation (JWKS)
- Server-side session store (Redis vb.), sticky session, load balancer, reverse proxy header güveni

### 2) Best Practices ve Endüstri Standartları
Aşağıdaki standart/rehberleri temel referans al:
- OWASP Session Management Cheat Sheet
- OWASP ASVS (özellikle authentication/session ile ilgili kontroller)
- OWASP Top 10 (authentication, access control, crypto, misconfig vb.)
- IETF: RFC 6265 (Cookies), RFC 6749 (OAuth 2.0), OpenID Connect Core, RFC 8725 (JWT BCP)
- Ek olarak uygun görürsen NIST 800-63 serisine referans ver

Best practice’leri “**Uygulama düzeyi**”, “**Altyapı düzeyi**”, “**İzleme/Denetim**” diye sınıflandır:
- TLS/HSTS, secure cookie zorunluluğu
- Session rotation/renewal (login sonrası, privilege change sonrası)
- Idle vs absolute timeout; logout invalidation
- Refresh token rotation + reuse detection
- CORS/CSP, XSS azaltımı, CSRF önlemleri
- Rate limiting, anomaly detection, device binding, step-up auth
- Audit logging (hangi alanlar loglanmalı / maskelenmeli)

### 3) Benzer Açık Kaynak Projeler ve Rakipler
En az şu sınıflarda örnekler ver ve karşılaştır:
- DAST araçları (oturum testleri ve auth akışları ile)
- Proxy tabanlı güvenlik test araçları
- SAST/Semgrep gibi code scanning (session/cookie/JWT hataları)
- Nuclei template ekosistemi (auth/session misconfig kontrolleri)
- IAM/SSO çözümleri (Keycloak gibi) ve ilgili güvenlik denetimleri
- RASP/WAF yaklaşımı (oturum anomalisi tespiti)

Her proje/ürün için:
- Ne tür session/auth risklerini yakalar?
- En güçlü olduğu alan ve zayıf kaldığı alan
- En uygun kullanım senaryosu
- Kurulum/entegrasyon yaklaşımı (CI/CD, pre-prod, prod observability)

### 4) Kritik Yapılandırma Dosyaları ve Parametreleri
Bu bölüm “konfig kontrol listesi” gibi net olmalı.
Genel parametre kategorileri:
- Cookie ayarları: Secure/HttpOnly/SameSite/Domain/Path/Max-Age/Expires
- Session timeout (idle/absolute/renewal)
- Session store (Redis/DB): encryption-at-rest, key TTL, prefixing, eviction politikası
- JWT/OAuth/OIDC parametreleri: issuer, audience, jwks_uri, kid, alg allowlist, clock skew, token lifetime
- Reverse proxy / LB: X-Forwarded-* güveni, trusted proxies
- CORS: allowlist, credentials, preflight cache
- CSP: script-src, nonce/sha, frame-ancestors
- CSRF: token strategy, double-submit cookie, same-site yaklaşımı

Mümkünse örnek konfig parçaları ekle:
- Nginx/Ingress (HSTS, secure headers)
- Uygulama framework’lerinden örnek (genel pseudocode olabilir)
- Redis TTL örnekleri

### 5) Güvenlik Açısından Kritik Noktalar (Threat Model)
Tehditleri “saldırı → etki → tespit/önlem” formatıyla anlat:
- Session fixation
- Session hijacking (XSS, network, malware)
- CSRF
- JWT alg none/HS-RS confusion, key injection (jku/x5u), SSRF riskleri
- Refresh token replay
- OAuth redirect_uri manipulation / open redirector
- Mixed content ve TLS downgrade riskleri
- Cache riskleri (Set-Cookie, no-store)
- Log/telemetry’de token sızıntısı
- Çoklu cookie senaryolarında doğrulama/binding hataları

## Kaynak Gereksinimleri (Zorunlu)
Aşağıdaki kaynaklar raporda mutlaka kullanılmalı (en azından ilgili bölümlerde):
- OWASP Session Management Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
- RFC 6265 (Cookies): https://datatracker.ietf.org/doc/html/rfc6265
- RFC 6749 (OAuth 2.0): https://datatracker.ietf.org/doc/html/rfc6749
- OpenID Connect Core: https://openid.net/specs/openid-connect-core-1_0.html
- RFC 8725 (JWT BCP): https://datatracker.ietf.org/doc/html/rfc8725
- OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/
- OWASP Top 10: https://owasp.org/Top10/

Ek kaynaklar kullanırsan:
- Tercihen birincil (standart, resmi dokümantasyon, OWASP, IETF, NIST) olsun.
- Blog yazısı ise, “uyarı/tecrübe paylaşımı” olarak konumlandır.

## Son Bölüm: Uygulanabilir Çıktılar
Raporun sonunda şunlar mutlaka olsun:
1) “Hızlı Kontrol Listesi” (10–25 madde)
2) “Anti-pattern’ler” (en az 8 örnek)
3) “Örnek Konfig” (en az 3 kısa snippet; cookie, JWT validation, reverse proxy trust gibi)

## Ton ve Dil
- Türkçe, teknik ve net.
- Gereksiz pazarlama dili yok.
- Belirsiz konularda “şu varsayımla ilerliyorum” diye belirt.
