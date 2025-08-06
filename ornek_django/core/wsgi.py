"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

# =============================================================================
# WSGI (Web Server Gateway Interface) KONFİGÜRASYON DOSYASI
# =============================================================================
#
# Bu dosya, Django projenizin WSGI sunucuları ile çalışmasını sağlayan
# konfigürasyon dosyasıdır. WSGI, Python web uygulamaları için standart
# bir arayüz protokolüdür.
#
# WSGI vs ASGI:
# - WSGI: Senkron (synchronous) web uygulamaları için
# - ASGI: Asenkron (asynchronous) web uygulamaları için (modern tercih)
#
# Kullanım Alanları:
# - Gunicorn, uWSGI gibi WSGI sunucuları ile deployment
# - Eski Django projeleri için uyumluluk
# - Basit web uygulamaları için
#
# NOT: Modern Django projeleri için ASGI (asgi.py) tercih edilir
# çünkü WebSocket, HTTP/2 ve async/await desteği sağlar.
# =============================================================================

# Django'nun WSGI uygulamasını almak için gerekli modülü import ediyoruz
import os

# Django'nun WSGI uygulamasını oluşturmak için kullanılan fonksiyonu import ediyoruz
# Bu fonksiyon, Django'nun WSGI uygulamasını döndürür
from django.core.wsgi import get_wsgi_application

# Django ayarlarının hangi modülde bulunduğunu belirtiyoruz
# Bu, Django'nun hangi settings.py dosyasını kullanacağını belirler
# Eğer DJANGO_SETTINGS_MODULE environment variable'ı zaten set edilmişse onu kullanır,
# aksi takdirde 'core.settings' değerini varsayılan olarak atar
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# WSGI uygulamasını oluşturuyoruz
# Bu, Django'nun WSGI sunucuları (gunicorn, uWSGI vb.) tarafından
# kullanılacak olan ana uygulama nesnesidir
# get_wsgi_application() fonksiyonu, Django'nun WSGI uygulamasını döndürür
# ve bu uygulama, HTTP isteklerini Django'nun request/response döngüsüne yönlendirir
#
# WSGI Uygulama Özellikleri:
# - Senkron işlem desteği
# - Basit HTTP istek/yanıt döngüsü
# - Eski web sunucuları ile uyumluluk
# - Django'nun geleneksel view sistemi ile çalışır
application = get_wsgi_application()
