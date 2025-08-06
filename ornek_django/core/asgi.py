"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

# =============================================================================
# ASGI (Asynchronous Server Gateway Interface) Konfigürasyon Dosyası
# =============================================================================
#
# Bu dosya, Django projenizin ASGI sunucuları ile çalışmasını sağlayan
# konfigürasyon dosyasıdır. ASGI, modern Python web uygulamaları için
# geliştirilmiş bir protokoldür ve WSGI'nin yerini almaktadır.
#
# ASGI'nin Avantajları:
# - Asenkron işlem desteği (async/await)
# - WebSocket desteği
# - HTTP/2 ve HTTP/3 desteği
# - Daha iyi performans
#
# Kullanım Alanları:
# - Uvicorn, Daphne, Hypercorn gibi ASGI sunucuları ile deployment
# - WebSocket gerektiren real-time uygulamalar
# - Yüksek performans gerektiren uygulamalar
#
# Bu dosya, Django projenizin modern web sunucuları ile uyumlu
# çalışmasını sağlayan kritik bir bileşendir.
# =============================================================================

# Django'nun ASGI uygulamasını almak için gerekli modülü import ediyoruz
import os

# Django'nun ASGI uygulamasını oluşturmak için kullanılan fonksiyonu import ediyoruz
from django.core.asgi import get_asgi_application

# Django ayarlarının hangi modülde bulunduğunu belirtiyoruz
# Bu, Django'nun hangi settings.py dosyasını kullanacağını belirler
# Eğer DJANGO_SETTINGS_MODULE environment variable'ı zaten set edilmişse onu kullanır,
# aksi takdirde 'core.settings' değerini varsayılan olarak atar
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# ASGI uygulamasını oluşturuyoruz
# Bu, Django'nun ASGI sunucuları (uvicorn, daphne, hypercorn vb.) tarafından
# kullanılacak olan ana uygulama nesnesidir
# get_asgi_application() fonksiyonu, Django'nun ASGI uygulamasını döndürür
# ve bu uygulama, HTTP isteklerini Django'nun request/response döngüsüne yönlendirir
application = get_asgi_application()
