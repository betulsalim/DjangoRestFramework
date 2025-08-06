"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# =============================================================================
# DJANGO URLS.PY ANA URL KONFİGÜRASYON DOSYASI
# =============================================================================
#
# Bu dosya, Django projenizin ana URL yönlendirme konfigürasyonudur.
# Gelen HTTP isteklerini hangi view'lara yönlendireceğini belirler.
# URL routing, Django'nun MVC (Model-View-Controller) mimarisinin
# Controller kısmını oluşturur.
#
# URL Yapısı:
# - path('pattern/', view_function, name='url_name')
#   - pattern: URL deseni (regex benzeri)
#   - view_function: Çalıştırılacak view fonksiyonu
#   - name: URL'ye referans vermek için kullanılan isim
#
# Önemli Özellikler:
# - URL desenleri yukarıdan aşağıya doğru kontrol edilir
# - İlk eşleşen URL kullanılır
# - include() ile alt URL dosyaları dahil edilebilir
# - name parametresi ile URL'lere dinamik referans verilebilir
# =============================================================================

# Django admin paneli için gerekli import
from django.contrib import admin

# URL yönlendirme için gerekli fonksiyonlar
# path: Basit URL desenleri için
# include: Alt URL dosyalarını dahil etmek için
from django.urls import path, include

# Kendi uygulamamızdan view'ı import ediyoruz
# Bu, ana sayfa için kullanılacak view fonksiyonudur
from products.views import home_view

# =============================================================================
# URL DESENLERİ TANIMLAMASI
# =============================================================================

# URL yönlendirme kuralları listesi
# Django, gelen istekleri bu listedeki desenlerle karşılaştırır
# İlk eşleşen desen kullanılır
urlpatterns = [
    # Ana sayfa URL'i - root path ('/')
    # Kullanıcı siteye geldiğinde ilk karşılaşacağı sayfa
    # home_view fonksiyonu çalıştırılır
    # name='home' ile bu URL'ye template'lerde {% url 'home' %} ile referans verilebilir
    path('', home_view, name='home'),

    # Django admin paneli URL'i
    # /admin/ adresine gelen istekler Django admin paneline yönlendirilir
    # admin.site.urls, Django'nun yerleşik admin URL'lerini içerir
    path('admin/', admin.site.urls),

    # API endpoint'leri için URL grubu
    # /api/ ile başlayan tüm URL'ler products.urls dosyasındaki
    # URL desenlerine yönlendirilir
    # Bu, REST API endpoint'lerini organize etmek için kullanılır
    # Örnek: /api/products/, /api/products/1/ gibi
    path('api/', include('products.urls')),
]
