import math
import sys

class HesapMakinesi:
    def __init__(self):
        self.hafiza = 0
        self.son_islem_sonucu = 0  
    
    def toplama(self, a, b):
        try:
            sonuc = a + b
            self.hafiza += sonuc
            self.son_islem_sonucu = sonuc
            return sonuc
        except Exception as e:
            return f"Hata: {str(e)}"
    
    def cikarma(self, a, b):
        try:
            sonuc = a - b
            self.hafiza += sonuc
            self.son_islem_sonucu = sonuc
            return sonuc
        except Exception as e:
            return f"Hata: {str(e)}"
    
    def carpma(self, a, b):
        try:
            sonuc = a * b
            self.hafiza += sonuc
            self.son_islem_sonucu = sonuc
            return sonuc
        except Exception as e:
            return f"Hata: {str(e)}"
    
    def bolme(self, a, b):
        try:
            if b != 0:
                sonuc = a / b
                self.hafiza += sonuc
                self.son_islem_sonucu = sonuc
                return sonuc
            else:
                return "Hata: Bölme işlemi için bölen sıfır olamaz!"
        except Exception as e:
            return f"Hata: {str(e)}"
    
    def karekok(self, a):
        try:
            if a >= 0:
                sonuc = math.sqrt(a)
                self.hafiza += sonuc
                self.son_islem_sonucu = sonuc
                return sonuc
            else:
                return "Hata: Negatif bir sayının veya sıfırın karekökü alınamaz!"
        except Exception as e:
            return f"Hata: {str(e)}"
    
    def kok_alma(self, a, b):
        try:
            if a > 0:
                sonuc = a ** (1/b)
                self.hafiza += sonuc
                self.son_islem_sonucu = sonuc
                return sonuc
            else:
                return "Hata: Negatif bir sayının veya sıfırın kökü alınamaz!"
        except Exception as e:
            return f"Hata: {str(e)}"
    
    def yuzde_hesapla(self, a, b):
        try:
            sonuc = (a * b) / 100
            self.hafiza += sonuc
            self.son_islem_sonucu = sonuc
            return sonuc
        except Exception as e:
            return f"Hata: {str(e)}"
    
    def grand_total(self):
        return self.hafiza
    
    def sifirla(self):
        self.hafiza = 0
        self.son_islem_sonucu = 0  # Son işlem sonucunu da sıfırlıyoruz
        print("Hafıza sıfırlandı.")
    
    def cikis(self):
        print("Programdan çıkılıyor...")
        sys.exit()
    
    def sayi_al(self, mesaj):
        while True:
            secim = input(f"{mesaj} (hafızadaki sonucu kullanmak için 'h', son işlemi kullanmak için 's' girin): ")
            if secim == 'h':
                return self.hafiza
            elif secim == 's':
                return self.son_islem_sonucu
            try:
                return float(secim)
            except ValueError:
                print("Geçersiz giriş, lütfen bir sayı girin veya 'h' ya da 's' tuşuna basarak hafızadaki veya son işlemdeki sonucu kullanın.")
    
    def islem_sec(self):
        while True:
            print("""
1: Toplama
2: Çıkarma
3: Çarpma
4: Bölme
5: Karekök Alma
6: Kök Alma
7: Yüzde Hesaplama
8: Grand total
9: Hafızayı Sıfırla
0: Çıkış
""")
            
            secim = input("Yapmak istediğiniz işlemi seçin: ")
            
            if secim == "1":
                a = self.sayi_al("Birinci sayıyı girin")
                b = self.sayi_al("İkinci sayıyı girin")
                print("Sonuç: ", self.toplama(a, b))
            elif secim == "2":
                a = self.sayi_al("Birinci sayıyı girin")
                b = self.sayi_al("İkinci sayıyı girin")
                print("Sonuç: ", self.cikarma(a, b))
            elif secim == "3":
                a = self.sayi_al("Birinci sayıyı girin")
                b = self.sayi_al("İkinci sayıyı girin")
                print("Sonuç: ", self.carpma(a, b))
            elif secim == "4":
                a = self.sayi_al("Bölünecek sayıyı girin")
                b = self.sayi_al("Böleni girin")
                print("Sonuç: ", self.bolme(a, b))
            elif secim == "5":
                a = self.sayi_al("Karekökünü almak istediğiniz sayıyı girin")
                print("Sonuç: ", self.karekok(a))
            elif secim == "6":
                a = self.sayi_al("Kökünü almak istediğiniz sayıyı girin")
                b = self.sayi_al("Kökün derecesini girin")
                print("Sonuç: ", self.kok_alma(a, b))
            elif secim == "7":
                a = self.sayi_al("Yüzdesini hesaplamak istediğiniz sayıyı girin")
                b = self.sayi_al("Yüzde değerini girin")
                print("Sonuç: ", self.yuzde_hesapla(a, b))
            elif secim == "8":
                print("Hafızadaki Toplam Sonuç: ", self.grand_total())
            elif secim == "9":
                self.sifirla()
            elif secim == "0":
                self.cikis()
            else:
                print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    hesap_makinesi = HesapMakinesi()
    hesap_makinesi.islem_sec()
