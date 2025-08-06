# Django uygulama konfigürasyonu için gerekli sınıfı import ediyoruz
# AppConfig, Django uygulamalarının konfigürasyonunu yönetmek için kullanılır
from django.apps import AppConfig

# =============================================================================
# PRODUCTS UYGULAMASI KONFİGÜRASYON SINIFI
# =============================================================================
#
# Bu dosya, 'products' Django uygulamasının konfigürasyon ayarlarını
# içerir. Her Django uygulaması, kendi davranışını ve ayarlarını
# kontrol etmek için bir AppConfig sınıfına sahiptir.
#
# AppConfig Sınıfının Görevleri:
# - Uygulama adını ve meta verilerini tanımlar
# - Uygulama başlatma işlemlerini yönetir
# - Uygulama özel ayarlarını içerir
# - Django'nun uygulamayı nasıl yükleyeceğini belirler
#
# Bu konfigürasyon, settings.py dosyasındaki INSTALLED_APPS
# listesinde kullanılır ve Django'nun uygulamayı tanımasını sağlar.
# =============================================================================

# Products uygulamasının konfigürasyon sınıfı
# Bu sınıf, Django'nun AppConfig sınıfından türetilir
# ve products uygulamasının özel ayarlarını tanımlar
class ProductsConfig(AppConfig):
    # =============================================================================
    # UYGULAMA AYARLARI
    # =============================================================================

    # Varsayılan birincil anahtar alan türü
    # Bu ayar, bu uygulamadaki modeller için varsayılan ID alan türünü belirler
    # BigAutoField: 64-bit integer, daha büyük ID'ler için kullanılır
    # Bu, modern Django projeleri için önerilen ayardır
    default_auto_field = 'django.db.models.BigAutoField'

    # Uygulama adı
    # Bu, Django'nun uygulamayı tanımlamak için kullandığı benzersiz isimdir
    # Bu isim, settings.py'daki INSTALLED_APPS listesinde kullanılır
    # Ayrıca, uygulama içindeki dosyalara referans verirken de kullanılır
    # Örnek: 'products.models', 'products.views' gibi
    name = 'products'

    # =============================================================================
    # OPSİYONEL AYARLAR (Şu anda kullanılmıyor)
    # =============================================================================
    #
    # Diğer yaygın AppConfig ayarları:
    # - verbose_name: Uygulamanın görünen adı (admin panelinde)
    # - label: Uygulama için benzersiz etiket
    # - path: Uygulama dosyalarının yolu
    # - ready(): Uygulama başlatıldığında çalışacak kod
    #
    # Örnek kullanım:
    # verbose_name = 'Ürün Yönetimi'
    # def ready(self):
    #     import products.signals  # Sinyal dosyalarını yükle
    # =============================================================================
