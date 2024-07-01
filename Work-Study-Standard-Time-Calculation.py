Rakam = [("0"),("1"),("2"),("3"),("4"),("5"),("6")]
b=1
liste_top = 0.0
#Veri Girişi Sütun
while True:
    sutun_sayisi = input("Kaç adet gözlem zamanınız var: \n")
    if not sutun_sayisi.isnumeric():
        print("Sayı girişi yapınız.\n")
    else:
        break
#Veri Girişi Satır
while True:
    satir_sayisi = input ("Kaç adet gözlem yapılacak eleman var: \n")
    if not satir_sayisi.isnumeric():
        print("Sayı girişi yapınız.\n")
    else:
        break 
#Matris Oluşturma----------------------------------------------------------------------------------------
for i in range(int(satir_sayisi)):
    for a in range(int(sutun_sayisi)):
        a+=1
        veri = input("{}. eleman için {}. gözlem değerini girin:\n". format(b,a))
        
        liste_top +=  float(veri)
    print("Liste toplamı =", liste_top)
    liste_ort=liste_top/int(sutun_sayisi)
    print("Liste ortalaması=", liste_ort)
#Performans-------------------------------------------------------------------------------------------------------

    performans_beceri_puan=performans_caba_puan=performans_kosullar_puan=performans_tutarlilik_puan=0.00
    print ("\nPerformans Derecelendirme Skalasında")
    
    while True:
        performans_beceri = input("Becerisi; \nÜstün yetenekli = 1\nÇok iyi = 2,\nİyi = 3,\nOrta = 4\nVasat = 5\nZayıf = 6\nBelirtilmemişse 0 değerini girin.\nHangisine karşılık geliyorsa ekrana o sayıyı giriniz:")
        if performans_beceri in Rakam:
            if int(performans_beceri) ==0:
                performans_beceri_puan=0.00
            elif int(performans_beceri) == 1:
                performans_beceri_puan=0.15
            elif int(performans_beceri)==2:
                performans_beceri_puan=0.11
            elif int(performans_beceri)==3:
                performans_beceri_puan=0.06
            elif int(performans_beceri)==4:
                performans_beceri_puan=0.00
            elif int(performans_beceri)==5:
                performans_beceri_puan=-0.05
            elif int(performans_beceri)==6:
                performans_beceri_puan=-0.16
            break
        else:
            print ("Yanlış giriş yapıldı.\n")
            
    while True:
        performans_caba = input("\nÇabası; \nAşırı = 1\nÇok iyi = 2\nİyi = 3\nOrta = 4\nVasat = 5\nZayıf = 6\nBelirtilmemişse 0 değerini giriniz.\nHangisine karşılık geliyorsa ekrana o sayıyı giriniz:")
        if performans_caba in Rakam:
            if int(performans_caba)==0:
                performans_caba_puan=0.00
            elif int(performans_caba)==1:
                performans_caba_puan=0.13
            elif int(performans_caba)==2:
                performans_caba_puan=0.10
            elif int(performans_caba)==3:
                performans_caba_puan=0.05
            elif int(performans_caba)==4:
                performans_caba_puan=0.00
            elif int(performans_caba)==5:
                performans_caba_puan=-0.04
            elif int(performans_caba)==6:
                performans_caba_puan=-0.12
            break
        else:
            print ("Yanlış giriş yapıldı.")
            
            
    while True:
        performans_kosullar = input("\nKoşulları; \nİdeal = 1 \nÇok İyi = 2\nİyi = 3 \nOrta = 4 \nVasat = 5  \nZayıf = 6\nBelirtilmemişse 0 değerini giriniz.\nHangisine karşılık geliyorsa ekrana o sayıyı giriniz:")
        if performans_kosullar in Rakam:
            if int(performans_kosullar)==0:
                performans_kosullar_puan=0.00
            elif int(performans_kosullar)==1:
                performans_kosullar_puan=0.06
            elif int(performans_kosullar)==2:
                performans_kosullar_puan=0.04
            elif int(performans_kosullar)==3:
                performans_kosullar_puan=0.02
            elif int(performans_kosullar)==4:
                performans_kosullar_puan=0.00
            elif int(performans_kosullar)==5:
                performans_kosullar_puan=-0.03
            elif int(performans_kosullar)==6:
                performans_kosullar_puan=-0.07
            break
        else:
            print ("Yanlış giriş yapıldı.")
            
    
    while True:
        performans_tutarlilik = input("\nTutarlılığı; \nMükemmel = 1 \nÇok İyi = 2 \nİyi = 3 \nOrta = 4 \nVasat = 5 \nZayıf = 6\nBelirtilmemişse 0 değerini giriniz.\nHangisine karşılık geliyorsa ekrana o sayıyı giriniz:")
        if performans_tutarlilik in Rakam :
            if int(performans_tutarlilik)==0:
                performans_tutarlilik=0.00
            elif int(performans_tutarlilik)==1:
                performans_tutarlilik_puan=0.04
            elif int(performans_tutarlilik)==2:
                performans_tutarlilik_puan=0.03
            elif int(performans_tutarlilik)==3:
                performans_tutarlilik_puan=0.01
            elif int(performans_tutarlilik)==4:
                performans_tutarlilik_puan=0.00
            elif int(performans_tutarlilik)==5:
                performans_tutarlilik_puan=-0.02
            elif int(performans_tutarlilik)==6:
                performans_tutarlilik_puan=-0.04
            break
        else:
            print ("Yanlış giriş yapıldı.")

    performanslar_toplam = performans_beceri_puan + performans_caba_puan + performans_kosullar_puan + performans_tutarlilik_puan + 1.00

    print("\nPerformans Toplam = ",performanslar_toplam)
    
    normal_zaman = performanslar_toplam * liste_ort
    
    print("Normal Zaman =",normal_zaman)
    
    
