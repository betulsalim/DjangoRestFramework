#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

# =============================================================================
# DJANGO MANAGE.PY YÖNETİM DOSYASI
# =============================================================================
#
# Bu dosya, Django projesinin komut satırı yönetim aracıdır.
# Django'nun tüm yönetim komutlarını çalıştırmak için kullanılır.
# Bu dosya, Django projesi oluşturulduğunda otomatik olarak oluşturulur.
#
# Manage.py'nin Görevleri:
# - Django yönetim komutlarını çalıştırma
# - Proje ayarlarını yükleme
# - Django ortamını başlatma
# - Komut satırı argümanlarını işleme
# - Hata yönetimi ve raporlama
#
# Yaygın Kullanım Alanları:
# - Sunucu başlatma: python manage.py runserver
# - Veritabanı işlemleri: python manage.py migrate
# - Admin kullanıcısı oluşturma: python manage.py createsuperuser
# - Shell başlatma: python manage.py shell
# - Test çalıştırma: python manage.py test
# =============================================================================

# Sistem modüllerini import ediyoruz
# os: İşletim sistemi ile etkileşim için
# sys: Sistem parametreleri ve komut satırı argümanları için
import os
import sys

# =============================================================================
# ANA FONKSİYON
# =============================================================================

# Django yönetim komutlarını çalıştıran ana fonksiyon
# Bu fonksiyon, komut satırından gelen argümanları işler
# ve uygun Django komutunu çalıştırır
def main():
    """
    Django yönetim komutlarını çalıştıran ana fonksiyon.
    Bu fonksiyon, komut satırı argümanlarını alır ve
    Django'nun uygun yönetim komutunu çalıştırır.
    """

    # Django ayarlar modülünü environment variable olarak ayarlıyoruz
    # Bu, Django'nun hangi settings.py dosyasını kullanacağını belirler
    # 'core.settings' - projenin ana ayar dosyasının yolu
    # setdefault: Eğer DJANGO_SETTINGS_MODULE zaten set edilmişse onu kullanır,
    # aksi takdirde 'core.settings' değerini atar
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

    # Django yönetim modülünü import etmeye çalışıyoruz
    # Bu modül, Django komutlarını çalıştırmak için gerekli
    try:
        # Django'nun yönetim modülünü import ediyoruz
        # execute_from_command_line: Komut satırı argümanlarını işleyen fonksiyon
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Django import edilemezse hata mesajı gösteriyoruz
        # Bu genellikle Django'nun yüklü olmadığı veya
        # virtual environment'ın aktif olmadığı durumlarda olur
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Django komutunu çalıştırıyoruz
    # sys.argv: Komut satırından gelen argümanlar listesi
    # Örnek: ['manage.py', 'runserver', '8000']
    # execute_from_command_line: Bu argümanları işler ve uygun Django komutunu çalıştırır
    execute_from_command_line(sys.argv)

# =============================================================================
# SCRIPT BAŞLATMA KONTROLÜ
# =============================================================================

# Bu dosya doğrudan çalıştırıldığında main() fonksiyonunu çağırıyoruz
# __name__ == '__main__': Dosyanın doğrudan çalıştırıldığını kontrol eder
# Bu, dosyanın import edildiğinde main() fonksiyonunun çalışmamasını sağlar
if __name__ == '__main__':
    main()

# =============================================================================
# YAYGIN KULLANIM ÖRNEKLERİ
# =============================================================================
#
# Bu dosya ile çalıştırılabilecek yaygın Django komutları:
#
# # Sunucu işlemleri
# python manage.py runserver                    # Geliştirme sunucusunu başlat
# python manage.py runserver 8080               # Belirli port'ta başlat
# python manage.py runserver 0.0.0.0:8000       # Tüm IP'lerden erişime aç
#
# # Veritabanı işlemleri
# python manage.py makemigrations              # Migration dosyaları oluştur
# python manage.py migrate                      # Veritabanını güncelle
# python manage.py migrate --plan               # Migration planını göster
# python manage.py showmigrations               # Migration durumunu göster
#
# # Kullanıcı işlemleri
# python manage.py createsuperuser              # Admin kullanıcısı oluştur
# python manage.py changepassword <username>    # Şifre değiştir
#
# # Geliştirme araçları
# python manage.py shell                        # Django shell başlat
# python manage.py shell_plus                   # Gelişmiş shell (django-extensions)
# python manage.py dbshell                      # Veritabanı shell'i başlat
#
# # Test işlemleri
# python manage.py test                         # Tüm testleri çalıştır
# python manage.py test products                # Belirli app'in testlerini çalıştır
# python manage.py test products.tests          # Belirli test dosyasını çalıştır
#
# # Statik dosya işlemleri
# python manage.py collectstatic                # Statik dosyaları topla
# python manage.py findstatic <file>            # Statik dosya yolunu bul
#
# # Proje yönetimi
# python manage.py check                        # Proje durumunu kontrol et
# python manage.py check --deploy               # Deployment kontrolü
# python manage.py validate                     # Model validasyonu
#
# # Özel komutlar
# python manage.py help                         # Tüm komutları listele
# python manage.py help <command>               # Belirli komutun yardımını göster
# =============================================================================
