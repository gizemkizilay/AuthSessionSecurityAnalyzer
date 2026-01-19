Auth Analyzer, Burp Suite için geliştirilmiş bir eklentidir ve web uygulamalarında yetkilendirme (authorization) hatalarını tespit etmek amacıyla kullanılır. Bu araç, yüksek yetkili bir kullanıcı oturumuyla yapılan istekleri düşük yetkili oturumlarla otomatik tekrarlayarak erişim kontrolü zafiyetlerini ortaya çıkarır.[web:7]

## Temel Çalışma Prensipleri
Auth Analyzer, proxy trafiğini yakalar ve tanımlanan birden fazla oturum (session) için istekleri otomatik olarak tekrarlama yapar.[web:7] Yüksek yetkili kullanıcıyla gezinirken, araç düşük yetkili oturumların cookie'leri veya header'larını kullanarak aynı istekleri gönderir ve yanıtları "same", "similar" veya "different" olarak etiketler.[web:4] Parametre tanımlama özelliğiyle CSRF token'ları veya oturum verileri otomatik çıkarıp değiştirerek gelişmiş testler yapar, böylece privilege escalation (yetki yükseltme) zafiyetlerini belirler.[web:7]

## En İyi Uygulama Yöntemleri
- Farklı roller (admin, user, guest) için ayrı oturumlar tanımlayarak istekleri bu oturumlarla tekrar ettir.[web:4]
- Burp scope ayarlarını sadece hedef domain/uygulamaya sınırlayarak gereksiz trafiği filtrele.[web:28]
- OWASP Session Management Cheat Sheet’teki oturum süresi, ID entropisi ve yenileme (rotation) önerilerini uygulayıp test senaryolarına dahil et.[web:24]

## Benzer Projeler ve Rakipler
- Autorize (Burp eklentisi): Broken access control ve IDOR tespiti için header/cookie değiştirme temelli çalışır.[web:16]
- AuthMatrix (Burp eklentisi): Rol–kaynak matrisine dayalı yetkilendirme testleri sağlar.[web:17]
- OWASP ZAP authorization script’leri: Benzer şekilde farklı roller için istek tekrarına imkan tanır.[web:3]

## Kritik Yapılandırma Parametreleri
- Session tanımları: Her kullanıcı rolü için ayrı cookie/header set’leri oluşturulmalıdır.[web:4]
- “Header(s) to Replace”: Özellikle Cookie ve Authorization header’larının hangi oturumla değiştirileceği burada tanımlanır.[web:7]
- Parametre tanımları: CSRF token gibi dinamik değerler için regex tabanlı extraction ve replace kuralları girilir.[web:7]

## Güvenlik Dikkat Noktaları
- Testleri sadece QA / staging ortamlarında çalıştır; production üzerinde agresif yeniden oynatma testleri iş mantığını bozabilir.[web:13]
- Proxy trafiğini scope dışında bırakmamaya, hassas cookie ve token’ların üçüncü taraflara gitmemesine dikkat et.[web:28]
- Eklenti üçüncü taraf geliştirme olduğundan, GitHub üzerindeki kaynak kodu ve Burp sürüm uyumluluğunu düzenli kontrol et.[web:25]