#Tolerans-------------------------------------------------------------------------------------------------------
    tolerans_puan=0
    while True:
        secim = input("Tolerans değerleri toplamını kendiniz girecekseniz 1'e, değilse 0 girin.\n")
        if secim == "1" or secim =="0":
            break
        else:
            print ("0 veya 1 girin")

    if int(secim)==1:
    
        while True:
            tolerans=input("Tolerans toplam değerlerini ondalıksız girin.\n")
            if not tolerans.isnumeric():
                print("Sayı girişi yapınız")
            else:
                break

        tolerans_puan = 1.00 + (int(tolerans) * 0.01)
        print("tolerans değeri=", tolerans_puan)
        std= tolerans_puan* normal_zaman
        print("normal zaman=", std)
        
    
    
    elif int(secim) == 0:
    
        while True:
            cinsiyet = input("\nErkek ise 0, kadın ise 1 giriniz: \n")
            if cinsiyet == "1" or cinsiyet =="0":
                break
            else:
                print ("0 veya 1 girin")
        while True:
            print("\nKişisel Gereksinim:")
            if int(cinsiyet) == 1:
                kişisel_gereksinim = input("Kadınlarda kişisel gereksinim 2 ve 7 arasında bir değer alır. Kişisel gereksinim yoksa ekrana 0 girilir.\n Değeri giriniz:")
                if int(kişisel_gereksinim)>=2 and int(kişisel_gereksinim)<=7:
                    tolerans_puan+=int(kişisel_gereksinim)
                    break 
                elif kişisel_gereksinim =="0":
                    kişisel_gereksinim = 0
                    break
                else:
                    print("Geçersiz değer girdiniz")
            if int(cinsiyet) == 0:
                kişisel_gereksinim = input("Erkeklerde kişisel gereksinim 2 ve 5 arasında bir değer alır. Kişisel gereksinim yoksa ekrana 0 girilir.\n Değeri giriniz:")
                if int(kişisel_gereksinim)>=2 and int(kişisel_gereksinim)<=5:
                    tolerans_puan+=int(kişisel_gereksinim)
                    break
                elif kişisel_gereksinim == "0":
                    kişisel_gereksinim = 0
                    break
                else:
                    print("Geçersiz değer girdiniz")
                    
        while True:
            print("\nFiziksel Çaba:")
            fiziksel_caba = input("Çok hafif (0.5kg) = 0\nHafif (0.5-5 kg) = 1\nOrta (5-10 kg) = 2\nAğır (10-25 kg) = 3\nÇok ağır (25kg ve üstü) = 4\n" "Hangisine karşılık geliyorsa ekrana o sayıyı yazınız:")
            if fiziksel_caba in Rakam :
                if int(fiziksel_caba) == 0:
                    tolerans_puan+=0
                elif int(fiziksel_caba) == 1:
                    tolerans_puan+=3
                elif int(fiziksel_caba) == 2:
                    tolerans_puan+=6
                elif int(fiziksel_caba) == 3:
                    tolerans_puan+=9
                elif int(fiziksel_caba) == 4:
                    tolerans_puan+=12
                break
            else:
                print("Geçersiz değer girdiniz")
                
            
        while True:
            print("\nDüşünsel Çaba:")
            düşünsel_caba = input("İşi planlamak için normal dikkat=1\nKarmaşık işler için normal dikkat=2\nİşi planlamak için yoğun dikkat=3\nKarmaşık işler için yoğun dikkat=4\nBelirtilmemişse 0 değerini giriniz.\nHangisine karşılık geliyorsa ekrana o sayıyı yazınız:")
            if düşünsel_caba in Rakam:
                if int(düşünsel_caba) == 0:
                    tolerans_puan+=0
                elif int(düşünsel_caba) == 1:
                    tolerans_puan+=0
                elif int(düşünsel_caba) == 2:
                    tolerans_puan+=2
                elif int(düşünsel_caba) == 3:
                    tolerans_puan+=4
                elif int(düşünsel_caba) == 4:
                    tolerans_puan+=10
                break
            else:
                print("Geçersiz değer girdiniz")
                    
                    
        while True:
            print("\nÇalışma Pozisyonu:")
            çalışma_pozisyonu = input("Durma ve yürümede serbest=1\nSabit duruş=2\nSabit ayakta duruş=3\nÇökme ve eğilme=4\nEllerin uzanması ve omuzların kalkması=5\nBelirtilmemişşe 0 değerini giriniz.\nHangisine karşılık geliyorsa ekrana o sayıyı yazınız: ")
            if çalışma_pozisyonu in Rakam:
                if int(çalışma_pozisyonu) == 0:
                    tolerans_puan+=0
                elif int(çalışma_pozisyonu) == 1:
                    tolerans_puan+=0
                elif int(çalışma_pozisyonu) == 2:
                    tolerans_puan+=1
                elif int(çalışma_pozisyonu) == 3:
                    tolerans_puan+=5
                elif int(çalışma_pozisyonu) == 4:
                    tolerans_puan+=8
                elif int(çalışma_pozisyonu) == 5:
                    tolerans_puan+=15
                break
            else:
                print("Geçersiz değer girdiniz\n")
                    
        lista=["Atmosfer","Isı","Gürültü","Genel","Koruyucu elbiseler"]
        listb=["Temiz hava iyi havalandırma = 1, Zararsız fakat kötü koku = 2, Zararlı toz veya gaz = 3, Belirtilmemişse 0 giriniz.","Soğuk (5-10C)=1,  Normal (10-25C)=2, Sıcak (25C- )=3, Belirtilmemişse 0 giriniz.",
               "Normal iş gürültüsü=1, Normal makine gürültüsü=2, Yüksek sabit gürültü=3, Yüksek frekanslı gürültü=4, Belirtilmemişse 0 giriniz.",
               "Kirli=1, Islak döşeme=2, Titreşim=3, Monotonluk=4, Düşünsel yorgunluk=5, Belirtilmemişse 0 giriniz.",
               "Takım=1, Eldiven=2, Ağır ve özel yelek=3, Maske=4, Belirtilmemişse 0 giriniz."]
        listepk=[]
        d=0
        e=1
        for i in range(5):
            print(lista[i],"koşulu")
            while True:
                pu =input(f"{tuple(listb[d:e])}uygun olan seçenek numarasını girin :")
                if pu == "0" or pu =="1" or pu == "2" or pu == "3" or pu == "4" or pu =="5":
                    break
                else:
                    print("İstenen değerlerden birini giriniz.")
            e = e + 1
            d = d + 1
            listepk.append(pu)
        
        if listepk[0]=="0":
            tolerans_puan+=0
        elif listepk[0]=="1":
            tolerans_puan+=0
        elif listepk[0]=="2":
            tolerans_puan+=3
        elif listepk[0]=="3":
            tolerans_puan+=8
        else:
            tolerans_puan+=0
        
        if listepk[1]=="0":
            tolerans_puan+=0
        elif listepk[1]=="1":
            tolerans_puan+=3
        elif listepk[1]=="2":
            tolerans_puan+=0
        elif listepk[1]=="3":
            tolerans_puan+=8
        else:
            tolerans_puan+=0
            
        if listepk[2]=="0":
            tolerans_puan+=0
        elif listepk[2]=="1":
            tolerans_puan+=0
        elif listepk[2]=="2":
            tolerans_puan+=1
        elif listepk[2]=="3":
            tolerans_puan+=5
        elif listepk[2]=="4":
            tolerans_puan+=8
        else:
            tolerans_puan+=0
            
        if listepk[3]=="0":
            tolerans_puan+=0
        elif listepk[3]=="1":
            tolerans_puan+=3
        elif listepk[3]=="2":
            tolerans_puan+=4
        elif listepk[3]=="3":
            tolerans_puan+=4
        elif listepk[3]=="4":
            tolerans_puan+=2
        elif listepk[3]=="5":
            tolerans_puan+=5
        else:
            tolerans_puan+=0
            
        
        if listepk[4]=="0":
            tolerans_puan+=0
        elif listepk[4]=="1":
            tolerans_puan+=0
        elif listepk[4]=="2":
            tolerans_puan+=2
        elif listepk[4]=="3":
            tolerans_puan+=15
        elif listepk[4]=="4":
            tolerans_puan+=15
        else:
            tolerans_puan+=0
            
        tolerans_puan = 1 + (int(tolerans_puan)*0.01)
            
        print("Tolerans Değer:", tolerans_puan)
     
        stzd = normal_zaman * tolerans_puan 
    
        print("Standart Zaman Değeri:", stzd)
    
    b+=1