<div align="center">

<a href="https://evolink.ai/gemini-4-neon?utm_source=github&amp;utm_medium=banner&amp;utm_campaign=awesome-gemini-4-neon-use-cases&amp;utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/banner/neon-use-cases-b56d48e57ac3.png" alt="Gemini 4 Neon Use Cases" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)

[![English](https://img.shields.io/badge/English-111111)](README.md)
[![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md)
[![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md)
[![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md)
[![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md)
[![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md)
[![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md)
[![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md)
[![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md)
[![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md)
[![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>

<a id="introduction"></a>
## 🍌 Giriş

**Genel iş akışları, görsel prototipler, entegrasyonlar ve değerlendirmeler aracılığıyla Gemini 4 Neon'u keşfedin. Her vaka kendi kaynağına bağlanır ve modelin rolünü ve rapor edilen sonucu açıklar.**

<a id="overview"></a>
## 📊 Genel Bakış

**252 Gemini 4 Neon kullanım örneği** ve kaynaklardan 321 görsel.

- Mühendislik ve Entegrasyonlar · 24
- Grafik ve Arayüz Prototipleri · 144
- Oyunlar ve Simülasyonlar · 20
- Bilgi Çalışması · 21
- Değerlendirmeler ve Limitler · 43

> [!NOTE]
> Her örnek kendi kaynağına bağlantı verir. Süreler, maliyetler ve kıyaslama sonuçları belirtilen test koşullarına aittir.

<a id="quick-start"></a>
## ⚡ Hızlı başlangıç

1. Menüden bir vaka seçin ve orijinal kaynağını açın.
2. Kaynağın bildirdiği model rolünü, aracı, ayarları ve sonucu kontrol edin.
3. Vakaları eşleşen görev ve ayarlarla karşılaştırın. İçerik oluşturucunun bildirdiği süreleri ve maliyetleri, bu çalıştırmalardan elde edilen gözlemler olarak değerlendirin.

<a id="menu"></a>
## 📑 Menü

| Örnek | Kategori | Ne gösteriyor? | Tür |
|---|---|---|---|
| [Gözetimsiz çalıştırmalar sırasında istikrarsızlığı gözlemleyin](#case-1) | Mühendislik ve Entegrasyonlar | Testi yapan kişi, çıkış gününde Neon’u grafik arayüz olmadan çalıştırırken kararsızlık gözlemlediğini ve çalışmayı Opus 5.5’in izlediğini belirtti. | Limit |
| [Mantık kapısı simülasyonu oluşturun](#case-2) | Mühendislik ve Entegrasyonlar | Yazar, simüle edilmiş mantık kapılarından ve devre kartlarından retro terminal ekranına kadar uzanan etkileşimli bir elektronik demosu gösteriyor. | Demo |
| [tscircuit'de bir Bluetooth diş fırçası tasarlayın](#case-3) | Mühendislik ve Entegrasyonlar | Bir tscircuit bakımcısı, Bluetooth elektrikli diş fırçasında Neon Yüksek, Opus 5.5 Yüksek ve Sol 6.2 Yüksek'i karşılaştırdı. | Evaluation |
| [Muse'un yan konuşmasını Neon'a aktarın](#case-4) | Mühendislik ve Entegrasyonlar | Yazar, istekleri ve yanıtları Neon'a ileten bir Muse yan sohbeti oluşturdu. | Integration |
| [Üç modelli bir T3 Code iş akışında metin yazarlığı için Neon'yi kullanın](#case-5) | Mühendislik ve Entegrasyonlar | Geliştirici, Neon'ye çok modelli bir T3 Code iş akışı içinde metin yazarlığı rolünü verir. | Integration |
| [Spotify tavsiye MCP'sini yeniden çalışın](#case-6) | Mühendislik ve Entegrasyonlar | Yaratıcı, orijinal olarak Argon ile oluşturulmuş bir Spotify tavsiye MCP'sini revize etmek için Neon'u kullandı. | Integration |
| [Bir arabanın SVG yandan görünümünü çizin](#case-7) | Grafik ve Arayüz Prototipleri | Yaratıcı, bir BMW M4 CS yandan görünüşlü SVG oluşturmak için AI Studio'da Neon High'ı kullandı. | Demo |
| [Bir SVG test serisi çalıştırın](#case-8) | Grafik ve Arayüz Prototipleri | Test cihazı, Neon SVG test serisinde üç çıktı paylaştı. | Demo |
| [Three.js'de bir pelikanı canlandırın](#case-9) | Grafik ve Arayüz Prototipleri | Test cihazı, Three.js'nin bisiklet üzerindeki pelikan çıktısını Neon'a bağlar. | Demo |
| [xhigh'de bir SVG portresi çizin](#case-10) | Grafik ve Arayüz Prototipleri | Testi yapan kişi, Neon xhigh'e atfedilen Ana de Armas'ın bir portresini paylaşıyor. | Demo |
| [Bisiklet süren bir pelikanı orta eforla canlandırın](#case-11) | Grafik ve Arayüz Prototipleri | Yazar, bir pelikan bisiklet demosu oluşturmak için Neon'u orta düzeyde bir çabayla kullandı ve videoyu yayınladı. | Demo |
| [İki voksel bahçesi sahnesini karşılaştırın](#case-12) | Grafik ve Arayüz Prototipleri | Yazar, GPT-6.2 Sol xhigh sonucunun yanı sıra Neon xhigh'den bir voksel bahçesi yayınladı. | Evaluation |
| [Three.js ve GLSL sahnesi oluşturun](#case-13) | Grafik ve Arayüz Prototipleri | İçerik oluşturucu, Neon'dan bir Three.js ve GLSL çıktısı paylaşıyor ve iki dakika 40 saniyelik bir çalışma rapor ediyor. | Demo |
| [Tamamen kodla resimler oluşturun](#case-14) | Grafik ve Arayüz Prototipleri | İçerik oluşturucu, resimleri işleyen kodu yazmak için erken erişim Neon'u kullandığını bildiriyor. | Demo |
| [Pelikan bisiklet animasyonlarını karşılaştırın](#case-15) | Grafik ve Arayüz Prototipleri | Testi yapan kişi bir pelikan animasyonunu Neon, Hydrogen, GPT-6.2 Astra ve GPT-6.2 Sol'da karşılaştırdı. | Evaluation |
| [Three.js bisiklet animasyonlarını üç modelde karşılaştırın](#case-16) | Grafik ve Arayüz Prototipleri | Test cihazı Neon, Opus 5.5 ve Carbon'un Three.js bisiklet karşılaştırmasını yayınladı. | Evaluation |
| [Okyanusta uzun bir gemi render edin](#case-17) | Grafik ve Arayüz Prototipleri | Testi yapan kişi, Neon xhigh'e atfedilen bir okyanusta yelken sahnesi paylaştı. | Demo |
| [Bir voksel pagodası oluşturun](#case-18) | Grafik ve Arayüz Prototipleri | Testi yapan kişi Neon xhigh'de oluşturulan bir voksel pagodasını yayınlıyor. | Demo |
| [Bisiklete binen hayal kırıklığına uğramış bir pelikan çizin](#case-19) | Grafik ve Arayüz Prototipleri | Yaratıcı, bisiklete binen hayal kırıklığına uğramış bir pelikanın SVG'sini çizmek için AI Studio'da Neon High'ı kullandı. | Demo |
| [Gamepad çizimlerini GPT-6.2 Sol ile karşılaştırın](#case-20) | Grafik ve Arayüz Prototipleri | Testi yapan kişi, her modelin mevcut en yüksek muhakemesinde aynı istemi kullandı ve çıktıların benzer olduğuna karar verdi. | Evaluation |
| [3 boyutlu deniz uçağı oluşturun](#case-21) | Grafik ve Arayüz Prototipleri | Testi gerçekleştiren kişi, 3D deniz uçağı oluşturmak için Neon xhigh'i kullandı ve bir video paylaştı. | Demo |
| [2 boyutlu bir at çizin](#case-22) | Grafik ve Arayüz Prototipleri | Yaratıcı iki boyutlu bir at üretmek için Neon'u kullandı ve çıktıyı yayınladı. | Demo |
| [Yağmurlu bir market sahnesini test edin](#case-23) | Grafik ve Arayüz Prototipleri | Testi yapan kişi Neon ve GPT-6.2 Sol için aynı istemi kullandı ve karşılaştırmayı yayınladı. | Evaluation |
| [Tek bir görüntüden dört ayaklı bir robotu canlandırın](#case-24) | Grafik ve Arayüz Prototipleri | Geliştirici Neon'a tek bir referans görseli verdi ve 3 boyutlu bir model istedi. | Demo |
| [Keats'i vanilya JavaScript'te canlandırın](#case-25) | Grafik ve Arayüz Prototipleri | Bir Google ekibi üyesi, Keats'in To Autumn filminin vanilya JavaScript animasyonu için GeokenAI ve Neon'a teşekkür ediyor. | Demo |
| [Triceratops demosu oluşturun](#case-26) | Grafik ve Arayüz Prototipleri | Yaratıcı, Triceratops gösterisini Neon'a atfediyor. | Demo |
| [3D dişli takımı görüntülerini karşılaştırın](#case-27) | Grafik ve Arayüz Prototipleri | Test cihazı, etiketli akıl yürütme seviyelerinde Neon, Carbon, Astra ve Sol için dişli mekanizması görüntülerini gösterir. | Evaluation |
| [Tek bir HTML dosyasında on etkileşimli efekt oluşturun](#case-28) | Grafik ve Arayüz Prototipleri | Bir Google ekibi üyesi, 27 KB'lik bir HTML dosyasında on etkileşimli 3D efekt oluşturmak için Neon'u kullandığını bildirdi. | Demo |
| [Antigravity Swarm ile bir Blender laboratuvar tezgahı oluşturun](#case-29) | Grafik ve Arayüz Prototipleri | Google, Gemini 4 ailesi temalı bir laboratuvar tezgahı sahnesi oluşturmak için Neon'un Antigravity Swarm ve Blender'ı kullandığını gösterdi. | Integration |
| [Opus 5.5 ile mimari illüstrasyonları karşılaştırın](#case-30) | Grafik ve Arayüz Prototipleri | Testi yapan kişi, aynı istemi kullanarak modelleri mevcut en yüksek mantıkla karşılaştırdı. | Evaluation |
| [Voyager 1’in uçuşunu görselleştirin](#case-31) | Grafik ve Arayüz Prototipleri | Yazar, fırlatma aşamasından Jüpiter karşılaşmasına kadar geçen 3 boyutlu Voyager 1 sekansını ve uzay aracının yakın çekimini gösteriyor. | Demo |
| [3B bir planetaryum oluşturun](#case-32) | Grafik ve Arayüz Prototipleri | Yazar, gezegenler arasında hareket eden bir 3 boyutlu planetaryumu ve takımyıldız görünümünü gösteriyor. | Demo |
| [Babbage’ın 2 Numaralı Fark Makinesi’ni görselleştirin](#case-33) | Grafik ve Arayüz Prototipleri | Yazar, dişli düzenekleri ve sayısal ekranıyla Babbage'nin 2 Numaralı Fark Motorunun 3 boyutlu görselleştirmesini gösteriyor. | Demo |
| [Antikythera mekanizmasını görselleştirin](#case-34) | Grafik ve Arayüz Prototipleri | Yazar, kurtarılan nesne, yeniden inşa edilen dişliler ve bir kadran arasında geçiş yapan bir 3D Antikythera mekanizması demosunu gösteriyor. | Demo |
| [Hava akışını gösteren bir rüzgâr tüneli prototipi yapın](#case-35) | Grafik ve Arayüz Prototipleri | Yazar, farklı şekiller etrafında görünür hava akışı düzeneklerine sahip bir 3 boyutlu rüzgar tüneli demosu gösteriyor. | Demo |
| [King’s College Şapeli’nin kesitini oluşturun](#case-36) | Grafik ve Arayüz Prototipleri | Yazar, King's College Şapeli'nin dış ve iç mekan arasında geçiş yapan 3 boyutlu bir kesitini gösteriyor. | Demo |
| [Nehir üzerindeki viyadüğü ve çevresini görselleştirin](#case-37) | Grafik ve Arayüz Prototipleri | Yazar, çok kemerli bir viyadük, bir tren ve çeşitli görsellerle birlikte 3 boyutlu bir nehir vadisini gösteriyor. | Demo |
| [Cambridge’den esinlenen bir 3B şehir görünümü oluşturun](#case-38) | Grafik ve Arayüz Prototipleri | Yazar, modellenen blokların havadan ve daha yakından görüntüleriyle Cambridge'den ilham alan bir şehir görselleştirmesi gösteriyor. | Demo |
| [Neon temalı bir Dünya oluşturma](#case-39) | Grafik ve Arayüz Prototipleri | Yaratıcı, neon temalı bir gezegen oluşturmak için Neon'u Antigravity'de yüksek olarak kullandı. | Demo |
| [Bir yat sahnesini yineleyin](#case-40) | Grafik ve Arayüz Prototipleri | Yaratıcı, Neon'un bir yat sahnesini iyileştirdiğini ve çıktıyı gösterdiğini bildiriyor. | Demo |
| [Özel bir VFX aracında kostüm malzemeleri hazırlayın](#case-41) | Grafik ve Arayüz Prototipleri | Yaratıcı, kostüm malzemeleri hazırlamak için Neon'u kullandı ve sonuçların altı resmini yayınladı. | Demo |
| [Voksel Ninjago sahnelerini karşılaştırın](#case-42) | Grafik ve Arayüz Prototipleri | Kaynak, Neon ve Fable 5.2'yi bir voksel rekreasyonunda karşılaştırıyor. | Evaluation |
| [Pelikan ürünü hareketli grafiği oluşturun](#case-43) | Grafik ve Arayüz Prototipleri | Yaratıcı, Neon'a pelikan temalı bir ürün hareketli grafiği sağladığını söylüyor. | Demo |
| [New York City sahne prototiplerini karşılaştırın](#case-44) | Grafik ve Arayüz Prototipleri | Testi yapan kişi Neon'un Brooklyn Köprüsü'nü, Özgürlük Anıtı'nı ve taksilerin bulunduğu bir caddeyi içerdiğini bildirdi. | Evaluation |
| [Muz görsel testi yapın](#case-45) | Grafik ve Arayüz Prototipleri | Testi yapan kişi Muz Testi başlıklı bir test için bir Neon çıktısı yayınlar. | Demo |
| [Perili bir katedrali tek seferde karşılaştırın](#case-46) | Grafik ve Arayüz Prototipleri | Testi yapan kişi Neon ve GPT-6.2 Sol'a aynı perili katedral görevini verdi. | Evaluation |
| [Antigravity'de bir telefon aksamının prototipini yapın](#case-47) | Grafik ve Arayüz Prototipleri | Geliştirici, Antigravity'de Neon'u kullandı ve tasarım bileşenlerinden oluşan bir pano ile işlenmiş bir telefon aksamını gösterdi. | Demo |
| [Etkileşimli bir tarihi yelkenli gemi oluşturun](#case-48) | Grafik ve Arayüz Prototipleri | Yazar, sıfır atışlı bir 3D yelkenli gemi gösterimi yayınladı. | Demo |
| [JavaScript'te bir model tanıtımı tasarlama](#case-49) | Grafik ve Arayüz Prototipleri | Yazar, modeli tanıtan bir hareketli grafik oluşturmak için Neon'u kullandı. | Demo |
| [Tek geçişte kayak kulübesi sahnesi oluşturun](#case-50) | Grafik ve Arayüz Prototipleri | DesignArena, Neon ve Argon'dan aynı Alp kulübesi ortamını oluşturmalarını istedi ve yan yana çıktıları yayınladı. | Evaluation |
| [Bir voksel fantezi kalesi oluşturun](#case-51) | Grafik ve Arayüz Prototipleri | Yaratıcı, Neon xhigh'de üretilen bir voksel kalesini paylaşıyor. | Demo |
| [Ahtapot bisiklet animasyonunu Astra ile karşılaştırın](#case-52) | Grafik ve Arayüz Prototipleri | Test kaydında Astra (xhigh) 21 dakika 53 saniye ve 2,52 USD, Neon (high) ise 41 dakika ve 4,02 USD sürdü. | Evaluation |
| [Three.js kelebek animasyonu](#case-53) | Grafik ve Arayüz Prototipleri | Bir yaratıcı, Three.js kelebek animasyonu oluşturmak için Antigravity'de Neon xhigh'i kullandı. | Demo |
| [Referans görüntülerden bileşenler ve hareket oluşturun](#case-54) | Grafik ve Arayüz Prototipleri | Yaratıcı, çeşitli bileşenleri ve bunlara eşlik eden hareketleri oluşturmak için görsel referanslar kullandı. | Demo |
| [Three.js'de piksel sihirbazı dünyası](#case-55) | Grafik ve Arayüz Prototipleri | Bir yaratıcı Neon'a referans görseller verdi ve Three.js sahnesini üç geçişte geliştirdi. | Demo |
| [Kale oluşturma karşılaştırması](#case-56) | Grafik ve Arayüz Prototipleri | İçerik oluşturucu, kale karşılaştırması için Neon'u kullandı ve video ve fotoğraflar yayınladı. | Evaluation |
| [Alan Turing’in 1936’daki çalışma odasını yeniden oluşturun](#case-57) | Grafik ve Arayüz Prototipleri | Google, arşiv fotoğraflarından etkileşimli bir yeniden yapılandırma oluşturmak için Neon'u Antigravity Swarm ile birlikte kullandı. | Demo |
| [Yan kaydırmalı bir engel oyunu oluşturun](#case-58) | Oyunlar ve Simülasyonlar | Testi yapan kişi Neon'dan Flappy Bird tarzı bir prototip istedi ve bir kayıt yayınladı. | Demo |
| [Kılıç ve kalkan savaş sahnelerini karşılaştırın](#case-59) | Oyunlar ve Simülasyonlar | Testi yapan kişi, bir savaş oyunu sahnesi için Fable 5.2 ve Neon çıkışları etiketli bir video yayınladı. | Evaluation |
| [Synthwave tarzında bir mini golf oyunu yapın](#case-60) | Oyunlar ve Simülasyonlar | Google Antigravity, Gemini 4 Neon’un Swarm ile tek bir istemden 3B mini golf oyunu oluşturmasını gösteriyor. | Demo |
| [Animasyonlu şövalye düellolarını karşılaştırın](#case-61) | Oyunlar ve Simülasyonlar | Testi yapan kişi, zırhlı karakterler arasında bir düello için Opus 5.5 ve Neon çıkışlarını ayrı ayrı etiketledi. | Evaluation |
| [Tek bir HTML dosyasında dışavurumcu bir sanat oyunu yapın](#case-62) | Oyunlar ve Simülasyonlar | Geliştirici, tek bir HTML dosyasında bulunan sonsuz bir JavaScript sanat oyunu oluşturmak için Neon'u kullandı. | Demo |
| [Buz patronu oyun prototiplerini karşılaştırın](#case-63) | Oyunlar ve Simülasyonlar | Testi yapan kişi, birinci şahıs buz patronu karşılaşması için etiketli Neon ve Opus 5.5 çıkışlarını yayınladı. | Evaluation |
| [Karpuz basketbol demosu](#case-64) | Oyunlar ve Simülasyonlar | Testi yapan kişi bir Neon karpuz basketbol videosu paylaşıyor. | Demo |
| [Gaussian sıçrayan bir fırın platformu inşa edin](#case-65) | Oyunlar ve Simülasyonlar | Yaratıcı, C++20 ve WebGPU Gaussian sıçrama motorunu dört kuleli bir platform oyununa dönüştürmek için Neon'u kullandı. | Demo |
| [Antigravity Swarm ile 3 boyutlu bir oyun oluşturun](#case-66) | Oyunlar ve Simülasyonlar | Geliştirici, küçük bir 3D oyun oluşturmak için Neon ve Antigravity Swarm'ı kullandı. | Demo |
| [Uzay yarışı prototipi](#case-67) | Oyunlar ve Simülasyonlar | Bir yaratıcı, yüksek mantıkla Neon'la bir uzay yarışçısı yaptığını bildirdi. | Demo |
| [Kule savunma prototipi](#case-68) | Oyunlar ve Simülasyonlar | Bir geliştirici, Neon yapılı bir kule savunma prototipinin oynanışını yayınladı. | Demo |
| [Birinci şahıs kayak simülatörü oluşturun](#case-69) | Oyunlar ve Simülasyonlar | Google, Mont Blanc ve Chamonix arazisinde bir WebGL2 serbest sürüş simülatörü oluşturmak için Neon'u kullandığını bildiriyor. | Demo |
| [Model seçimlerini bir araştırma tablosunda özetleme](#case-70) | Bilgi Çalışması | Yazar, Gemini 4 model seçim tablosunu Neon tarafından gerçekleştirilen araştırmaya bağlıyor. | Demo |
| [Neon ile birlikte bir lansman filmi oluşturun](#case-71) | Bilgi Çalışması | Bir Google ekibi üyesi Neon ile birlikte bir film yapıldığını bildiriyor ve sonucu paylaşıyor. | Demo |
| [Bir VR oyununda ekipman mekaniğini açıklama](#case-72) | Bilgi Çalışması | Yazar, Meta Quest oyunu H3VR2'deki ekipmanı özetlemek için Neon'u kullandı ve resimli bir açıklayıcı ekledi. | Demo |
| [Görüntü kırpma sırasında öz değerlendirmeyi inceleyin](#case-73) | Bilgi Çalışması | Testçi, Neon'un bir görüntü düzenleme testi sırasında kendi ürününe iltifat ettiğini bildirdi. | Limit |
| [Bir makaleyi düzenlenebilir slaytlara dönüştürün](#case-74) | Bilgi Çalışması | Yaratıcı, Neon'a bir makale gönderdi ve herkese açık slayt oluşturma becerisini kullandı. | Demo |
| [Bir fantastik roman açılışı oluşturun](#case-75) | Bilgi Çalışması | Yazar Neon'u bir yazma testi için kullandı ve bir Çin fantastik öyküsünün açılışını yayınladı. | Demo |
| [Orijinal bir Dario şakasını yorumlayın](#case-76) | Bilgi Çalışması | Yazar, Neon'un yazdıkları bir şakayı anladığını ancak Opus 5.5'in anlamadığını bildirdi. | Evaluation |
| [E-Tablolar'da bilgisayarlı görüntü laboratuvarı oluşturma](#case-77) | Bilgi Çalışması | Google, bir Neon sürüsünün bir referans görselini 100.000 hücreli bir e-tabloya dönüştürdüğünü bildiriyor. | Demo |
| [Vals Index'te alan adı performansını ölçün](#case-78) | Değerlendirmeler ve Limitler | Vals AI, Neon için %70,9'luk bir puan elde etti ve toplamda Fable 5.2'nin 0,4 puan gerisinde ikinci sırada yer aldı. | Benchmark |
| [Erken erişim sırasında etkileşimli demoları test edin](#case-79) | Değerlendirmeler ve Limitler | Yazar, 17 etkileşimli demo oluşturmak için Neon'u Antigravity'de kullandığını ve ek kodlama ve araç testlerini belgelediğini bildiriyor. | Evaluation |
| [Agent Arena'daki temsilci oturumlarını karşılaştırın](#case-80) | Değerlendirmeler ve Limitler | Arena, Neon High için 1336 puan, ikincilik ve görev başına 2,82 USD medyan maliyet bildirdi. | Benchmark |
| [Neon'u Text Arena'ya yerleştirin](#case-81) | Değerlendirmeler ve Limitler | Arena, Neon High'ı 1518'de, Carbon High'ı 1526'da ve Argon High'ı 1521'de takip ediyor. | Benchmark |
| [Wojak-Bench’te 3B baskıya uygun figürleri değerlendirin](#case-82) | Değerlendirmeler ve Limitler | Kıyaslama ortak yazarı, Neon'un dördüncü sırada çıkış yaptığını bildirdi. Yayınlanan lider tablosu anlık görüntüsü Neon'a 1056 puan veriyor. | Benchmark |
| [Kodlama aracılarını koşum takımlarıyla karşılaştırın](#case-83) | Değerlendirmeler ve Limitler | Yapay Analiz, Antigravity CLI ile Neon xhigh için 59 ve Carbon high için 55 rapor ediyor. | Benchmark |
| [AA-Briefcase üzerindeki bilgi çalışmasını değerlendirin](#case-84) | Değerlendirmeler ve Limitler | Yapay Analiz, Neon xhigh için 1700 Elo ve Carbon high için 1611 Elo rapor ediyor. | Benchmark |
| [Zaman Artificial Analysis Intelligence Index görevleri](#case-85) | Değerlendirmeler ve Limitler | Yapay Analiz, Neon xhigh için görev başına yaklaşık 21 dakika ve Carbon high için 36 dakika olduğunu bildirdi. | Benchmark |
| [Otomat iş simülasyonu çalıştırın](#case-86) | Değerlendirmeler ve Limitler | Andon Labs, yayınlandığı sırada Neon'u ilk olarak Vending-Bench 2'de bildirdi. | Benchmark |
| [RuneScape kıyaslama zaman sınırını inceleyin](#case-87) | Değerlendirmeler ve Limitler | Karşılaştırma yazarı, Neon'un iddialı stratejilerinin son teslim tarihinden önce tamamlanmadığını bildirdi. | Limit |
| [APEX-Agents'ta profesyonel görevleri çalıştırın](#case-88) | Değerlendirmeler ve Limitler | Mercor, APEX-Agents'ta Neon için %82,9 Pass@1 ve %88,9 ortalama puan bildirdi. | Benchmark |
| [CursorBench 4.1'de Neon ve Hydrogen'yi karşılaştırın](#case-89) | Değerlendirmeler ve Limitler | Cursor, varsayılan eforda Neon için %63,7 ve Hydrogen için %57,3 rapor eder. | Benchmark |
| [CUDA hata ayıklama görevinde duvar saati süresini ölçün](#case-90) | Değerlendirmeler ve Limitler | Yazar, modelleri bir CUDA hata ayıklama isteminde çalıştırdı ve belirteç hızını ve uçtan uca gecikmeyi ayrı ayrı ölçtü. | Benchmark |
| [Tuesday@Work'de işyeri görevlerini ölçün](#case-91) | Değerlendirmeler ve Limitler | Surge AI, Neon'u değerlendirme paketinde çalıştırdı ve Tuesday@Work'te 71,6 rapor ederken, Fable 5.2 için 71,2 rapor verdi. | Benchmark |
| [Antigravity'deki ceza kararlarını inceleyin](#case-92) | Değerlendirmeler ve Limitler | Penalty Bench'in yaratıcısı, Neon'un Antigravity koşum takımını kullanarak kıyaslamada ilk sırada yer aldığını bildirdi. | Benchmark |
| [Tarayıcı Kullanım karşılaştırması](#case-93) | Değerlendirmeler ve Limitler | Tarayıcı Kullanımı, Neon için Opus 5.5 sonucuna eşit olan %74'lük bir sonuç bildirdi ve GPT-6.2 Sol için %82'ye karşılık geldi. | Benchmark |
| [PandaCode'da araç çağrısı hatalarını ölçün](#case-94) | Değerlendirmeler ve Limitler | Yazar, bir lansman gecesi penceresi sırasında 9.465 Neon çağrısında 65 başarısız araç çağrısını ölçtü. | Evaluation |
| [43 soruluk Plotly veri analizi karşılaştırmasını çalıştırın](#case-95) | Değerlendirmeler ve Limitler | Plotly'nin düzeltilmiş sonucu, Neon'un 43 yanıttan 43'ünü aldığını ve tüm çalışma için 17,03 USD rapor ettiğini gösteriyor. | Benchmark |
| [Three.js ile çöp adam dövüşünü canlandırmak](#case-96) | Grafik ve Arayüz Prototipleri | Yapımcı bu Three.js animasyonu için Antigravity ortamında Swarm ile birlikte Neon kullandı. | Demo |
| [Üç modelin yelkenli sahnelerini karşılaştırmak](#case-97) | Grafik ve Arayüz Prototipleri | Yapımcı Claude Fable 5.2, GPT-6.2 Astra ve Gemini 4 Neon çıktılarını aynı videoda üst üste yerleştirdi. | Evaluation |
| [Avatarları hareketli koleksiyon kartlarına dönüştürmek](#case-98) | Grafik ve Arayüz Prototipleri | Yapımcı Gemini 4 Neon web arayüzünden aldığı kodu kullandı ve sonuçları hareketli GIF biçimine çevirdi. | Demo |
| [Soyut mürekkep çizimini canlandırmak](#case-99) | Grafik ve Arayüz Prototipleri | Yapımcı, soyut çizim animasyonunu Gemini 4 Neon ile yaptığını belirtiyor. | Demo |
| [Three.js ile yapılan Kyoto yürüyüşlerini karşılaştırmak](#case-100) | Grafik ve Arayüz Prototipleri | Üstte GPT-6.2 Astra, altta Gemini 4 Neon yer alıyor. 20 saniyelik Three.js yürüyüşü Kyoto’da şafak vakti torii kapılarından ve bambu korusundan geçiyor. | Evaluation |
| [Enstrümantal bir düzenlemeyi göstermek](#case-101) | Grafik ve Arayüz Prototipleri | Yapımcı enstrümantal parçayı Gemini 4 Neon’a atfediyor. | Demo |
| [İki Shibuya gece sahnesini karşılaştırmak](#case-102) | Grafik ve Arayüz Prototipleri | Video Opus 5.5 ve Gemini 4 Neon’un Shibuya Kavşağı gece sahnelerini model adlarıyla gösteriyor. | Evaluation |
| [Bir robotun montajını ve kalkışını canlandırmak](#case-103) | Grafik ve Arayüz Prototipleri | Yapımcı robot montajı ve kalkışıyla ilgili önceki Three.js görevini yeniden kullandı. Videoda robotun parçaları birleşiyor ve robot havalanıyor. | Demo |
| [Model eğitimini bir müzik videosuyla anlatmak](#case-104) | Bilgi Çalışması | Yapımcı Gemini 4 Neon’dan en gelişmiş modellerin nasıl eğitildiğini anlatan bir müzik videosu istedi. | Demo |
| [Kodlama modellerini bileşik bir endeksle karşılaştırmak](#case-105) | Değerlendirmeler ve Limitler | Yazarın yayımladığı Models Engineering Index tablosunda Gemini 4 Neon, 68,1 puanla 20 kayıt arasında birinci. | Benchmark |
| [OpenClaw'da Neon model kaydını bulma](#case-106) | Mühendislik ve Entegrasyonlar | OpenClaw, sürüm denetimine alınmış yapılandırmasında Gemini 4 Neon'u önerilen model olarak gösterir. | Integration |
| [İki akıl yürütme düzeyindeki kıyaslama puanlarını karşılaştırma](#case-107) | Değerlendirmeler ve Limitler | Kıyaslamayı yürüten kişi, hata düzeltme görevlerinde Neon'un xhigh ve high sonuçlarını yayımlıyor. | Benchmark |
| [Bisikletleri eşzamanlı glissandoyla canlandırma](#case-108) | Grafik ve Arayüz Prototipleri | Üretici, bisikletli görsel-işitsel deneyi Neon'a atfediyor ve sesli klibi paylaşıyor. | Demo |
| [Three.js ile prosedürel bir kaiju modelleme](#case-109) | Grafik ve Arayüz Prototipleri | Üretici, Three.js TSL ile oluşturulan prosedürel yaratığı Neon'a atfediyor ve görünümünü videoda gösteriyor. | Demo |
| [Paper ile bir açılış sayfası tasarlama](#case-110) | Grafik ve Arayüz Prototipleri | Üretici, açılış sayfası tasarımını Neon ve Paper kullanılan iş akışına atfediyor ve yerleşimin ekran görüntüsünü paylaşıyor. | Demo |
| [Açık coğrafi veri akışları için pano oluşturma](#case-111) | Mühendislik ve Entegrasyonlar | Üretici, açık coğrafi veri akışlarını ve haberleri birleştiren GROUND arayüzünü Neon kullanan bir Grok Bot iş akışına atfediyor. Kaynak video panoyu gösteriyor. | Integration |
| [JavaScript ile halka arzı anlatan animasyon yapma](#case-112) | Grafik ve Arayüz Prototipleri | Üretici Neon'dan hareketli bir anlatım istediğini ve sonucun JavaScript ile yazıldığını belirtiyor. Özgün klip animasyonun bir bölümünü gösteriyor. | Demo |
| [Neon ajanlarıyla davul animasyonu yapma](#case-113) | Grafik ve Arayüz Prototipleri | Üretici, özgün animasyonu birden fazla Neon ajanının çalışmasına atfediyor. Dördüncü saniye civarında davulcunun ayak hareketleri yakından görülüyor. | Demo |
| [Blender'da fantastik bir şehir ve ejderha görüntüleme](#case-114) | Grafik ve Arayüz Prototipleri | Üretici, Antigravity'de Neon kullanarak Blender sahnesini kodla kurduğunu ve görüntülediğini bildiriyor. Şehri ve ejderhayı tanımlıyor, çalışmanın 11 saat sürdüğünü belirtiyor. | Demo |
| [Sundar Pichai'nin SVG portresini çizme](#case-115) | Grafik ve Arayüz Prototipleri | Üretici, paylaşılan portrenin Neon ile üretilmiş bir SVG olduğunu belirtiyor. Özgün görsel sonucu gösteriyor. | Demo |
| [Kırmızı akçaağaç bonsaisini canlandırmak](#case-116) | Grafik ve Arayüz Prototipleri | Üretici, bonsai görselleştirmesini Neon'a atfediyor ve ortaya çıkan animasyonu yayımlıyor. | Demo |
| [Bir istemden kişisel animasyon klibi yapma](#case-117) | Grafik ve Arayüz Prototipleri | Üretici, kişisel videoyu Neon'a atfediyor ve başka bir üreticinin istemini uyarladığını söylüyor. Paylaşımda sonuç klibi bulunuyor. | Demo |
| [Blender'da yağmurlu bir baraj sahnesini canlandırma](#case-118) | Grafik ve Arayüz Prototipleri | Üretici, baraj kapağı açıldığında suyun aktığı gece sahnesini Neon xhigh ve Blender ile görüntülediğini bildiriyor. | Demo |
| [Fuji Dağı manzarası çizmek](#case-119) | Grafik ve Arayüz Prototipleri | Üretici, Fuji Dağı çizim dizisinde bu çalışmayı Neon sürümü olarak tanımlıyor. | Demo |
| [Yalnızca kodla üç farklı görsel üretme](#case-120) | Grafik ve Arayüz Prototipleri | Üretici üç çıktıyı Neon'a atfediyor ve kodla üretildiklerini belirtiyor. Özgün eklerde sonuç görselleri var. | Demo |
| [Üç haftalık sosyal medya verisini analiz etme](#case-121) | Bilgi Çalışması | Üretici, Neon High'dan üç haftalık X metriklerini incelemesini istediğini ve göstergeler için sıralı bir korelasyon analizi aldığını bildiriyor. Ekte analizin bir kısmı görülüyor. | Demo |
| [Bir projeyi anlatan kısa hareketli grafik hazırlama](#case-122) | Grafik ve Arayüz Prototipleri | Üretici Neon'dan bir açık kaynak projesi hakkında 20 saniyelik hareketli grafik istediğini ve ilk sonucu kullandığını söylüyor. Paylaşımda istek ve video var. | Demo |
| [Blender MCP üzerinden manga arka planları modelleme](#case-123) | Grafik ve Arayüz Prototipleri | Üretici, manga arka planları için Neon'u Antigravity ve Blender MCP üzerinden kullandığını bildiriyor. Ek, Blender çalışma alanını ve bir modeli gösteriyor. | Demo |
| [Animasyonlu bir sitenin tüm yapım sürecini kaydetme](#case-124) | Grafik ve Arayüz Prototipleri | Üretici, animasyonlu siteyi Neon'a atfediyor ve 12 dakikalık süreç kaydını paylaşıyor. | Tutorial |
| [Sesli özetten hareketli politika özeti hazırlama](#case-125) | Bilgi Çalışması | Üretici kaynak olarak Japon bir çalışma grubunun kamuya açık belgesini, girdi olarak Gemini Notebook'un sesli özetini, eşlik eden video için de Neon'u kullanıyor. | Demo |
| [Ortak ajan panosunda rollere model atama](#case-126) | Mühendislik ve Entegrasyonlar | Üretici, Neon'un Orchestrator olarak çalıştığı ve diğer ajanların ön yüz görevlerine atandığı bir Antigravity grubunu gösteriyor. | Integration |
| [Blender'da yağmurlu Kyoto sokaklarını karşılaştırma](#case-127) | Grafik ve Arayüz Prototipleri | Yazar üç modele aynı istemi verdi ve sonuçları yukarıdan aşağıya tanımlıyor. Blender'da sırasıyla 37, 29 ve 25 düzeltme turu bildiriyor, Neon en altta yer alıyor. | Evaluation |
| [Dört seramik fırınlama animasyonunu karşılaştırma](#case-128) | Grafik ve Arayüz Prototipleri | Üretici, fırınlama etkileri hakkında aynı istemi kullandı ve dört farklı animasyon yayımladı. | Evaluation |
| [Astra'ya karşı bildirilen satranç maçını inceleme](#case-129) | Değerlendirmeler ve Limitler | Yazar, Astra'nın beyaz, Neon'un siyah taşlarla oynadığı bir maçı belgeliyor. | Evaluation |
| [Prosedürel bir dört ayaklı robot simülasyonu geliştirme](#case-130) | Oyunlar ve Simülasyonlar | Üretici, bir referans görselden türetilen dört ayaklı simülasyonu Neon'a atfediyor ve prosedürel gölgelendiriciler, fizik ve kablo simülasyonu kullanıldığını belirtiyor. | Demo |
| [İki etkileşimli saat yapılandırıcısını karşılaştırma](#case-131) | Grafik ve Arayüz Prototipleri | Üretici, Neon ve Opus 5.5'e aynı saat yapılandırıcısı görevini verdi. | Evaluation |
| [Etkileşimli voksel ejderha dioramalarını karşılaştırmak](#case-132) | Grafik ve Arayüz Prototipleri | Yazar, Neon ve Opus'a hazır varlık kullanmadan ejderha ve pagoda yapma görevi verdi. İki sonucun farklı bölümlerini tercih etti. | Evaluation |
| [Düz bir tabloyu etkileşimli olarak yeniden aydınlatma](#case-133) | Grafik ve Arayüz Prototipleri | Üretici, hareketli ışığın düz bir görüntüde yönlü gölgeler oluşturup oluşturamayacağını bir Vermeer tablosuyla denedi. Özgün video sonucu gösteriyor. | Demo |
| [ErdosBench araştırma matematiği sonuçlarını karşılaştırma](#case-134) | Değerlendirmeler ve Limitler | Kıyaslamanın sorumlusu Neon'u ErdosBench'teki 226 araştırma düzeyinde matematik problemiyle değerlendirdiğini bildiriyor. | Benchmark |
| [Kodla oluşturulan üç araç sahnesini karşılaştırma](#case-135) | Grafik ve Arayüz Prototipleri | Yazar hazır 3B varlık kullanmadan üretilen üç etiketli araç sahnesi sunuyor ve tahmini oluşturma maliyetlerini veriyor. | Evaluation |
| [FutureSim tahmin sonuçlarını karşılaştırma](#case-136) | Değerlendirmeler ve Limitler | Yayıncı Neon'un FutureSim'de en yüksek puanı aldığını bildiriyor ve kıyaslama grafiğini yayımlıyor. Paylaşım, araç çağrılarını ve farklı alanlardaki simülasyon sorularını anlatıyor. | Benchmark |
| [Tablo görünümündeki iki 3B dünyayı karşılaştırma](#case-137) | Grafik ve Arayüz Prototipleri | Üretici, üstte Astra ve altta Neon olarak etiketlenen yağlı boya tarzında iki dünyayı karşılaştırıyor. Tamamlanma sürelerinin ve fırça darbesi sayılarının farklı olduğunu bildiriyor. | Evaluation |
| [Three.js neon sahnesine bir araba eklemek](#case-138) | Grafik ve Arayüz Prototipleri | Üretici, Three.js ile oluşturulan neon ışıklı sahneyi Neon'a atfediyor ve sonunda bir BMW M4 CS eklemesini istediğini belirtiyor. | Demo |
| [Blender'da bir karakter referansı oluşturma](#case-139) | Grafik ve Arayüz Prototipleri | Üretici, Blender'da gösterilen karakterin yapımını Neon'a atfediyor. Özgün görsel, modeli farklı açılardan gösteriyor. | Demo |
| [Dört çilek animasyonu çıktısını karşılaştırma](#case-140) | Grafik ve Arayüz Prototipleri | Yazar Neon, Carbon, Fable 5.2 ve Opus 5.5'e aynı animasyonlu çilek görevini verdi. | Evaluation |
| [Geniş bir klip koleksiyonunu videoya dönüştürme](#case-141) | Bilgi Çalışması | Android Developers hesabı, Neon ile yaklaşık bin klibi dizine ekleyen bir iş akışı sunuyor ve sonrasındaki video düzenlemeyi gösteriyor. | Demo |
| [Görsel çıktıları BrushArena oylarına göre karşılaştırma](#case-142) | Değerlendirmeler ve Limitler | Yazar, Neon'un BrushArena'da ilk sıradan giriş yaptığını bildiriyor ve ziyaretçi oylarına dayanan bir kesit sunuyor. | Benchmark |
| [Alp manzarasını yalnızca kodla görüntüleme](#case-143) | Grafik ve Arayüz Prototipleri | Üretici, sahnenin kodla çizilmesini ve canlandırılmasını Neon'a atfediyor. Kaynak videoda Alp manzarası ve bir viyadük görünüyor. | Demo |
| [Ajan geri bildirimiyle ASCII bisikletçi canlandırma](#case-144) | Grafik ve Arayüz Prototipleri | Üretici, ASCII ile canlandırılan bisikletli pelikanı Neon'a atfediyor ve görselleri değerlendirmek için ayrı bir eleştirmen kullandığını anlatıyor. | Demo |
| [Neon ajan grubunu tek ajanla karşılaştırma](#case-145) | Grafik ve Arayüz Prototipleri | Yazar, aynı sincap bakış açılı animasyonda grup ve tek ajan yaklaşımlarını karşılaştırıyor ve bu testte tek ajanı tercih ettiğini belirtiyor. | Evaluation |
| [Neon'u sohbet arayüzüne entegre etme](#case-146) | Mühendislik ve Entegrasyonlar | Geliştirme ekibi, yeni modelin kendi sağlayıcısını sohbet arayüzüne entegre etmeye yardım ettiğini anlatıyor ve gösterilen sonucu Neon'a atfediyor. | Integration |
| [Three.js ile prosedürel bir sinematik sahne oluşturma](#case-147) | Grafik ve Arayüz Prototipleri | Üretici, Neon ile dış varlık kullanmadan yapılan bir WebGL sinematik sahne anlatıyor ve klibi paylaşıyor. | Demo |
| [Modelleri pazarlama görevlerinde değerlendirme](#case-148) | Değerlendirmeler ve Limitler | Değerlendirmeyi yapan kişi Neon, Opus ve Sol'u pazarlama görevlerinde karşılaştırıyor ve sonuç grafiğini paylaşıyor. Karşılaştırma, değerlendiricinin test koşullarıyla sınırlı. | Benchmark |
| [Motor görselleştirmesi için Hydrogen ajanlarını koordine etme](#case-149) | Mühendislik ve Entegrasyonlar | Yazar Neon'u koordinatör yaptı ve Hydrogen ajanlarıyla birkaç yinelemede Three.js üzerinde bir V12 görselleştirmesi oluşturduğunu bildiriyor. | Integration |
| [Blender'da on iki karakter animasyonu üretme](#case-150) | Grafik ve Arayüz Prototipleri | Üretici on iki Blender animasyonunu Neon'a atfediyor ve hareketleri bir ızgarada paylaşıyor. | Demo |
| [Modelleri eğitim verisi düzenleyicisi olarak değerlendirme](#case-151) | Değerlendirmeler ve Limitler | Kıyaslama yazarları Hyper-Intervention'da Neon ve altı başka modeli eğitim yörüngelerinin düzenleyicileri olarak test ediyor. | Benchmark |
| [Dört deniz uçağı iniş sahnesini karşılaştırmak](#case-152) | Grafik ve Arayüz Prototipleri | Testi yapan kişi, Bora Bora yakınında deniz uçağı inişi hakkında tek cümle kullandı. Yazar, etkileşimli Three.js sahnesini Neon'a atfediyor ve denemeyi OutputBench'te kaydediyor. | Evaluation |
| [Antarktika verilerini ajanlarla inceleme](#case-153) | Bilgi Çalışması | Üretici, açık uydu hız verilerini ve Antarktika'nın buz altı topografyasını incelemek için Neon ajan grubu kullandığını bildiriyor. | Demo |
| [Three.js'de Monako tünel çıkışlarını karşılaştırma](#case-154) | Grafik ve Arayüz Prototipleri | Yazar iki modele aynı alacakaranlık tünel görevini verdi ve etiketli bir karşılaştırma yayımladı. Neon için 55 dakika 44 saniye bildiriyor. | Evaluation |
| [Gün batımında dört bisiklet animasyonunu karşılaştırma](#case-155) | Grafik ve Arayüz Prototipleri | Üretici Neon, Fable 5.2, Sol ve DeepSeek V4.1 Flash'a atfedilen bisiklet sahnelerini gösteriyor. | Evaluation |
| [Sincap bakış açısından üç prosedürel filmi karşılaştırma](#case-156) | Grafik ve Arayüz Prototipleri | Üretici 30 saniyelik ortak bir görev verdi ve çıktının yalnızca kodla yapılmasını istedi. Video Neon, Astra ve Fable'a atfedilen sonuçları gösteriyor. | Evaluation |
| [Çok ajanlı kodlama ortamlarını değerlendirme](#case-157) | Değerlendirmeler ve Limitler | Değerlendirici, Neon'u ve birkaç rakip modeli 100 çok ajanlı kodlama ortamında test ettiğini bildiriyor. | Benchmark |
| [Kodla çizilen resmi hızlandırılmış kayıtta gösterme](#case-158) | Grafik ve Arayüz Prototipleri | Üretici, kodla oluşturulan hızlandırılmış çizim kaydını Neon'a atfediyor. Özgün medya çizimin ilerleyişini gösteriyor. | Demo |
| [Üç gece kalkış sahnesinin ışığını karşılaştırma](#case-159) | Grafik ve Arayüz Prototipleri | Üretici aynı gece kalkış görevini kullandı ve Neon sahnesinde uçağın karanlıkta seçilemediğini bildiriyor. Özgün video birden çok etiketli çıktı gösteriyor. | Evaluation |
| [3B yazıcıdan çıkan iki mekanik oyuncağı karşılaştırma](#case-160) | Mühendislik ve Entegrasyonlar | Yazar, ek yönlendirme vermeden Neon ve Fable'dan 3B yazdırılabilir bir nesne tasarlamalarını istedi. Fotoğrafta iki baskı da var. Yazara göre Neon baskısının dişlileri daha istikrarlı çalıştı. | Evaluation |
| [FrontierMemory performansını karşılaştırma](#case-161) | Değerlendirmeler ve Limitler | Kıyaslamanın sorumlusu Gemini 4 Neon'un FrontierMemory sonucunu paylaşıyor. | Benchmark |
| [Referanssız bir görevde Blender MCP çıktılarını karşılaştırma](#case-162) | Grafik ve Arayüz Prototipleri | Üretici üç modele görsel referans, web araması ve hazır varlık olmadan basit bir çekiç görevi verdi. Neon için 19 dakika bildiriyor ve sonuçları paylaşıyor. | Evaluation |
| [Blender'da yinelemelerle Lamborghini modelleme](#case-163) | Grafik ve Arayüz Prototipleri | Üretici, Blender'daki otomobil modelini Neon'a atfediyor ve birden çok yinelemede yapıldığını belirtiyor. | Demo |
| [Ayrıntılı motosiklet görselleştirmelerini karşılaştırma](#case-164) | Grafik ve Arayüz Prototipleri | Üretici, Neon xhigh ve Fable 5.2 xhigh etiketli motosiklet görsellerini yan yana yayımlıyor. | Evaluation |
| [Yazdırılabilir bir şarj cihazı muhafazası tasarlama](#case-165) | Mühendislik ve Entegrasyonlar | Yazar cihazı kısaca tarif etti ve Neon'dan muhafaza tasarlayıp yazdırmasını istedi. Özgün fotoğrafta yazdırılan parça yer alıyor. | Demo |
| [Neon'u AFK Pilot uzantısına ekleme](#case-166) | Mühendislik ve Entegrasyonlar | Uzantıyı geliştiren kişi, AFK Pilot 4.16.0 ve 4.17.0 sürümlerinde Antigravity CLI ile Neon erişimi eklediğini bildiriyor ve arayüzü gösteriyor. | Integration |
| [Sayfa ayrıştırma ve tablo düzenini değerlendirme](#case-167) | Değerlendirmeler ve Limitler | ParseBench-2 yayıncısı, Neon'u düşük düşünme düzeyinde başka model sürümleriyle karşılaştırdığını bildiriyor. | Benchmark |
| [İki The Last Take oyun sahnesini karşılaştırma](#case-168) | Oyunlar ve Simülasyonlar | Üretici, The Last Take'in Neon ve Fable 5.2'ye atfedilen sürümlerini karşılaştırıyor. | Evaluation |
| [AI Studio'da model tanıtım klibi oluşturma](#case-169) | Grafik ve Arayüz Prototipleri | Üretici, AI Studio'da Neon'dan bir tanıtım videosu istediğini bildiriyor ve ilk üretilen sekansı paylaşıyor. | Demo |
| [Blender sahnesini gece boyunca görüntüleme](#case-170) | Grafik ve Arayüz Prototipleri | Üretici, Blender 5.3'teki sahneyi Neon'a atfediyor ve görüntülenen sonucu paylaşıyor. İş akışının gece boyunca çalıştığını bildiriyor. | Demo |
| [CodePilot'taki sekiz sorunun düzeltmelerini karşılaştırma](#case-171) | Değerlendirmeler ve Limitler | Geliştirici, CodePilot'ta belirlenen sekiz sorunu iki modele düzelttirdi ve değerlendirme için üçüncü bir model kullandı. Kaynak Neon için 8,5, Opus için 9 puan bildiriyor. | Evaluation |
| [Tek istemden çıkan iki sahneyi karşılaştırma](#case-172) | Grafik ve Arayüz Prototipleri | Üretici, iki sahnenin aynı istemi farklı renklerle kullandığını söylüyor ve etiketli Neon ve Opus çıktılarını yayımlıyor. | Evaluation |
| [Kodla üretilen bir konsept fragmanı hazırlama](#case-173) | Grafik ve Arayüz Prototipleri | Üretici, 60 saniyelik konsept film için Neon, Antigravity ve OpenMotion kullanıyor. Sahnelerin kodla oluşturulduğunu ve açık kaynak müziğin ayrıca miksajlandığını anlatıyor. | Demo |
| [Three.js'de Gotik katedral yürüyüşlerini karşılaştırma](#case-174) | Grafik ve Arayüz Prototipleri | Yazar iki modelden de vitray pencereye doğru aynı 20 saniyelik yürüyüşü istedi. Videoda Astra üstte, Neon altta. | Evaluation |
| [Gözetimsiz çalışmada oturumun sona ermesini inceleme](#case-175) | Değerlendirmeler ve Limitler | Yazar, Neon ile bir Antigravity oturumunun kimlik doğrulama süresi dolana kadar iki saatten uzun çalıştığını bildiriyor. Ekran görüntüsü bu oturumun hatasını belgeliyor. | Limit |
| [Etkileşimli bir vitray sahnesi oluşturma](#case-176) | Grafik ve Arayüz Prototipleri | Üretici tek bir fotoğrafı referans aldığını, web sesini prosedürel ürettiğini ve içe varlık aktarmadan kedi ile vitray sahnesini kodla görüntülediğini bildiriyor. | Demo |
| [Tek denemelik dört HTML animasyonunu karşılaştırma](#case-177) | Grafik ve Arayüz Prototipleri | Yazar dört modele yağmurlu pencere pervazındaki kedi hakkında aynı istemi verdi. Her model, düzeltme veya ikinci deneme olmadan tek çıktı üretti. | Evaluation |
| [Ajan döngüsünde turun durumunu görselleştirme](#case-178) | Bilgi Çalışması | Üretici ajan döngüsünü etkileşimli bir HTML açıklaması olarak sunmak için Neon kullandı. | Tutorial |
| [Ajanlarla Mars'ın sismik dalga biçimlerini inceleme](#case-179) | Bilgi Çalışması | Üretici, Antigravity'deki Neon ajan grubunun dört yıllık açık NASA InSight dalga biçimi verisini işlediğini belirtiyor. Grafikler yazarın keşif niteliğindeki sonuçları. | Demo |
| [Etkileşimli prosedürel kiraz çiçeği sahnesi oluşturma](#case-180) | Grafik ve Arayüz Prototipleri | Üretici, prosedürel dalları ve kopabilen taç yaprakları olan etkileşimli siteyi Neon'a atfediyor. | Demo |
| [Dikey bir ürün animasyonu hazırlama](#case-181) | Grafik ve Arayüz Prototipleri | Üretici ilk hareket tasarımı denemesini Neon'a atfediyor. | Demo |
| [Antigravity'de masaüstü evcil hayvan cihazının kartını tasarlama](#case-182) | Mühendislik ve Entegrasyonlar | Üretici, Neon'un masaüstü evcil hayvan denetleyicisi ve şarj istasyonu için EasyEDA MCP iş akışını yürüttüğünü anlatıyor. | Demo |
| [Derinlik tahminlerinden normal haritaları üretme](#case-183) | Grafik ve Arayüz Prototipleri | Üretici, Neon desteğiyle Apple Depth Pro 2 ağırlıklarını değiştirdiğini ve normal haritalarıyla diğer PBR haritaları için prosedürel araç hazırladığını bildiriyor. | Demo |
| [Hareket geçişlerini ve ses tercihlerini karşılaştırma](#case-184) | Grafik ve Arayüz Prototipleri | Üretici Neon ile oluşturulan bir hareket tasarımını gösteriyor ve Claude'un ses efektlerini tercih ettiğini belirtiyor. Görsel ve işitsel değerlendirmeler yazara ait. | Evaluation |
| [Üç modelin ve bir insanın kısa öykülerini karşılaştırma](#case-185) | Bilgi Çalışması | Yazar, 500 karakterlik ortak bir görev veriyor ve insanın yardımsız yazdığı sürümü Sol, Neon ve Opus'un ilk taslaklarıyla karşılaştırıyor. | Evaluation |
| [Three.js ile neon ışıklı elektronikçiler bölgesi oluşturma](#case-186) | Grafik ve Arayüz Prototipleri | Üretici Neon'la tek bir görseli, kodla yönetilen kamera içeren kurgusal ve yağmurlu bir elektronikçiler bölgesine dönüştürdü. | Demo |
| [Kurgusal karakter çizim arayüzlerini karşılaştırma](#case-187) | Grafik ve Arayüz Prototipleri | Üretici Neon ve Fable'dan kurgusal bir oyun karakteri için çizim arayüzü hazırlamalarını istiyor. Kaynak Neon için 21, Fable için 27 dakika bildiriyor. | Evaluation |
| [Sayfa bloklarını ve arayüz bileşenlerini yinelemelerle geliştirme](#case-188) | Grafik ve Arayüz Prototipleri | Geliştirici Neon'la üretilen ve farklı bileşenlerin görüldüğü bir blok dizisi yayımlıyor. İlgili klipler aynı çalışmanın sonraki yinelemelerini gösteriyor. | Demo |
| [Film görüntüleme ve tarama emülatörü prototipi geliştirme](#case-189) | Grafik ve Arayüz Prototipleri | Üretici fizik temelli film görüntüleme ve tarama projesini Neon'a atfediyor ve önizlemenin yanında bir geliştirme dizisi paylaşıyor. Bağımsız maliyet ölçümü verilmemiş. | Demo |
| [OpenCode yapılandırmasında çıkarım hızını karşılaştırma](#case-190) | Değerlendirmeler ve Limitler | Kıyaslama katılımcısı, InferenceBench'te kaydedilen bir Neon yapılandırmasını sunuyor. | Benchmark |
| [Kod barındırma arayüzü prototipi geliştirme](#case-191) | Mühendislik ve Entegrasyonlar | Üretici kod barındırma prototipini Neon'a atfediyor ve uygulamanın videosunu yayımlıyor. | Demo |
| [İki etkileşimli okyanus dioramasını karşılaştırma](#case-192) | Grafik ve Arayüz Prototipleri | Üretici aynı görevi Neon ve Opus 5.5 ile çalıştırdığını bildiriyor. | Evaluation |
| [Altı modelin site tasarımlarını karşılaştırma](#case-193) | Grafik ve Arayüz Prototipleri | Yazar aynı yeniden tasarım isteğini high düzeyde ve ek beceri olmadan kullandı. Kaynak deneme başına süre ve maliyetleri, Neon için de alt maliyet sınırını bildiriyor. | Evaluation |
| [Antigravity'de önbellek isabet değişimini izleme](#case-194) | Değerlendirmeler ve Limitler | Yapımcı sonraki paylaşımında önbellek isabet oranını %98,9, daha önceki paylaşımında ise yaklaşık %50 olarak bildiriyor. | Limit |
| [Ortak bir Three.js isteminden Jeep modellerini karşılaştırma](#case-195) | Grafik ve Arayüz Prototipleri | Üretici daha önceki Jeep istemini yeniden kullandığını bildiriyor ve sonuçları yan yana yayımlıyor. Neon High denemesinde 45 dakika kaydetti. | Evaluation |
| [Üç modelin arayüz yaklaşımlarını karşılaştırma](#case-196) | Grafik ve Arayüz Prototipleri | Üretici Opus 5.5, Sol ve Gemini 4 Neon ile ilişkilendirilen kullanıcı arayüzü tasarımlarını incelediğini bildiriyor. | Evaluation |
| [Prosedürel kodla şarkılı bir sahne oluşturma](#case-197) | Grafik ve Arayüz Prototipleri | Yazar Neon'dan görselleri, müziği ve sesi harici kitaplık, varlık veya metinden sese dönüştürme kullanmadan kodla üretmesini istediğini bildiriyor. Sonucu tek deney olarak sunuyor. | Demo |
| [Üretilen klipleri ilk ve son kareleri düzenleyerek birleştirme](#case-198) | Grafik ve Arayüz Prototipleri | Yazar daha uzun bir video iş akışında ilk ve son karelerin yanı sıra kurgu için Neon kullandığını anlatıyor. | Integration |
| [Antigravity'de kısa bir anlatım videosu hazırlama](#case-199) | Bilgi Çalışması | Üretici, 90 saniyelik videoyu Neon ve Antigravity'ye atfediyor; Google medya araçlarını, metinden sese dönüştürmeyi ve HyperFrames'i iş akışının parçaları olarak sıralıyor. | Demo |
| [Tarayıcı sahnesinde bir voksel modeli sergileme](#case-200) | Grafik ve Arayüz Prototipleri | Üretici voksel model demosunu Neon'a atfediyor. Video muz biçimli bir voksel nesnesini ve etkileşimli sunum denetimlerini gösteriyor. | Demo |
| [Tanıtım görselini neon tabela gibi canlandırma](#case-201) | Grafik ve Arayüz Prototipleri | Üretici, Neon'dan modelin tanıtım yazısındaki bir görseli canlandırmasını istediğini belirtiyor. | Demo |
| [LilyPond'da üretilen iki mazurkayı karşılaştırma](#case-202) | Grafik ve Arayüz Prototipleri | Üretici, Neon ve Fable 5.2'ye LilyPond'da piyano mazurkası için aynı görevi verdi. | Evaluation |
| [Dört holografik paralaks animasyonunu karşılaştırma](#case-203) | Grafik ve Arayüz Prototipleri | Üretici dört görsel girdiden holografik paralaks animasyonu elde ettiğini anlatıyor ve adları belirtilen dört çıktıyı karşılaştırıyor. | Evaluation |
| [ASCII figürlerini kodla canlandırma](#case-204) | Grafik ve Arayüz Prototipleri | Üretici, yalnızca kodla yapılan bir ASCII deneyini anlatıyor. Özgün klip metinle çizilen hareketli figürleri gösteriyor. | Demo |
| [Mevcut kodda CI tür denetimini hızlandırma](#case-205) | Mühendislik ve Entegrasyonlar | Geliştirici, önceki iyileştirmenin ardından CI'ı Neon ile yeniden incelediğini bildiriyor. Kendi kod tabanında tür denetiminin 6,5 dakikadan 1,5 dakikaya düştüğünü belirtiyor. | Evaluation |
| [Sahne kurulumu ve animasyonu modellere bölüştürme](#case-206) | Grafik ve Arayüz Prototipleri | Üreticiye göre Neon genel sahne kurulumunu yaptı, Claude Mythos 5.2 ayrıntıları ve hareketi iyileştirdi. Video sonucu gösteriyor. | Integration |
| [Microduck simülasyonunda JEPA yardımcı modülünü prototipleme](#case-207) | Mühendislik ve Entegrasyonlar | Üretici, Microduck için proprioseptif bir JEPA yardımcı modülü geliştirirken Gemini 4 Neon ve Carbon kullandığını bildiriyor. | Demo |
| [Sekiz düğümünü fizik simülasyonu kaydıyla puanlama](#case-208) | Değerlendirmeler ve Limitler | Üreticinin KnotBench v0 kaydı dört model için aynı sekiz düğümü görevini gösteriyor. Neon, gösterilen denemede çıkarılabilir bir düğüm açıklaması üretmedi. | Limit |
| [Ozymandias'ın Minecraft yorumlarını karşılaştırma](#case-209) | Oyunlar ve Simülasyonlar | Üretici Shelley'nin şiirine dayanan aynı istemi kullandı. Neon için 19 dakika ve 2,88 ABD doları, Sol için 12 dakika ve 1,06 ABD doları bildiriyor. | Evaluation |
| [Bir beceriyle kısa bir bilgi videosu oluşturma](#case-210) | Bilgi Çalışması | Yazar iki dakikadan uzun bir videoyu tamamlamak için Neon'u mevcut bilgi videosu becerisiyle ve ayrı bir görüntüleme iyileştirmesiyle kullandı. Zaman ve kota rakamları bu denemeye ait. | Demo |
| [Three.js gondol gezilerini karşılaştırma](#case-211) | Grafik ve Arayüz Prototipleri | Üretici Astra ve Neon'dan gün batımında bir Venedik köprüsünün altından geçen aynı yirmi saniyelik gondol gezisini istedi. | Evaluation |
| [Bir MotionBricks karakter demosunu yerelde çalıştırma](#case-212) | Mühendislik ve Entegrasyonlar | Üretici, MotionBricks deposunu inceleme ve ONNX modelleriyle etkileşimli demo kurma işini Neon'a atfediyor. Demoyu NVIDIA GPU olmadan yerelde çalıştırdığını bildiriyor. | Integration |
| [Dört Three.js Eyfel Kulesi modelini karşılaştırma](#case-213) | Grafik ve Arayüz Prototipleri | Üretici Neon, Astra, Sol ve Opus'tan Three.js'de Eyfel Kulesi yapmalarını istedi. | Evaluation |
| [İki Gemini sürümünün motor animasyonlarını karşılaştırma](#case-214) | Grafik ve Arayüz Prototipleri | Üretici, Antigravity'de Gemini 4 Neon High ve Gemini 3.7 Flash High'ı motor görselleştirmesinde karşılaştırıyor. | Evaluation |
| [Tarayıcı için sahte 3B voksel sprite'ları oluşturma](#case-215) | Grafik ve Arayüz Prototipleri | Üretici, kamera döndükçe sahnenin hacimli görünmesi için düz sprite katmanlarını birleştirdiğini açıklıyor. Demo yöntemi tarayıcı arayüzünde gösteriyor. | Demo |
| [Dört Alpine Gold sahnesini karşılaştırma](#case-216) | Grafik ve Arayüz Prototipleri | Karşılaştırmada ortak Alpine Gold isteminden çıkan dört çıktı etiketlenmiş. Üretici Neon'un bu testte 1 saat 31 dakika 11 saniye sürdüğünü ve 11,84 ABD doları tuttuğunu bildiriyor. | Evaluation |
| [Dört hareketli zebra sahnesini karşılaştırma](#case-217) | Grafik ve Arayüz Prototipleri | Üretici Neon, Carbon, Fable 5.2 ve DeepSeek V4.1 Flash'tan dört etiketli zebra animasyonu sunuyor. | Evaluation |
| [Neon ve Carbon'u FrontierMath'te karşılaştırma](#case-218) | Değerlendirmeler ve Limitler | Yazar belirli bir düzeye ait FrontierMath grafiğine işaret ediyor ve o grafikte Neon'un Carbon'un önünde olduğunu bildiriyor. | Benchmark |
| [İki ekskavatör animasyonunu karşılaştırma](#case-219) | Grafik ve Arayüz Prototipleri | Özgün video Neon ve Opus 5.5 ile hazırlanan şantiye sahnelerini etiketliyor. | Evaluation |
| [JPEN Dict'in macOS arayüzünü geliştirme](#case-220) | Mühendislik ve Entegrasyonlar | Geliştirici JPEN Dict 1.8.0'ı geliştirirken Antigravity'de Neon'a geçtiğini bildiriyor. | Integration |
| [Sekiz televizyon mekânının Minecraft yapılarını karşılaştırma](#case-221) | Oyunlar ve Simülasyonlar | Üretici Neon ve Sol'a sekiz mekân için aynı Minecraft görevini verdi. | Evaluation |
| [AI Studio'da bir zar atma aracı oluşturma](#case-222) | Oyunlar ve Simülasyonlar | Üretici, evde hazırlanan masa oyunlarında kullanılan zar aracını Google AI Studio'da Neon ile yaptığını anlatıyor. | Demo |
| [Antigravity'de W16 motor canlandırma](#case-223) | Grafik ve Arayüz Prototipleri | Üretici, Bugatti Chiron W16 görselleştirmesi için Antigravity'de Neon High kullandığını belirtiyor. | Demo |
| [Su setinin göçme biçimlerini üç boyutlu kesitle gösterme](#case-224) | Bilgi Çalışması | Üretici, basitleştirilmiş iki boyutlu sızıntı hesabını üç boyutlu kesitle birleştiren bir çalışma görselleştirmesi için Neon kullandı. | Demo |
| [Neon'un yönettiği müzik videosunu yinelemelerle geliştirme](#case-225) | Grafik ve Arayüz Prototipleri | Üretici müzik videosunun yönetimini Neon'a bıraktı ve birkaç gün boyunca çalışmaya geri döndüğünü belirtiyor. | Demo |
| [Oynanabilir ipuçlarıyla kaçış odası prototipi yapma](#case-226) | Oyunlar ve Simülasyonlar | Üretici, Astrolab kaçış odasının ilk oynanabilir sürümünü tek istekten oluşturmayı Neon'a atfediyor. | Demo |
| [Pi'nin ajan altyapısını etkileşimli şemayla açıklama](#case-227) | Bilgi Çalışması | Üretici Pi'nin ajan altyapısını ve dört yerleşik aracını göstermek için Neon kullandı. | Tutorial |
| [İki Three.js kütüphane gezisini karşılaştırma](#case-228) | Grafik ve Arayüz Prototipleri | Üretici Astra ve Neon'a büyük bir Barok kütüphanesi için aynı görevi verdi. | Evaluation |
| [Etkileşimli bir likidite radarı oluşturma](#case-229) | Mühendislik ve Entegrasyonlar | Üretici, yayımlanan SI Liquidity Radar'ın yapımını Neon'a atfediyor. | Demo |
| [Ondalık sayı karşılaştırmasında yanıt tarzını inceleme](#case-230) | Değerlendirmeler ve Limitler | Neon olarak etiketlenen ekran görüntüsü 9,3 ile 9,12'yi karşılaştırıyor ve 9,3'ün daha büyük olduğunu belirtiyor. | Evaluation |
| [Ağırlıklı LiveBench 2.0 sonuçlarını karşılaştırma](#case-231) | Değerlendirmeler ve Limitler | Paylaşımda, gösterilen LiveBench 2.0 sürümünde Neon'un genel puanı 87,4. | Benchmark |
| [Referans klipten fantastik bir geçiş kurgulama](#case-232) | Grafik ve Arayüz Prototipleri | Üretici referans klip verdi ve kurguyu Neon'a atfetti. Klonlanmış anlatımı Doubao TTS2 üretti. | Tutorial |
| [Ondalık basamak değerini açıklayan iki yanıtı karşılaştırma](#case-233) | Değerlendirmeler ve Limitler | Yazar 9,12 ve 9,8'i karşılaştıran aynı soruya verilmiş iki yanıt gösteriyor. | Evaluation |
| [Sulu boya gözetleme kulesini WebGPU sahnesine dönüştürme](#case-234) | Grafik ve Arayüz Prototipleri | Üretici Neon ve Carbon'a aynı sulu boya görselini ve WebGPU gözetleme kulesi görevini verdi. | Evaluation |
| [Three.js otomobil yapımında Hydrogen ajanlarını koordine etme](#case-235) | Mühendislik ve Entegrasyonlar | Üretici, Three.js'de Lamborghini Veneno yapan beş Hydrogen ajanının koordinasyonunu Neon'a verdi. | Integration |
| [tvOS için sıra tabanlı topçu oyunu prototipi geliştirme](#case-236) | Oyunlar ve Simülasyonlar | Geliştirici, tvOS topçu oyunu prototipini Neon'a ve Amp'in Mac yardımcı süreçlerine atfediyor. | Demo |
| [Neon için verilere uyarlanan kıyaslama eğrilerini okuma](#case-237) | Değerlendirmeler ve Limitler | Priors yazarı, 45 kıyaslama için ayrı Neon gözlemleri içeren uyum eğrilerini gösteriyor. | Benchmark |
| [Kodla bir şarkı ve ASCII görselleştirmesi yazma](#case-238) | Grafik ve Arayüz Prototipleri | Üretici Neon'dan kendi şarkı sözlerini seçmesini ve düşünme sürecini ASCII animasyonu olarak göstermesini istedi. | Demo |
| [Ezberden çizilen üç SVG logosunu değerlendirme](#case-239) | Değerlendirmeler ve Limitler | Üretici, web erişimi kapalı ve terminal çalıştırma açıkken Antigravity'de orta düşünme düzeyindeki Neon'un hazırladığı üç logoyu gösteriyor. | Evaluation |
| [Dört motor kesiti animasyonunu karşılaştırma](#case-240) | Grafik ve Arayüz Prototipleri | Üretici dört modele çalışan bir motoru kesit olarak gösteren aynı görevi verdi. | Evaluation |
| [Düşük poligonlu bir karakter tabanı oluşturma](#case-241) | Grafik ve Arayüz Prototipleri | Üretici, tek istemden çıkan karakter ağını Gemini 4 Neon ve Blender'a atfediyor ve yaklaşık 4.800 üçgen bildiriyor. | Tutorial |
| [Dört donmuş karpuz animasyonunu karşılaştırma](#case-242) | Grafik ve Arayüz Prototipleri | Üretici dört modele aynı donma, erime ve patlama görevini verdiğini bildiriyor. Etiketli dört panel çıktıları tek klipte gösteriyor. | Evaluation |
| [Etkileşimli bir modelle göz optiğini öğretin](#case-243) | Bilgi Çalışması | Video 3B bir gözü, odak ve mercek ayarlarını ve renkli görme görünümlerini gösteriyor. | Demo |
| [Üç asistanın tek seferlik rastgele sayı yanıtlarını karşılaştırmak](#case-244) | Değerlendirmeler ve Limitler | Yazarın paylaştığı üç ekran görüntüsünde Gemini 4 Neon Medium, 6 Luna Medium ve Sonnet 5.5 High 47 yanıtını verdi. | Limit |
| [3B mahallede birinci şahıs dedektiflik oyunu oluşturun](#case-245) | Oyunlar ve Simülasyonlar | Gösterimde oyuncu mekânlara giriyor, karakterleri sorguluyor ve ipuçlarını inceliyor. | Demo |
| [Özel bir DAW üzerinden piyano parçası besteleyin](#case-246) | Mühendislik ve Entegrasyonlar | Kayıt, tamamlanan düzenlemenin çalma sırasında nota ızgarasında kaydığını gösteriyor. | Integration |
| [Referans fotoğraflardan hareketli robotu yeniden oluşturun](#case-247) | Grafik ve Arayüz Prototipleri | Video, aşamalı montajı ve modelle referans fotoğrafı karşılaştıran son geçişi gösteriyor. | Demo |
| [Sabit GPU bütçesiyle Polytopia eğitimini karşılaştırın](#case-248) | Değerlendirmeler ve Limitler | Yaklaşık 325 Elo’da grafik Neon için yaklaşık 3 GPU saati, gösterilen en iyi alternatif için yaklaşık 7 saat gösteriyor. | Benchmark |
| [Uydu yörüngelerini tarayıcıda canlı izleyin](#case-249) | Grafik ve Arayüz Prototipleri | Videoda yazar Dünya çevresindeki bakış açısını oynattıkça uydular ve izleri değişiyor. | Demo |
| [Akıllı ev için özel bir uyandırma sözcüğü eğitin](#case-250) | Mühendislik ve Entegrasyonlar | Gösterimde uyandırma modeli, sesle tetiklenen ev otomasyonuyla birlikte çalışıyor. | Integration |
| [Antigravity’de video maskeleme prototipi oluşturun](#case-251) | Grafik ve Arayüz Prototipleri | Ekran görüntüsü, geliştirme sırasındaki kare önizlemelerini gösteriyor. | Demo |
| [Dört modelin 3B halka animasyonlarını karşılaştırın](#case-252) | Değerlendirmeler ve Limitler | Kaynak video, etiketli dört 3B halkanın yan yana açılmasını gösteriyor. | Evaluation |

| Bölüm | Amaç |
|---|---|
| [İlgili depolar](#related-repositories) | Diğer Gemini vaka koleksiyonları |
| [Hızlı başlangıç](#quick-start) | Vakalar nasıl okunmalı? |
| [Teşekkür](#acknowledge) | Krediler ve düzeltmeler |

## 🛠️ Mühendislik ve Entegrasyonlar
<a id="engineering"></a>

<a id="case-1"></a>
### Case 1: [Gözetimsiz çalıştırmalar sırasında istikrarsızlığı gözlemleyin](https://x.com/IndependentEco/status/2123155946801070204) (by [@IndependentEco](https://x.com/IndependentEco))

**Gözetimsiz çalıştırmalarda yeniden denemeleri ve tamamlamaları izleyin ve denetleyen modelin ayrı bir kaydını tutun.**

Testi yapan kişi, çıkış gününde Neon’u grafik arayüz olmadan çalıştırırken kararsızlık gözlemlediğini ve çalışmayı Opus 5.5’in izlediğini belirtti.

Ekran görüntüleri bu ortamı belgeliyor. Raporda temel nedene atıf yapılmadı.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-1-1-cffe1f4d2f8c.png" alt="Gözetimsiz çalıştırmalar sırasında istikrarsızlığı gözlemleyin · 1" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-1-2-33b7cb88e773.png" alt="Gözetimsiz çalıştırmalar sırasında istikrarsızlığı gözlemleyin · 2" width="560">

Type: Limit | Date: 2026-11-18

---

<a id="case-2"></a>
### Case 2: [Mantık kapısı simülasyonu oluşturun](https://x.com/SamuelAlbanie/status/2123174394889687151) (by [@SamuelAlbanie](https://x.com/SamuelAlbanie))

**Simülasyonun çip, devre kartı ve ekran seviyelerinde neler gösterdiğini kontrol edin.**

Yazar, simüle edilmiş mantık kapılarından ve devre kartlarından retro terminal ekranına kadar uzanan etkileşimli bir elektronik demosu gösteriyor.

Seri, ayrıntılandırma yapılmadan demo başına bir bilgi istemi bildirir. Kayıt, arayüzü ve simülasyon davranışını gösterir.

[Ek kaynak](https://x.com/SamuelAlbanie/status/2123174391617867925)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-2-1-b7233891bf19.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-2-1-7cb8c5a2b86d.jpg" alt="Mantık kapısı simülasyonu oluşturun · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-3"></a>
### Case 3: [tscircuit'de bir Bluetooth diş fırçası tasarlayın](https://x.com/seveibar/status/2123229845274653112) (by [@seveibar](https://x.com/seveibar))

**Yönlendirmeyi ve kapladığı alan seçimini işlenmiş muhafazadan bağımsız olarak inceleyin.**

Bir tscircuit bakımcısı, Bluetooth elektrikli diş fırçasında Neon Yüksek, Opus 5.5 Yüksek ve Sol 6.2 Yüksek'i karşılaştırdı.

Bakımcı Neon'un görsel sonucunu tercih etti ancak yönlendirmenin eksik olduğunu ve ayak izi seçimlerinin yetersiz olduğunu bildirdi.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-3-1-f5a7948ce417.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-3-1-c5c60f2fdcf3.jpg" alt="tscircuit&#x27;de bir Bluetooth diş fırçası tasarlayın · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-19

---

<a id="case-4"></a>
### Case 4: [Muse'un yan konuşmasını Neon'a aktarın](https://x.com/kajikent/status/2123232182298976767) (by [@kajikent](https://x.com/kajikent))

**Muse aktarıcısına güvenmeden önce hangi yanıtların Neon'den geldiğini kontrol edin.**

Yazar, istekleri ve yanıtları Neon'a ileten bir Muse yan sohbeti oluşturdu.

Yayınlanan Japonca talimat Muse rölesini yapılandırır. Bu, Muse'a yönelik bir talimattır ve Neon'a gönderilen doğrudan bir istemi oluşturmaz.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-4-1-7b5f3b451dc2.jpg" alt="Muse&#x27;un yan konuşmasını Neon&#x27;a aktarın · 1" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-4-2-636fe982bfee.jpg" alt="Muse&#x27;un yan konuşmasını Neon&#x27;a aktarın · 2" width="560">

Type: Integration | Date: 2026-11-19

---

<a id="case-5"></a>
### Case 5: [Üç modelli bir T3 Code iş akışında metin yazarlığı için Neon'yi kullanın](https://x.com/theo/status/2123273253850628260) (by [@theo](https://x.com/theo))

**Bir modeli metin yazarlığına atayın ve uygulama ve oyun testine geçişini kontrol edin.**

Geliştirici, Neon'ye çok modelli bir T3 Code iş akışı içinde metin yazarlığı rolünü verir.

Geliştirici, uygulamayı Fable'a ve oynatma testini GPT-6.2 Astra'ya atar. T3 Code ekran görüntüsü, aktif iş akışında metin yazarlarının yer aldığı bir yaratık yetiştirme oyununu gösteriyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-5-1-3899936a871e.jpg" alt="Üç modelli bir T3 Code iş akışında metin yazarlığı için Neon&#x27;yi kullanın · 1" width="560">

Type: Integration | Date: 2026-11-19

---

<a id="case-6"></a>
### Case 6: [Spotify tavsiye MCP'sini yeniden çalışın](https://x.com/Lentils80/status/2123285929649455409) (by [@Lentils80](https://x.com/Lentils80))

**Öneri değişikliklerini inceleyin ve istenmeyen özelliklerin sonucu iyileştirip iyileştirmediğini test edin.**

Yaratıcı, orijinal olarak Argon ile oluşturulmuş bir Spotify tavsiye MCP'sini revize etmek için Neon'u kullandı.

İçerik oluşturucu, hata düzeltmeleri ve talep edilmeyen zevke dayalı bir öneri modeli bildirdi. Gönderi öneri doğruluğunu sağlamaz.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-6-1-a5dafa9b6b4e.jpg" alt="Spotify tavsiye MCP&#x27;sini yeniden çalışın · 1" width="560">

Type: Integration | Date: 2026-11-19

---

<a id="case-106"></a>
### Case 106: [OpenClaw'da Neon model kaydını bulma](https://x.com/openclaw/status/2123640619931484511) (by [@openclaw](https://x.com/openclaw))

**Entegrasyonun model desteğini yayımlanan yapılandırma kaydından doğrulayın.**

OpenClaw, sürüm denetimine alınmış yapılandırmasında Gemini 4 Neon'u önerilen model olarak gösterir.

OpenClaw ekibi modelin eklendiğini duyurdu ve yayımladığı önerilen model yapılandırmasında gemini-4-neon kimliğine yer verdi. Kaynaklar kaydın varlığını doğruluyor.

[Ek kaynak](https://github.com/openclaw/openclaw/blob/adb2f7c4d4bc3b7479b180c24db943b9cc64923c/scripts/lib/recommended-models.json)

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-106-1-7d8612587051.jpg" alt="OpenClaw&#x27;da Neon model kaydını bulma · 1" width="560">

Type: Integration | Date: 2026-11-20

---

<a id="case-111"></a>
### Case 111: [Açık coğrafi veri akışları için pano oluşturma](https://x.com/GOD2FREEX/status/2123659651703292096) (by [@GOD2FREEX](https://x.com/GOD2FREEX))

**Üretilen arayüzü değerlendirirken hangi girdilerin dış veri akışlarından geldiğini izleyin.**

Üretici, açık coğrafi veri akışlarını ve haberleri birleştiren GROUND arayüzünü Neon kullanan bir Grok Bot iş akışına atfediyor. Kaynak video panoyu gösteriyor.

Özgün videoda GROUND panosu görülüyor. Yazar, panoyu Grok Bot üzerinden Neon ile oluşturduğunu ve herkese açık kaynakları tek arayüzde topladığını anlatıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-111-1-18a94faed52a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-111-1-93e664897230.jpg" alt="Açık coğrafi veri akışları için pano oluşturma · 1" width="560"></a>

Type: Integration | Date: 2026-11-20

---

<a id="case-126"></a>
### Case 126: [Ortak ajan panosunda rollere model atama](https://x.com/SimonT242613/status/2123753724367826978) (by [@SimonT242613](https://x.com/SimonT242613))

**Her göreve belirli bir model atayın ve ilerlemeyi ortak görev panosundan izleyin.**

Üretici, Neon'un Orchestrator olarak çalıştığı ve diğer ajanların ön yüz görevlerine atandığı bir Antigravity grubunu gösteriyor.

Ekran görüntüsü bu projedeki model atamalarını ve görev durumlarını gösteriyor. Yazar kendi kullanımındaki kurulum gözlemlerini ayrıca anlatıyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-126-1-6c3fe29fa2c2.jpg" alt="Ortak ajan panosunda rollere model atama · 1" width="560">

Type: Integration | Date: 2026-11-20

---

<a id="case-146"></a>
### Case 146: [Neon'u sohbet arayüzüne entegre etme](https://x.com/superdoteng/status/2123834081515635115) (by [@superdoteng](https://x.com/superdoteng))

**Sohbet ile terminal arasında bağlamın ve denetimlerin korunduğunu test edin.**

Geliştirme ekibi, yeni modelin kendi sağlayıcısını sohbet arayüzüne entegre etmeye yardım ettiğini anlatıyor ve gösterilen sonucu Neon'a atfediyor.

Özgün içerikte sohbeti terminal akışına bağlayan arayüz görülüyor. Geliştirici, arka plan ajanlarını, yönlendirmeyi ve kullanım göstergesini sıralıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-146-1-486b313368a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-146-1-144e4deed3ec.jpg" alt="Neon&#x27;u sohbet arayüzüne entegre etme · 1" width="560"></a>

Type: Integration | Date: 2026-11-20

---

<a id="case-149"></a>
### Case 149: [Motor görselleştirmesi için Hydrogen ajanlarını koordine etme](https://x.com/thtbee_/status/2123843882937155607) (by [@thtbee_](https://x.com/thtbee_))

**Sonucu kime atfettiğinizi açıklarken koordinatör ve uygulayıcı rollerini kaydedin.**

Yazar Neon'u koordinatör yaptı ve Hydrogen ajanlarıyla birkaç yinelemede Three.js üzerinde bir V12 görselleştirmesi oluşturduğunu bildiriyor.

Üretici Neon'u koordinatör, Hydrogen ajanlarını uygulayıcı olarak tanımlıyor. Özgün görsel, yinelemelerin sonucu olan V12 çalışmasını gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-149-1-5487f081868e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-149-1-6d1c71ce1847.jpg" alt="Motor görselleştirmesi için Hydrogen ajanlarını koordine etme · 1" width="560"></a>

Type: Integration | Date: 2026-11-20

---

<a id="case-160"></a>
### Case 160: [3B yazıcıdan çıkan iki mekanik oyuncağı karşılaştırma](https://x.com/davis7/status/2123906899074822159) (by [@davis7](https://x.com/davis7))

**Tasarımların görünümüyle birlikte basılı nesnelerin nasıl çalıştığını karşılaştırın.**

Yazar, ek yönlendirme vermeden Neon ve Fable'dan 3B yazdırılabilir bir nesne tasarlamalarını istedi. Fotoğrafta iki baskı da var. Yazara göre Neon baskısının dişlileri daha istikrarlı çalıştı.

Fotoğraf iki basılı nesneyi gösteriyor. Dişli istikrarı, nesneleri yazdıran kişinin nitel gözlemi.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-160-1-2ac12dc80c68.jpg" alt="3B yazıcıdan çıkan iki mekanik oyuncağı karşılaştırma · 1" width="560">

Type: Evaluation | Date: 2026-11-20

---

<a id="case-165"></a>
### Case 165: [Yazdırılabilir bir şarj cihazı muhafazası tasarlama](https://x.com/davis7/status/2123934402510287059) (by [@davis7](https://x.com/davis7))

**Fiziksel baskıyı yazarın muhafaza görevine göre karşılaştırın.**

Yazar cihazı kısaca tarif etti ve Neon'dan muhafaza tasarlayıp yazdırmasını istedi. Özgün fotoğrafta yazdırılan parça yer alıyor.

Fotoğraf şarj cihazının basılı muhafazasını gösteriyor. İlk görev kısa bir açıklamayla verildi.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-165-1-5ca9c7b79790.jpg" alt="Yazdırılabilir bir şarj cihazı muhafazası tasarlama · 1" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-165-2-4ca465c878d2.jpg" alt="Yazdırılabilir bir şarj cihazı muhafazası tasarlama · 2" width="560">

Type: Demo | Date: 2026-11-21

---

<a id="case-166"></a>
### Case 166: [Neon'u AFK Pilot uzantısına ekleme](https://x.com/PawelHuryn/status/2123934736049488318) (by [@PawelHuryn](https://x.com/PawelHuryn))

**Uzantı sürümünü kontrol edin ve uzantının özellikleriyle modelin davranışını ayrı değerlendirin.**

Uzantıyı geliştiren kişi, AFK Pilot 4.16.0 ve 4.17.0 sürümlerinde Antigravity CLI ile Neon erişimi eklediğini bildiriyor ve arayüzü gösteriyor.

Geliştirici iki sürümü ve Antigravity CLI entegrasyonunu listeliyor. Özgün görsel sürümdeki değişikliğe eşlik ediyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-166-1-719205d06961.jpg" alt="Neon&#x27;u AFK Pilot uzantısına ekleme · 1" width="560">

Type: Integration | Date: 2026-11-21

---

<a id="case-182"></a>
### Case 182: [Antigravity'de masaüstü evcil hayvan cihazının kartını tasarlama](https://x.com/GoGoFly23/status/2124036617937760579) (by [@GoGoFly23](https://x.com/GoGoFly23))

**Prototipi üretmeden önce her aşamada devre şemasını ve kart yerleşimini inceleyin.**

Üretici, Neon'un masaüstü evcil hayvan denetleyicisi ve şarj istasyonu için EasyEDA MCP iş akışını yürüttüğünü anlatıyor.

Özgün ekler bileşen seçimini, devre şemalarını ve bağlantı yönlendirmesini belgeliyor. Paylaşım tasarım kanıtı sunuyor, donanım doğrulaması bildirmiyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-182-1-ea3cf789e3e3.jpg" alt="Antigravity&#x27;de masaüstü evcil hayvan cihazının kartını tasarlama · 1" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-182-2-c4998720a0a2.jpg" alt="Antigravity&#x27;de masaüstü evcil hayvan cihazının kartını tasarlama · 2" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-182-3-dba688ec02b8.jpg" alt="Antigravity&#x27;de masaüstü evcil hayvan cihazının kartını tasarlama · 3" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-182-4-6881f9f40dfd.jpg" alt="Antigravity&#x27;de masaüstü evcil hayvan cihazının kartını tasarlama · 4" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-182-5-8a9eff67f95b.jpg" alt="Antigravity&#x27;de masaüstü evcil hayvan cihazının kartını tasarlama · 5" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-182-6-2cec402f5c8a.jpg" alt="Antigravity&#x27;de masaüstü evcil hayvan cihazının kartını tasarlama · 6" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-182-7-a3a91362e1cf.jpg" alt="Antigravity&#x27;de masaüstü evcil hayvan cihazının kartını tasarlama · 7" width="560">

Type: Demo | Date: 2026-11-21

---

<a id="case-191"></a>
### Case 191: [Kod barındırma arayüzü prototipi geliştirme](https://x.com/TheDoraaaaaaaa/status/2124105099522068925) (by [@TheDoraaaaaaaa](https://x.com/TheDoraaaaaaaa))

**Özgün klipten hangi depo iş akışlarının gösterildiğini doğrulayın.**

Üretici kod barındırma prototipini Neon'a atfediyor ve uygulamanın videosunu yayımlıyor.

Özgün video prototip arayüzünü gösteriyor. Geliştirici yapımı Neon'a atfediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-191-1-5ced1b8bdd0c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-191-1-e229f7eea576.jpg" alt="Kod barındırma arayüzü prototipi geliştirme · 1" width="560"></a>

Type: Demo | Date: 2026-11-21

---

<a id="case-205"></a>
### Case 205: [Mevcut kodda CI tür denetimini hızlandırma](https://x.com/PokeBenchTV/status/2124158885749485816) (by [@PokeBenchTV](https://x.com/PokeBenchTV))

**İkinci iyileştirmeyi aynı kod tabanından elde edilen ölçümlerle değerlendirin.**

Geliştirici, önceki iyileştirmenin ardından CI'ı Neon ile yeniden incelediğini bildiriyor. Kendi kod tabanında tür denetiminin 6,5 dakikadan 1,5 dakikaya düştüğünü belirtiyor.

Ekran görüntüsü önceki ve sonraki ölçümlere eşlik ediyor. İyileşme, paylaşımda belirtilen kod tabanı ve CI ayarlarına ait.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-205-1-7b61661c2400.jpg" alt="Mevcut kodda CI tür denetimini hızlandırma · 1" width="560">

Type: Evaluation | Date: 2026-11-21

---

<a id="case-207"></a>
### Case 207: [Microduck simülasyonunda JEPA yardımcı modülünü prototipleme](https://x.com/rafaelcaricio/status/2124160567417897088) (by [@rafaelcaricio](https://x.com/rafaelcaricio))

**Yardımcı modülü simülasyonda değerlendirin ve hangi parçaların donanımda doğrulanması gerektiğini kaydedin.**

Üretici, Microduck için proprioseptif bir JEPA yardımcı modülü geliştirirken Gemini 4 Neon ve Carbon kullandığını bildiriyor.

Kaynak prototipi simülasyonla sınırlı olarak tanımlıyor. İki modeli belirtiyor ancak uygulama parçalarını modellere tek tek atamıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-207-1-ea19fe8ae519.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-207-1-53c032afc54f.jpg" alt="Microduck simülasyonunda JEPA yardımcı modülünü prototipleme · 1" width="560"></a>

Type: Demo | Date: 2026-11-21

---

<a id="case-212"></a>
### Case 212: [Bir MotionBricks karakter demosunu yerelde çalıştırma](https://x.com/ai_for_success/status/2124192968345338206) (by [@ai_for_success](https://x.com/ai_for_success))

**Modelin çalışma ortamına ait parçalarla çevresine eklenenleri belirleyin.**

Üretici, MotionBricks deposunu inceleme ve ONNX modelleriyle etkileşimli demo kurma işini Neon'a atfediyor. Demoyu NVIDIA GPU olmadan yerelde çalıştırdığını bildiriyor.

Özgün demo karakteri ve hareket denetimlerini gösteriyor. Yerel çalışma bilgisi üreticinin kurulumuna ait.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-212-1-5908a6b66d3f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-212-1-90af2b83d938.jpg" alt="Bir MotionBricks karakter demosunu yerelde çalıştırma · 1" width="560"></a>

Type: Integration | Date: 2026-11-21

---

<a id="case-220"></a>
### Case 220: [JPEN Dict'in macOS arayüzünü geliştirme](https://x.com/jake_j_jung/status/2124293069797495257) (by [@jake_j_jung](https://x.com/jake_j_jung))

**Yayımlanan arayüz değişikliğinde modelin rolünü belgeleyin.**

Geliştirici JPEN Dict 1.8.0'ı geliştirirken Antigravity'de Neon'a geçtiğini bildiriyor.

Yedi özgün ek çevrimdışı Japonca–İngilizce sözlüğün arayüzünün bölümlerini belgeliyor. Geliştirici arayüz düzenlemelerini Neon destekli iş akışına atfediyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-220-1-b51af065b24f.jpg" alt="JPEN Dict&#x27;in macOS arayüzünü geliştirme · 1" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-220-2-89151a2fd48f.jpg" alt="JPEN Dict&#x27;in macOS arayüzünü geliştirme · 2" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-220-3-1451faf9f0bc.jpg" alt="JPEN Dict&#x27;in macOS arayüzünü geliştirme · 3" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-220-4-da3ced85253b.jpg" alt="JPEN Dict&#x27;in macOS arayüzünü geliştirme · 4" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-220-5-3102c60b17cb.jpg" alt="JPEN Dict&#x27;in macOS arayüzünü geliştirme · 5" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-220-6-bc25ae9b22e4.jpg" alt="JPEN Dict&#x27;in macOS arayüzünü geliştirme · 6" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-220-7-3af8cc4f6099.jpg" alt="JPEN Dict&#x27;in macOS arayüzünü geliştirme · 7" width="560">

Type: Integration | Date: 2026-11-22

---

<a id="case-229"></a>
### Case 229: [Etkileşimli bir likidite radarı oluşturma](https://x.com/G33K13765260/status/2124355729507365148) (by [@G33K13765260](https://x.com/G33K13765260))

**Tek bir arayüzün fon hareketlerini ve likidite değişimlerini incelemeyi kolaylaştırıp kolaylaştırmadığını deneyin.**

Üretici, yayımlanan SI Liquidity Radar'ın yapımını Neon'a atfediyor.

Kaynak video görselleştirmeyi ve etkileşimi gösteriyor. Geliştirme süresi bu yayına ait.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-229-1-006c1092d04c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-229-1-7e81a5c9049e.jpg" alt="Etkileşimli bir likidite radarı oluşturma · 1" width="560"></a>

Type: Demo | Date: 2026-11-22

---

<a id="case-235"></a>
### Case 235: [Three.js otomobil yapımında Hydrogen ajanlarını koordine etme](https://x.com/Leviwoyun/status/2124421508563149279) (by [@Leviwoyun](https://x.com/Leviwoyun))

**Koordinasyonu bir modele verin ve geometri işini farklı ajanlara bölüştürün.**

Üretici, Three.js'de Lamborghini Veneno yapan beş Hydrogen ajanının koordinasyonunu Neon'a verdi.

Üretici üç yineleme bildiriyor. Özgün klip, oluşturulan otomobili ve iç mekânı farklı açılardan gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-235-1-de84a06d03f1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-235-1-043c69234b09.jpg" alt="Three.js otomobil yapımında Hydrogen ajanlarını koordine etme · 1" width="560"></a>

Type: Integration | Date: 2026-11-22

---

<a id="case-246"></a>
### Case 246: [Özel bir DAW üzerinden piyano parçası besteleyin](https://x.com/WichtelArt/status/2124570040318005314) (by [@WichtelArt](https://x.com/WichtelArt))

**DAW’ı MCP ile Neon’a bağlayın ve ajanın düzenlenebilir nota ızgarasına doğrudan nota yerleştirmesini sağlayın.**

Kayıt, tamamlanan düzenlemenin çalma sırasında nota ızgarasında kaydığını gösteriyor.

Yazar Antigravity’de Neon’u kendi DAW’u ile kullandı. Herkese açık gönderide “nice” ifadesi ve parçanın sonucu yer alıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-23/videos/case-246-1-8f9dda0956e4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-23/posters/case-246-1-d3f6fe0d1fab.jpg" alt="Özel bir DAW üzerinden piyano parçası besteleyin · 1" width="560"></a>

Type: Integration | Date: 2026-11-22

---

<a id="case-250"></a>
### Case 250: [Akıllı ev için özel bir uyandırma sözcüğü eğitin](https://x.com/ivanleomk/status/2124733026282406216) (by [@ivanleomk](https://x.com/ivanleomk))

**Antigravity’de Neon ile bir uyandırma modeli eğitin ve tetikleyiciyi ayrı bir niyet sınıflandırıcısına bağlayın.**

Gösterimde uyandırma modeli, sesle tetiklenen ev otomasyonuyla birlikte çalışıyor.

Yazar eğitilen hey_vanya.onnx modelini gösteriyor. Eylemleri ayrı Gemini Decisions sınıflandırıcısı seçiyor ve videoda Neon’un Home Assistant kurulumu görülüyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-23/videos/case-250-1-0b48e53c99c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-23/posters/case-250-1-0974fdf48dde.jpg" alt="Akıllı ev için özel bir uyandırma sözcüğü eğitin · 1" width="560"></a>

Type: Integration | Date: 2026-11-23

---

## 🎨 Grafik ve Arayüz Prototipleri
<a id="graphics"></a>

<a id="case-7"></a>
### Case 7: [Bir arabanın SVG yandan görünümünü çizin](https://x.com/HarshithLucky3/status/2123158145380085991) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Kodla işlenmiş yan görünümleri karşılaştırırken orantıyı ve silueti kontrol edin.**

Yaratıcı, bir BMW M4 CS yandan görünüşlü SVG oluşturmak için AI Studio'da Neon High'ı kullandı.

Eser yazıya eklenmiştir. Tam bir bilgi isteminden alıntı yapılmadı.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-7-1-ffea70bbfd83.png" alt="Bir arabanın SVG yandan görünümünü çizin · 1" width="560">

Type: Demo | Date: 2026-11-18

---

<a id="case-8"></a>
### Case 8: [Bir SVG test serisi çalıştırın](https://x.com/AdamHoltererer/status/2123159230291054903) (by [@AdamHoltererer](https://x.com/AdamHoltererer))

**SVG görevlerinde tutarlılığı değerlendirmeden önce çeşitli çıktıları inceleyin.**

Test cihazı, Neon SVG test serisinde üç çıktı paylaştı.

Sonuçlar birlikte sunulur ve bir test serisi olarak sayılır.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-8-1-2eb686ec5f13.jpg" alt="Bir SVG test serisi çalıştırın · 1" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-8-2-7f4fbb41bac4.jpg" alt="Bir SVG test serisi çalıştırın · 2" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-8-3-8ffa94a0957b.jpg" alt="Bir SVG test serisi çalıştırın · 3" width="560">

Type: Demo | Date: 2026-11-18

---

<a id="case-9"></a>
### Case 9: [Three.js'de bir pelikanı canlandırın](https://x.com/StatsWire/status/2123160089854898346) (by [@StatsWire](https://x.com/StatsWire))

**Döngü hareketini ve sahne oluşturmayı animasyonun ayrı parçaları olarak kontrol edin.**

Test cihazı, Three.js'nin bisiklet üzerindeki pelikan çıktısını Neon'a bağlar.

Yaratıcı bir kayıt sağlıyor ancak zamanlama veya akıl yürütme ayarı yok.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-9-1-80dcbc4fb2e8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-9-1-e0a6df02d79f.jpg" alt="Three.js&#x27;de bir pelikanı canlandırın · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-10"></a>
### Case 10: [xhigh'de bir SVG portresi çizin](https://x.com/lyraxana/status/2123161268647539052) (by [@lyraxana](https://x.com/lyraxana))

**Benzerliği ve SVG düzenlenebilirliğini bir portre testinde ayrı ayrı değerlendirin.**

Testi yapan kişi, Neon xhigh'e atfedilen Ana de Armas'ın bir portresini paylaşıyor.

Kaynak, konu ve çaba ayarını tam olarak belirtmeden veriyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-10-1-014b0af2bac3.jpg" alt="xhigh&#x27;de bir SVG portresi çizin · 1" width="560">

Type: Demo | Date: 2026-11-18

---

<a id="case-11"></a>
### Case 11: [Bisiklet süren bir pelikanı orta eforla canlandırın](https://x.com/xiangning0/status/2123161354496557071) (by [@xiangning0](https://x.com/xiangning0))

**Farklı muhakeme ayarlarındaki sonuçları karşılaştırmak için sabit bir animasyon görevi kullanın.**

Yazar, bir pelikan bisiklet demosu oluşturmak için Neon'u orta düzeyde bir çabayla kullandı ve videoyu yayınladı.

Klip, bu yaratıcının ortak bir test görevinin ayrı çalışmasını belgeliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-11-1-0b2be9516bad.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-11-1-200a792de0b6.jpg" alt="Bisiklet süren bir pelikanı orta eforla canlandırın · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-12"></a>
### Case 12: [İki voksel bahçesi sahnesini karşılaştırın](https://x.com/Angaisb_/status/2123161449681805531) (by [@Angaisb_](https://x.com/Angaisb_))

**Benzer görünen çıktıları toplam çalıştırma maliyetine ve her kaynağın açıkladığı ayarlara göre kontrol edin.**

Yazar, GPT-6.2 Sol xhigh sonucunun yanı sıra Neon xhigh'den bir voksel bahçesi yayınladı.

Kaynak, ilk görüntünün Neon olduğunu belirtiyor ve Sol için 0,19 ABD dolarına karşılık 1,01 ABD doları bildiriyor. Gönderi, istemlerin ve araçların eşleşip eşleşmediğini belirtmiyor.

<table>
<tr>
<td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-12-1-115849b38af5.jpg" alt="İki voksel bahçesi sahnesini karşılaştırın · 1" width="560"></td>
<td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-12-2-59e2b840c413.jpg" alt="İki voksel bahçesi sahnesini karşılaştırın · 2" width="560"></td>
</tr>
</table>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-13"></a>
### Case 13: [Three.js ve GLSL sahnesi oluşturun](https://x.com/cfenghub/status/2123162154132242885) (by [@cfenghub](https://x.com/cfenghub))

**Bir grafik testinde gölgelendirici davranışını, sahne geometrisini ve oluşturma süresini ayırın.**

İçerik oluşturucu, Neon'dan bir Three.js ve GLSL çıktısı paylaşıyor ve iki dakika 40 saniyelik bir çalışma rapor ediyor.

Ana gönderi, alıntı yapmadan talimata verilen yanıtlara işaret eder.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-13-1-e62c3cb9bbab.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-13-1-f2c7b50bad23.jpg" alt="Three.js ve GLSL sahnesi oluşturun · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-14"></a>
### Case 14: [Tamamen kodla resimler oluşturun](https://x.com/kickingkeys/status/2123162238643044705) (by [@kickingkeys](https://x.com/kickingkeys))

**Kodun nasıl tutarlı bir görsel dizi oluşturabileceğini görmek için işlenmiş örnekleri açın.**

İçerik oluşturucu, resimleri işleyen kodu yazmak için erken erişim Neon'u kullandığını bildiriyor.

Kaynak aynı seriden bir dizi sonuç sağlıyor. Her kesin istemi sağlamaz.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-1-9f61a388e0c1.jpg" alt="Tamamen kodla resimler oluşturun · 1" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-2-3362674fdd00.jpg" alt="Tamamen kodla resimler oluşturun · 2" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-3-51899966784e.jpg" alt="Tamamen kodla resimler oluşturun · 3" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-4-74693c0f8c18.jpg" alt="Tamamen kodla resimler oluşturun · 4" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-5-977a643ac612.jpg" alt="Tamamen kodla resimler oluşturun · 5" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-6-74e97910a739.jpg" alt="Tamamen kodla resimler oluşturun · 6" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-7-516b3420d145.jpg" alt="Tamamen kodla resimler oluşturun · 7" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-8-7766df7b1a79.jpg" alt="Tamamen kodla resimler oluşturun · 8" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-9-1a353988571a.jpg" alt="Tamamen kodla resimler oluşturun · 9" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-10-57e623c52098.jpg" alt="Tamamen kodla resimler oluşturun · 10" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-11-e9fe2e7b6c2c.jpg" alt="Tamamen kodla resimler oluşturun · 11" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-12-2213841fb938.jpg" alt="Tamamen kodla resimler oluşturun · 12" width="560">

Type: Demo | Date: 2026-11-18

---

<a id="case-15"></a>
### Case 15: [Pelikan bisiklet animasyonlarını karşılaştırın](https://x.com/Super_Nius/status/2123162610254442796) (by [@Super_Nius](https://x.com/Super_Nius))

**Bildirilen çalışma süresini aynı videodaki hareket ve sahne ayrıntılarıyla karşılaştırın.**

Testi yapan kişi bir pelikan animasyonunu Neon, Hydrogen, GPT-6.2 Astra ve GPT-6.2 Sol'da karşılaştırdı.

Yazar üç dakikalık bir Neon koşusu yaptığını ve bunun görünümünü tercih ettiğini bildiriyor. Kaydedilen Yalnızca Sol takibi aynı teste aittir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-15-1-e9c127cb6e40.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-15-1-444e97e2290b.jpg" alt="Pelikan bisiklet animasyonlarını karşılaştırın · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-16"></a>
### Case 16: [Three.js bisiklet animasyonlarını üç modelde karşılaştırın](https://x.com/AI_Screening/status/2123164032882659819) (by [@AI_Screening](https://x.com/AI_Screening))

**Hareketi, ışığı ve sahne kompozisyonunu karşılaştırmak için etiketli klipleri kullanın.**

Test cihazı Neon, Opus 5.5 ve Carbon'un Three.js bisiklet karşılaştırmasını yayınladı.

Yazar, Neon'u Opus'a tercih etti ve onu Carbon'a yakın olarak değerlendirdi. Bu yazarın görsel değerlendirmesidir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-16-1-2fcea711afca.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-16-1-491c82d3f1f5.jpg" alt="Three.js bisiklet animasyonlarını üç modelde karşılaştırın · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-17"></a>
### Case 17: [Okyanusta uzun bir gemi render edin](https://x.com/Mr_Salio/status/2123164576275370440) (by [@Mr_Salio](https://x.com/Mr_Salio))

**Klip boyunca dalga animasyonu ve gemi görselleştirmesinin tutarlı kalıp kalmadığını kontrol edin.**

Testi yapan kişi, Neon xhigh'e atfedilen bir okyanusta yelken sahnesi paylaştı.

Videoda animasyonlu bir yelkenli gemi gösterilmektedir. Kaynak belirli bir iş akışı veya zamanlama sağlamıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-17-1-39aa1af81d28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-17-1-c2e29bd290ea.jpg" alt="Okyanusta uzun bir gemi render edin · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-18"></a>
### Case 18: [Bir voksel pagodası oluşturun](https://x.com/LuminaBench/status/2123164858996908367) (by [@LuminaBench](https://x.com/LuminaBench))

**Katmanlamayı, silueti ve kompozisyonu değerlendirmek için voksel sahnesini kullanın.**

Testi yapan kişi Neon xhigh'de oluşturulan bir voksel pagodasını yayınlıyor.

Gönderi, oluşturulan sonucu ve yazarın tasarım tepkisini içerir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-18-1-66d691af4081.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-18-1-8da133675a5d.jpg" alt="Bir voksel pagodası oluşturun · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-19"></a>
### Case 19: [Bisiklete binen hayal kırıklığına uğramış bir pelikan çizin](https://x.com/HarshithLucky3/status/2123165824576114932) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Karakter ifadesinin ve bisiklet hareketinin net bir şekilde okunup okunmadığını kontrol edin.**

Yaratıcı, bisiklete binen hayal kırıklığına uğramış bir pelikanın SVG'sini çizmek için AI Studio'da Neon High'ı kullandı.

Gönderi sonucu gösterir ve efor ayarını tanımlar.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-19-1-44580d20f3b7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-19-1-b8df2a6ac156.jpg" alt="Bisiklete binen hayal kırıklığına uğramış bir pelikan çizin · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-20"></a>
### Case 20: [Gamepad çizimlerini GPT-6.2 Sol ile karşılaştırın](https://x.com/notjazii/status/2123166093422272839) (by [@notjazii](https://x.com/notjazii))

**İki gamepad çıkışı için işleme kalitesini, süreyi ve maliyeti ayrı ayrı karşılaştırın.**

Testi yapan kişi, her modelin mevcut en yüksek muhakemesinde aynı istemi kullandı ve çıktıların benzer olduğuna karar verdi.

Yazar, Neon için 20 dakika ve yaklaşık 1,60 ABD Doları, Sol için ise dokuz dakika ve yaklaşık 0,53 ABD Doları bildirdi.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-20-1-617938f21f28.jpg" alt="Gamepad çizimlerini GPT-6.2 Sol ile karşılaştırın · 1" width="560">

Type: Evaluation | Date: 2026-11-18

---

<a id="case-21"></a>
### Case 21: [3 boyutlu deniz uçağı oluşturun](https://x.com/LuminaBench/status/2123166304664191391) (by [@LuminaBench](https://x.com/LuminaBench))

**Prototipi bir bütün olarak değerlendirmeden önce deniz uçağı ve su etkileşimini inceleyin.**

Testi gerçekleştiren kişi, 3D deniz uçağı oluşturmak için Neon xhigh'i kullandı ve bir video paylaştı.

Yaratıcı, duvar saati ölçümü yapmadan, yapıyı hızlı ve arayüzü daha temiz olarak tanımlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-21-1-738f7ccd5e11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-21-1-b2943474925e.jpg" alt="3 boyutlu deniz uçağı oluşturun · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-22"></a>
### Case 22: [2 boyutlu bir at çizin](https://x.com/jony_palino/status/2123168463640269001) (by [@jony_palino](https://x.com/jony_palino))

**At klibini görsel bir örnek olarak ele alın ve modeller arası ayarları aklınızda bulundurun.**

Yaratıcı iki boyutlu bir at üretmek için Neon'u kullandı ve çıktıyı yayınladı.

Yaratıcı bunu önceki Gemini sonuçlarına tercih etti. Gönderi eşleşen ayarları sağlamıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-22-1-0806852b6c63.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-22-1-e4f265e40f74.jpg" alt="2 boyutlu bir at çizin · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-23"></a>
### Case 23: [Yağmurlu bir market sahnesini test edin](https://x.com/Super_Nius/status/2123169627815698522) (by [@Super_Nius](https://x.com/Super_Nius))

**Sunumun daha kısa oluşturma süresiyle nasıl değiştiğini değerlendirmek için eşleşen sahneyi kullanın.**

Testi yapan kişi Neon ve GPT-6.2 Sol için aynı istemi kullandı ve karşılaştırmayı yayınladı.

Yazar, bu çalışmada Neon'un daha hızlı ve daha ucuz tamamlandığını bildirirken Sol görsel çıktısını tercih etti.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-23-1-9e27412d4ad5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-23-1-d8e64f437d92.jpg" alt="Yağmurlu bir market sahnesini test edin · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-24"></a>
### Case 24: [Tek bir görüntüden dört ayaklı bir robotu canlandırın](https://x.com/thebuggeddev/status/2123170821250400282) (by [@thebuggeddev](https://x.com/thebuggeddev))

**Yürüyüşü ve hareketi, sahnenin referansı ne kadar yakından takip ettiğinden ayrı olarak kontrol edin.**

Geliştirici Neon'a tek bir referans görseli verdi ve 3 boyutlu bir model istedi.

Geliştirici, dört ayaklı ters kinematik ve yürüyüş, süratli ve dörtnala animasyonları içeren bir Three.js WebGPU gösterimini rapor ediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-24-1-acb1deb37714.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-24-1-22e170b487dd.jpg" alt="Tek bir görüntüden dört ayaklı bir robotu canlandırın · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-25"></a>
### Case 25: [Keats'i vanilya JavaScript'te canlandırın](https://x.com/vamsibatchuk/status/2123170948568535488) (by [@GeokenAI](https://x.com/GeokenAI))

**Edebi bir kaynağı yorumlamak için kod kullanırken animasyon ve fırça çalışmalarını karşılaştırın.**

Bir Google ekibi üyesi, Keats'in To Autumn filminin vanilya JavaScript animasyonu için GeokenAI ve Neon'a teşekkür ediyor.

Gönderi, kütüphanesi olmayan, 12 fps'lik, resimsel bir 3D animasyonu anlatıyor. Paylaşım hesabı, adı geçen yaratıcıdan farklıdır.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-25-1-251f0dd0d495.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-25-1-3927f6ba8991.jpg" alt="Keats&#x27;i vanilya JavaScript&#x27;te canlandırın · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-26"></a>
### Case 26: [Triceratops demosu oluşturun](https://x.com/LeslieNooteboom/status/2123171009167765651) (by [@LeslieNooteboom](https://x.com/LeslieNooteboom))

**Yeniden yapılandırma sırasını ve son görseli inceleyin.**

Yaratıcı, Triceratops gösterisini Neon'a atfediyor.

Video eseri göstermektedir. Gönderi, giriş formatını veya oluşturma adımlarını belirtmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-26-1-8c4ac6bb4433.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-26-1-e0d7589c04bb.jpg" alt="Triceratops demosu oluşturun · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-27"></a>
### Case 27: [3D dişli takımı görüntülerini karşılaştırın](https://x.com/SPAC89/status/2123171830739632189) (by [@SPAC89](https://x.com/SPAC89))

**Dört dişli dizisi görüntüsünün tümünü karşılaştırmak için etiketli ayarları ve çıktı geometrisini kullanın.**

Test cihazı, etiketli akıl yürütme seviyelerinde Neon, Carbon, Astra ve Sol için dişli mekanizması görüntülerini gösterir.

Yazar Neon'u tercih etti. Klip, görsel bir karşılaştırmayı belgelemektedir ve genel maliyet iddiasını oluşturmamaktadır.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-27-1-94516eb237d5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-27-1-c7804af5b07a.jpg" alt="3D dişli takımı görüntülerini karşılaştırın · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-28"></a>
### Case 28: [Tek bir HTML dosyasında on etkileşimli efekt oluşturun](https://x.com/agenticjay/status/2123172043533508664) (by [@agenticjay](https://x.com/agenticjay))

**Efektlerin küçük bir HTML verisi içinde duyarlı ve okunabilir kalıp kalmadığını kontrol edin.**

Bir Google ekibi üyesi, 27 KB'lik bir HTML dosyasında on etkileşimli 3D efekt oluşturmak için Neon'u kullandığını bildirdi.

Demoda gölgelendiriciler, su ve aydınlatma yer alıyor. Varyasyonlar yayınlanmış tek bir proje olarak gruplandırılır.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-28-1-7af28a595410.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-28-1-91d62f30b2e1.jpg" alt="Tek bir HTML dosyasında on etkileşimli efekt oluşturun · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-29"></a>
### Case 29: [Antigravity Swarm ile bir Blender laboratuvar tezgahı oluşturun](https://x.com/Google/status/2123172290250621166) (by [@Google](https://x.com/Google))

**Hangi Swarm koordinatlarının çalıştığını ve Blender'ın hangi işlemleri gerçekleştirdiğinin izini sürün.**

Google, Gemini 4 ailesi temalı bir laboratuvar tezgahı sahnesi oluşturmak için Neon'un Antigravity Swarm ve Blender'ı kullandığını gösterdi.

Klip, entegre iş akışının sağlayıcı demosudur.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-29-1-24f7c4b89ee2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-29-1-5515f85f88ea.jpg" alt="Antigravity Swarm ile bir Blender laboratuvar tezgahı oluşturun · 1" width="560"></a>

Type: Integration | Date: 2026-11-18

---

<a id="case-30"></a>
### Case 30: [Opus 5.5 ile mimari illüstrasyonları karşılaştırın](https://x.com/notjazii/status/2123172429791129848) (by [@notjazii](https://x.com/notjazii))

**Aynı görsel görevi belirleyin ve çıktı kalitesini, çalışma süresini ve maliyetini bağımsız olarak karşılaştırın.**

Testi yapan kişi, aynı istemi kullanarak modelleri mevcut en yüksek mantıkla karşılaştırdı.

Yazar, Opus çıkışını tercih ederek Neon için yaklaşık 20 dakika ve 3,50 ABD Doları ve Opus için 18 dakika ve 7,20 ABD Doları bildirdi.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-30-1-b5e87dfb79f7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-30-1-b13b60aca1f2.jpg" alt="Opus 5.5 ile mimari illüstrasyonları karşılaştırın · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-31"></a>
### Case 31: [Voyager 1’in uçuşunu görselleştirin](https://x.com/SamuelAlbanie/status/2123174398064570622) (by [@SamuelAlbanie](https://x.com/SamuelAlbanie))

**Sırayı değerlendirirken kalkış, uçuş ve yakın çekim arasındaki geçişleri gözden geçirin.**

Yazar, fırlatma aşamasından Jüpiter karşılaşmasına kadar geçen 3 boyutlu Voyager 1 sekansını ve uzay aracının yakın çekimini gösteriyor.

Yazar bunu serideki rafine edilmemiş bir ipucu olarak tanımlıyor. Hiçbir yörünge doğrulaması bildirilmedi.

[Ek kaynak](https://x.com/SamuelAlbanie/status/2123174391617867925)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-31-1-2819a8649adb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-31-1-49c120f1aa13.jpg" alt="Voyager 1’in uçuşunu görselleştirin · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-32"></a>
### Case 32: [3B bir planetaryum oluşturun](https://x.com/SamuelAlbanie/status/2123174400572719261) (by [@SamuelAlbanie](https://x.com/SamuelAlbanie))

**Basit bir eğitim demosu olarak gezegen ve takımyıldız görünümlerinin birlikte çalışıp çalışmadığını kontrol edin.**

Yazar, gezegenler arasında hareket eden bir 3 boyutlu planetaryumu ve takımyıldız görünümünü gösteriyor.

Kayıt, Dünya ve Satürn'ün de aralarında bulunduğu örnekleri gösteriyor. Tek istem serisi astronomik kesinlik sağlamaz.

[Ek kaynak](https://x.com/SamuelAlbanie/status/2123174391617867925)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-32-1-3744b688f28d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-32-1-f238cb6328df.jpg" alt="3B bir planetaryum oluşturun · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-33"></a>
### Case 33: [Babbage’ın 2 Numaralı Fark Makinesi’ni görselleştirin](https://x.com/SamuelAlbanie/status/2123174403038982379) (by [@SamuelAlbanie](https://x.com/SamuelAlbanie))

**Görselleştirmeyi incelerken dişli hareketine, sayısal ekrana ve tam makine görünümüne bakın.**

Yazar, dişli düzenekleri ve sayısal ekranıyla Babbage'nin 2 Numaralı Fark Motorunun 3 boyutlu görselleştirmesini gösteriyor.

Kayıt, hareketli mekanizmanın yakın çekimleri ile makinenin tamamının görünümü arasında hareket eder.

[Ek kaynak](https://x.com/SamuelAlbanie/status/2123174391617867925)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-33-1-8f8b964cd1a7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-33-1-e80ac8cce5ad.jpg" alt="Babbage’ın 2 Numaralı Fark Makinesi’ni görselleştirin · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-34"></a>
### Case 34: [Antikythera mekanizmasını görselleştirin](https://x.com/SamuelAlbanie/status/2123174406419828813) (by [@SamuelAlbanie](https://x.com/SamuelAlbanie))

**Kurtarılan parça görünümünü, donanım yeniden yapılandırmasını ve kadran okumasını aynı demoda karşılaştırın.**

Yazar, kurtarılan nesne, yeniden inşa edilen dişliler ve bir kadran arasında geçiş yapan bir 3D Antikythera mekanizması demosunu gösteriyor.

Kayıt, düzeneğin bir görüntüsünü ve hareketli mekanizmanın ayrıntılarını gösterir.

[Ek kaynak](https://x.com/SamuelAlbanie/status/2123174391617867925)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-34-1-de291a3cf77f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-34-1-8f404bea04c4.jpg" alt="Antikythera mekanizmasını görselleştirin · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-35"></a>
### Case 35: [Hava akışını gösteren bir rüzgâr tüneli prototipi yapın](https://x.com/SamuelAlbanie/status/2123174409284260270) (by [@SamuelAlbanie](https://x.com/SamuelAlbanie))

**Görselleştirmeyi bir öğretim örneği olarak kullanmadan önce akış çizgilerinin test şekilleri arasında nasıl değiştiğini karşılaştırın.**

Yazar, farklı şekiller etrafında görünür hava akışı düzeneklerine sahip bir 3 boyutlu rüzgar tüneli demosu gösteriyor.

Videoda bir uçak ve diğer test şekilleri yer alıyor. Simülasyon için bağımsız bir doğruluk kontrolü sağlamaz.

[Ek kaynak](https://x.com/SamuelAlbanie/status/2123174391617867925)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-35-1-9424d7eab5ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-35-1-acc3f3a6f94a.jpg" alt="Hava akışını gösteren bir rüzgâr tüneli prototipi yapın · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-36"></a>
### Case 36: [King’s College Şapeli’nin kesitini oluşturun](https://x.com/SamuelAlbanie/status/2123174412488716605) (by [@SamuelAlbanie](https://x.com/SamuelAlbanie))

**Her görünümün binayı nasıl açıkladığını görmek için dış cepheyi, nefi ve kesiti karşılaştırın.**

Yazar, King's College Şapeli'nin dış ve iç mekan arasında geçiş yapan 3 boyutlu bir kesitini gösteriyor.

Sahne, nefi, pencereleri ve binanın kesitini göstermek için farklı görünümler kullanıyor.

[Ek kaynak](https://x.com/SamuelAlbanie/status/2123174391617867925)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-36-1-8c718b6a7b3c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-36-1-72acb7ce83d2.jpg" alt="King’s College Şapeli’nin kesitini oluşturun · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-37"></a>
### Case 37: [Nehir üzerindeki viyadüğü ve çevresini görselleştirin](https://x.com/SamuelAlbanie/status/2123174416154759418) (by [@SamuelAlbanie](https://x.com/SamuelAlbanie))

**Hem köprüyü hem de çevresindeki sahneyi değerlendirmek için yakın, uzak ve tel çerçeve görünümlerini kullanın.**

Yazar, çok kemerli bir viyadük, bir tren ve çeşitli görsellerle birlikte 3 boyutlu bir nehir vadisini gösteriyor.

Kayıt, yakın ve uzak kamera açıları arasında geçiş yapar ve tel çerçeve benzeri bir görünüm içerir.

[Ek kaynak](https://x.com/SamuelAlbanie/status/2123174391617867925)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-37-1-d12ab14ffcb0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-37-1-56962c64e01c.jpg" alt="Nehir üzerindeki viyadüğü ve çevresini görselleştirin · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-38"></a>
### Case 38: [Cambridge’den esinlenen bir 3B şehir görünümü oluşturun](https://x.com/SamuelAlbanie/status/2123174419379962139) (by [@SamuelAlbanie](https://x.com/SamuelAlbanie))

**Kamera sahnede hareket ederken önemli noktaların ve nehrin nasıl tanınabilir kaldığını kontrol edin.**

Yazar, modellenen blokların havadan ve daha yakından görüntüleriyle Cambridge'den ilham alan bir şehir görselleştirmesi gösteriyor.

Klipte nehir, binalar ve sahne katmanları gösteriliyor. Yazar ortamı Cambridge benzeri olarak tanımlıyor.

[Ek kaynak](https://x.com/SamuelAlbanie/status/2123174391617867925)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-38-1-731938345922.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-38-1-fdabb0976ddb.jpg" alt="Cambridge’den esinlenen bir 3B şehir görünümü oluşturun · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-39"></a>
### Case 39: [Neon temalı bir Dünya oluşturma](https://x.com/HarshithLucky3/status/2123175900007309696) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Küre döndükçe görsel temanın tutarlı olup olmadığını kontrol edin.**

Yaratıcı, neon temalı bir gezegen oluşturmak için Neon'u Antigravity'de yüksek olarak kullandı.

Kaynak, sonuç ve çaba ayarını sağlar.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-39-1-b5f3ce29cb24.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-39-1-113aeb084222.jpg" alt="Neon temalı bir Dünya oluşturma · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-40"></a>
### Case 40: [Bir yat sahnesini yineleyin](https://x.com/LyalinDotCom/status/2123176455123165366) (by [@LyalinDotCom](https://x.com/LyalinDotCom))

**Modelden bir 3B sahneyi iyileştirmesini isterken önceki ve sonraki yapıtları inceleyin.**

Yaratıcı, Neon'un bir yat sahnesini iyileştirdiğini ve çıktıyı gösterdiğini bildiriyor.

Firebase dağıtımı, gönderi sırasında belirtilen bir niyetti.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-40-1-367b9069fe9e.jpg" alt="Bir yat sahnesini yineleyin · 1" width="560">

Type: Demo | Date: 2026-11-18

---

<a id="case-41"></a>
### Case 41: [Özel bir VFX aracında kostüm malzemeleri hazırlayın](https://x.com/fofrAI/status/2123176812360745019) (by [@fofrAI](https://x.com/fofrAI))

**Bir malzeme seçerken aynı kostüm formunun uygulamalarını karşılaştırın.**

Yaratıcı, kostüm malzemeleri hazırlamak için Neon'u kullandı ve sonuçların altı resmini yayınladı.

İçerik oluşturucu, VFX araçlarını kendisine ait olarak tanımlıyor. Kaynak bağımsız bir performans karşılaştırması oluşturmaz.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-41-1-ec60d5cf5112.jpg" alt="Özel bir VFX aracında kostüm malzemeleri hazırlayın · 1" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-41-2-88c3a0c15c9e.jpg" alt="Özel bir VFX aracında kostüm malzemeleri hazırlayın · 2" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-41-3-a6a770888735.jpg" alt="Özel bir VFX aracında kostüm malzemeleri hazırlayın · 3" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-41-4-66dd457d66be.jpg" alt="Özel bir VFX aracında kostüm malzemeleri hazırlayın · 4" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-41-5-adda34356599.jpg" alt="Özel bir VFX aracında kostüm malzemeleri hazırlayın · 5" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-41-6-4dbc04fb999c.jpg" alt="Özel bir VFX aracında kostüm malzemeleri hazırlayın · 6" width="560">

Type: Demo | Date: 2026-11-18

---

<a id="case-42"></a>
### Case 42: [Voksel Ninjago sahnelerini karşılaştırın](https://x.com/thehypedotnews/status/2123182627674796462) (by [@thehypedotnews](https://x.com/thehypedotnews))

**Aynı konudaki bir voksel karşılaştırmasında görsel çerçeveyi ve maliyeti ayrı ayrı değerlendirin.**

Kaynak, Neon ve Fable 5.2'yi bir voksel rekreasyonunda karşılaştırıyor.

Yazar Neon için 12,93 ABD Doları ve Fable için 11,19 ABD Doları bildirmiştir ve ikincisinin çerçevelemesini tercih etmiştir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-42-1-e2257b7ed90f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-42-1-1c3b543e0111.jpg" alt="Voksel Ninjago sahnelerini karşılaştırın · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-43"></a>
### Case 43: [Pelikan ürünü hareketli grafiği oluşturun](https://x.com/chetaslua/status/2123184113561817370) (by [@chetaslua](https://x.com/chetaslua))

**Kısa bir ürün animasyonunda zamanlamaya ve tipografiye bir arada bakın.**

Yaratıcı, Neon'a pelikan temalı bir ürün hareketli grafiği sağladığını söylüyor.

Bağlantılı klip çıktıyı gösterir. Gönderi, uygulamayı veya kesin bir istemi açıklamıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-43-1-41540f06843a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-43-1-d81b2060fc29.jpg" alt="Pelikan ürünü hareketli grafiği oluşturun · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-44"></a>
### Case 44: [New York City sahne prototiplerini karşılaştırın](https://x.com/aipulseda1ly/status/2123188460639117489) (by [@aipulseda1ly](https://x.com/aipulseda1ly))

**Bir şehir sahnesi yapısında dönüm noktası sadakatini ve çalışma zamanı performansını ayrı ayrı değerlendirin.**

Testi yapan kişi Neon'un Brooklyn Köprüsü'nü, Özgürlük Anıtı'nı ve taksilerin bulunduğu bir caddeyi içerdiğini bildirdi.

Testi gerçekleştiren kişi, Opus çıktısındaki bazı ayrıntıları tercih etti ve Neon sahnesini çalıştırmanın bilgisayarlarında gecikme yaşadığını bildirdi.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-44-1-85f5c28fc00c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-44-1-7a276a2045df.jpg" alt="New York City sahne prototiplerini karşılaştırın · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-45"></a>
### Case 45: [Muz görsel testi yapın](https://x.com/AdamHoltererer/status/2123189288107999706) (by [@AdamHoltererer](https://x.com/AdamHoltererer))

**Basit bir görsel görevin ayrıntılar ve oranlar karşısında nasıl ayakta kaldığını inceleyin.**

Testi yapan kişi Muz Testi başlıklı bir test için bir Neon çıktısı yayınlar.

Çıktı kaynağa eklenir. Kaynak kesin bir bilgi vermiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-45-1-9efc4470be00.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-45-1-c82bae60d92d.jpg" alt="Muz görsel testi yapın · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-46"></a>
### Case 46: [Perili bir katedrali tek seferde karşılaştırın](https://x.com/jan_volad/status/2123205954649100424) (by [@jan_volad](https://x.com/jan_volad))

**Açıklanan koşullar altında iki katedral görüntüsünü karşılaştırmak için yayınlanan istemi kullanın.**

Testi yapan kişi Neon ve GPT-6.2 Sol'a aynı perili katedral görevini verdi.

İçerik oluşturucu, Neon için 2,67 ABD Doları ve Sol için 1,69 ABD Doları bildirdi; değerlendirmesinde net bir görsel kazanan yok.

**Prompt:**

```
Build a huge haunted vampire cathedral
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-46-1-c1293f480928.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-46-1-8adbefb0cdfe.jpg" alt="Perili bir katedrali tek seferde karşılaştırın · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-19

---

<a id="case-47"></a>
### Case 47: [Antigravity'de bir telefon aksamının prototipini yapın](https://x.com/ai_for_success/status/2123207149870547423) (by [@ai_for_success](https://x.com/ai_for_success))

**Bir tasarım prototipini incelerken bileşen doğruluğunu ve son montajı ayrı ayrı kontrol edin.**

Geliştirici, Antigravity'de Neon'u kullandı ve tasarım bileşenlerinden oluşan bir pano ile işlenmiş bir telefon aksamını gösterdi.

Geliştirici, zamanlamalar veya kontrollü bir Carbon karşılaştırması olmadan, kodlama ve hıza ilişkin erken izlenimleri rapor eder.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-47-1-188cdb56dd8e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-47-1-e54b9bc965db.jpg" alt="Antigravity&#x27;de bir telefon aksamının prototipini yapın · 1" width="560"></a>

Type: Demo | Date: 2026-11-19

---

<a id="case-48"></a>
### Case 48: [Etkileşimli bir tarihi yelkenli gemi oluşturun](https://x.com/abhinavflac/status/2123212198663323848) (by [@abhinavflac](https://x.com/abhinavflac))

**İnteraktif çıktıda gemi ile su arasındaki sınırları inceleyin.**

Yazar, sıfır atışlı bir 3D yelkenli gemi gösterimi yayınladı.

Yazar, geminin ve suyun farklı katmanlar halinde oluşturulduğunu bildiriyor ve çıktıyı Sol sonuçlarından daha gerçekçi olarak tanımlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-48-1-8398538c7634.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-48-1-19d730412b53.jpg" alt="Etkileşimli bir tarihi yelkenli gemi oluşturun · 1" width="560"></a>

Type: Demo | Date: 2026-11-19

---

<a id="case-49"></a>
### Case 49: [JavaScript'te bir model tanıtımı tasarlama](https://x.com/chetaslua/status/2123219124260315301) (by [@chetaslua](https://x.com/chetaslua))

**JavaScript hareketli grafiğinde tipografiyi ve ilerleme hızını inceleyin.**

Yazar, modeli tanıtan bir hareketli grafik oluşturmak için Neon'u kullandı.

Yazar, harici varlıklar olmadan JavaScript kullandığını söylüyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-49-1-640c76599969.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-49-1-213f5084a7a0.jpg" alt="JavaScript&#x27;te bir model tanıtımı tasarlama · 1" width="560"></a>

Type: Demo | Date: 2026-11-19

---

<a id="case-50"></a>
### Case 50: [Tek geçişte kayak kulübesi sahnesi oluşturun](https://x.com/DesignArena/status/2123220446074253768) (by [@DesignArena](https://x.com/DesignArena))

**Bu tek geçişli sahne karşılaştırmasını değerlendirirken kulübeyi, karı ve ağaçları ayrı ayrı kontrol edin.**

DesignArena, Neon ve Argon'dan aynı Alp kulübesi ortamını oluşturmalarını istedi ve yan yana çıktıları yayınladı.

DesignArena her iki görselleştirmenin de öğelerini tercih etti. Neon'un sorulmadan kar yağışı eklediğini bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-50-1-a966b54bde0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-50-1-d867d8d5e6d7.jpg" alt="Tek geçişte kayak kulübesi sahnesi oluşturun · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-19

---

<a id="case-51"></a>
### Case 51: [Bir voksel fantezi kalesi oluşturun](https://x.com/Lentils80/status/2123226306351661099) (by [@Lentils80](https://x.com/Lentils80))

**Tek istemli bir derlemeyi değerlendirirken son sahneyi ve bildirilen çalışma süresini gözden geçirin.**

Yaratıcı, Neon xhigh'de üretilen bir voksel kalesini paylaşıyor.

İçerik oluşturucu bir istemi ve 27 dakikalık bir tamamlanma süresini bildirir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-51-1-27fe32067ec9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-51-1-e38a5f2c5e9e.jpg" alt="Bir voksel fantezi kalesi oluşturun · 1" width="560"></a>

Type: Demo | Date: 2026-11-19

---

<a id="case-52"></a>
### Case 52: [Ahtapot bisiklet animasyonunu Astra ile karşılaştırın](https://x.com/ZryMiller/status/2123228351984980040) (by [@ZryMiller](https://x.com/ZryMiller))

**İki muhakeme ayarını açık tutarak animasyonu ve maliyeti karşılaştırın.**

Test kaydında Astra (xhigh) 21 dakika 53 saniye ve 2,52 USD, Neon (high) ise 41 dakika ve 4,02 USD sürdü.

Yazar, animasyon kalitesini yakın olarak adlandırıyor. Bu, farklı akıl yürütme ayarlarında yapılan bir çalışmadır.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-52-1-0039f05541ac.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-52-1-546dd90156c6.jpg" alt="Ahtapot bisiklet animasyonunu Astra ile karşılaştırın · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-19

---

<a id="case-53"></a>
### Case 53: [Three.js kelebek animasyonu](https://x.com/thtbee_/status/2123259795172212871) (by [@thtbee_](https://x.com/thtbee_))

**Benzer bir Three.js deneyini boyutlandırmak için klibi ve rapor edilen kaynak kullanımını kullanın.**

Bir yaratıcı, Three.js kelebek animasyonu oluşturmak için Antigravity'de Neon xhigh'i kullandı.

Yaratıcı, 57 dakikayı, yani beş saatlik kotasının yaklaşık %23'ünü ve haftalık kotasının %7'sini bildirdi.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-53-1-efb25e8f446f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-53-1-7a50c0010ea3.jpg" alt="Three.js kelebek animasyonu · 1" width="560"></a>

Type: Demo | Date: 2026-11-19

---

<a id="case-54"></a>
### Case 54: [Referans görüntülerden bileşenler ve hareket oluşturun](https://x.com/op7418/status/2123269503736070603) (by [@op7418](https://x.com/op7418))

**Görsel referanslar sağlayın ve düzen doğruluğunu ve hareketi ayrı kriterler olarak değerlendirin.**

Yaratıcı, çeşitli bileşenleri ve bunlara eşlik eden hareketleri oluşturmak için görsel referanslar kullandı.

Demo sonucu gösterir. Opus'a kıyasla nasıl bir his verdiğine dair iddia yaratıcının takdiridir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-54-1-aab23e8d82f9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-54-1-c4200a430fb5.jpg" alt="Referans görüntülerden bileşenler ve hareket oluşturun · 1" width="560"></a>

Type: Demo | Date: 2026-11-19

---

<a id="case-55"></a>
### Case 55: [Three.js'de piksel sihirbazı dünyası](https://x.com/thtbee_/status/2123279727935033355) (by [@thtbee_](https://x.com/thtbee_))

**Yinelemeyle görsel cilanın nasıl değiştiğini yargılamak için üç geçişi kullanın.**

Bir yaratıcı Neon'a referans görseller verdi ve Three.js sahnesini üç geçişte geliştirdi.

Yaratıcı, Antigravity'de beş saatlik kotasının %39'unu ve haftalık kotasının %11'ini kullandığını bildirdi.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-55-1-ea88133798aa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-55-1-bdca3bf63f42.jpg" alt="Three.js&#x27;de piksel sihirbazı dünyası · 1" width="560"></a>

Type: Demo | Date: 2026-11-19

---

<a id="case-56"></a>
### Case 56: [Kale oluşturma karşılaştırması](https://x.com/nemumusitocha/status/2123287660525719823) (by [@nemumusitocha](https://x.com/nemumusitocha))

**Kaleyi tek bir yaratıcının görsel referans noktası olarak değerlendirin ve hesaba özel kota bağlamını koruyun.**

İçerik oluşturucu, kale karşılaştırması için Neon'u kullandı ve video ve fotoğraflar yayınladı.

Yaratıcı, planındaki haftalık kotanın yaklaşık %4'ünü kullandığını bildirdi. Gönderi, bu kullanımın diğer hesaplara genellenip genellenmediğini belirlemez.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-56-1-74e98240a81a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-56-1-17acc3f87741.jpg" alt="Kale oluşturma karşılaştırması · 1" width="560"></a>
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-56-2-b4f97941d7b2.jpg" alt="Kale oluşturma karşılaştırması · 2" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-56-3-05bccf69bb0c.jpg" alt="Kale oluşturma karşılaştırması · 3" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-56-4-a8081504106d.jpg" alt="Kale oluşturma karşılaştırması · 4" width="560">

Type: Evaluation | Date: 2026-11-19

---

<a id="case-57"></a>
### Case 57: [Alan Turing’in 1936’daki çalışma odasını yeniden oluşturun](https://x.com/GoogleAI/status/2123168242797809944) (by [@GoogleAI](https://x.com/GoogleAI))

**Yeniden yapılandırmanın ayrı parçaları olarak arşiv doğruluğunu ve etkileşimli işlevselliği kontrol edin.**

Google, arşiv fotoğraflarından etkileşimli bir yeniden yapılandırma oluşturmak için Neon'u Antigravity Swarm ile birlikte kullandı.

Sahnede Kral Şapeli, Turing'in çalışma odası ve masanın üzerindeki evrensel bir Turing makinesinin çalışan simülasyonu yer alıyor.

[Ek kaynak](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

[Ek kaynak](https://www.youtube.com/watch?v=KgLLa4WhMSo)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-57-1-22665c6264ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-57-1-b7fab25c354f.jpg" alt="Alan Turing’in 1936’daki çalışma odasını yeniden oluşturun · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-96"></a>
### Case 96: [Three.js ile çöp adam dövüşünü canlandırmak](https://x.com/chetaslua/status/2123720700670398680) (by [@chetaslua](https://x.com/chetaslua))

**Kamera hareket ederken ve sahne değişirken kodla oluşturulan dövüşün takip edilebilirliğini kontrol edin.**

Yapımcı bu Three.js animasyonu için Antigravity ortamında Swarm ile birlikte Neon kullandı.

Çöp adamlar farklı sahnelerde dövüşüyor. Yapımcı tüm iş akışını aktarıyor ancak Swarm’ın katkısını ayrı ayrı göstermiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/videos/case-96-1-fa6b22c69e07.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/posters/case-96-1-32e162b0152f.jpg" alt="Three.js ile çöp adam dövüşünü canlandırmak · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-97"></a>
### Case 97: [Üç modelin yelkenli sahnelerini karşılaştırmak](https://x.com/Da7_Tech/status/2123712489443713478) (by [@Da7_Tech](https://x.com/Da7_Tech))

**Etiketlenmiş üç çıktıda gemileri, dalgaları ve ışığı karşılaştırın.**

Yapımcı Claude Fable 5.2, GPT-6.2 Astra ve Gemini 4 Neon çıktılarını aynı videoda üst üste yerleştirdi.

Görüntüler gün batımındaki bir yelkenlinin üç farklı yorumunu gösteriyor. Gönderide istemler, ayarlar veya puanlama ölçütleri açıklanmıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/videos/case-97-1-ab9ad6fc022d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/posters/case-97-1-f7556a59ef3e.jpg" alt="Üç modelin yelkenli sahnelerini karşılaştırmak · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-20

---

<a id="case-98"></a>
### Case 98: [Avatarları hareketli koleksiyon kartlarına dönüştürmek](https://x.com/aiiii498/status/2123657122575450535) (by [@aiiii498](https://x.com/aiiii498))

**Çerçeve, kaplama ve nadirlik etiketi değiştiğinde avatarın hâlâ tanınabilir olup olmadığını kontrol edin.**

Yapımcı Gemini 4 Neon web arayüzünden aldığı kodu kullandı ve sonuçları hareketli GIF biçimine çevirdi.

Dört döngü örnek avatar kartları gösteriyor. Nadirlik etiketleri ve dolar tutarları kurgusal tasarım öğeleri.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/images/case-98-1-185f6b4b974f.gif" alt="Avatarları hareketli koleksiyon kartlarına dönüştürmek · 1" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/images/case-98-2-880ecaab9212.gif" alt="Avatarları hareketli koleksiyon kartlarına dönüştürmek · 2" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/images/case-98-3-4476e0e8019e.gif" alt="Avatarları hareketli koleksiyon kartlarına dönüştürmek · 3" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/images/case-98-4-ca5307d9f6fd.gif" alt="Avatarları hareketli koleksiyon kartlarına dönüştürmek · 4" width="560">

Type: Demo | Date: 2026-11-20

---

<a id="case-99"></a>
### Case 99: [Soyut mürekkep çizimini canlandırmak](https://x.com/thtbee_/status/2123636478932881627) (by [@thtbee_](https://x.com/thtbee_))

**Tek tek kareleri ve motifler arasındaki geçişleri görmek için videonun farklı noktalarına gidin.**

Yapımcı, soyut çizim animasyonunu Gemini 4 Neon ile yaptığını belirtiyor.

Video mürekkeple çizilen bir gözden çiçeklere, kelebeklere ve başka motiflere geçiyor. Yapımcı 0:14 ve 0:42 anlarını öne çıkarıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/videos/case-99-1-a1a192bbdb28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/posters/case-99-1-f4a4516de977.jpg" alt="Soyut mürekkep çizimini canlandırmak · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-100"></a>
### Case 100: [Three.js ile yapılan Kyoto yürüyüşlerini karşılaştırmak](https://x.com/teddyaisi/status/2123627618146959641) (by [@teddyaisi](https://x.com/teddyaisi))

**Kodla oluşturulan yürüyüşlerde kamera hareketi ve sahne sürekliliğini, üretim süresi ve maliyetle birlikte karşılaştırın.**

Üstte GPT-6.2 Astra, altta Gemini 4 Neon yer alıyor. 20 saniyelik Three.js yürüyüşü Kyoto’da şafak vakti torii kapılarından ve bambu korusundan geçiyor.

Yapımcıya göre Astra 41 dk 9 sn sürdü ve 6,67 USD tuttu. Neon 1 sa 8 dk 19 sn sürdü ve 9,14 USD tuttu.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/videos/case-100-1-0c11ca888805.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/posters/case-100-1-201a20be9461.jpg" alt="Three.js ile yapılan Kyoto yürüyüşlerini karşılaştırmak · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-20

---

<a id="case-101"></a>
### Case 101: [Enstrümantal bir düzenlemeyi göstermek](https://x.com/aisearchio/status/2123621132024848408) (by [@aisearchio](https://x.com/aisearchio))

**Müziği dinlerken ekrandaki kanalları takip edip bölümlerin nasıl üst üste geldiğini ve tekrarlandığını inceleyin.**

Yapımcı enstrümantal parçayı Gemini 4 Neon’a atfediyor.

Klipte sesle birlikte çeşitli kanallar ve nota düzenleme ekranı görünüyor. Neon’un üretimin hangi aşamalarını üstlendiği açıklanmıyor.

[Ek kaynak](https://youtu.be/3FE-hBh1rsY)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/videos/case-101-1-5c63abb4a8a3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/posters/case-101-1-6683cee3534d.jpg" alt="Enstrümantal bir düzenlemeyi göstermek · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-102"></a>
### Case 102: [İki Shibuya gece sahnesini karşılaştırmak](https://x.com/petergyang/status/2123620968568676457) (by [@petergyang](https://x.com/petergyang))

**Aynı anda ilerleyen görüntülerle tabelaları, kalabalığı ve aydınlatmayı karşılaştırın.**

Video Opus 5.5 ve Gemini 4 Neon’un Shibuya Kavşağı gece sahnelerini model adlarıyla gösteriyor.

Etiketlerden hangi çıktının hangi modele ait olduğu anlaşılabiliyor. Yapımcı izleyicilerin tercihini soruyor ve sayısal bir puan vermiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/videos/case-102-1-fd1902096bb4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/posters/case-102-1-50188e47a613.jpg" alt="İki Shibuya gece sahnesini karşılaştırmak · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-20

---

<a id="case-103"></a>
### Case 103: [Bir robotun montajını ve kalkışını canlandırmak](https://x.com/alohaproxy/status/2123619339995668726) (by [@alohaproxy](https://x.com/alohaproxy))

**Uzun bir Three.js sekansını değerlendirirken montajı, yakın planları ve kalkışı birlikte inceleyin.**

Yapımcı robot montajı ve kalkışıyla ilgili önceki Three.js görevini yeniden kullandı. Videoda robotun parçaları birleşiyor ve robot havalanıyor.

Yapımcı üretimin 10 dakikadan uzun sürdüğünü, iki çalıştırmada 83.000 token kullanıldığını ve toplam maliyetin 1,20 USD olduğunu bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/videos/case-103-1-2b1ac80156f4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/posters/case-103-1-572151b639e1.jpg" alt="Bir robotun montajını ve kalkışını canlandırmak · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-108"></a>
### Case 108: [Bisikletleri eşzamanlı glissandoyla canlandırma](https://x.com/alexanderchen/status/2123653501616320961) (by [@alexanderchen](https://x.com/alexanderchen))

**Özgün klibi oynatarak ses perdesindeki kaymanın hareketle nasıl örtüştüğünü inceleyin.**

Üretici, bisikletli görsel-işitsel deneyi Neon'a atfediyor ve sesli klibi paylaşıyor.

Özgün klip, bisiklet hareketlerini glissandoyla eşleştiriyor. Üretici, görsel-işitsel deneyin Neon ile yapıldığını belirtiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-108-1-6771e5e897fa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-108-1-09d488ebf67c.jpg" alt="Bisikletleri eşzamanlı glissandoyla canlandırma · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-109"></a>
### Case 109: [Three.js ile prosedürel bir kaiju modelleme](https://x.com/majidmanzarpour/status/2123654802626220217) (by [@majidmanzarpour](https://x.com/majidmanzarpour))

**Kodla görüntülenen biçimi ve görünümü doğrudan paylaşılan sonuç üzerinden inceleyin.**

Üretici, Three.js TSL ile oluşturulan prosedürel yaratığı Neon'a atfediyor ve görünümünü videoda gösteriyor.

Üretici Three.js gölgelendirme ortamını belirtiyor ve animasyonu paylaşıyor. Video bitmiş görünümü gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-109-1-6c6d98ed0242.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-109-1-06e38f5f5820.jpg" alt="Three.js ile prosedürel bir kaiju modelleme · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-110"></a>
### Case 110: [Paper ile bir açılış sayfası tasarlama](https://x.com/robinebers/status/2123658087722856773) (by [@robinebers](https://x.com/robinebers))

**Paylaşılan önizlemeden görsel hiyerarşiyi ve grafikleri inceleyin.**

Üretici, açılış sayfası tasarımını Neon ve Paper kullanılan iş akışına atfediyor ve yerleşimin ekran görüntüsünü paylaşıyor.

Ekran görüntüsü sayfanın kompozisyonunu gösteriyor. Üretici tasarımın Paper ile Neon kullanılarak yapıldığını belirtiyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-110-1-680ee1274833.jpg" alt="Paper ile bir açılış sayfası tasarlama · 1" width="560">

Type: Demo | Date: 2026-11-20

---

<a id="case-112"></a>
### Case 112: [JavaScript ile halka arzı anlatan animasyon yapma](https://x.com/ann_nnng/status/2123690116296372624) (by [@ann_nnng](https://x.com/ann_nnng))

**Tipografinin ve sahne geçişlerinin kodla nasıl oluşturulduğunu örnek üzerinden inceleyin.**

Üretici Neon'dan hareketli bir anlatım istediğini ve sonucun JavaScript ile yazıldığını belirtiyor. Özgün klip animasyonun bir bölümünü gösteriyor.

Klip, üretilen hareketli grafiğin bir kısmını içeriyor. Kaynak görevi ve JavaScript ile gerçekleştirildiğini belirtiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-112-1-248cf18556a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-112-1-d7c6529c4f69.jpg" alt="JavaScript ile halka arzı anlatan animasyon yapma · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-113"></a>
### Case 113: [Neon ajanlarıyla davul animasyonu yapma](https://x.com/RainG999/status/2123702323692380671) (by [@RainG999](https://x.com/RainG999))

**Yakın plandan zamanlamayı ve animasyon ayrıntılarını değerlendirin.**

Üretici, özgün animasyonu birden fazla Neon ajanının çalışmasına atfediyor. Dördüncü saniye civarında davulcunun ayak hareketleri yakından görülüyor.

Klibin başlarında davulcunun ayakları yakın planda. Yazar, çalışmayı bir Neon ajan grubuna atfediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-113-1-5355fdb1bce1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-113-1-68e65a603aee.jpg" alt="Neon ajanlarıyla davul animasyonu yapma · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-114"></a>
### Case 114: [Blender'da fantastik bir şehir ve ejderha görüntüleme](https://x.com/mspd4100/status/2123720793888829509) (by [@mspd4100](https://x.com/mspd4100))

**Bildirilen kurulumu ve süreyi ilgili sahneyle birlikte değerlendirin.**

Üretici, Antigravity'de Neon kullanarak Blender sahnesini kodla kurduğunu ve görüntülediğini bildiriyor. Şehri ve ejderhayı tanımlıyor, çalışmanın 11 saat sürdüğünü belirtiyor.

Kaynak, şehir ve ejderha içeren Blender sahnesinin sonucunu gösteriyor. Uzun süre, üreticinin kendi kurulumuna ait.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-114-1-c8affe5eeb9d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-114-1-13091fab9c1f.jpg" alt="Blender&#x27;da fantastik bir şehir ve ejderha görüntüleme · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-115"></a>
### Case 115: [Sundar Pichai'nin SVG portresini çizme](https://x.com/Haleeeemahh/status/2123722575884763480) (by [@Haleeeemahh](https://x.com/Haleeeemahh))

**Vektör portreyi kaynak görsel üzerinden değerlendirin.**

Üretici, paylaşılan portrenin Neon ile üretilmiş bir SVG olduğunu belirtiyor. Özgün görsel sonucu gösteriyor.

Özgün görsel, tek bir model görevinden çıkan SVG portresini sunuyor. Yazar konuyu ve modeli belirtiyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-115-1-6b9d34896640.png" alt="Sundar Pichai&#x27;nin SVG portresini çizme · 1" width="560">

Type: Demo | Date: 2026-11-20

---

<a id="case-116"></a>
### Case 116: [Kırmızı akçaağaç bonsaisini canlandırmak](https://x.com/anxuanng/status/2123725543421935630) (by [@anxuanng](https://x.com/anxuanng))

**Yaprakların ve dalların nasıl temsil edildiğini özgün sonuçtan inceleyin.**

Üretici, bonsai görselleştirmesini Neon'a atfediyor ve ortaya çıkan animasyonu yayımlıyor.

Klip, bonsainin tamamlanmış animasyonunu gösteriyor. Yapımcı sahneyi Neon ile hazırladığını belirtiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-116-1-68111ee5c6ce.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-116-1-bb4fc08e7454.jpg" alt="Kırmızı akçaağaç bonsaisini canlandırmak · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-117"></a>
### Case 117: [Bir istemden kişisel animasyon klibi yapma](https://x.com/wenwen11703261/status/2123726068712706176) (by [@wenwen11703261](https://x.com/wenwen11703261))

**İstemi kimin hazırladığını ve yeni sonucu kimin ürettiğini ayrı ayrı belirtin.**

Üretici, kişisel videoyu Neon'a atfediyor ve başka bir üreticinin istemini uyarladığını söylüyor. Paylaşımda sonuç klibi bulunuyor.

Üretici, özgün istemi uyarladığını bildiriyor ve ekli klibi Neon'a atfediyor. Klip uyarlamanın sonucunu gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-117-1-d0d7f68574da.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-117-1-e18f2f687dc7.jpg" alt="Bir istemden kişisel animasyon klibi yapma · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-118"></a>
### Case 118: [Blender'da yağmurlu bir baraj sahnesini canlandırma](https://x.com/lucian__03/status/2123732898230755591) (by [@lucian__03](https://x.com/lucian__03))

**Işık ve su etkilerini bir görsel simülasyon olarak değerlendirin.**

Üretici, baraj kapağı açıldığında suyun aktığı gece sahnesini Neon xhigh ve Blender ile görüntülediğini bildiriyor.

Kaynak klip, yağmur altındaki su akışını gösteriyor. Yazar Neon xhigh ve Blender görüntülemesini belirtiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-118-1-e949de8cc6d1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-118-1-faeed3c97e90.jpg" alt="Blender&#x27;da yağmurlu bir baraj sahnesini canlandırma · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-119"></a>
### Case 119: [Fuji Dağı manzarası çizmek](https://x.com/thegenioo/status/2123733388461006999) (by [@thegenioo](https://x.com/thegenioo))

**Yansıyan silueti ve bitki katmanlarını kullanarak manzarayı inceleyin.**

Üretici, Fuji Dağı çizim dizisinde bu çalışmayı Neon sürümü olarak tanımlıyor.

Özgün sahnede dağlar, bitki örtüsü ve göl yansıması görülüyor. Bu örnek Neon çıktısını belgeliyor.

[Ek kaynak](https://x.com/thegenioo/status/2123733377626829049)

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-119-1-3f6cf888062a.jpg" alt="Fuji Dağı manzarası çizmek · 1" width="560">

Type: Demo | Date: 2026-11-20

---

<a id="case-120"></a>
### Case 120: [Yalnızca kodla üç farklı görsel üretme](https://x.com/BubbleBrain/status/2123740760306827297) (by [@BubbleBrain](https://x.com/BubbleBrain))

**Kodla üretilen sahnelerin renk, geometri ve kompozisyonunu karşılaştırın.**

Üretici üç çıktıyı Neon'a atfediyor ve kodla üretildiklerini belirtiyor. Özgün eklerde sonuç görselleri var.

Üç özgün görsel, üreticinin yalnızca kodla çizim yaptığı deneyin sonuçları. Kaynak, görüntülemeyi Neon'a atfediyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-120-1-0af17d5fdeb2.jpg" alt="Yalnızca kodla üç farklı görsel üretme · 1" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-120-2-e50d5b747b95.jpg" alt="Yalnızca kodla üç farklı görsel üretme · 2" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-120-3-e86f71feffdf.jpg" alt="Yalnızca kodla üç farklı görsel üretme · 3" width="560">

Type: Demo | Date: 2026-11-20

---

<a id="case-122"></a>
### Case 122: [Bir projeyi anlatan kısa hareketli grafik hazırlama](https://x.com/hqmank/status/2123745410405831123) (by [@hqmank](https://x.com/hqmank))

**Son klibin temposunu ve geçişlerini üreticinin belirttiği görevle karşılaştırın.**

Üretici Neon'dan bir açık kaynak projesi hakkında 20 saniyelik hareketli grafik istediğini ve ilk sonucu kullandığını söylüyor. Paylaşımda istek ve video var.

Özgün paylaşım görevi açıklıyor ve ilk sonucu gösteriyor. Seçilen süre, anlatılan açık kaynak projesine ait.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-122-1-7cf664de112d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-122-1-7587fa343b00.jpg" alt="Bir projeyi anlatan kısa hareketli grafik hazırlama · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-123"></a>
### Case 123: [Blender MCP üzerinden manga arka planları modelleme](https://x.com/rootport/status/2123749016928460873) (by [@rootport](https://x.com/rootport))

**Üreticinin anlattığı iş akışını ara geometri üzerinden inceleyin.**

Üretici, manga arka planları için Neon'u Antigravity ve Blender MCP üzerinden kullandığını bildiriyor. Ek, Blender çalışma alanını ve bir modeli gösteriyor.

Üretici manga arka planını Antigravity ile Blender MCP kullanılan iş akışına atfediyor. Özgün görselde Blender geometrisi görülüyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-123-1-69fb56b09f2d.jpg" alt="Blender MCP üzerinden manga arka planları modelleme · 1" width="560">

Type: Demo | Date: 2026-11-20

---

<a id="case-124"></a>
### Case 124: [Animasyonlu bir sitenin tüm yapım sürecini kaydetme](https://x.com/viktoroddy/status/2123749364963426674) (by [@viktoroddy](https://x.com/viktoroddy))

**Görsel sonuca hangi adımların ulaştırdığını kayıttan takip edin.**

Üretici, animasyonlu siteyi Neon'a atfediyor ve 12 dakikalık süreç kaydını paylaşıyor.

12 dakikalık kayıt sitenin yapımını gösteriyor. Üretici Neon'u kullandığını belirtiyor ve sonucu iş akışına örnek olarak sunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-124-1-fbaac8aa35d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-124-1-31224659e289.jpg" alt="Animasyonlu bir sitenin tüm yapım sürecini kaydetme · 1" width="560"></a>

Type: Tutorial | Date: 2026-11-20

---

<a id="case-127"></a>
### Case 127: [Blender'da yağmurlu Kyoto sokaklarını karşılaştırma](https://x.com/mizugame_22/status/2123756243827486822) (by [@mizugame_22](https://x.com/mizugame_22))

**Sahneleri karşılaştırırken kaynaktaki sıralamayı ve düzeltme sayılarını dikkate alın.**

Yazar üç modele aynı istemi verdi ve sonuçları yukarıdan aşağıya tanımlıyor. Blender'da sırasıyla 37, 29 ve 25 düzeltme turu bildiriyor, Neon en altta yer alıyor.

Klip üç sonucu dikey sırayla etiketliyor. Yazarın bildirdiği yineleme sayıları bu Blender karşılaştırmasına ait.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-127-1-297dd4a15d79.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-127-1-8d5572ca8197.jpg" alt="Blender&#x27;da yağmurlu Kyoto sokaklarını karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-20

---

<a id="case-128"></a>
### Case 128: [Dört seramik fırınlama animasyonunu karşılaştırma](https://x.com/lemomo_ai/status/2123756402879631565) (by [@lemomo_ai](https://x.com/lemomo_ai))

**Her klibin aynı malzeme sürecini nasıl görselleştirdiğini karşılaştırın.**

Üretici, fırınlama etkileri hakkında aynı istemi kullandı ve dört farklı animasyon yayımladı.

Üretici aynı fırınlama etkilerinin dört animasyonunu sunuyor. Görsel farkları model çıktılarıyla eşleştirmek için etiketleri kullanın.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-128-1-3bf6f9cb050f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-128-1-4ce0c0ac5a03.jpg" alt="Dört seramik fırınlama animasyonunu karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-20

---

<a id="case-131"></a>
### Case 131: [İki etkileşimli saat yapılandırıcısını karşılaştırma](https://x.com/karanC_12/status/2123765421388234855) (by [@karanC_12](https://x.com/karanC_12))

**Görünüm ve parça ayrıntılarının yanı sıra yapılandırıcının etkileşimlerini test edin.**

Üretici, Neon ve Opus 5.5'e aynı saat yapılandırıcısı görevini verdi.

Klip iki sonucu etiketliyor. Üretici, Neon çıktısında eksik veya bozuk etkileşimler bildiriyor. Parça sayıları ve maliyetler bu denemeye ait.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-131-1-c9df0cda7792.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-131-1-690e6caf50aa.jpg" alt="İki etkileşimli saat yapılandırıcısını karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-20

---

<a id="case-132"></a>
### Case 132: [Etkileşimli voksel ejderha dioramalarını karşılaştırmak](https://x.com/marcthecreatorr/status/2123772997328576587) (by [@marcthecreatorr](https://x.com/marcthecreatorr))

**Sahne kompozisyonunu ve ışığı, yazarın denemeye ilişkin gözlemleriyle birlikte karşılaştırın.**

Yazar, Neon ve Opus'a hazır varlık kullanmadan ejderha ve pagoda yapma görevi verdi. İki sonucun farklı bölümlerini tercih etti.

Aynı ejderha ve pagoda görevi, hazır varlık kullanılmadan her iki modele de verildi. Paylaşım iki sahnenin farklı güçlü yanlarını bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-132-1-1cb05044d9d9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-132-1-22f253d0078d.jpg" alt="Etkileşimli voksel ejderha dioramalarını karşılaştırmak · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-20

---

<a id="case-133"></a>
### Case 133: [Düz bir tabloyu etkileşimli olarak yeniden aydınlatma](https://x.com/ai_for_success/status/2123780898562986388) (by [@ai_for_success](https://x.com/ai_for_success))

**Işık kaynağının hareketiyle parlak bölgelerin ve gölgelerin nasıl değiştiğini inceleyin.**

Üretici, hareketli ışığın düz bir görüntüde yönlü gölgeler oluşturup oluşturamayacağını bir Vermeer tablosuyla denedi. Özgün video sonucu gösteriyor.

Videoda ışığın tablo üzerinde hareketi görülüyor. Işık yönünün değişmesi görüntülenen gölgeleri etkiliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-133-1-53f1359312b0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-133-1-ccffe7cefd7d.jpg" alt="Düz bir tabloyu etkileşimli olarak yeniden aydınlatma · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-135"></a>
### Case 135: [Kodla oluşturulan üç araç sahnesini karşılaştırma](https://x.com/ivanainai/status/2123787634787098976) (by [@ivanainai](https://x.com/ivanainai))

**Yazarın maliyet tahminlerini planlamada kullanmadan önce görsel sonuçları karşılaştırın.**

Yazar hazır 3B varlık kullanmadan üretilen üç etiketli araç sahnesi sunuyor ve tahmini oluşturma maliyetlerini veriyor.

Özgün görsel üç çıktıyı etiketliyor ve hazır varlık kullanılmadığını belirtiyor. Maliyetler üreticinin tahminlerine dayanıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-135-1-520573442b93.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-135-1-e1c037befdfe.jpg" alt="Kodla oluşturulan üç araç sahnesini karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-20

---

<a id="case-137"></a>
### Case 137: [Tablo görünümündeki iki 3B dünyayı karşılaştırma](https://x.com/FiniYang/status/2123807667026264561) (by [@FiniYang](https://x.com/FiniYang))

**Işıklandırmayı ve sahnenin okunabilirliğini, bildirilen ölçümlerle birlikte karşılaştırın.**

Üretici, üstte Astra ve altta Neon olarak etiketlenen yağlı boya tarzında iki dünyayı karşılaştırıyor. Tamamlanma sürelerinin ve fırça darbesi sayılarının farklı olduğunu bildiriyor.

Kaynak üstte Astra'yı, altta Neon'u gösteriyor. Süreler ve fırça darbesi sayıları üreticinin karşılaştırmasına ait.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-137-1-bb92b945afc9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-137-1-2b1ca2f87b39.jpg" alt="Tablo görünümündeki iki 3B dünyayı karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-20

---

<a id="case-138"></a>
### Case 138: [Three.js neon sahnesine bir araba eklemek](https://x.com/HarshithLucky3/status/2123809735401202001) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Eklenen nesnenin özgün sahneye nasıl uyduğunu inceleyin.**

Üretici, Three.js ile oluşturulan neon ışıklı sahneyi Neon'a atfediyor ve sonunda bir BMW M4 CS eklemesini istediğini belirtiyor.

Klip güncellenen sahneyi ve içine yerleştirilen BMW'yi gösteriyor. Otomobil daha sonra verilen bir talimatla eklendi.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-138-1-dd60068cfc4f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-138-1-47630aa4d643.jpg" alt="Three.js neon sahnesine bir araba eklemek · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-139"></a>
### Case 139: [Blender'da bir karakter referansı oluşturma](https://x.com/HarshithLucky3/status/2123813583054414160) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Karakter siluetini ve görünüm tutarlılığını farklı açılardan karşılaştırın.**

Üretici, Blender'da gösterilen karakterin yapımını Neon'a atfediyor. Özgün görsel, modeli farklı açılardan gösteriyor.

Ekte Blender karakterinin birden çok görünümü var. Üretici modeli Neon'a atfediyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-139-1-e3a8eb0d8ebc.jpg" alt="Blender&#x27;da bir karakter referansı oluşturma · 1" width="560">

Type: Demo | Date: 2026-11-20

---

<a id="case-140"></a>
### Case 140: [Dört çilek animasyonu çıktısını karşılaştırma](https://x.com/AIMind_Ai/status/2123816445180088544) (by [@AIMind_Ai](https://x.com/AIMind_Ai))

**Görünen sekans boyunca her çıktının istenen meyveyi koruyup korumadığını kontrol edin.**

Yazar Neon, Carbon, Fable 5.2 ve Opus 5.5'e aynı animasyonlu çilek görevini verdi.

Dört etiketli çıktı meyve ve çevre açısından gözle görülür biçimde farklı. Yazar denemelerdeki düşünme düzeylerini ve tahmini maliyetleri bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-140-1-b4c69ccb7471.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-140-1-c560c3d3f255.jpg" alt="Dört çilek animasyonu çıktısını karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-20

---

<a id="case-143"></a>
### Case 143: [Alp manzarasını yalnızca kodla görüntüleme](https://x.com/Mr_Salio/status/2123828049598611929) (by [@Mr_Salio](https://x.com/Mr_Salio))

**Prosedürel sahnenin derinlik ve ölçek hissini nasıl verdiğini klipten inceleyin.**

Üretici, sahnenin kodla çizilmesini ve canlandırılmasını Neon'a atfediyor. Kaynak videoda Alp manzarası ve bir viyadük görünüyor.

Görüntülenen sahne Alp manzarasını ve viyadüğü içeriyor. Yazar hem çizim hem animasyon kodunu Neon'a atfediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-143-1-01247a901cf2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-143-1-4ca5b794ae1d.jpg" alt="Alp manzarasını yalnızca kodla görüntüleme · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-144"></a>
### Case 144: [Ajan geri bildirimiyle ASCII bisikletçi canlandırma](https://x.com/chetaslua/status/2123831991061840145) (by [@chetaslua](https://x.com/chetaslua))

**Hareketi, üreticinin geri bildirim döngüsüyle birlikte değerlendirin.**

Üretici, ASCII ile canlandırılan bisikletli pelikanı Neon'a atfediyor ve görselleri değerlendirmek için ayrı bir eleştirmen kullandığını anlatıyor.

Üretici Neon'un yanında bir eleştirmen kullandı. Özgün klip metin karakterleriyle canlandırılan bisikletçiyi gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-144-1-8315e85c1e75.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-144-1-5cd6f4e87199.jpg" alt="Ajan geri bildirimiyle ASCII bisikletçi canlandırma · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-145"></a>
### Case 145: [Neon ajan grubunu tek ajanla karşılaştırma](https://x.com/DanielZambrini/status/2123832990598045903) (by [@DanielZambrini](https://x.com/DanielZambrini))

**Aynı görevden yararlanarak koordinasyon yükünü ve gözlenen çıktı kalitesini karşılaştırın.**

Yazar, aynı sincap bakış açılı animasyonda grup ve tek ajan yaklaşımlarını karşılaştırıyor ve bu testte tek ajanı tercih ettiğini belirtiyor.

Yazar iki ajan düzenini aynı animasyon göreviyle değerlendiriyor. Tercihi gösterilen çıktılar ve bu testin koşullarıyla sınırlı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-145-1-b4b90886d367.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-145-1-2f1bbc10a111.jpg" alt="Neon ajan grubunu tek ajanla karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-20

---

<a id="case-147"></a>
### Case 147: [Three.js ile prosedürel bir sinematik sahne oluşturma](https://x.com/filicroval/status/2123842978925977909) (by [@filicroval](https://x.com/filicroval))

**Yalnızca kodla yapılan sahnede geometri, ışık ve hareketin kullanımını inceleyin.**

Üretici, Neon ile dış varlık kullanmadan yapılan bir WebGL sinematik sahne anlatıyor ve klibi paylaşıyor.

Yazar sahneyi dış varlıksız, prosedürel bir WebGL çalışması olarak tanımlıyor. Medya sinematik sonucu gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-147-1-619523d42513.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-147-1-130e24ca2112.jpg" alt="Three.js ile prosedürel bir sinematik sahne oluşturma · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-150"></a>
### Case 150: [Blender'da on iki karakter animasyonu üretme](https://x.com/HarshithLucky3/status/2123862930152460362) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Tek iş akışında oluşturulan pozları ve hareket çeşitliliğini karşılaştırın.**

Üretici on iki Blender animasyonunu Neon'a atfediyor ve hareketleri bir ızgarada paylaşıyor.

Video, üretilen karakter hareketlerinin ızgarasını gösteriyor. Yazar Blender'ı ve on iki animasyonluk kapsamı belirtiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-150-1-9b37b516bd99.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-150-1-5bf5f0b4bb8c.jpg" alt="Blender&#x27;da on iki karakter animasyonu üretme · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-152"></a>
### Case 152: [Dört deniz uçağı iniş sahnesini karşılaştırmak](https://x.com/eliadele/status/2123878763624857693) (by [@eliadele](https://x.com/eliadele))

**Aynı sahne için denetimleri, görsel doğruluğu ve bildirilen çalışma sürelerini karşılaştırın.**

Testi yapan kişi, Bora Bora yakınında deniz uçağı inişi hakkında tek cümle kullandı. Yazar, etkileşimli Three.js sahnesini Neon'a atfediyor ve denemeyi OutputBench'te kaydediyor.

Paylaşım, ortak iniş senaryosunu açıklıyor ve test bağlamına bağlantı veriyor. Ekli görüntü ortaya çıkan sahneyi incelemeyi sağlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-152-1-0699c6160306.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-152-1-cecb296db1d9.jpg" alt="Dört deniz uçağı iniş sahnesini karşılaştırmak · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-20

---

<a id="case-154"></a>
### Case 154: [Three.js'de Monako tünel çıkışlarını karşılaştırma](https://x.com/teddyaisi/status/2123884091221348830) (by [@teddyaisi](https://x.com/teddyaisi))

**Aynı görevdeki animasyon ve ışık farklarını kaynaktan inceleyin.**

Yazar iki modele aynı alacakaranlık tünel görevini verdi ve etiketli bir karşılaştırma yayımladı. Neon için 55 dakika 44 saniye bildiriyor.

Üretici iki Three.js geçişini etiketliyor ve ayrı sürelerini veriyor. Ortak görev mekânı ve alacakaranlık ışığını belirliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-154-1-9160086c7475.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-154-1-8c08634c295f.jpg" alt="Three.js&#x27;de Monako tünel çıkışlarını karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-20

---

<a id="case-155"></a>
### Case 155: [Gün batımında dört bisiklet animasyonunu karşılaştırma](https://x.com/jony_palino/status/2123889278501495127) (by [@jony_palino](https://x.com/jony_palino))

**Her etiketli sahnede pedal hareketini ve vücut duruşunu inceleyin.**

Üretici Neon, Fable 5.2, Sol ve DeepSeek V4.1 Flash'a atfedilen bisiklet sahnelerini gösteriyor.

Özgün klip dört animasyonu etiketliyor. Paylaşım bu karşılaştırmayı belgeliyor ancak aynı çalışma ayarlarının kullanıldığını belirtmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-155-1-3d8d70616e52.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-155-1-c43c4d2e3c43.jpg" alt="Gün batımında dört bisiklet animasyonunu karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-20

---

<a id="case-156"></a>
### Case 156: [Sincap bakış açısından üç prosedürel filmi karşılaştırma](https://x.com/DanielZambrini/status/2123891957529510012) (by [@DanielZambrini](https://x.com/DanielZambrini))

**Aynı üretim kısıtları altında her çıktının bakış açısını nasıl yorumladığını karşılaştırın.**

Üretici 30 saniyelik ortak bir görev verdi ve çıktının yalnızca kodla yapılmasını istedi. Video Neon, Astra ve Fable'a atfedilen sonuçları gösteriyor.

Paylaşım, üç model için aynı kodla üretim görevini belirtiyor. Etiketli video çıktılarında hareket ve kadraj düzeni karşılaştırılabiliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-156-1-fae523eef096.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-156-1-5f3aca1ce926.jpg" alt="Sincap bakış açısından üç prosedürel filmi karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-20

---

<a id="case-158"></a>
### Case 158: [Kodla çizilen resmi hızlandırılmış kayıtta gösterme](https://x.com/chetaslua/status/2123895603973537832) (by [@chetaslua](https://x.com/chetaslua))

**İşaretler eklendikçe son kompozisyonun nasıl oluştuğunu inceleyin.**

Üretici, kodla oluşturulan hızlandırılmış çizim kaydını Neon'a atfediyor. Özgün medya çizimin ilerleyişini gösteriyor.

Klip, çizimin zaman içinde oluşmasını gösteriyor. Yazar görsel programı Neon'a atfediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-158-1-32e734b1fd02.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-158-1-3d83cb3153ed.jpg" alt="Kodla çizilen resmi hızlandırılmış kayıtta gösterme · 1" width="560"></a>
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-158-2-cf80c3fa2e6b.jpg" alt="Kodla çizilen resmi hızlandırılmış kayıtta gösterme · 2" width="560">

Type: Demo | Date: 2026-11-20

---

<a id="case-159"></a>
### Case 159: [Üç gece kalkış sahnesinin ışığını karşılaştırma](https://x.com/SamgreyAi/status/2123898746329071698) (by [@SamgreyAi](https://x.com/SamgreyAi))

**Sahnelerin atmosferi ve konunun görünürlüğünü nasıl dengelediğini karşılaştırın.**

Üretici aynı gece kalkış görevini kullandı ve Neon sahnesinde uçağın karanlıkta seçilemediğini bildiriyor. Özgün video birden çok etiketli çıktı gösteriyor.

Ek, ışığın her sahnede görünürlüğü nasıl etkilediğini gösteriyor. Yazara göre bu görevde Neon'un uçağını görmek zordu.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-159-1-76cb2adcbe79.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-159-1-bc7acdd749ae.jpg" alt="Üç gece kalkış sahnesinin ışığını karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-20

---

<a id="case-162"></a>
### Case 162: [Referanssız bir görevde Blender MCP çıktılarını karşılaştırma](https://x.com/maxt3chno/status/2123911052832190818) (by [@maxt3chno](https://x.com/maxt3chno))

**Geometri ve malzemeleri ortak göreve göre karşılaştırın.**

Üretici üç modele görsel referans, web araması ve hazır varlık olmadan basit bir çekiç görevi verdi. Neon için 19 dakika bildiriyor ve sonuçları paylaşıyor.

Yazar, aynı referanssız görevde süreyi ve bildirilen kullanımı karşılaştırıyor. Özgün medya ortaya çıkan Blender nesnelerini gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-162-1-7693de561db9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-162-1-22bc25d26fbc.jpg" alt="Referanssız bir görevde Blender MCP çıktılarını karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-20

---

<a id="case-163"></a>
### Case 163: [Blender'da yinelemelerle Lamborghini modelleme](https://x.com/scottstts/status/2123919916244128036) (by [@scottstts](https://x.com/scottstts))

**Ara geometriyi gözden geçirin ve karmaşık bir modelde birden çok düzeltme için süre ayırın.**

Üretici, Blender'daki otomobil modelini Neon'a atfediyor ve birden çok yinelemede yapıldığını belirtiyor.

Özgün içerik modeli Blender içinde gösteriyor. Üretici bu iş akışı için yaklaşık iki saat bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-163-1-7734196d1ca6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-163-1-e6bf72104971.jpg" alt="Blender&#x27;da yinelemelerle Lamborghini modelleme · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-164"></a>
### Case 164: [Ayrıntılı motosiklet görselleştirmelerini karşılaştırma](https://x.com/ZryMiller/status/2123921248191479993) (by [@ZryMiller](https://x.com/ZryMiller))

**Motor ve şasi ayrıntılarını aynı paylaşımda bildirilen maliyet ve süreyle birlikte karşılaştırın.**

Üretici, Neon xhigh ve Fable 5.2 xhigh etiketli motosiklet görsellerini yan yana yayımlıyor.

Üretici gösterilen denemelerin süre ve maliyetlerini ayrı ayrı bildiriyor. Ek, model görselleştirmelerini gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-164-1-8d800cc8674a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-164-1-f4b1a2ced69c.jpg" alt="Ayrıntılı motosiklet görselleştirmelerini karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-20

---

<a id="case-169"></a>
### Case 169: [AI Studio'da model tanıtım klibi oluşturma](https://x.com/liu8in/status/2123948163539329148) (by [@liu8in](https://x.com/liu8in))

**Tek bir denemedeki görsel tercihleri ve zamanlamayı klip üzerinden inceleyin.**

Üretici, AI Studio'da Neon'dan bir tanıtım videosu istediğini bildiriyor ve ilk üretilen sekansı paylaşıyor.

Üretici klibi AI Studio'da verdiği görevin ilk sonucu olarak sunuyor. Örnek, ilk üretilen sekansı belgeliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-169-1-5a7a870bc691.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-169-1-63ff63cc9554.jpg" alt="AI Studio&#x27;da model tanıtım klibi oluşturma · 1" width="560"></a>

Type: Demo | Date: 2026-11-21

---

<a id="case-170"></a>
### Case 170: [Blender sahnesini gece boyunca görüntüleme](https://x.com/KanaWorks_AI/status/2123950255389749729) (by [@KanaWorks_AI](https://x.com/KanaWorks_AI))

**Son ışığı, dokuları ve kompozisyonu iş akışı açıklamasıyla birlikte inceleyin.**

Üretici, Blender 5.3'teki sahneyi Neon'a atfediyor ve görüntülenen sonucu paylaşıyor. İş akışının gece boyunca çalıştığını bildiriyor.

Özgün görüntü Blender sonucunu gösteriyor. Çalışma süresi ve gözetim, üreticinin anlattığı bu projeye ait.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-170-1-99360ff2dd50.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-170-1-f45a02be80a1.jpg" alt="Blender sahnesini gece boyunca görüntüleme · 1" width="560"></a>

Type: Demo | Date: 2026-11-21

---

<a id="case-172"></a>
### Case 172: [Tek istemden çıkan iki sahneyi karşılaştırma](https://x.com/JamesMalsawm/status/2123967133084516858) (by [@JamesMalsawm](https://x.com/JamesMalsawm))

**Tek bir estetik denemeden genelleme yapmadan önce etiketli çıktıları inceleyin.**

Üretici, iki sahnenin aynı istemi farklı renklerle kullandığını söylüyor ve etiketli Neon ve Opus çıktılarını yayımlıyor.

Yazar iki sahne için ortak istem ve farklı renkler kullanıldığını bildiriyor. Model yorumlarının yanında renk farklarını dikkate alın.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-172-1-3fd237b363b0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-172-1-3fd75fdb0851.jpg" alt="Tek istemden çıkan iki sahneyi karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-21

---

<a id="case-173"></a>
### Case 173: [Kodla üretilen bir konsept fragmanı hazırlama](https://x.com/likka_ailive/status/2123978932336881882) (by [@likka_ailive](https://x.com/likka_ailive))

**Kodla görüntülenen sekanslarla kullanılan sesin kaynaklarını ayrı ayrı izleyin.**

Üretici, 60 saniyelik konsept film için Neon, Antigravity ve OpenMotion kullanıyor. Sahnelerin kodla oluşturulduğunu ve açık kaynak müziğin ayrıca miksajlandığını anlatıyor.

Üretici görsel iş akışındaki araçları belirtiyor ve açık kaynak müziği ayrı miksajladığını bildiriyor. Klip bağımsız bir konsept film olarak sunuluyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-173-1-743b25bb0fcd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-173-1-8d3ee500229f.jpg" alt="Kodla üretilen bir konsept fragmanı hazırlama · 1" width="560"></a>

Type: Demo | Date: 2026-11-21

---

<a id="case-174"></a>
### Case 174: [Three.js'de Gotik katedral yürüyüşlerini karşılaştırma](https://x.com/teddyaisi/status/2123993556419264532) (by [@teddyaisi](https://x.com/teddyaisi))

**Işığı ve kamera hareketini, kaynağın zamanlama gözlemleriyle birlikte karşılaştırın.**

Yazar iki modelden de vitray pencereye doğru aynı 20 saniyelik yürüyüşü istedi. Videoda Astra üstte, Neon altta.

Üretici üst ve alt çıktıları etiketliyor. Görev iki yürüyüş için hedefi ve oynatma süresini sabitliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-174-1-556584bdda3f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-174-1-299bed6ec042.jpg" alt="Three.js&#x27;de Gotik katedral yürüyüşlerini karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-21

---

<a id="case-176"></a>
### Case 176: [Etkileşimli bir vitray sahnesi oluşturma](https://x.com/abhinavflac/status/2124001055939891411) (by [@abhinavflac](https://x.com/abhinavflac))

**Işığın ve prosedürel ses ortamının sahneye katkısını inceleyin.**

Üretici tek bir fotoğrafı referans aldığını, web sesini prosedürel ürettiğini ve içe varlık aktarmadan kedi ile vitray sahnesini kodla görüntülediğini bildiriyor.

Üretici fotoğrafı referans olarak gösteriyor ve geometriyle sesi prosedürel oluşturduğunu söylüyor. Özgün klip sonucu gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-176-1-c6d6da01fdde.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-176-1-fac673484965.jpg" alt="Etkileşimli bir vitray sahnesi oluşturma · 1" width="560"></a>

Type: Demo | Date: 2026-11-21

---

<a id="case-177"></a>
### Case 177: [Tek denemelik dört HTML animasyonunu karşılaştırma](https://x.com/bangbuilds/status/2124005847655125400) (by [@bangbuilds](https://x.com/bangbuilds))

**Görsel yorumları tek deneme koşullarını dikkate alarak karşılaştırın.**

Yazar dört modele yağmurlu pencere pervazındaki kedi hakkında aynı istemi verdi. Her model, düzeltme veya ikinci deneme olmadan tek çıktı üretti.

Video, yazarın tek deneme koşuluyla aynı yağmurlu pencere görevine verilen dört yorumu gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-177-1-5a940614e1d4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-177-1-cb04b35cf781.jpg" alt="Tek denemelik dört HTML animasyonunu karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-21

---

<a id="case-180"></a>
### Case 180: [Etkileşimli prosedürel kiraz çiçeği sahnesi oluşturma](https://x.com/thebuggeddev/status/2124033700350525497) (by [@thebuggeddev](https://x.com/thebuggeddev))

**Bir siteye prosedürel ayrıntı eklerken hareketi ve etkileşimi ayrı değerlendirin.**

Üretici, prosedürel dalları ve kopabilen taç yaprakları olan etkileşimli siteyi Neon'a atfediyor.

Özgün klip çiçek geometrisini ve simüle edilen rüzgârı gösteriyor. Ölçümler yayımlanan örneğe ait.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-180-1-34434d7bbd8e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-180-1-24dc153c8f53.jpg" alt="Etkileşimli prosedürel kiraz çiçeği sahnesi oluşturma · 1" width="560"></a>

Type: Demo | Date: 2026-11-21

---

<a id="case-181"></a>
### Case 181: [Dikey bir ürün animasyonu hazırlama](https://x.com/ogabezim/status/2124036193776263671) (by [@ogabezim](https://x.com/ogabezim))

**Hareketi ve metin geçişlerini hedeflenen dikey biçimde önizleyin.**

Üretici ilk hareket tasarımı denemesini Neon'a atfediyor.

Video bir telefon arayüzü maketini, hareketli metni ve yüksek kontrastlı yeşil arka planı birleştiriyor. Üretici test düzenini paylaşımda açıklıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-181-1-0fa3c92f6742.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-181-1-a2ecdbad56b2.jpg" alt="Dikey bir ürün animasyonu hazırlama · 1" width="560"></a>

Type: Demo | Date: 2026-11-21

---

<a id="case-183"></a>
### Case 183: [Derinlik tahminlerinden normal haritaları üretme](https://x.com/WrongNebula/status/2124037902594387991) (by [@WrongNebula](https://x.com/WrongNebula))

**Bağlantıdaki uygulamayı inceleyin, derinlik modelini ve üretilen aracı ayrı ayrı belirtin.**

Üretici, Neon desteğiyle Apple Depth Pro 2 ağırlıklarını değiştirdiğini ve normal haritalarıyla diğer PBR haritaları için prosedürel araç hazırladığını bildiriyor.

İş akışında tahmini derinlik haritası bir ara adım. Üretici malzeme haritalarından bir örnek gösteriyor ve araç üzerindeki çalışmayı Neon'a atfediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-183-1-bc725e19fcf1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-183-1-3cb208dca4ab.jpg" alt="Derinlik tahminlerinden normal haritaları üretme · 1" width="560"></a>

Type: Demo | Date: 2026-11-21

---

<a id="case-184"></a>
### Case 184: [Hareket geçişlerini ve ses tercihlerini karşılaştırma](https://x.com/pankajkumar_dev/status/2124040952658682263) (by [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**Geçişleri, yazarın bildirdiği ses karşılaştırmasından ayrı inceleyin.**

Üretici Neon ile oluşturulan bir hareket tasarımını gösteriyor ve Claude'un ses efektlerini tercih ettiğini belirtiyor. Görsel ve işitsel değerlendirmeler yazara ait.

Yazar, karşılaştırmada geçişleri ses tasarımından ayrı ele alıyor. Özgün medya Neon çıktısını gösteriyor, tercih yazarın değerlendirmesi.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-184-1-92892fee2e04.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-184-1-86891b989575.jpg" alt="Hareket geçişlerini ve ses tercihlerini karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-21

---

<a id="case-186"></a>
### Case 186: [Three.js ile neon ışıklı elektronikçiler bölgesi oluşturma](https://x.com/niramayo2096/status/2124042263512904187) (by [@niramayo2096](https://x.com/niramayo2096))

**Referansı, sahne kodunu ve müziği sağlayan araçları ayrı ayrı kaydedin.**

Üretici Neon'la tek bir görseli, kodla yönetilen kamera içeren kurgusal ve yağmurlu bir elektronikçiler bölgesine dönüştürdü.

Yazar görüntüleme için Three.js, referans görsel için ChatGPT, müzik için Suno kullandığını belirtiyor. Klip, kodla oluşturulan sahneyi gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-186-1-49a8afa32037.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-186-1-ebf8f615af74.jpg" alt="Three.js ile neon ışıklı elektronikçiler bölgesi oluşturma · 1" width="560"></a>

Type: Demo | Date: 2026-11-21

---

<a id="case-187"></a>
### Case 187: [Kurgusal karakter çizim arayüzlerini karşılaştırma](https://x.com/noclipepe/status/2124074648266535253) (by [@noclipepe](https://x.com/noclipepe))

**Arayüzleri aynı kurgusal karakter referansına göre karşılaştırın.**

Üretici Neon ve Fable'dan kurgusal bir oyun karakteri için çizim arayüzü hazırlamalarını istiyor. Kaynak Neon için 21, Fable için 27 dakika bildiriyor.

21 ve 27 dakikalık süreler bu karakter görevine ait. Klip çizim arayüzüne yönelik iki yaklaşımı sunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-187-1-51123c7e0e4d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-187-1-65794f737a1b.jpg" alt="Kurgusal karakter çizim arayüzlerini karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-21

---

<a id="case-188"></a>
### Case 188: [Sayfa bloklarını ve arayüz bileşenlerini yinelemelerle geliştirme](https://x.com/csaba_kissi/status/2124080629642154476) (by [@csaba_kissi](https://x.com/csaba_kissi))

**Yeniden kullanılabilir bileşenleri bir geliştirme dizisi olarak değerlendirin.**

Geliştirici Neon'la üretilen ve farklı bileşenlerin görüldüğü bir blok dizisi yayımlıyor. İlgili klipler aynı çalışmanın sonraki yinelemelerini gösteriyor.

Paylaşım birbirine bağlı blok öğelerini ve etkileşimlerini gösteriyor. Sonraki kliplerde aynı arayüz geliştiriliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-188-1-e34e22429fe4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-188-1-934dceb92441.jpg" alt="Sayfa bloklarını ve arayüz bileşenlerini yinelemelerle geliştirme · 1" width="560"></a>

Type: Demo | Date: 2026-11-21

---

<a id="case-189"></a>
### Case 189: [Film görüntüleme ve tarama emülatörü prototipi geliştirme](https://x.com/WrongNebula/status/2124083607635718386) (by [@WrongNebula](https://x.com/WrongNebula))

**Film efektlerini, üreticinin uygulama için sunduğu kanıtlara dayandırın.**

Üretici fizik temelli film görüntüleme ve tarama projesini Neon'a atfediyor ve önizlemenin yanında bir geliştirme dizisi paylaşıyor. Bağımsız maliyet ölçümü verilmemiş.

Özgün önizleme film görüntüleme tekniğini gösteriyor. Üretici süren geliştirmeye bağlantı veriyor ve örnek o aşamayı yansıtıyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-189-1-1c30899f38b7.jpg" alt="Film görüntüleme ve tarama emülatörü prototipi geliştirme · 1" width="560">

Type: Demo | Date: 2026-11-21

---

<a id="case-192"></a>
### Case 192: [İki etkileşimli okyanus dioramasını karşılaştırma](https://x.com/thebuggeddev/status/2124109788883853698) (by [@thebuggeddev](https://x.com/thebuggeddev))

**Aynı yapım görevini değerlendirirken sahneleri ve etkileşim denetimlerini karşılaştırın.**

Üretici aynı görevi Neon ve Opus 5.5 ile çalıştırdığını bildiriyor.

Klip bir ağaç ve yükseltilmiş yapının bulunduğu okyanus sahnesi de dahil olmak üzere iki dioramayı gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-192-1-f857f4c4c848.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-192-1-72361365787b.jpg" alt="İki etkileşimli okyanus dioramasını karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-21

---

<a id="case-193"></a>
### Case 193: [Altı modelin site tasarımlarını karşılaştırma](https://x.com/guilippert_v4/status/2124110586753482802) (by [@guilippert_v4](https://x.com/guilippert_v4))

**Bildirilen en düşük maliyeti alt sınır olarak alın ve ortaya çıkan tasarım farklarını inceleyin.**

Yazar aynı yeniden tasarım isteğini high düzeyde ve ek beceri olmadan kullandı. Kaynak deneme başına süre ve maliyetleri, Neon için de alt maliyet sınırını bildiriyor.

Bildirilen maliyetler ve süreler altı modelin bu tasarım karşılaştırmasına ait. Grafikte Neon için bir maliyet alt sınırı var.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-193-1-99e1c89f24f0.jpg" alt="Altı modelin site tasarımlarını karşılaştırma · 1" width="560">

Type: Evaluation | Date: 2026-11-21

---

<a id="case-195"></a>
### Case 195: [Ortak bir Three.js isteminden Jeep modellerini karşılaştırma](https://x.com/maxt3chno/status/2124122272440951080) (by [@maxt3chno](https://x.com/maxt3chno))

**Etiketli sahneleri karşılaştırın ve sürelerin bu teste ait olduğunu dikkate alın.**

Üretici daha önceki Jeep istemini yeniden kullandığını bildiriyor ve sonuçları yan yana yayımlıyor. Neon High denemesinde 45 dakika kaydetti.

Karşılaştırma, bitmiş modelleri etiketlerle gösteriyor. Sonucu okurken önceki görevi ve bu denemenin süresini birlikte değerlendirin.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-195-1-d8995fa4ad08.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-195-1-b043ad346c1f.jpg" alt="Ortak bir Three.js isteminden Jeep modellerini karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-21

---

<a id="case-196"></a>
### Case 196: [Üç modelin arayüz yaklaşımlarını karşılaştırma](https://x.com/csaba_kissi/status/2124131369076887639) (by [@csaba_kissi](https://x.com/csaba_kissi))

**Yan yana verilen özgün örneklerde bileşen durumlarını ve yerleşim tercihlerini karşılaştırın.**

Üretici Opus 5.5, Sol ve Gemini 4 Neon ile ilişkilendirilen kullanıcı arayüzü tasarımlarını incelediğini bildiriyor.

Klip, yazarın nitel değerlendirmesine dayanak olan tasarım ayrıntılarını gösteriyor. Paylaşım kontrollü bir üretim yapılandırması belirtmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-196-1-29b7d822288e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-196-1-1b9b7d84fabd.jpg" alt="Üç modelin arayüz yaklaşımlarını karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-21

---

<a id="case-197"></a>
### Case 197: [Prosedürel kodla şarkılı bir sahne oluşturma](https://x.com/chetaslua/status/2124131378770182389) (by [@chetaslua](https://x.com/chetaslua))

**Prosedürel çıktının anlatımını, üretilmiş ses veya video varlıkları kullanan projelerle karşılaştırın.**

Yazar Neon'dan görselleri, müziği ve sesi harici kitaplık, varlık veya metinden sese dönüştürme kullanmadan kodla üretmesini istediğini bildiriyor. Sonucu tek deney olarak sunuyor.

Video üretilen görüntülerle şarkıyı birleştiriyor. Kitaplık ve varlık kısıtlarını üretici belirledi.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-197-1-213fbfb6cae0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-197-1-1888ae3cd2cf.jpg" alt="Prosedürel kodla şarkılı bir sahne oluşturma · 1" width="560"></a>

Type: Demo | Date: 2026-11-21

---

<a id="case-198"></a>
### Case 198: [Üretilen klipleri ilk ve son kareleri düzenleyerek birleştirme](https://x.com/leaf_sanren/status/2124132471046606916) (by [@leaf_sanren](https://x.com/leaf_sanren))

**Video üreten model ile klipleri birleştiren iş akışını ayrı ayrı belirtin.**

Yazar daha uzun bir video iş akışında ilk ve son karelerin yanı sıra kurgu için Neon kullandığını anlatıyor.

Klip Seedance 2.5 Flash ve Omni 1.2 Flash çıktılarını karşılaştırıyor. Üretici, genel süreçteki birleştirme işini Neon'a atfediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-198-1-8f18177543e8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-198-1-3fd9cb6977d0.jpg" alt="Üretilen klipleri ilk ve son kareleri düzenleyerek birleştirme · 1" width="560"></a>

Type: Integration | Date: 2026-11-21

---

<a id="case-200"></a>
### Case 200: [Tarayıcı sahnesinde bir voksel modeli sergileme](https://x.com/DrstaOne/status/2124141602629439754) (by [@DrstaOne](https://x.com/DrstaOne))

**Voksel nesnenin siluetini ve ayrıntılarını döndürülebilen tarayıcı önizlemesinden inceleyin.**

Üretici voksel model demosunu Neon'a atfediyor. Video muz biçimli bir voksel nesnesini ve etkileşimli sunum denetimlerini gösteriyor.

Yazar ortaya çıkan görselleştirmeyi paylaşıyor. Tam istem ve üretim adımları gösterilmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-200-1-8229b8e32f2f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-200-1-f27b8f50fc90.jpg" alt="Tarayıcı sahnesinde bir voksel modeli sergileme · 1" width="560"></a>

Type: Demo | Date: 2026-11-21

---

<a id="case-201"></a>
### Case 201: [Tanıtım görselini neon tabela gibi canlandırma](https://x.com/blueemi99/status/2124142635808084445) (by [@blueemi99](https://x.com/blueemi99))

**Tek bir referans görseli kısa bir açılışla döngüsel bir animasyona dönüştürün.**

Üretici, Neon'dan modelin tanıtım yazısındaki bir görseli canlandırmasını istediğini belirtiyor.

Videoda logo ve yazılar neon tabela gibi yanıyor. Üretici kendi animasyonunu paylaşıyor ve kullanılan girdinin kaynağını belirtiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-201-1-de28701f4a50.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-201-1-8a321a8314f2.jpg" alt="Tanıtım görselini neon tabela gibi canlandırma · 1" width="560"></a>

Type: Demo | Date: 2026-11-21

---

<a id="case-202"></a>
### Case 202: [LilyPond'da üretilen iki mazurkayı karşılaştırma](https://x.com/aug5thmusic/status/2124143855474024663) (by [@aug5thmusic](https://x.com/aug5thmusic))

**İki notayı inceleyin ve modellerin aynı müzik biçimini nasıl yorumladığını dinleyin.**

Üretici, Neon ve Fable 5.2'ye LilyPond'da piyano mazurkası için aynı görevi verdi.

İki özgün ek, ortaya çıkan notaları içeriyor. Talebin tamamı kaynakta yazıyor.

<table>
<tr>
<td><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-202-1-72d2c08479e2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-202-1-e3bd42078e4b.jpg" alt="LilyPond&#x27;da üretilen iki mazurkayı karşılaştırma · 1" width="560"></a></td>
<td><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-202-2-7ef00c8de125.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-202-2-687e3078bdd4.jpg" alt="LilyPond&#x27;da üretilen iki mazurkayı karşılaştırma · 2" width="560"></a></td>
</tr>
</table>

Type: Evaluation | Date: 2026-11-21

---

<a id="case-203"></a>
### Case 203: [Dört holografik paralaks animasyonunu karşılaştırma](https://x.com/DeepBlueX0/status/2124148150525128836) (by [@DeepBlueX0](https://x.com/DeepBlueX0))

**Karşılaştırmada sıra ve model etiketleri görünür kalsın.**

Üretici dört görsel girdiden holografik paralaks animasyonu elde ettiğini anlatıyor ve adları belirtilen dört çıktıyı karşılaştırıyor.

Üretici çıktıları soldan sağa sıralıyor ve özgün görevi bir yanıtta veriyor. Girdiler arasında karakter resmi, derinlik haritası, arka plan ve dekoratif çerçeve bulunuyor.

[Ek kaynak](https://x.com/DeepBlueX0/status/2124148165456896504)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-203-1-81f1ab3f9fc3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-203-1-a11f9dd1c373.jpg" alt="Dört holografik paralaks animasyonunu karşılaştırma · 1" width="560"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-203-2-a2e7f9bd83df.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-203-2-5438f383c859.jpg" alt="Dört holografik paralaks animasyonunu karşılaştırma · 2" width="560"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-203-3-5379a86e8c80.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-203-3-4532a2efa270.jpg" alt="Dört holografik paralaks animasyonunu karşılaştırma · 3" width="560"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-203-4-c7ac0b28dcb2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-203-4-cef9725be0b4.jpg" alt="Dört holografik paralaks animasyonunu karşılaştırma · 4" width="560"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-203-5-16e550968df5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-203-5-d7c9a8051252.jpg" alt="Dört holografik paralaks animasyonunu karşılaştırma · 5" width="560"></a>

Type: Evaluation | Date: 2026-11-21

---

<a id="case-204"></a>
### Case 204: [ASCII figürlerini kodla canlandırma](https://x.com/chetaslua/status/2124157978425294867) (by [@chetaslua](https://x.com/chetaslua))

**Dışarıdan görüntü aktarmak yerine metin karakterlerini kodla canlandırmayı deneyin.**

Üretici, yalnızca kodla yapılan bir ASCII deneyini anlatıyor. Özgün klip metinle çizilen hareketli figürleri gösteriyor.

Özgün klip, figürleri hareketli metin olarak sunuyor. Kaynak hem görüntüyü hem kodu deneye atfediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-204-1-58ddb14c108f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-204-1-ac09984e8d2e.jpg" alt="ASCII figürlerini kodla canlandırma · 1" width="560"></a>

Type: Demo | Date: 2026-11-21

---

<a id="case-206"></a>
### Case 206: [Sahne kurulumu ve animasyonu modellere bölüştürme](https://x.com/nemumusitocha/status/2124160079398314141) (by [@nemumusitocha](https://x.com/nemumusitocha))

**İlk yapı ile hareket ayrıntılarını ayrı aşamalara ayırın.**

Üreticiye göre Neon genel sahne kurulumunu yaptı, Claude Mythos 5.2 ayrıntıları ve hareketi iyileştirdi. Video sonucu gösteriyor.

Üretici görev paylaşımını açıkça belirtiyor. Klip sahne ve animasyonun birleşik sonucunu gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-206-1-c5b50ac39e35.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-206-1-62c30412688a.jpg" alt="Sahne kurulumu ve animasyonu modellere bölüştürme · 1" width="560"></a>

Type: Integration | Date: 2026-11-21

---

<a id="case-211"></a>
### Case 211: [Three.js gondol gezilerini karşılaştırma](https://x.com/teddyaisi/status/2124190810900140286) (by [@teddyaisi](https://x.com/teddyaisi))

**Sahnedeki hareketi karşılaştırmak için kamera rotasını ve klip süresini eşitleyin.**

Üretici Astra ve Neon'dan gün batımında bir Venedik köprüsünün altından geçen aynı yirmi saniyelik gondol gezisini istedi.

Video Büyük Kanal'a çıkan iki rotayı etiketleyip eşzamanlı gösteriyor. Açıklamada her iki çalışmanın oluşturma süresi ve maliyeti var.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-211-1-174a20462ed7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-211-1-422ac975b76b.jpg" alt="Three.js gondol gezilerini karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-21

---

<a id="case-213"></a>
### Case 213: [Dört Three.js Eyfel Kulesi modelini karşılaştırma](https://x.com/Bhavani_00007/status/2124203254011854973) (by [@Bhavani_00007](https://x.com/Bhavani_00007))

**Aynı konunun yapısını ve görsel ayrıntılarını karşılaştırmak için etiketli çıktıları bir araya getirin.**

Üretici Neon, Astra, Sol ve Opus'tan Three.js'de Eyfel Kulesi yapmalarını istedi.

Özgün video sonuçları birlikte gösteriyor. Paylaşım, bu yapım testini anlatıyor ve izleyicileri çıktıları incelemeye çağırıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-213-1-ee11cc01b612.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-213-1-174020bf0c57.jpg" alt="Dört Three.js Eyfel Kulesi modelini karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-21

---

<a id="case-214"></a>
### Case 214: [İki Gemini sürümünün motor animasyonlarını karşılaştırma](https://x.com/HarshithLucky3/status/2124205275272097970) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Geometriyi, animasyonu ve sesi ayrı boyutlar olarak inceleyin.**

Üretici, Antigravity'de Gemini 4 Neon High ve Gemini 3.7 Flash High'ı motor görselleştirmesinde karşılaştırıyor.

Özgün video iki sonucu etiketliyor. Üretici karşılaştırmadaki motor sesini Neon'a atfediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-214-1-ffd6e1923276.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-214-1-2c9a3ecfc799.jpg" alt="İki Gemini sürümünün motor animasyonlarını karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-21

---

<a id="case-215"></a>
### Case 215: [Tarayıcı için sahte 3B voksel sprite'ları oluşturma](https://x.com/studio_yebisu/status/2124212957332799933) (by [@studio_yebisu](https://x.com/studio_yebisu))

**Dönüşü taklit ederken piksel sanatı kenarlarını korumak için katmanlı sprite'lar kullanın.**

Üretici, kamera döndükçe sahnenin hacimli görünmesi için düz sprite katmanlarını birleştirdiğini açıklıyor. Demo yöntemi tarayıcı arayüzünde gösteriyor.

Klipte kamera sprite tabanlı sahnenin çevresinde hareket ediyor. Üretici, hacim yanılsamasını düz öğelerin katmanlarına bağlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-215-1-d0a6a4368033.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-215-1-e6726fb3bbd6.jpg" alt="Tarayıcı için sahte 3B voksel sprite&#x27;ları oluşturma · 1" width="560"></a>

Type: Demo | Date: 2026-11-21

---

<a id="case-216"></a>
### Case 216: [Dört Alpine Gold sahnesini karşılaştırma](https://x.com/EnvolDev/status/2124238419140444661) (by [@EnvolDev](https://x.com/EnvolDev))

**Ortak istemde sahneleri ve üreticinin bildirdiği süre ile maliyetleri karşılaştırın.**

Karşılaştırmada ortak Alpine Gold isteminden çıkan dört çıktı etiketlenmiş. Üretici Neon'un bu testte 1 saat 31 dakika 11 saniye sürdüğünü ve 11,84 ABD doları tuttuğunu bildiriyor.

Klipteki etiketler ve süre bu Alpine Gold karşılaştırmasına ait. Maliyetlerden önce görünen hareketi ve sahne düzenini karşılaştırın.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-216-1-089c1cb26acd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-216-1-b373fcaeaef5.jpg" alt="Dört Alpine Gold sahnesini karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-21

---

<a id="case-217"></a>
### Case 217: [Dört hareketli zebra sahnesini karşılaştırma](https://x.com/jony_palino/status/2124246473667961005) (by [@jony_palino](https://x.com/jony_palino))

**Her etiketli çıktıda silueti, bacak hareketlerini ve arka planı değerlendirin.**

Üretici Neon, Carbon, Fable 5.2 ve DeepSeek V4.1 Flash'tan dört etiketli zebra animasyonu sunuyor.

Klip gönderilen çıktıların görsel karşılaştırmasını sağlar. Üretici aynı istemin veya üretim ayarlarının kullanıldığını belirtmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-217-1-b408ad8ddc0a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-217-1-50fbb1ab984d.jpg" alt="Dört hareketli zebra sahnesini karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-21

---

<a id="case-219"></a>
### Case 219: [İki ekskavatör animasyonunu karşılaştırma](https://x.com/ivanainai/status/2124273127614017837) (by [@ivanainai](https://x.com/ivanainai))

**Her sahnenin araç hareketini ve zemin temasını nasıl gösterdiğini inceleyin.**

Özgün video Neon ve Opus 5.5 ile hazırlanan şantiye sahnelerini etiketliyor.

Modellerin ekskavatörleri ve kamyonları yan yana görülüyor. Paylaşımda ortak ayarlara ilişkin yeterli ayrıntı yok.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-219-1-5dabf3de2232.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-219-1-340c55caaee6.jpg" alt="İki ekskavatör animasyonunu karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-21

---

<a id="case-223"></a>
### Case 223: [Antigravity'de W16 motor canlandırma](https://x.com/HarshithLucky3/status/2124313664790671814) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**Hangi parçaların seçilebildiğini görmek için animasyonlu motor grubunu çeşitli açılardan inceleyin.**

Üretici, Bugatti Chiron W16 görselleştirmesi için Antigravity'de Neon High kullandığını belirtiyor.

Özgün video, neon ışığı altında hareket eden motor grubunu gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-223-1-0f69dc8a5571.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-223-1-7dc0da961dd8.jpg" alt="Antigravity&#x27;de W16 motor canlandırma · 1" width="560"></a>

Type: Demo | Date: 2026-11-22

---

<a id="case-225"></a>
### Case 225: [Neon'un yönettiği müzik videosunu yinelemelerle geliştirme](https://x.com/anabology/status/2124322570652528876) (by [@anabology](https://x.com/anabology))

**İlk çıktıyı gözden geçirin ve birkaç yineleme boyunca ek yönlendirme verin.**

Üretici müzik videosunun yönetimini Neon'a bıraktı ve birkaç gün boyunca çalışmaya geri döndüğünü belirtiyor.

Özgün paylaşım, sonraki düzenlemeyi yinelemelerin sonucu olarak gösteriyor. Görsel ve ses araçlarının tümü ayrı ayrı belirtilmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-225-1-128f7f022ace.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-225-1-7b92100ced8e.jpg" alt="Neon&#x27;un yönettiği müzik videosunu yinelemelerle geliştirme · 1" width="560"></a>

Type: Demo | Date: 2026-11-22

---

<a id="case-228"></a>
### Case 228: [İki Three.js kütüphane gezisini karşılaştırma](https://x.com/teddyaisi/status/2124353151646200097) (by [@teddyaisi](https://x.com/teddyaisi))

**Aynı yirmi saniyelik gezide kamera temposunu ve iç mekân ayrıntılarını karşılaştırın.**

Üretici Astra ve Neon'a büyük bir Barok kütüphanesi için aynı görevi verdi.

Eşzamanlı klipte Astra üstte, Neon altta etiketlenmiş. Zaman ve maliyet rakamları üreticinin denemesinden geliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-228-1-2aa76da8bbd0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-228-1-1f13fcf905f2.jpg" alt="İki Three.js kütüphane gezisini karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-22

---

<a id="case-232"></a>
### Case 232: [Referans klipten fantastik bir geçiş kurgulama](https://x.com/GeekCatX/status/2124365617243595014) (by [@GeekCatX](https://x.com/GeekCatX))

**Birden çok aracın kullanıldığı video iş akışında kurgu ve seslendirme katkılarını ayrı kaydedin.**

Üretici referans klip verdi ve kurguyu Neon'a atfetti. Klonlanmış anlatımı Doubao TTS2 üretti.

Kaynak video kurgulanmış sonucu gösteriyor. Üretici referans klibi ayrı girdi olarak belirtiyor ve seslendirmeyi Doubao TTS2'ye atfediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-232-1-36b1032c3599.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-232-1-6fcad8e8f8d9.jpg" alt="Referans klipten fantastik bir geçiş kurgulama · 1" width="560"></a>

Type: Tutorial | Date: 2026-11-22

---

<a id="case-234"></a>
### Case 234: [Sulu boya gözetleme kulesini WebGPU sahnesine dönüştürme](https://x.com/thebuggeddev/status/2124387668461236268) (by [@thebuggeddev](https://x.com/thebuggeddev))

**Prosedürel sahneleri karşılaştırırken referans görseli ve yineleme sayısını sabit tutun.**

Üretici Neon ve Carbon'a aynı sulu boya görselini ve WebGPU gözetleme kulesi görevini verdi.

Video Neon'u sağda etiketliyor ve iki etkileşimli çalışmayı yan yana gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-234-1-26a170aa0e64.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-234-1-49bef4fc01c7.jpg" alt="Sulu boya gözetleme kulesini WebGPU sahnesine dönüştürme · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-22

---

<a id="case-238"></a>
### Case 238: [Kodla bir şarkı ve ASCII görselleştirmesi yazma](https://x.com/chetaslua/status/2124460788501106722) (by [@chetaslua](https://x.com/chetaslua))

**Uyumlu bir görsel-işitsel sekansı test etmek için kodla üretilen ses ve metin animasyonu kullanın.**

Üretici Neon'dan kendi şarkı sözlerini seçmesini ve düşünme sürecini ASCII animasyonu olarak göstermesini istedi.

Üretici dış varlık, metinden sese dönüştürme veya eklenti olmadan yalnızca kod kullanıldığını belirtiyor. Klip hareketli figürü ve altyazıları içeriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-238-1-ae91d567a285.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-238-1-2ca901896111.jpg" alt="Kodla bir şarkı ve ASCII görselleştirmesi yazma · 1" width="560"></a>

Type: Demo | Date: 2026-11-22

---

<a id="case-240"></a>
### Case 240: [Dört motor kesiti animasyonunu karşılaştırma](https://x.com/kinderlayer/status/2124465319087308918) (by [@kinderlayer](https://x.com/kinderlayer))

**Her çıktının aynı hareketli motor parçalarını anlaşılır biçimde gösterip göstermediğini kontrol edin.**

Üretici dört modele çalışan bir motoru kesit olarak gösteren aynı görevi verdi.

Özgün karşılaştırma dört çıktıyı etiketliyor ve pistonların, dişlilerin ve yakıtın farklı çizimlerini gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-240-1-18c6e9ce30c8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-240-1-ceec44a1212a.jpg" alt="Dört motor kesiti animasyonunu karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-22

---

<a id="case-241"></a>
### Case 241: [Düşük poligonlu bir karakter tabanı oluşturma](https://x.com/fe_yukichi/status/2124470064422527151) (by [@fe_yukichi](https://x.com/fe_yukichi))

**Ön ve yan referanslar sağlayın, karakteri ayrıntılandırmadan önce topolojiyi inceleyin.**

Üretici, tek istemden çıkan karakter ağını Gemini 4 Neon ve Blender'a atfediyor ve yaklaşık 4.800 üçgen bildiriyor.

Özgün paylaşım ön ve yan geometriyle Blender ağını gösteriyor. Üretici Japonca girdinin tamamını bir yanıtta paylaşıyor ve bunu başlangıç noktası olarak tanımlıyor.

[Ek kaynak](https://x.com/fe_yukichi/status/2124470794327843162)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-241-1-1487bbbb7c98.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-241-1-cb267d3ea061.jpg" alt="Düşük poligonlu bir karakter tabanı oluşturma · 1" width="560"></a>
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-241-2-b2df80e6eb9b.png" alt="Düşük poligonlu bir karakter tabanı oluşturma · 2" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-241-3-81209abff7e9.png" alt="Düşük poligonlu bir karakter tabanı oluşturma · 3" width="560">

Type: Tutorial | Date: 2026-11-22

---

<a id="case-242"></a>
### Case 242: [Dört donmuş karpuz animasyonunu karşılaştırma](https://x.com/AIMind_Ai/status/2124474268079567329) (by [@AIMind_Ai](https://x.com/AIMind_Ai))

**Her animasyonun geçişlerde nesnenin tanınabilirliğini koruyup korumadığını ortak olay dizisiyle sınayın.**

Üretici dört modele aynı donma, erime ve patlama görevini verdiğini bildiriyor. Etiketli dört panel çıktıları tek klipte gösteriyor.

Karşılaştırma üreticinin tek testine ait. Gösterilen süreler ve maliyet tahminleri bildirilen kuruluma bağlı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-242-1-51a984366ca1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-242-1-8782fd0ff6d5.jpg" alt="Dört donmuş karpuz animasyonunu karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-22

---

<a id="case-247"></a>
### Case 247: [Referans fotoğraflardan hareketli robotu yeniden oluşturun](https://x.com/majidmanzarpour/status/2124582261374742710) (by [@majidmanzarpour](https://x.com/majidmanzarpour))

**Görsellerden ölçü alın, Blender’da parçaları ayrı modelleyin ve sonucu referansla yan yana inceleyin.**

Video, aşamalı montajı ve modelle referans fotoğrafı karşılaştıran son geçişi gösteriyor.

Yazar, Antigravity’de Neon’un Tesla Optimus Gen 2 fotoğraflarına dayanarak 145 rig’li parça oluşturduğunu ve görselleri denetlediğini söylüyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-23/videos/case-247-1-c0babc1e04a7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-23/posters/case-247-1-aacac143c86e.jpg" alt="Referans fotoğraflardan hareketli robotu yeniden oluşturun · 1" width="560"></a>

Type: Demo | Date: 2026-11-22

---

<a id="case-249"></a>
### Case 249: [Uydu yörüngelerini tarayıcıda canlı izleyin](https://x.com/DynamicWebPaige/status/2124698835801031129) (by [@DynamicWebPaige](https://x.com/DynamicWebPaige))

**CelesTrak’ın açık yörünge verilerini önbelleğe alın ve gezilebilir bir 3B görünüm için konumları tarayıcıda hesaplayın.**

Videoda yazar Dünya çevresindeki bakış açısını oynattıkça uydular ve izleri değişiyor.

Yazar izleyiciyi Neon ile kurdu ve açık verilerle Starlink uyduları, ISS ve GPS uydularının konumlarını nasıl öngördüğünü açıkladı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-23/videos/case-249-1-53d247877385.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-23/posters/case-249-1-8e3a28ab80f1.jpg" alt="Uydu yörüngelerini tarayıcıda canlı izleyin · 1" width="560"></a>

Type: Demo | Date: 2026-11-23

---

<a id="case-251"></a>
### Case 251: [Antigravity’de video maskeleme prototipi oluşturun](https://x.com/ai_for_success/status/2124760076825301195) (by [@ai_for_success](https://x.com/ai_for_success))

**Neon ile segmentasyon ve video maskeleme araçlarını bağlayın, ardından ara kareleri karşılaştırın.**

Ekran görüntüsü, geliştirme sırasındaki kare önizlemelerini gösteriyor.

Yazar Antigravity’de Gemini 4 Neon, Meta SAM 3 ve MatAnyone 2’yi birlikte kullandı. Kaynak, nicel değerlendirmesi bulunmayan bir prototip gösteriyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-23/images/case-251-1-86fdd55e6559.jpg" alt="Antigravity’de video maskeleme prototipi oluşturun · 1" width="560">

Type: Demo | Date: 2026-11-23

---

## 🎮 Oyunlar ve Simülasyonlar
<a id="games"></a>

<a id="case-58"></a>
### Case 58: [Yan kaydırmalı bir engel oyunu oluşturun](https://x.com/notjazii/status/2123162053292458218) (by [@notjazii](https://x.com/notjazii))

**Küçük bir oyun prototipini incelerken engel döngüsünü ve çarpışma davranışını test edin.**

Testi yapan kişi Neon'dan Flappy Bird tarzı bir prototip istedi ve bir kayıt yayınladı.

Yazar yaklaşık beş dakikayı aktarıyor ve maliyet ve kullanıma ilişkin kendi izlenimlerini tartışıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-58-1-9c665bbec561.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-58-1-316557add829.jpg" alt="Yan kaydırmalı bir engel oyunu oluşturun · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-59"></a>
### Case 59: [Kılıç ve kalkan savaş sahnelerini karşılaştırın](https://x.com/IndependentEco/status/2123169526619758996) (by [@IndependentEco](https://x.com/IndependentEco))

**Görsel ve etkileşim farklılıklarını kendiniz değerlendirmek için etiketli iki klibi kullanın.**

Testi yapan kişi, bir savaş oyunu sahnesi için Fable 5.2 ve Neon çıkışları etiketli bir video yayınladı.

Video iki sonucu kaydediyor ve genel bir model sıralaması oluşturmuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-59-1-ba79ec8e02b6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-59-1-8644c701cdea.jpg" alt="Kılıç ve kalkan savaş sahnelerini karşılaştırın · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-60"></a>
### Case 60: [Synthwave tarzında bir mini golf oyunu yapın](https://x.com/antigravity/status/2123176067380711725) (by [@antigravity](https://x.com/antigravity))

**Ajanların işi nasıl paylaştığını ve sekiz parkurun tarayıcıda nasıl doğrulandığını inceleyin.**

Google Antigravity, Gemini 4 Neon’un Swarm ile tek bir istemden 3B mini golf oyunu oluşturmasını gösteriyor.

Videoda sekiz görev ajanı, tarayıcıda oynanış ve yerleşik doğrulayıcının sekiz parkurun tamamını denetlemesi görülüyor.

**Prompt:**

```
Build NEONPUTT '84: a 2-player synthwave 3D mini golf game with custom GLSL shaders, 240Hz fixed-timestep physics, procedural Web Audio SFX, and 8 animated courses.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-60-1-bb8fa045c256.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-60-1-aabeaf2b1557.jpg" alt="Synthwave tarzında bir mini golf oyunu yapın · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-61"></a>
### Case 61: [Animasyonlu şövalye düellolarını karşılaştırın](https://x.com/IndependentEco/status/2123177347046355324) (by [@IndependentEco](https://x.com/IndependentEco))

**İki düello klibindeki hareket okunabilirliğini ve karakter sahnelemesini karşılaştırın.**

Testi yapan kişi, zırhlı karakterler arasında bir düello için Opus 5.5 ve Neon çıkışlarını ayrı ayrı etiketledi.

Gönderi, okuyuculardan oluşturulan sonuçları değerlendirmelerini istiyor ve kontrollü bir protokol açıklamıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-61-1-e225fa617e25.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-61-1-9759ab506b69.jpg" alt="Animasyonlu şövalye düellolarını karşılaştırın · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-62"></a>
### Case 62: [Tek bir HTML dosyasında dışavurumcu bir sanat oyunu yapın](https://x.com/GeokenAI/status/2123178088439959750) (by [@GeokenAI](https://x.com/GeokenAI))

**Tek bir HTML dosyası olarak sunulan oyunun görsel stilini ve kontrollerini inceleyin.**

Geliştirici, tek bir HTML dosyasında bulunan sonsuz bir JavaScript sanat oyunu oluşturmak için Neon'u kullandı.

Geliştirici sonucu yayınladı ve dışavurumcu görsel işleyişini açıkladı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-62-1-2f66690ce4f1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-62-1-c9b9995f7891.jpg" alt="Tek bir HTML dosyasında dışavurumcu bir sanat oyunu yapın · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-63"></a>
### Case 63: [Buz patronu oyun prototiplerini karşılaştırın](https://x.com/IndependentEco/status/2123187721040503097) (by [@IndependentEco](https://x.com/IndependentEco))

**Paylaşılan bir istem olduğunu varsaymadan sahnenin okunabilirliğini değerlendirmek için etiketli karşılaşma görüntülerini kullanın.**

Testi yapan kişi, birinci şahıs buz patronu karşılaşması için etiketli Neon ve Opus 5.5 çıkışlarını yayınladı.

Video görsel bir karşılaştırma sağlıyor. Gönderi, bilgi istemini, ayarları, zamanlamayı ve kazananı açık bırakıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-63-1-698acd0d6e0b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-63-1-ebb40849a72b.jpg" alt="Buz patronu oyun prototiplerini karşılaştırın · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-64"></a>
### Case 64: [Karpuz basketbol demosu](https://x.com/AdamHoltererer/status/2123189375831859349) (by [@AdamHoltererer](https://x.com/AdamHoltererer))

**Bu prototipteki sahayı, hareketi ve top etkileşimini inceleyin.**

Testi yapan kişi bir Neon karpuz basketbol videosu paylaşıyor.

Yazar, test edilen modeli adlandırır ve sonucu bağlar ancak zamanlama veya yapı ayarları sağlamaz.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-64-1-12fdea478ad2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-64-1-832287da058f.jpg" alt="Karpuz basketbol demosu · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-65"></a>
### Case 65: [Gaussian sıçrayan bir fırın platformu inşa edin](https://x.com/GlitterPixely/status/2123235794747891968) (by [@GlitterPixely](https://x.com/GlitterPixely))

**Oluşturma işini oyun ayarlamasından ayırmak için kaydedilen oynatmayı kullanın.**

Yaratıcı, C++20 ve WebGPU Gaussian sıçrama motorunu dört kuleli bir platform oyununa dönüştürmek için Neon'u kullandı.

Yaratıcı, üç uyarı ve yaklaşık 60 dakikalık aktif sürü süresi bildirdi, ardından modelden demoyu kaydetmesini istedi.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-65-1-02f40215c097.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-65-1-df9397699125.jpg" alt="Gaussian sıçrayan bir fırın platformu inşa edin · 1" width="560"></a>

Type: Demo | Date: 2026-11-19

---

<a id="case-66"></a>
### Case 66: [Antigravity Swarm ile 3 boyutlu bir oyun oluşturun](https://x.com/ai_for_success/status/2123239282626478306) (by [@ai_for_success](https://x.com/ai_for_success))

**Ortaya çıkan mobil ve masaüstü yollarını Swarm destekli bir yapıda ayrı ayrı inceleyin.**

Geliştirici, küçük bir 3D oyun oluşturmak için Neon ve Antigravity Swarm'ı kullandı.

Geliştirici hem mobil hem de masaüstü desteğini açıklıyor ve bir adım adım açıklamalı konuyu paylaşıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-66-1-ec1085204901.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-66-1-63e6c5c75657.jpg" alt="Antigravity Swarm ile 3 boyutlu bir oyun oluşturun · 1" width="560"></a>

Type: Demo | Date: 2026-11-19

---

<a id="case-67"></a>
### Case 67: [Uzay yarışı prototipi](https://x.com/badboyfoxy/status/2123251809183785076) (by [@badboyfoxy](https://x.com/badboyfoxy))

**Oynanabilir sonucu, ilk yapının bildirilen süresi ve maliyetiyle karşılaştırın.**

Bir yaratıcı, yüksek mantıkla Neon'la bir uzay yarışçısı yaptığını bildirdi.

Yaratıcı, yaklaşık 15 dakikalık bir çalışmanın 1,50 ABD dolarına mal olduğunu bildirdi ve çıktıyı yayınladı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-67-1-538f36726201.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-67-1-22fc51387262.jpg" alt="Uzay yarışı prototipi · 1" width="560"></a>

Type: Demo | Date: 2026-11-19

---

<a id="case-68"></a>
### Case 68: [Kule savunma prototipi](https://x.com/DeryaTR_/status/2123276863481254210) (by [@DeryaTR_](https://x.com/DeryaTR_))

**Yazarın akıcılık raporundan genelleme yapmadan önce kule savunma döngüsünü kendiniz test edin.**

Bir geliştirici, Neon yapılı bir kule savunma prototipinin oynanışını yayınladı.

Geliştirici yaklaşık 20 dakika ve beş saatlik kotasının %2'sini bildirdi. Sorunsuz oyun iddiası geliştiricinin değerlendirmesidir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-68-1-4fadc1a0a053.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-68-1-9adcd74642bd.jpg" alt="Kule savunma prototipi · 1" width="560"></a>

Type: Demo | Date: 2026-11-19

---

<a id="case-69"></a>
### Case 69: [Birinci şahıs kayak simülatörü oluşturun](https://www.youtube.com/watch?v=xhG-jNObuz4) (by [@Google](https://blog.google/))

**Kayak simülatörünü değerlendirirken araziye, harekete ve sese ayrı ayrı bakın.**

Google, Mont Blanc ve Chamonix arazisinde bir WebGL2 serbest sürüş simülatörü oluşturmak için Neon'u kullandığını bildiriyor.

Gösteride altı kayak hattı, 120 Hz'lik fizik döngüsü, pist oymaları ve mekansal ses yer alıyor.

[Ek kaynak](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

<a href="https://www.youtube.com/watch?v=xhG-jNObuz4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-69-1-42268a3924ba.jpg" alt="Birinci şahıs kayak simülatörü oluşturun · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-130"></a>
### Case 130: [Prosedürel bir dört ayaklı robot simülasyonu geliştirme](https://x.com/thebuggeddev/status/2123760487183872482) (by [@thebuggeddev](https://x.com/thebuggeddev))

**Ekrandaki fizik gösterimiyle fiziksel robot hakkındaki iddiaları ayrı değerlendirin.**

Üretici, bir referans görselden türetilen dört ayaklı simülasyonu Neon'a atfediyor ve prosedürel gölgelendiriciler, fizik ve kablo simülasyonu kullanıldığını belirtiyor.

Demo simüle edilen modeli ve malzemeleri gösteriyor. Paylaşımda prosedürel gölgelendiriciler ve simüle hareket içeren bir tarayıcı prototipi anlatılıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-130-1-0bf50c697b90.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-130-1-57d1a7297441.jpg" alt="Prosedürel bir dört ayaklı robot simülasyonu geliştirme · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-168"></a>
### Case 168: [İki The Last Take oyun sahnesini karşılaştırma](https://x.com/atakoylanai/status/2123947041147740484) (by [@atakoylanai](https://x.com/atakoylanai))

**Etiketli iki sürümde arayüzün okunabilirliğini ve sahne kompozisyonunu karşılaştırın.**

Üretici, The Last Take'in Neon ve Fable 5.2'ye atfedilen sürümlerini karşılaştırıyor.

Özgün yan yana klip, oyun görünümlerini ve arayüzleri gösteriyor. Paylaşımda bağımsız bir oynanabilirlik testi bulunmuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-168-1-33c5197747b2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-168-1-d3791fbcdfd2.jpg" alt="İki The Last Take oyun sahnesini karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-21

---

<a id="case-209"></a>
### Case 209: [Ozymandias'ın Minecraft yorumlarını karşılaştırma](https://x.com/jan_volad/status/2124174497914003925) (by [@jan_volad](https://x.com/jan_volad))

**Ortak yapım görevinde yaratıcı yorumları ve bildirilen çalışma sürelerini karşılaştırın.**

Üretici Shelley'nin şiirine dayanan aynı istemi kullandı. Neon için 19 dakika ve 2,88 ABD doları, Sol için 12 dakika ve 1,06 ABD doları bildiriyor.

Yan yana çıktılar aynı şiirin iki ayrı yorumunu gösteriyor. Süre ve maliyetler üreticinin kendi denemelerine ait.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-209-1-2c405e9f4e01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-209-1-3bad09e19ba2.jpg" alt="Ozymandias&#x27;ın Minecraft yorumlarını karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-21

---

<a id="case-221"></a>
### Case 221: [Sekiz televizyon mekânının Minecraft yapılarını karşılaştırma](https://x.com/jan_volad/status/2124308264456233400) (by [@jan_volad](https://x.com/jan_volad))

**Sekiz mekânın tamamında görsel benzerliği, maliyet ve üretim süresiyle birlikte karşılaştırın.**

Üretici Neon ve Sol'a sekiz mekân için aynı Minecraft görevini verdi.

Etiketli karşılaştırmaya Neon için toplam 22, Sol için 24 dakikalık süre eşlik ediyor. Üretici maliyetleri ve görsel tercihini ayrıca bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-221-1-538854ff5d01.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-221-1-5f26eb812b14.jpg" alt="Sekiz televizyon mekânının Minecraft yapılarını karşılaştırma · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-22

---

<a id="case-222"></a>
### Case 222: [AI Studio'da bir zar atma aracı oluşturma](https://x.com/LyalinDotCom/status/2124309371932832221) (by [@LyalinDotCom](https://x.com/LyalinDotCom))

**Küçük bir tarayıcı aracıyla başlayın ve çalıştığını oyun sırasında doğrulayın.**

Üretici, evde hazırlanan masa oyunlarında kullanılan zar aracını Google AI Studio'da Neon ile yaptığını anlatıyor.

Ekli görsel zarı ve arayüzünü gösteriyor. Uygulama, açıkça tarif edilen tek bir işi yapıyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-222-1-56174d1476fd.jpg" alt="AI Studio&#x27;da bir zar atma aracı oluşturma · 1" width="560">

Type: Demo | Date: 2026-11-22

---

<a id="case-226"></a>
### Case 226: [Oynanabilir ipuçlarıyla kaçış odası prototipi yapma](https://x.com/jacalulu/status/2124325874212446345) (by [@jacalulu](https://x.com/jacalulu))

**Düzenleme gereken ipuçlarını ve etkileşimleri bulmak için ilk sürümü oynayın.**

Üretici, Astrolab kaçış odasının ilk oynanabilir sürümünü tek istekten oluşturmayı Neon'a atfediyor.

Üretici bir arkadaşının oyunu denemesinin ardından küçük değişiklikler yaptığını bildiriyor. Video bulmaca ortamını ve tezgâhı gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-226-1-9c47f9e589ce.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-226-1-949fefc74792.jpg" alt="Oynanabilir ipuçlarıyla kaçış odası prototipi yapma · 1" width="560"></a>

Type: Demo | Date: 2026-11-22

---

<a id="case-236"></a>
### Case 236: [tvOS için sıra tabanlı topçu oyunu prototipi geliştirme](https://x.com/thorstenball/status/2124439072235991520) (by [@thorstenball](https://x.com/thorstenball))

**Oturma odasındaki oynanışta oyun alanının ve sıra durumunun kolayca görülüp görülmediğini kontrol edin.**

Geliştirici, tvOS topçu oyunu prototipini Neon'a ve Amp'in Mac yardımcı süreçlerine atfediyor.

Özgün klip oyun alanını ve geliştirme ortamını gösteriyor. Paylaşım, geliştirme sürecini belgeliyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-236-1-383dae26ca13.jpg" alt="tvOS için sıra tabanlı topçu oyunu prototipi geliştirme · 1" width="560">

Type: Demo | Date: 2026-11-22

---

<a id="case-245"></a>
### Case 245: [3B mahallede birinci şahıs dedektiflik oyunu oluşturun](https://x.com/venturetwins/status/2124568183902449764) (by [@venturetwins](https://x.com/venturetwins))

**Oyuncunun şüpheliyi işaretleyebilmesi için bir Three.js mahallesini dallanan diyaloglar ve ipucu ekranıyla birleştirin.**

Gösterimde oyuncu mekânlara giriyor, karakterleri sorguluyor ve ipuçlarını inceliyor.

Yazar hikâyeyi, Golden Gai’nin 3B canlandırmasını, girilebilen 16 bardaki karakter ve ipuçlarını ve tanıtım videosunu Neon’a atfediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-23/videos/case-245-1-2389fb584242.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-23/posters/case-245-1-c8850b38c8df.jpg" alt="3B mahallede birinci şahıs dedektiflik oyunu oluşturun · 1" width="560"></a>

Type: Demo | Date: 2026-11-22

---

## 📚 Bilgi Çalışması
<a id="knowledge"></a>

<a id="case-70"></a>
### Case 70: [Model seçimlerini bir araştırma tablosunda özetleme](https://x.com/Arcadia_Bao/status/2123171058002088343) (by [@Arcadia_Bao](https://x.com/Arcadia_Bao))

**Karar vermek için kullanmadan önce model seçim tablosundaki iddiaları kaynaklara göre doğrulayın.**

Yazar, Gemini 4 model seçim tablosunu Neon tarafından gerçekleştirilen araştırmaya bağlıyor.

Ekran görüntüsü sonuçta ortaya çıkan öneridir. Girişleri, bağımsız olarak doğrulanmış ürün kılavuzu değil, araştırma görevinin çıktısıdır.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-70-1-220032ad276d.jpg" alt="Model seçimlerini bir araştırma tablosunda özetleme · 1" width="560">

Type: Demo | Date: 2026-11-18

---

<a id="case-71"></a>
### Case 71: [Neon ile birlikte bir lansman filmi oluşturun](https://x.com/gracepursuits/status/2123190512853176421) (by [@gracepursuits](https://x.com/gracepursuits))

**Filmi sağlayıcı örneği olarak kullanın ve üretim adımlarını ilişkilendirmeden önce diğer araçları tanımlayın.**

Bir Google ekibi üyesi Neon ile birlikte bir film yapıldığını bildiriyor ve sonucu paylaşıyor.

Film, sağlayıcı tarafının bir gösterimidir. Gönderi, hangi araçların tek tek kareleri veya sesi oluşturduğunu tanımlamıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-71-1-b0eb81c105f2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-71-1-aef8fd5224ef.jpg" alt="Neon ile birlikte bir lansman filmi oluşturun · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-72"></a>
### Case 72: [Bir VR oyununda ekipman mekaniğini açıklama](https://x.com/Msfs2000J/status/2123201737217773826) (by [@Msfs2000J](https://x.com/Msfs2000J))

**Açıklayıcı eseri bir kılavuz olarak ele almadan önce oyun mekaniğiyle karşılaştırın.**

Yazar, Meta Quest oyunu H3VR2'deki ekipmanı özetlemek için Neon'u kullandı ve resimli bir açıklayıcı ekledi.

Eser oyun senaryosunu belgeliyor. Kaynak, tam istemi tanımlamıyor veya video prodüksiyonunu Neon'a atamıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-72-1-edea62f20bb5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-72-1-b669c1f763a7.jpg" alt="Bir VR oyununda ekipman mekaniğini açıklama · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-73"></a>
### Case 73: [Görüntü kırpma sırasında öz değerlendirmeyi inceleyin](https://x.com/viticci/status/2123208444681372133) (by [@viticci](https://x.com/viticci))

**Modelin kalitesine ilişkin açıklamasına güvenmeden önce mahsulün kendisini değerlendirin.**

Testçi, Neon'un bir görüntü düzenleme testi sırasında kendi ürününe iltifat ettiğini bildirdi.

Ekran görüntüsü tek bir etkileşimi belgeliyor. Mahsul kalitesini veya diğer araçların davranışını belirlemez.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-73-1-be1d8691e528.jpg" alt="Görüntü kırpma sırasında öz değerlendirmeyi inceleyin · 1" width="560">

Type: Limit | Date: 2026-11-19

---

<a id="case-74"></a>
### Case 74: [Bir makaleyi düzenlenebilir slaytlara dönüştürün](https://x.com/tetumemo/status/2123210419137601764) (by [@tetumemo](https://x.com/tetumemo))

**Slaytların düzenlenebilir olduğundan ve görsellerinin orijinal makaleyi desteklediğinden emin olun.**

Yaratıcı, Neon'a bir makale gönderdi ve herkese açık slayt oluşturma becerisini kullandı.

İçerik oluşturucu, iş akışının resimler oluşturup eklediğini ve düzenlenebilir Google Slaytlar sunduğunu bildiriyor. Gönderi, görüntü oluşturucuyu tanımlamadan genel iş akışını açıklıyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-74-1-b1cfed0393a4.jpg" alt="Bir makaleyi düzenlenebilir slaytlara dönüştürün · 1" width="560">

Type: Demo | Date: 2026-11-19

---

<a id="case-75"></a>
### Case 75: [Bir fantastik roman açılışı oluşturun](https://x.com/Arcadia_Bao/status/2123222272697913481) (by [@Arcadia_Bao](https://x.com/Arcadia_Bao))

**Daha uzun bir taslak hakkında sonuca varmadan önce stil ve ses açısından açılışı gözden geçirin.**

Yazar Neon'u bir yazma testi için kullandı ve bir Çin fantastik öyküsünün açılışını yayınladı.

Gönderi, tamamlanmış bir açılış alıntısını gösterir. Uzunluğu ve kalitesi, modelin uzun süreli performansını belirlemez.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-75-1-142f892ae717.jpg" alt="Bir fantastik roman açılışı oluşturun · 1" width="560">

Type: Demo | Date: 2026-11-19

---

<a id="case-76"></a>
### Case 76: [Orijinal bir Dario şakasını yorumlayın](https://x.com/MichaelLee009/status/2123236918456733855) (by [@MichaelLee009](https://x.com/MichaelLee009))

**Belirli bir şakayı anlamayı geniş kapsamlı yazma becerisinden ayırmak için eşleşen örnekleri kullanın.**

Yazar, Neon'un yazdıkları bir şakayı anladığını ancak Opus 5.5'in anlamadığını bildirdi.

Bu, ekran görüntüleriyle yapılan bir denemedir. Geniş kapsamlı yazma veya muhakeme performansı oluşturmaz.

<table>
<tr>
<td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-76-1-0e02d7ae6f39.jpg" alt="Orijinal bir Dario şakasını yorumlayın · 1" width="560"></td>
<td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-76-2-d1e4fd891049.jpg" alt="Orijinal bir Dario şakasını yorumlayın · 2" width="560"></td>
</tr>
</table>

Type: Evaluation | Date: 2026-11-19

---

<a id="case-77"></a>
### Case 77: [E-Tablolar'da bilgisayarlı görüntü laboratuvarı oluşturma](https://www.youtube.com/watch?v=vPsBbuz9IbE) (by [@Google](https://blog.google/))

**Yalnızca elektronik tablo görselleştirmesini değerlendirirken formüllerden hangi efektlerin geldiğini inceleyin.**

Google, bir Neon sürüsünün bir referans görselini 100.000 hücreli bir e-tabloya dönüştürdüğünü bildiriyor.

Demo, kenar algılama, derinlik haritalama ve yeniden aydınlatma gibi görevler için altı modda 500.000'den fazla formül kullanıyor.

[Ek kaynak](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

<a href="https://www.youtube.com/watch?v=vPsBbuz9IbE"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-77-1-8d819090ab15.jpg" alt="E-Tablolar&#x27;da bilgisayarlı görüntü laboratuvarı oluşturma · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-104"></a>
### Case 104: [Model eğitimini bir müzik videosuyla anlatmak](https://x.com/elliotarledge/status/2123608819943211022) (by [@elliotarledge](https://x.com/elliotarledge))

**Eğitim aşamalarını müzik videosuyla tanıtın ve teknik ayrıntıları ayrıca doğrulayın.**

Yapımcı Gemini 4 Neon’dan en gelişmiş modellerin nasıl eğitildiğini anlatan bir müzik videosu istedi.

Yayımlanan video eğitim ve eğitim sonrasını şarkı sözleriyle ve hareketli şemalarla anlatıyor. Bu, teknik bir konunun nasıl sunulabileceğine dair bir örnek.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/videos/case-104-1-704072667b23.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/posters/case-104-1-fd4f10acc8b5.jpg" alt="Model eğitimini bir müzik videosuyla anlatmak · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-121"></a>
### Case 121: [Üç haftalık sosyal medya verisini analiz etme](https://x.com/poolmoon6/status/2123744162285785300) (by [@poolmoon6](https://x.com/poolmoon6))

**Korelasyonları bu hesaba özgü keşif niteliğinde gözlemler olarak değerlendirin.**

Üretici, Neon High'dan üç haftalık X metriklerini incelemesini istediğini ve göstergeler için sıralı bir korelasyon analizi aldığını bildiriyor. Ekte analizin bir kısmı görülüyor.

Ek, yazarın üç haftalık örnekleminden elde edilen korelasyonların bir bölümünü gösteriyor. Bulgular bildirilen hesap verileriyle sınırlı.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-121-1-d3d49f1d7a7f.jpg" alt="Üç haftalık sosyal medya verisini analiz etme · 1" width="560">

Type: Demo | Date: 2026-11-20

---

<a id="case-125"></a>
### Case 125: [Sesli özetten hareketli politika özeti hazırlama](https://x.com/HiromitsuTakagi/status/2123751869319389642) (by [@HiromitsuTakagi](https://x.com/HiromitsuTakagi))

**Kaynak belgeyi, sesli özeti ve sonradan eklenen görsel katmanı ayrı değerlendirin.**

Üretici kaynak olarak Japon bir çalışma grubunun kamuya açık belgesini, girdi olarak Gemini Notebook'un sesli özetini, eşlik eden video için de Neon'u kullanıyor.

Üretici kamuya açık toplantı belgesini belirtiyor ve ayrı oluşturulmuş sesli özeti kullanıyor. Eşlik eden videoyu Neon'a atfediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-125-1-8144b9389ca3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-125-1-6d61156c32ae.jpg" alt="Sesli özetten hareketli politika özeti hazırlama · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-141"></a>
### Case 141: [Geniş bir klip koleksiyonunu videoya dönüştürme](https://x.com/AndroidDev/status/2123824825198170569) (by [@AndroidDev](https://x.com/AndroidDev))

**Medyanın dizine eklenmesinden düzenlemeye kadar gösterilen adımları inceleyin.**

Android Developers hesabı, Neon ile yaklaşık bin klibi dizine ekleyen bir iş akışı sunuyor ve sonrasındaki video düzenlemeyi gösteriyor.

Android Developers kaynağı, düzenleme sürecinde geniş bir klip koleksiyonunda arama yapıldığını gösteriyor. Yaklaşık klip sayısını yayıncı bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-141-1-a8c7174a1ef5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-141-1-2b58a5045533.png" alt="Geniş bir klip koleksiyonunu videoya dönüştürme · 1" width="560"></a>

Type: Demo | Date: 2026-11-20

---

<a id="case-153"></a>
### Case 153: [Antarktika verilerini ajanlarla inceleme](https://x.com/DynamicWebPaige/status/2123880090203570480) (by [@DynamicWebPaige](https://x.com/DynamicWebPaige))

**Veri girdilerini kaydedin ve modelin fiziksel yorumlarını hipotez olarak değerlendirin.**

Üretici, açık uydu hız verilerini ve Antarktika'nın buz altı topografyasını incelemek için Neon ajan grubu kullandığını bildiriyor.

Yayımlanan grafikler Thwaites ve Pine Island buzullarının incelenmesine eşlik ediyor. Kaynak, deneysel bir iş akışı anlatıyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-153-1-3751af053ea4.jpg" alt="Antarktika verilerini ajanlarla inceleme · 1" width="560">

Type: Demo | Date: 2026-11-20

---

<a id="case-178"></a>
### Case 178: [Ajan döngüsünde turun durumunu görselleştirme](https://x.com/antiAIvo/status/2124028084022353961) (by [@antiAIvo](https://x.com/antiAIvo))

**Okurların normal tamamlanmayı ve iptali izleyebilmesi için kaynak kodu durum şemasıyla eşleştirin.**

Üretici ajan döngüsünü etkileşimli bir HTML açıklaması olarak sunmak için Neon kullandı.

Video kod ve şema arasındaki eşleşen vurguları ve farklı çıkış yollarının dal filtrelerini gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-178-1-4f6d09202c74.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-178-1-7c5ece5f7cef.jpg" alt="Ajan döngüsünde turun durumunu görselleştirme · 1" width="560"></a>

Type: Tutorial | Date: 2026-11-21

---

<a id="case-179"></a>
### Case 179: [Ajanlarla Mars'ın sismik dalga biçimlerini inceleme](https://x.com/DynamicWebPaige/status/2124030792385052735) (by [@DynamicWebPaige](https://x.com/DynamicWebPaige))

**Analiz iş akışını kaynak verilerden ve gösterilen grafiklerden inceleyin.**

Üretici, Antigravity'deki Neon ajan grubunun dört yıllık açık NASA InSight dalga biçimi verisini işlediğini belirtiyor. Grafikler yazarın keşif niteliğindeki sonuçları.

Ek, kamuya açık NASA ölçümlerinin keşif amaçlı işlenmesini belgeliyor. Yorum, üreticinin bildirdiği bir araştırma yardımcısı niteliğinde.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-179-1-e8e966e654bb.jpg" alt="Ajanlarla Mars&#x27;ın sismik dalga biçimlerini inceleme · 1" width="560">

Type: Demo | Date: 2026-11-21

---

<a id="case-185"></a>
### Case 185: [Üç modelin ve bir insanın kısa öykülerini karşılaştırma](https://x.com/risui1012/status/2124041518109614235) (by [@risui1012](https://x.com/risui1012))

**Ortak öykü fikrine dayanarak anlatım ve yapı farklarını inceleyin.**

Yazar, 500 karakterlik ortak bir görev veriyor ve insanın yardımsız yazdığı sürümü Sol, Neon ve Opus'un ilk taslaklarıyla karşılaştırıyor.

Yazar insan tarafından yazılan yanıtı ve üç model çıktısını belirtiyor. Örnek, Japonca tek bir yazma görevini ve yazarın değerlendirmesini belgeliyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-185-1-49210b78c3ea.jpg" alt="Üç modelin ve bir insanın kısa öykülerini karşılaştırma · 1" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-185-2-00ffccb0856e.jpg" alt="Üç modelin ve bir insanın kısa öykülerini karşılaştırma · 2" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-185-3-57fcab7847e7.jpg" alt="Üç modelin ve bir insanın kısa öykülerini karşılaştırma · 3" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-185-4-3d39c206cff1.jpg" alt="Üç modelin ve bir insanın kısa öykülerini karşılaştırma · 4" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-185-5-dedf7868e54d.jpg" alt="Üç modelin ve bir insanın kısa öykülerini karşılaştırma · 5" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-185-6-3a8317a8d885.jpg" alt="Üç modelin ve bir insanın kısa öykülerini karşılaştırma · 6" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-185-7-7397ce5c273e.jpg" alt="Üç modelin ve bir insanın kısa öykülerini karşılaştırma · 7" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-185-8-d29e292ef86b.jpg" alt="Üç modelin ve bir insanın kısa öykülerini karşılaştırma · 8" width="560">

Type: Evaluation | Date: 2026-11-21

---

<a id="case-199"></a>
### Case 199: [Antigravity'de kısa bir anlatım videosu hazırlama](https://x.com/DynamicWebPaige/status/2124132842179350814) (by [@DynamicWebPaige](https://x.com/DynamicWebPaige))

**Demoyu birden çok medya aracının koordine edildiği bir iş akışı olarak değerlendirin.**

Üretici, 90 saniyelik videoyu Neon ve Antigravity'ye atfediyor; Google medya araçlarını, metinden sese dönüştürmeyi ve HyperFrames'i iş akışının parçaları olarak sıralıyor.

Yazar birden çok aracın kullanıldığı üretimi ve Neon'un katkı verdiği adımları açıklıyor. Ekte bitmiş anlatım videosu var.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-199-1-96168cce27f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-199-1-fe669c11d8c2.jpg" alt="Antigravity&#x27;de kısa bir anlatım videosu hazırlama · 1" width="560"></a>

Type: Demo | Date: 2026-11-21

---

<a id="case-210"></a>
### Case 210: [Bir beceriyle kısa bir bilgi videosu oluşturma](https://x.com/GeekCatX/status/2124175490516918376) (by [@GeekCatX](https://x.com/GeekCatX))

**Modelin katkısını ve mevcut görüntüleme iyileştirmesini ayrı ayrı belirtin.**

Yazar iki dakikadan uzun bir videoyu tamamlamak için Neon'u mevcut bilgi videosu becerisiyle ve ayrı bir görüntüleme iyileştirmesiyle kullandı. Zaman ve kota rakamları bu denemeye ait.

Paylaşım yeniden kullanılabilir video becerisiyle görüntüleme iyileştirmesini ayrı ayrı tanımlıyor. Medya bu ortak iş akışının sonucu.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-210-1-41bd33ccd376.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-210-1-537494d8c9fe.jpg" alt="Bir beceriyle kısa bir bilgi videosu oluşturma · 1" width="560"></a>

Type: Demo | Date: 2026-11-21

---

<a id="case-224"></a>
### Case 224: [Su setinin göçme biçimlerini üç boyutlu kesitle gösterme](https://x.com/doboku_works/status/2124318343780090323) (by [@doboku_works](https://x.com/doboku_works))

**Farklı arıza mekanizmalarının nerede oluştuğunu döndürülebilen görünümden inceleyin.**

Üretici, basitleştirilmiş iki boyutlu sızıntı hesabını üç boyutlu kesitle birleştiren bir çalışma görselleştirmesi için Neon kullandı.

Görünümler taşma, sızıntı, borulanma ve oyulmayı kapsıyor. Üretici bunları kişisel çalışma malzemesi olarak sunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-224-1-90625643834c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-224-1-660c143ab28d.jpg" alt="Su setinin göçme biçimlerini üç boyutlu kesitle gösterme · 1" width="560"></a>

Type: Demo | Date: 2026-11-22

---

<a id="case-227"></a>
### Case 227: [Pi'nin ajan altyapısını etkileşimli şemayla açıklama](https://x.com/chasen_liao/status/2124352577852821919) (by [@chasen_liao](https://x.com/chasen_liao))

**Araçların ve uzantıların ajan durumunu nasıl etkilediğini etkileşimli şemadan izleyin.**

Üretici Pi'nin ajan altyapısını ve dört yerleşik aracını göstermek için Neon kullandı.

Anlatım araç çağrılarını, MCP bağlamını ve çekirdekle uzantılar arasındaki sınırı kapsıyor. Video durumların adım adım incelendiğini gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-227-1-0d9f175cbc3f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-227-1-15fc189a1e88.jpg" alt="Pi&#x27;nin ajan altyapısını etkileşimli şemayla açıklama · 1" width="560"></a>

Type: Tutorial | Date: 2026-11-22

---

<a id="case-243"></a>
### Case 243: [Etkileşimli bir modelle göz optiğini öğretin](https://x.com/thebuggeddev/status/2124508873897726028) (by [@thebuggeddev](https://x.com/thebuggeddev))

**Öğrencilerin optik ayarları değiştirmesini, benzetilen ışık yolu ve retina odağını gözlemlemesini sağlayın.**

Video 3B bir gözü, odak ve mercek ayarlarını ve renkli görme görünümlerini gösteriyor.

Yazar eğitim görselleştirmesini Neon kullanarak Navarro ve Gullstrand göz modelleri üzerine kurdu. Gösterimde astigmatizm ve düzeltici mercekler bulunuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-23/videos/case-243-1-a6e63a9e64b8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-23/posters/case-243-1-d0dca018e12c.jpg" alt="Etkileşimli bir modelle göz optiğini öğretin · 1" width="560"></a>

Type: Demo | Date: 2026-11-22

---

## 📈 Değerlendirmeler ve Limitler
<a id="evaluations"></a>

<a id="case-78"></a>
### Case 78: [Vals Index'te alan adı performansını ölçün](https://x.com/ValsAI/status/2123168167879147542) (by [@ValsAI](https://x.com/ValsAI))

**Toplam sıralamanın alanınızla eşleşip eşleşmediğini görmek için görev düzeyindeki sonuçları kullanın.**

Vals AI, Neon için %70,9'luk bir puan elde etti ve toplamda Fable 5.2'nin 0,4 puan gerisinde ikinci sırada yer aldı.

Değerlendirici aynı zamanda Finans ve Hukuk endeksleri ile Vergi Temsilcisi ve Hukuki Araştırma görevlerinde de birinci sırayı bildirir.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-78-1-a072bf0d10fb.jpg" alt="Vals Index&#x27;te alan adı performansını ölçün · 1" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="case-79"></a>
### Case 79: [Erken erişim sırasında etkileşimli demoları test edin](https://x.com/kimmonismus/status/2123168299890704735) (by [@kimmonismus](https://x.com/kimmonismus))

**Başarılı prototipleri aynı erken erişim başlığında bildirilen hatalarla karşılaştırın.**

Yazar, 17 etkileşimli demo oluşturmak için Neon'u Antigravity'de kullandığını ve ek kodlama ve araç testlerini belgelediğini bildiriyor.

Yayınlanan başlıkta hem başarılar hem de sorunlar rapor ediliyor. Demoları tek bir erken erişim test serisi olarak gruplandırılmıştır.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-79-1-2c55ce07666c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-79-1-d15a99ad1fc4.jpg" alt="Erken erişim sırasında etkileşimli demoları test edin · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-80"></a>
### Case 80: [Agent Arena'daki temsilci oturumlarını karşılaştırın](https://x.com/arena/status/2123169189397709174) (by [@arena](https://x.com/arena))

**Agent Arena sonuçlarını karşılaştırırken bildirilen puanın yanı sıra görev başına ortalama maliyeti kullanın.**

Arena, Neon High için 1336 puan, ikincilik ve görev başına 2,82 USD medyan maliyet bildirdi.

Arena'nın gönderisinde 4,2 bin topluluk temsilcisi oturumuna dayanan bir değerlendirme anlatılıyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-80-1-98fe72255edb.png" alt="Agent Arena&#x27;daki temsilci oturumlarını karşılaştırın · 1" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="case-81"></a>
### Case 81: [Neon'u Text Arena'ya yerleştirin](https://x.com/arena/status/2123169199396946279) (by [@arena](https://x.com/arena))

**Skorları okurken aynı Arena anlık görüntüsünü ve muhakeme ayarlarını karşılaştırın.**

Arena, Neon High'ı 1518'de, Carbon High'ı 1526'da ve Argon High'ı 1521'de takip ediyor.

Bu, karşılaştırma yayıncısından bir Text Arena anlık görüntüsüdür.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-81-1-c75a9fa2d99d.png" alt="Neon&#x27;u Text Arena&#x27;ya yerleştirin · 1" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="case-82"></a>
### Case 82: [Wojak-Bench’te 3B baskıya uygun figürleri değerlendirin](https://x.com/lukaspet/status/2123169317076574513) (by [@lukaspet](https://x.com/lukaspet))

**Yayımlanan sırayı ikili karşılaştırmanın o andaki sonucu olarak okuyun. Puanı aktarmadan önce güncel sıralamaya bakın.**

Kıyaslama ortak yazarı, Neon'un dördüncü sırada çıkış yaptığını bildirdi. Yayınlanan lider tablosu anlık görüntüsü Neon'a 1056 puan veriyor.

Modeller aynı referans çizimini yazdırılabilir şekillere dönüştürür. Ziyaretçiler çıktı çiftlerini karşılaştırır, böylece oylar biriktikçe canlı derecelendirme değişebilir.

[Ek kaynak](https://wojak-bench.dev.pion.dev/)

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-82-1-fb8d9cb391a5.jpg" alt="Wojak-Bench’te 3B baskıya uygun figürleri değerlendirin · 1" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="case-83"></a>
### Case 83: [Kodlama aracılarını koşum takımlarıyla karşılaştırın](https://x.com/ArtificialAnlys/status/2123170648772288540) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Kodlama sonuçlarını karşılaştırırken her modelin değerlendirme kurulumunu ve ayarlarını görünür tutun.**

Yapay Analiz, Antigravity CLI ile Neon xhigh için 59 ve Carbon high için 55 rapor ediyor.

Neon için görev başına ortalama 6,86 USD maliyet bildiriyor. Kaynaktaki Claude karşılaştırmalarında Claude Kodu ve ayrı muhakeme ayarları kullanılmıştır.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-83-1-ca536c909af6.jpg" alt="Kodlama aracılarını koşum takımlarıyla karşılaştırın · 1" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="case-84"></a>
### Case 84: [AA-Briefcase üzerindeki bilgi çalışmasını değerlendirin](https://x.com/ArtificialAnlys/status/2123170651980931421) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Karşılaştırmalı değerlendirmeyi yorumlarken sunum kalitesini genel puandan ayırın.**

Yapay Analiz, Neon xhigh için 1700 Elo ve Carbon high için 1611 Elo rapor ediyor.

Yayıncı, Neon'un Sunum puanı için 1771'i rapor ediyor. Bağlantılı karşılaştırma, genel Evrak Çantası-Lite görevlerini kullanır.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-84-1-b09c2428be07.jpg" alt="AA-Briefcase üzerindeki bilgi çalışmasını değerlendirin · 1" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="case-85"></a>
### Case 85: [Zaman Artificial Analysis Intelligence Index görevleri](https://x.com/ArtificialAnlys/status/2123170655424450840) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Bir akıl yürütme ayarı seçerken uçtan uca süreyi belirteç çıkış hızından ayrı olarak ölçün.**

Yapay Analiz, Neon xhigh için görev başına yaklaşık 21 dakika ve Carbon high için 36 dakika olduğunu bildirdi.

Yayıncı, Neon'un daha yüksek bir çıktı oranında yaklaşık %15 daha fazla çıktı tokeni kullandığını bildirdi. Bu farklı ayarlarda Neon'u 61'de ve Carbon'u 60'ta sıraladı.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-85-1-69e9aff683fe.jpg" alt="Zaman Artificial Analysis Intelligence Index görevleri · 1" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="case-86"></a>
### Case 86: [Otomat iş simülasyonu çalıştırın](https://x.com/andonlabs/status/2123174738789011875) (by [@andonlabs](https://x.com/andonlabs))

**Bir temsilci simülasyonunu değerlendirirken son bakiyenin yanı sıra işlem günlüklerini de inceleyin.**

Andon Labs, yayınlandığı sırada Neon'u ilk olarak Vending-Bench 2'de bildirdi.

Simülasyon kayıtları sahte pazarlık iddialarını içeriyordu ancak raporlanan süreçte uydurma kayıp sipariş veya kaçırılan ödeme yoktu.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-86-1-7dc3cded4337.jpg" alt="Otomat iş simülasyonu çalıştırın · 1" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="case-87"></a>
### Case 87: [RuneScape kıyaslama zaman sınırını inceleyin](https://x.com/maxbittker/status/2123183525515886696) (by [@maxbittker](https://x.com/maxbittker))

**Planı makul görünse bile, görevin son tarihini aşan bir çalıştırmayı eksik olarak değerlendirin.**

Karşılaştırma yazarı, Neon'un iddialı stratejilerinin son teslim tarihinden önce tamamlanmadığını bildirdi.

Gözlem, bu zamanlanmış ortamla ilgilidir ve plan kalitesi ile zamanında tamamlanmanın neden ayrı kontrollere ihtiyaç duyduğunu göstermektedir.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-87-1-e374930df0e2.jpg" alt="RuneScape kıyaslama zaman sınırını inceleyin · 1" width="560">

Type: Limit | Date: 2026-11-18

---

<a id="case-88"></a>
### Case 88: [APEX-Agents'ta profesyonel görevleri çalıştırın](https://x.com/mercor/status/2123184025808650641) (by [@mercor](https://x.com/mercor))

**Profesyonel görevleri karşılaştırırken ilk denemede geçme oranını ortalama puandan ayırın.**

Mercor, APEX-Agents'ta Neon için %82,9 Pass@1 ve %88,9 ortalama puan bildirdi.

Bunlar ayrı ölçümlerdir. Yayıncı ayrıca ayrı APEX-Accounting testinde %23,5 Pass@1 sonucu bildirdi.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-88-1-8c2587fa0e1d.jpg" alt="APEX-Agents&#x27;ta profesyonel görevleri çalıştırın · 1" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="case-89"></a>
### Case 89: [CursorBench 4.1'de Neon ve Hydrogen'yi karşılaştırın](https://x.com/cursor_ai/status/2123198346802450926) (by [@cursor_ai](https://x.com/cursor_ai))

**Aynı CursorBench sürümünü kullanın ve belirtilen akıl yürütme ayarlarında puanları karşılaştırın.**

Cursor, varsayılan eforda Neon için %63,7 ve Hydrogen için %57,3 rapor eder.

Karşılaştırma Cursor'un değerlendirmesinde yapıldı ve diğer koşum takımlarının performansını belirlemedi.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-89-1-5735136cf3d0.jpg" alt="CursorBench 4.1&#x27;de Neon ve Hydrogen&#x27;yi karşılaştırın · 1" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="case-90"></a>
### Case 90: [CUDA hata ayıklama görevinde duvar saati süresini ölçün](https://x.com/elliotarledge/status/2123200759819124893) (by [@elliotarledge](https://x.com/elliotarledge))

**Üretimden sonuç çıkarmadan önce aynı hata ayıklama görevinde duvar saati süresini ölçün.**

Yazar, modelleri bir CUDA hata ayıklama isteminde çalıştırdı ve belirteç hızını ve uçtan uca gecikmeyi ayrı ayrı ölçtü.

Yazar bu sonuçta Neon için yaklaşık 76 saniye, Astra ve Opus 5.5 için ise yaklaşık 20 saniye raporladı.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-90-1-1ba56f57fa03.jpg" alt="CUDA hata ayıklama görevinde duvar saati süresini ölçün · 1" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-90-2-a4be57aa7260.jpg" alt="CUDA hata ayıklama görevinde duvar saati süresini ölçün · 2" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-90-3-93ad692aa067.jpg" alt="CUDA hata ayıklama görevinde duvar saati süresini ölçün · 3" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="case-91"></a>
### Case 91: [Tuesday@Work'de işyeri görevlerini ölçün](https://x.com/HelloSurgeAI/status/2123213638819348485) (by [@HelloSurgeAI](https://x.com/HelloSurgeAI))

**Tuesday@Work toplamının yanında alana özgü sonuçları kullanın.**

Surge AI, Neon'u değerlendirme paketinde çalıştırdı ve Tuesday@Work'te 71,6 rapor ederken, Fable 5.2 için 71,2 rapor verdi.

Yayıncı ayrıca DAYJOB Finance, GDP.xlsx ve Riemann-bench'te de üst sıraları rapor ediyor. Puanlar testleri için geçerlidir.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-91-1-d95fd2a981f4.png" alt="Tuesday@Work&#x27;de işyeri görevlerini ölçün · 1" width="560">

Type: Benchmark | Date: 2026-11-19

---

<a id="case-92"></a>
### Case 92: [Antigravity'deki ceza kararlarını inceleyin](https://x.com/wenhaocha1/status/2123252530713124967) (by [@wenhaocha1](https://x.com/wenhaocha1))

**Temsilci kararlarını aynı değerlendirme kurulumundaki referans kararlarıyla karşılaştırın.**

Penalty Bench'in yaratıcısı, Neon'un Antigravity koşum takımını kullanarak kıyaslamada ilk sırada yer aldığını bildirdi.

Kaynak, hakem kararlarıyla karşılaştırılan küçük bir dizi ceza kararını anlatıyor. Bu değerlendirmenin içinde bir sonuç bu.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-92-1-8856d3ed5c45.jpg" alt="Antigravity&#x27;deki ceza kararlarını inceleyin · 1" width="560">

Type: Benchmark | Date: 2026-11-19

---

<a id="case-93"></a>
### Case 93: [Tarayıcı Kullanım karşılaştırması](https://x.com/browser_use/status/2123263050501509123) (by [@browser_use](https://x.com/browser_use))

**Yayıncının değerlendirme kurulumunda tarayıcı karşılaştırmasını ve yürütme maliyetini karşılaştırın.**

Tarayıcı Kullanımı, Neon için Opus 5.5 sonucuna eşit olan %74'lük bir sonuç bildirdi ve GPT-6.2 Sol için %82'ye karşılık geldi.

Bu puanlar yayıncının karşılaştırmasını tanımlar. Maliyet karşılaştırması bu değerlendirme için geçerlidir.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-93-1-348151332c55.jpg" alt="Tarayıcı Kullanım karşılaştırması · 1" width="560">

Type: Benchmark | Date: 2026-11-19

---

<a id="case-94"></a>
### Case 94: [PandaCode'da araç çağrısı hatalarını ölçün](https://x.com/aicodeking/status/2123277076174196882) (by [@aicodeking](https://x.com/aicodeking))

**Eşleşen pencerelerdeki arızaları karşılaştırın ve test kurulumundaki farklılıkları hesaba katın.**

Yazar, bir lansman gecesi penceresi sırasında 9.465 Neon çağrısında 65 başarısız araç çağrısını ölçtü.

Aynı zaman aralığında Neon ve Carbon için oran yuvarlandığında %0,7 oldu. Diğer modellerin çoğunun sonuçları farklı test düzeneklerindeki tüm kayıt dönemini kapsıyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-94-1-95b9a0bbc14d.jpg" alt="PandaCode&#x27;da araç çağrısı hatalarını ölçün · 1" width="560">

Type: Evaluation | Date: 2026-11-19

---

<a id="case-95"></a>
### Case 95: [43 soruluk Plotly veri analizi karşılaştırmasını çalıştırın](https://news.ycombinator.com/item?id=50553968) (by [@chriddyp](https://news.ycombinator.com/user?id=chriddyp))

**Aynı Plotly değerlendirmesinde soru başına doğruluğu, maliyeti ve ortalama süreyi karşılaştırın.**

Plotly'nin düzeltilmiş sonucu, Neon'un 43 yanıttan 43'ünü aldığını ve tüm çalışma için 17,03 USD rapor ettiğini gösteriyor.

Hydrogen da 43 sorunun 43’ünü doğru yanıtladı ve 6,36 USD’ye mal oldu. Plotly, soru başına medyan süreyi Neon için 46 saniye, Hydrogen için 32 saniye olarak bildirdi. Veri analizi test ortamında her model bir kez çalıştırıldı.

[Ek kaynak](https://plotly.com/blog/gemini-4-neon-plotly-data-analytics-bench/)

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-95-1-3c8ca3bdc83b.webp" alt="43 soruluk Plotly veri analizi karşılaştırmasını çalıştırın · 1" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-95-2-477010cdc694.webp" alt="43 soruluk Plotly veri analizi karşılaştırmasını çalıştırın · 2" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-95-3-40967c5923ed.webp" alt="43 soruluk Plotly veri analizi karşılaştırmasını çalıştırın · 3" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="case-105"></a>
### Case 105: [Kodlama modellerini bileşik bir endeksle karşılaştırmak](https://news.ycombinator.com/item?id=50568130) (by [@hn-aarvin](https://news.ycombinator.com/user?id=hn-aarvin))

**Toplam puana göre model seçmeden önce her model için hangi testlerin hesaba katıldığını kontrol edin.**

Yazarın yayımladığı Models Engineering Index tablosunda Gemini 4 Neon, 68,1 puanla 20 kayıt arasında birinci.

Endeks, modelleri farklı kapsamda ölçen açık testleri birleştiriyor. Yazarın beş grafiği puanı, maliyeti veya token kullanımını gösteriyor. Sıra bu tabloya ait.

[Ek kaynak](https://git-aarvin.github.io/mei/)

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/images/case-105-1-5dfd5718e697.png" alt="Kodlama modellerini bileşik bir endeksle karşılaştırmak · 1" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/images/case-105-2-2ef233529798.png" alt="Kodlama modellerini bileşik bir endeksle karşılaştırmak · 2" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/images/case-105-3-fc8054c9f70c.png" alt="Kodlama modellerini bileşik bir endeksle karşılaştırmak · 3" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/images/case-105-4-5bb9486abc97.png" alt="Kodlama modellerini bileşik bir endeksle karşılaştırmak · 4" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-20/images/case-105-5-69e0f22dd548.png" alt="Kodlama modellerini bileşik bir endeksle karşılaştırmak · 5" width="560">

Type: Benchmark | Date: 2026-11-19

---

<a id="case-107"></a>
### Case 107: [İki akıl yürütme düzeyindeki kıyaslama puanlarını karşılaştırma](https://x.com/PawelHuryn/status/2123650600453693460) (by [@PawelHuryn](https://x.com/PawelHuryn))

**Test edilen her düzeyin puanını ve tahmini abonelik maliyetini karşılaştırın.**

Kıyaslamayı yürüten kişi, hata düzeltme görevlerinde Neon'un xhigh ve high sonuçlarını yayımlıyor.

Özgün grafik iki düzeyi karşılaştırıyor. Yazar kendi maliyet tahminini kullanarak xhigh için 105 üzerinden 63, high için 57 puan bildiriyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-107-1-6d411a52a86a.jpg" alt="İki akıl yürütme düzeyindeki kıyaslama puanlarını karşılaştırma · 1" width="560">

Type: Benchmark | Date: 2026-11-20

---

<a id="case-129"></a>
### Case 129: [Astra'ya karşı bildirilen satranç maçını inceleme](https://x.com/Leapofcode/status/2123757501531476294) (by [@Leapofcode](https://x.com/Leapofcode))

**Hamleleri ve token kullanımını bu maçtaki renk dağılımına göre karşılaştırın.**

Yazar, Astra'nın beyaz, Neon'un siyah taşlarla oynadığı bir maçı belgeliyor.

Videoda tahta görülüyor. Üretici Astra'nın kazandığını bildiriyor ve maçta her modelin kullandığı token sayısını veriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-129-1-a9b885b8c116.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-129-1-230174feb89a.jpg" alt="Astra&#x27;ya karşı bildirilen satranç maçını inceleme · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-20

---

<a id="case-134"></a>
### Case 134: [ErdosBench araştırma matematiği sonuçlarını karşılaştırma](https://x.com/prz_chojecki/status/2123782382876602540) (by [@prz_chojecki](https://x.com/prz_chojecki))

**Kıyaslama sırasıyla birlikte not dağılımını inceleyin.**

Kıyaslamanın sorumlusu Neon'u ErdosBench'teki 226 araştırma düzeyinde matematik problemiyle değerlendirdiğini bildiriyor.

Ekli sonuçlarda 3,234 puan ve A, B, C notlarının dağılımı yer alıyor. Veriler bu kıyaslama ve puanlama yöntemine ait.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-134-1-551f173bb536.jpg" alt="ErdosBench araştırma matematiği sonuçlarını karşılaştırma · 1" width="560">

Type: Benchmark | Date: 2026-11-20

---

<a id="case-136"></a>
### Case 136: [FutureSim tahmin sonuçlarını karşılaştırma](https://x.com/nikhilchandak29/status/2123804028312203664) (by [@nikhilchandak29](https://x.com/nikhilchandak29))

**Tahmin sonucunu okurken kıyaslamanın tarihini ve yöntemini dikkate alın.**

Yayıncı Neon'un FutureSim'de en yüksek puanı aldığını bildiriyor ve kıyaslama grafiğini yayımlıyor. Paylaşım, araç çağrılarını ve farklı alanlardaki simülasyon sorularını anlatıyor.

Kıyaslamanın eş yürütücüsü sıralamayı ve görev kapsamını gösteriyor. Yazarın sonucu belgelenen FutureSim kesitine ait.

[Ek kaynak](https://openforecaster.github.io/futuresim/)

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-136-1-52f1bff62ba9.jpg" alt="FutureSim tahmin sonuçlarını karşılaştırma · 1" width="560">

Type: Benchmark | Date: 2026-11-20

---

<a id="case-142"></a>
### Case 142: [Görsel çıktıları BrushArena oylarına göre karşılaştırma](https://x.com/kickingkeys/status/2123826506287939624) (by [@kickingkeys](https://x.com/kickingkeys))

**Sıralamayı bu kıyaslamaya ait bir tercih kesiti olarak değerlendirin.**

Yazar, Neon'un BrushArena'da ilk sıradan giriş yaptığını bildiriyor ve ziyaretçi oylarına dayanan bir kesit sunuyor.

Kaynak belirli bir tarihteki ziyaretçi oyu sıralamasını bildiriyor. Sonucu BrushArena kesitindeki model ve çalışmalarla birlikte yorumlayın.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-142-1-a134e1ddeeac.jpg" alt="Görsel çıktıları BrushArena oylarına göre karşılaştırma · 1" width="560">

Type: Benchmark | Date: 2026-11-20

---

<a id="case-148"></a>
### Case 148: [Modelleri pazarlama görevlerinde değerlendirme](https://x.com/boringmarketer/status/2123843589063008291) (by [@boringmarketer](https://x.com/boringmarketer))

**Sıralamadan genel sonuç çıkarmadan önce yöntemi ve görev bazındaki sonuçları inceleyin.**

Değerlendirmeyi yapan kişi Neon, Opus ve Sol'u pazarlama görevlerinde karşılaştırıyor ve sonuç grafiğini paylaşıyor. Karşılaştırma, değerlendiricinin test koşullarıyla sınırlı.

Yazar, beş laboratuvardan hakemlerin yer aldığı ikili oylama yöntemini açıklıyor. Grafik, değerlendirilen pazarlama görevlerinin sonuçlarını gösteriyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-148-1-9c51ceb178cc.jpg" alt="Modelleri pazarlama görevlerinde değerlendirme · 1" width="560">

Type: Benchmark | Date: 2026-11-20

---

<a id="case-151"></a>
### Case 151: [Modelleri eğitim verisi düzenleyicisi olarak değerlendirme](https://x.com/hyperstition_cc/status/2123877109907288098) (by [@hyperstition_cc](https://x.com/hyperstition_cc))

**Düzenleyicileri değerlendirirken ayrı tutulan test verisindeki doğruluğu ve çalışma süresini karşılaştırın.**

Kıyaslama yazarları Hyper-Intervention'da Neon ve altı başka modeli eğitim yörüngelerinin düzenleyicileri olarak test ediyor.

Yayımlanan grafik, matematik kurulumunda test doğruluğunun oturum boyunca nasıl değiştiğini gösteriyor. Yazarlar yapılandırmayı ve gözlenen sınırlamaları ayrıca açıklıyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-151-1-1842a7df516d.jpg" alt="Modelleri eğitim verisi düzenleyicisi olarak değerlendirme · 1" width="560">

Type: Benchmark | Date: 2026-11-20

---

<a id="case-157"></a>
### Case 157: [Çok ajanlı kodlama ortamlarını değerlendirme](https://x.com/leo_linsky/status/2123894236789739768) (by [@leo_linsky](https://x.com/leo_linsky))

**Puanları ortak ortam kümesi ve değerlendirme koşullarıyla birlikte karşılaştırın.**

Değerlendirici, Neon'u ve birkaç rakip modeli 100 çok ajanlı kodlama ortamında test ettiğini bildiriyor.

Kaynak, değerlendirilen modeller için toplu sonuç tablosu veriyor. Karşılaştırma bu ortamlarla sınırlı.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-157-1-9f4d245131ab.jpg" alt="Çok ajanlı kodlama ortamlarını değerlendirme · 1" width="560">

Type: Benchmark | Date: 2026-11-20

---

<a id="case-161"></a>
### Case 161: [FrontierMemory performansını karşılaştırma](https://x.com/Letta_AI/status/2123910446021530047) (by [@Letta_AI](https://x.com/Letta_AI))

**Sıralamayı kıyaslamadaki bellek görevlerine ait bir sonuç kesiti olarak okuyun.**

Kıyaslamanın sorumlusu Gemini 4 Neon'un FrontierMemory sonucunu paylaşıyor.

Özgün görsel test edilen modelin sırasını belgeliyor. Sıralama, yayımlanmış kıyaslama kesitine ait.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-161-1-0b52f1bd3f05.jpg" alt="FrontierMemory performansını karşılaştırma · 1" width="560">

Type: Benchmark | Date: 2026-11-20

---

<a id="case-167"></a>
### Case 167: [Sayfa ayrıştırma ve tablo düzenini değerlendirme](https://x.com/jerryjliu0/status/2123945742872293505) (by [@jerryjliu0](https://x.com/jerryjliu0))

**Belge ayrıştırıcı seçerken düzen ve tablo metriklerini ayrı ayrı inceleyin.**

ParseBench-2 yayıncısı, Neon'u düşük düşünme düzeyinde başka model sürümleriyle karşılaştırdığını bildiriyor.

Özgün tablo belge ayrıştırma, tablolar ve düzen için ayrı ölçümler verir. Kıyaslama yapılandırmasını ve veri bölünmesini dikkate alın.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-167-1-2fc287ffe70d.jpg" alt="Sayfa ayrıştırma ve tablo düzenini değerlendirme · 1" width="560">

Type: Benchmark | Date: 2026-11-21

---

<a id="case-171"></a>
### Case 171: [CodePilot'taki sekiz sorunun düzeltmelerini karşılaştırma](https://x.com/op7418/status/2123959051126177841) (by [@op7418](https://x.com/op7418))

**Puanları tek modelle yapılan değerlendirme ve kaynak koşullarıyla birlikte okuyun.**

Geliştirici, CodePilot'ta belirlenen sekiz sorunu iki modele düzelttirdi ve değerlendirme için üçüncü bir model kullandı. Kaynak Neon için 8,5, Opus için 9 puan bildiriyor.

Yazar sorunları belirlemek ve iki düzeltme kümesini puanlamak için Fable kullandı. Puanlar bu düzene ve seçilen sekiz soruna ait.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-171-1-371bdf9cfbd4.jpg" alt="CodePilot&#x27;taki sekiz sorunun düzeltmelerini karşılaştırma · 1" width="560">

Type: Evaluation | Date: 2026-11-21

---

<a id="case-175"></a>
### Case 175: [Gözetimsiz çalışmada oturumun sona ermesini inceleme](https://x.com/vipinxtwt/status/2123995317410349467) (by [@vipinxtwt](https://x.com/vipinxtwt))

**Oturum sorununu modelin görevi nasıl yürüttüğünden ayrı değerlendirin.**

Yazar, Neon ile bir Antigravity oturumunun kimlik doğrulama süresi dolana kadar iki saatten uzun çalıştığını bildiriyor. Ekran görüntüsü bu oturumun hatasını belgeliyor.

Görüntü, bildirilen oturumda kimlik doğrulama süresinin dolduğunu gösteriyor. Gözlem Antigravity'deki tek bir gözetimsiz çalışmaya ait.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-175-1-6108a9aa4efc.jpg" alt="Gözetimsiz çalışmada oturumun sona ermesini inceleme · 1" width="560">

Type: Limit | Date: 2026-11-21

---

<a id="case-190"></a>
### Case 190: [OpenCode yapılandırmasında çıkarım hızını karşılaştırma](https://x.com/maksym_andr/status/2124100080152035403) (by [@maksym_andr](https://x.com/maksym_andr))

**Çalıştırma ortamını ve düşünme ayarlarını toplam sıralamayla birlikte okuyun.**

Kıyaslama katılımcısı, InferenceBench'te kaydedilen bir Neon yapılandırmasını sunuyor.

Ekli grafik söz konusu yapılandırmanın sonuçlarını bildiriyor. Bunları kıyaslama ölçümlerinin tanımları ve model ayarlarıyla birlikte yorumlayın.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-190-1-2e1161cc8668.jpg" alt="OpenCode yapılandırmasında çıkarım hızını karşılaştırma · 1" width="560">

Type: Benchmark | Date: 2026-11-21

---

<a id="case-194"></a>
### Case 194: [Antigravity'de önbellek isabet değişimini izleme](https://x.com/leo114119/status/2124119129863209157) (by [@leo114119](https://x.com/leo114119))

**Kota değişikliklerini model kalitesine atfetmeden önce önbellek isabet oranlarını zaman içinde karşılaştırın.**

Yapımcı sonraki paylaşımında önbellek isabet oranını %98,9, daha önceki paylaşımında ise yaklaşık %50 olarak bildiriyor.

Sonraki ekran görüntüsünde mevcut istek için %98,1, birikimli olarak %78,7 görünüyor. Görüntülenen oturuma ait bu değerler paylaşım metnindekilerden farklı.

[Ek kaynak](https://x.com/leo114119/status/2123738543214506324)

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-194-1-24575429840c.png" alt="Antigravity&#x27;de önbellek isabet değişimini izleme · 1" width="560">

Type: Limit | Date: 2026-11-21

---

<a id="case-208"></a>
### Case 208: [Sekiz düğümünü fizik simülasyonu kaydıyla puanlama](https://x.com/li9292/status/2124165078014427440) (by [@li9292](https://x.com/li9292))

**Fizik puanını diğer çıktılarla karşılaştırmadan önce modelin kullanılabilir bir düğüm açıklaması verdiğini kontrol edin.**

Üreticinin KnotBench v0 kaydı dört model için aynı sekiz düğümü görevini gösteriyor. Neon, gösterilen denemede çıkarılabilir bir düğüm açıklaması üretmedi.

Klip, Neon'un simülasyona girmeden L0 düzeyinde kaldığını gösteriyor. Aynı denemede Astra ve Sol L5'e ulaşıyor. Her model için tek gönderim yer alıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-208-1-c8cb041cac46.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-208-1-d3f1f68bdb20.jpg" alt="Sekiz düğümünü fizik simülasyonu kaydıyla puanlama · 1" width="560"></a>

Type: Limit | Date: 2026-11-21

---

<a id="case-218"></a>
### Case 218: [Neon ve Carbon'u FrontierMath'te karşılaştırma](https://x.com/DominikPeters/status/2124251171061981439) (by [@DominikPeters](https://x.com/DominikPeters))

**Puanları yorumlarken bildirilen FrontierMath düzeyini ve kesit tarihini kullanın.**

Yazar belirli bir düzeye ait FrontierMath grafiğine işaret ediyor ve o grafikte Neon'un Carbon'un önünde olduğunu bildiriyor.

Paylaşım belirli bir FrontierMath sonuç grafiğine bağlantı veriyor. Başka matematik görevleriyle kıyaslamadan önce düzeyine ve kapsamına bakın.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-218-1-83c8764a3819.jpg" alt="Neon ve Carbon&#x27;u FrontierMath&#x27;te karşılaştırma · 1" width="560">

Type: Benchmark | Date: 2026-11-21

---

<a id="case-230"></a>
### Case 230: [Ondalık sayı karşılaştırmasında yanıt tarzını inceleme](https://x.com/JamesMalsawm/status/2124359719523332536) (by [@JamesMalsawm](https://x.com/JamesMalsawm))

**Matematiksel doğruluğu ve yanıtın tonunu ayrı ayrı değerlendirin.**

Neon olarak etiketlenen ekran görüntüsü 9,3 ile 9,12'yi karşılaştırıyor ve 9,3'ün daha büyük olduğunu belirtiyor.

Doğru sonuca alaycı bir yanıt eşlik ediyor. Kaynak tek bir etkileşimi belgeliyor ve kısa sorunun tam metnini ekran görüntüsünde veriyor.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-230-1-4aba910e6c2b.jpg" alt="Ondalık sayı karşılaştırmasında yanıt tarzını inceleme · 1" width="560">

Type: Evaluation | Date: 2026-11-22

---

<a id="case-231"></a>
### Case 231: [Ağırlıklı LiveBench 2.0 sonuçlarını karşılaştırma](https://x.com/alexmichael/status/2124364037270253826) (by [@alexmichael](https://x.com/alexmichael))

**Genel puanla model seçmeden önce görev grubu ağırlıklarını ve tek tek puanları inceleyin.**

Paylaşımda, gösterilen LiveBench 2.0 sürümünde Neon'un genel puanı 87,4.

Kıyaslama sahibinin sürüm dosyalarında Long Agentic 2×, Coding ve Design 1,5× ağırlıkla 87,4 sonucu yeniden elde ediliyor. Sıralama, gösterilen sürümü ve değerlendirme düzenini yansıtıyor.

[Ek kaynak](https://livebench.ai/)

[Ek kaynak](https://livebench.ai/data/20261106/table.csv)

[Ek kaynak](https://livebench.ai/data/20261106/categories.json)

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-231-1-cc4b47c2de35.jpg" alt="Ağırlıklı LiveBench 2.0 sonuçlarını karşılaştırma · 1" width="560">

Type: Benchmark | Date: 2026-11-22

---

<a id="case-233"></a>
### Case 233: [Ondalık basamak değerini açıklayan iki yanıtı karşılaştırma](https://x.com/itsvishaltwt/status/2124366238013145441) (by [@itsvishaltwt](https://x.com/itsvishaltwt))

**Akıl yürütme adımını ve sayısal sonucu birbirinden bağımsız kontrol edin.**

Yazar 9,12 ve 9,8'i karşılaştıran aynı soruya verilmiş iki yanıt gösteriyor.

Neon ekran görüntüsü 9,8'in daha büyük olduğunu doğru belirtiyor. Diğer çıktı, 9,8'i 9,80'e çevirmesine rağmen ters sonuca varıyor. İki çıktıyı da yazar yayımladı.

<table>
<tr>
<td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-233-1-3e763f2c2978.jpg" alt="Ondalık basamak değerini açıklayan iki yanıtı karşılaştırma · 1" width="560"></td>
<td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-233-2-a701c521d929.jpg" alt="Ondalık basamak değerini açıklayan iki yanıtı karşılaştırma · 2" width="560"></td>
</tr>
</table>

Type: Evaluation | Date: 2026-11-22

---

<a id="case-237"></a>
### Case 237: [Neon için verilere uyarlanan kıyaslama eğrilerini okuma](https://x.com/AdamHoltererer/status/2124457945983267216) (by [@AdamHoltererer](https://x.com/AdamHoltererer))

**Her eğriyi ve toplu sonuca temel oluşturan kıyaslama kümesini inceleyin.**

Priors yazarı, 45 kıyaslama için ayrı Neon gözlemleri içeren uyum eğrilerini gösteriyor.

Grafik 20 Kasım kesiti için 172,1 değeri ve 0,6 standart hata veriyor. Model başına test edilen en güçlü ayarı kullanıyor.

[Ek kaynak](https://www.mypriors.com/models/gemini-4-neon)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/videos/case-237-1-6b7ce21da511.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/posters/case-237-1-b22d95d7c3d9.jpg" alt="Neon için verilere uyarlanan kıyaslama eğrilerini okuma · 1" width="560"></a>

Type: Benchmark | Date: 2026-11-22

---

<a id="case-239"></a>
### Case 239: [Ezberden çizilen üç SVG logosunu değerlendirme](https://x.com/a__tomala/status/2124463500517113952) (by [@a__tomala](https://x.com/a__tomala))

**Çevrimdışı tek dosyalı SVG isteyin ve geometrilerini özgün logolarla karşılaştırın.**

Üretici, web erişimi kapalı ve terminal çalıştırma açıkken Antigravity'de orta düşünme düzeyindeki Neon'un hazırladığı üç logoyu gösteriyor.

Üretici sonraki paylaşımında Google'ın G harfindeki küçük ve OpenAI simgesindeki daha görünür farkları belirtiyor. Ekran görüntüsünde görevin özgün metni var.

[Ek kaynak](https://x.com/a__tomala/status/2124468291385299120)

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-22-backfill/images/case-239-1-27b3bdb30704.jpg" alt="Ezberden çizilen üç SVG logosunu değerlendirme · 1" width="560">

Type: Evaluation | Date: 2026-11-22

---

<a id="case-244"></a>
### Case 244: [Üç asistanın tek seferlik rastgele sayı yanıtlarını karşılaştırmak](https://news.ycombinator.com/item?id=50600208) (by [@financltravsty](https://news.ycombinator.com/user?id=financltravsty))

**Tekil yanıtları karşılaştırırken istemleri ve ayarları aynen kaydedin.**

Yazarın paylaştığı üç ekran görüntüsünde Gemini 4 Neon Medium, 6 Luna Medium ve Sonnet 5.5 High 47 yanıtını verdi.

Her görüntü bir yanıt gösteriyor. Uygulamalar ve istem metinleri biraz farklı. Yazar, mevcut bir projede yeni Neon oturumu açtığını söylüyor.

**Prompt:**

```
Pick a random numbe
```

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-23/images/case-244-1-cb6ed3fbc4de.png" alt="Üç asistanın tek seferlik rastgele sayı yanıtlarını karşılaştırmak · 1" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-23/images/case-244-2-4b666a2aa98b.png" alt="Üç asistanın tek seferlik rastgele sayı yanıtlarını karşılaştırmak · 2" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-23/images/case-244-3-80fb07a79b19.png" alt="Üç asistanın tek seferlik rastgele sayı yanıtlarını karşılaştırmak · 3" width="560">

Type: Limit | Date: 2026-11-22

---

<a id="case-248"></a>
### Case 248: [Sabit GPU bütçesiyle Polytopia eğitimini karşılaştırın](https://x.com/maxbittker/status/2124694590250693021) (by [@maxbittker](https://x.com/maxbittker))

**Oyun ajanı için eğitim yöntemlerini karşılaştırırken GPU bütçesini sabit tutun.**

Yaklaşık 325 Elo’da grafik Neon için yaklaşık 3 GPU saati, gösterilen en iyi alternatif için yaklaşık 7 saat gösteriyor.

Yazar grafikte 2,3× oranını işaretliyor. Karşılaştırma bu Elo düzeyinde grafiğe alınan Polytopia çalıştırmalarına ait.

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-23/images/case-248-1-350942e64ce6.jpg" alt="Sabit GPU bütçesiyle Polytopia eğitimini karşılaştırın · 1" width="560">

Type: Benchmark | Date: 2026-11-23

---

<a id="case-252"></a>
### Case 252: [Dört modelin 3B halka animasyonlarını karşılaştırın](https://x.com/SPAC89/status/2124760560445030409) (by [@SPAC89](https://x.com/SPAC89))

**Aynı mekanik halkanın dört sürümünü oluşturup hareketin aynı anlarında karşılaştırın.**

Kaynak video, etiketli dört 3B halkanın yan yana açılmasını gösteriyor.

Video etiketleri GLM-5.4 Max, Gemini 4 Neon Extra, Claude Fable 5.2 High ve Claude Opus 5.5 xhigh. Yazarın sıralaması bu gösterime ait.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-23/videos/case-252-1-87957df8ab6f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/daily/2026-11-23/posters/case-252-1-70135862cc61.jpg" alt="Dört modelin 3B halka animasyonlarını karşılaştırın · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-23

---

<a id="related-repositories"></a>
## İlgili depolar

- [Gemini 4 Karbon Kılavuzu ve Kullanım Durumları](https://github.com/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases)
- [Gemini 4 Hidrojenin Kullanım Durumları](https://github.com/Evolink-AI/awesome-gemini-4-hydrogen-use-cases)

<a id="acknowledge"></a>
## 🙏 Teşekkür

Çalışmalarını paylaşan yaratıcılara ve değerlendiricilere teşekkür ederiz.

[@IndependentEco](https://x.com/IndependentEco), [@SamuelAlbanie](https://x.com/SamuelAlbanie), [@seveibar](https://x.com/seveibar), [@kajikent](https://x.com/kajikent), [@theo](https://x.com/theo), [@Lentils80](https://x.com/Lentils80), [@HarshithLucky3](https://x.com/HarshithLucky3), [@AdamHoltererer](https://x.com/AdamHoltererer), [@StatsWire](https://x.com/StatsWire), [@lyraxana](https://x.com/lyraxana), [@xiangning0](https://x.com/xiangning0), [@Angaisb_](https://x.com/Angaisb_), [@cfenghub](https://x.com/cfenghub), [@kickingkeys](https://x.com/kickingkeys), [@Super_Nius](https://x.com/Super_Nius), [@AI_Screening](https://x.com/AI_Screening), [@Mr_Salio](https://x.com/Mr_Salio), [@LuminaBench](https://x.com/LuminaBench), [@notjazii](https://x.com/notjazii), [@jony_palino](https://x.com/jony_palino), [@thebuggeddev](https://x.com/thebuggeddev), [@GeokenAI](https://x.com/GeokenAI), [@LeslieNooteboom](https://x.com/LeslieNooteboom), [@SPAC89](https://x.com/SPAC89), [@agenticjay](https://x.com/agenticjay), [@Google](https://x.com/Google), [@LyalinDotCom](https://x.com/LyalinDotCom), [@fofrAI](https://x.com/fofrAI), [@thehypedotnews](https://x.com/thehypedotnews), [@chetaslua](https://x.com/chetaslua), [@aipulseda1ly](https://x.com/aipulseda1ly), [@jan_volad](https://x.com/jan_volad), [@ai_for_success](https://x.com/ai_for_success), [@abhinavflac](https://x.com/abhinavflac), [@DesignArena](https://x.com/DesignArena), [@ZryMiller](https://x.com/ZryMiller), [@thtbee_](https://x.com/thtbee_), [@op7418](https://x.com/op7418), [@nemumusitocha](https://x.com/nemumusitocha), [@GoogleAI](https://x.com/GoogleAI), [@antigravity](https://x.com/antigravity), [@GlitterPixely](https://x.com/GlitterPixely), [@badboyfoxy](https://x.com/badboyfoxy), [@DeryaTR_](https://x.com/DeryaTR_), [@Google](https://blog.google/), [@Arcadia_Bao](https://x.com/Arcadia_Bao), [@gracepursuits](https://x.com/gracepursuits), [@Msfs2000J](https://x.com/Msfs2000J), [@viticci](https://x.com/viticci), [@tetumemo](https://x.com/tetumemo), [@MichaelLee009](https://x.com/MichaelLee009), [@ValsAI](https://x.com/ValsAI), [@kimmonismus](https://x.com/kimmonismus), [@arena](https://x.com/arena), [@lukaspet](https://x.com/lukaspet), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@andonlabs](https://x.com/andonlabs), [@maxbittker](https://x.com/maxbittker), [@mercor](https://x.com/mercor), [@cursor_ai](https://x.com/cursor_ai), [@elliotarledge](https://x.com/elliotarledge), [@HelloSurgeAI](https://x.com/HelloSurgeAI), [@wenhaocha1](https://x.com/wenhaocha1), [@browser_use](https://x.com/browser_use), [@aicodeking](https://x.com/aicodeking), [@chriddyp](https://news.ycombinator.com/user?id=chriddyp), [@Da7_Tech](https://x.com/Da7_Tech), [@aiiii498](https://x.com/aiiii498), [@teddyaisi](https://x.com/teddyaisi), [@aisearchio](https://x.com/aisearchio), [@petergyang](https://x.com/petergyang), [@alohaproxy](https://x.com/alohaproxy), [@hn-aarvin](https://news.ycombinator.com/user?id=hn-aarvin), [@openclaw](https://x.com/openclaw), [@PawelHuryn](https://x.com/PawelHuryn), [@alexanderchen](https://x.com/alexanderchen), [@majidmanzarpour](https://x.com/majidmanzarpour), [@robinebers](https://x.com/robinebers), [@GOD2FREEX](https://x.com/GOD2FREEX), [@ann_nnng](https://x.com/ann_nnng), [@RainG999](https://x.com/RainG999), [@mspd4100](https://x.com/mspd4100), [@Haleeeemahh](https://x.com/Haleeeemahh), [@anxuanng](https://x.com/anxuanng), [@wenwen11703261](https://x.com/wenwen11703261), [@lucian__03](https://x.com/lucian__03), [@thegenioo](https://x.com/thegenioo), [@BubbleBrain](https://x.com/BubbleBrain), [@poolmoon6](https://x.com/poolmoon6), [@hqmank](https://x.com/hqmank), [@rootport](https://x.com/rootport), [@viktoroddy](https://x.com/viktoroddy), [@HiromitsuTakagi](https://x.com/HiromitsuTakagi), [@SimonT242613](https://x.com/SimonT242613), [@mizugame_22](https://x.com/mizugame_22), [@lemomo_ai](https://x.com/lemomo_ai), [@Leapofcode](https://x.com/Leapofcode), [@karanC_12](https://x.com/karanC_12), [@marcthecreatorr](https://x.com/marcthecreatorr), [@prz_chojecki](https://x.com/prz_chojecki), [@ivanainai](https://x.com/ivanainai), [@nikhilchandak29](https://x.com/nikhilchandak29), [@FiniYang](https://x.com/FiniYang), [@AIMind_Ai](https://x.com/AIMind_Ai), [@AndroidDev](https://x.com/AndroidDev), [@DanielZambrini](https://x.com/DanielZambrini), [@superdoteng](https://x.com/superdoteng), [@filicroval](https://x.com/filicroval), [@boringmarketer](https://x.com/boringmarketer), [@hyperstition_cc](https://x.com/hyperstition_cc), [@eliadele](https://x.com/eliadele), [@DynamicWebPaige](https://x.com/DynamicWebPaige), [@leo_linsky](https://x.com/leo_linsky), [@SamgreyAi](https://x.com/SamgreyAi), [@davis7](https://x.com/davis7), [@Letta_AI](https://x.com/Letta_AI), [@maxt3chno](https://x.com/maxt3chno), [@scottstts](https://x.com/scottstts), [@jerryjliu0](https://x.com/jerryjliu0), [@atakoylanai](https://x.com/atakoylanai), [@liu8in](https://x.com/liu8in), [@KanaWorks_AI](https://x.com/KanaWorks_AI), [@JamesMalsawm](https://x.com/JamesMalsawm), [@likka_ailive](https://x.com/likka_ailive), [@vipinxtwt](https://x.com/vipinxtwt), [@bangbuilds](https://x.com/bangbuilds), [@antiAIvo](https://x.com/antiAIvo), [@ogabezim](https://x.com/ogabezim), [@GoGoFly23](https://x.com/GoGoFly23), [@WrongNebula](https://x.com/WrongNebula), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@risui1012](https://x.com/risui1012), [@niramayo2096](https://x.com/niramayo2096), [@noclipepe](https://x.com/noclipepe), [@csaba_kissi](https://x.com/csaba_kissi), [@maksym_andr](https://x.com/maksym_andr), [@TheDoraaaaaaaa](https://x.com/TheDoraaaaaaaa), [@guilippert_v4](https://x.com/guilippert_v4), [@leo114119](https://x.com/leo114119), [@leaf_sanren](https://x.com/leaf_sanren), [@DrstaOne](https://x.com/DrstaOne), [@blueemi99](https://x.com/blueemi99), [@aug5thmusic](https://x.com/aug5thmusic), [@DeepBlueX0](https://x.com/DeepBlueX0), [@PokeBenchTV](https://x.com/PokeBenchTV), [@rafaelcaricio](https://x.com/rafaelcaricio), [@li9292](https://x.com/li9292), [@GeekCatX](https://x.com/GeekCatX), [@Bhavani_00007](https://x.com/Bhavani_00007), [@studio_yebisu](https://x.com/studio_yebisu), [@EnvolDev](https://x.com/EnvolDev), [@DominikPeters](https://x.com/DominikPeters), [@jake_j_jung](https://x.com/jake_j_jung), [@doboku_works](https://x.com/doboku_works), [@anabology](https://x.com/anabology), [@jacalulu](https://x.com/jacalulu), [@chasen_liao](https://x.com/chasen_liao), [@G33K13765260](https://x.com/G33K13765260), [@alexmichael](https://x.com/alexmichael), [@itsvishaltwt](https://x.com/itsvishaltwt), [@Leviwoyun](https://x.com/Leviwoyun), [@thorstenball](https://x.com/thorstenball), [@a__tomala](https://x.com/a__tomala), [@kinderlayer](https://x.com/kinderlayer), [@fe_yukichi](https://x.com/fe_yukichi), [@financltravsty](https://news.ycombinator.com/user?id=financltravsty), [@venturetwins](https://x.com/venturetwins), [@WichtelArt](https://x.com/WichtelArt), [@ivanleomk](https://x.com/ivanleomk)

*Medya ve üçüncü taraf çalışmaları ilgili hak sahiplerine aittir. Bir kaynağın, kredinin veya medya öğesinin düzeltilmesi gerekiyorsa lütfen bir sayı açın.*
