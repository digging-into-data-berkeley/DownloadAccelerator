Performance Evaluation for Download utilities for book
=======================================================
Utilities: `wget`, `curl`, `aria2`

<pre>

$ python dnld.py --input="src/source_sample.csv" --utility="aria2" --format="djvu"
Parsing src/source_sample.csv to get download urls
Starting Downloads

07/07 23:51:41 [NOTICE] Allocating disk space. Use --file-allocation=none to disable it. See --file-allocation option in man page for more details.

07/07 23:51:41 [NOTICE] Download complete: downloads/aria2//populationschedu533unit_djvu.xml
[DL:2.9MiB UL:0B][#2de575 6.1MiB/8.8MiB(69%)][#ec66b9 2.4MiB/3.0MiB(81%)][#c5f6c1 6.8MiB/20MiB(34%)][#32fb05 4.7MiB/9.1MiB(51%)]
07/07 23:51:49 [NOTICE] Download complete: downloads/aria2//benjaminnoldman00kniggoog_djvu.xml
[DL:3.0MiB UL:0B][#2de575 8.4MiB/8.8MiB(94%)][#c5f6c1 10MiB/20MiB(49%)][#32fb05 7.9MiB/9.1MiB(86%)]
07/07 23:51:52 [NOTICE] Download complete: downloads/aria2//beitrgezurwirth00krgoog_djvu.xml

07/07 23:51:52 [NOTICE] Download complete: downloads/aria2//bulletin16fragoog_djvu.xml
[#c5f6c1 19MiB/20MiB(95%) CN:1 DL:1.1MiB]
07/07 23:51:58 [NOTICE] Download complete: downloads/aria2//bulletin01queegoog_djvu.xml

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
1d5a1d|OK  |    86KiB/s|downloads/aria2//populationschedu533unit_djvu.xml
ec66b9|OK  |   468KiB/s|downloads/aria2//benjaminnoldman00kniggoog_djvu.xml
2de575|OK  |   894KiB/s|downloads/aria2//beitrgezurwirth00krgoog_djvu.xml
32fb05|OK  |   0.9MiB/s|downloads/aria2//bulletin16fragoog_djvu.xml
c5f6c1|OK  |   1.2MiB/s|downloads/aria2//bulletin01queegoog_djvu.xml

Status Legend:
(OK):download completed.


=========> Downloaded in : 16.852747 s


Back in Python

</pre>

## For the whole sample set of 100 books

<pre>
Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
2fd597|OK  |        n/a|downloads/aria2//populationschedu533unit_djvu.xml
7d49b6|ERR |       0B/s|http://www.archive.org/download/princetonprecept00thil/princetonprecept00thil_djvu.xml
50f573|OK  |   417KiB/s|downloads/aria2//benjaminnoldman00kniggoog_djvu.xml
46ed36|OK  |   534KiB/s|downloads/aria2//cfgellertssmmtl01heyegoog_djvu.xml
e4fed2|OK  |   528KiB/s|downloads/aria2//bulletin16fragoog_djvu.xml
553a59|ERR |       0B/s|http://www.archive.org/download/TohfaAhmediaPartIii/TohfaAhmediaPartIii_djvu.xml
e87797|OK  |   425KiB/s|downloads/aria2//choixderapports00lallgoog_djvu.xml
a6bd09|ERR |       0B/s|http://www.archive.org/download/RCIA2011-HW/RCIA2011-HW_djvu.xml
a38bb4|ERR |       0B/s|http://www.archive.org/download/favicon_45/favicon_45_djvu.xml
d77f72|ERR |       0B/s|http://www.archive.org/download/ProvincialDeSeleccionesSub15-Licitacion/ProvincialDeSeleccionesSub15-Licitacion_djvu.xml
2406f3|OK  |   525KiB/s|downloads/aria2//bulletin16musegoog_djvu.xml
549739|OK  |   272KiB/s|downloads/aria2//beitrgezurwirth00krgoog_djvu.xml
33577e|ERR |       0B/s|http://www.archive.org/download/Psiconeurobiologa_en_el_Maltrato_Infantil/Psiconeurobiologa_en_el_Maltrato_Infantil_djvu.xml
728a11|ERR |       0B/s|http://www.archive.org/download/stuffz/stuffz_djvu.xml
b817f5|ERR |       0B/s|http://www.archive.org/download/Sunanenasaisharif.part-03-bangla-visit-alhamdulillah-library.b/Sunanenasaisharif.part-03-bangla-visit-alhamdulillah-library.b_djvu.xml
af7f5a|ERR |       0B/s|http://www.archive.org/download/philtrans06859574/philtrans06859574_djvu.xml
1df274|ERR |       0B/s|http://www.archive.org/download/philtrans06478808/philtrans06478808_djvu.xml
b4637f|ERR |       0B/s|http://www.archive.org/download/philtrans08431301/philtrans08431301_djvu.xml
499435|ERR |       0B/s|http://www.archive.org/download/philtrans08029176/philtrans08029176_djvu.xml
51fcea|ERR |       0B/s|http://www.archive.org/download/TersenyumLyrics/TersenyumLyrics_djvu.xml
3f6876|ERR |       0B/s|http://www.archive.org/download/SteveNote9.7.05.pdf/SteveNote9.7.05.pdf_djvu.xml
6cee86|ERR |       0B/s|http://www.archive.org/download/The_Effect_Of_A_Quart_Of_Water/The_Effect_Of_A_Quart_Of_Water_djvu.xml
c7c2e4|ERR |       0B/s|http://www.archive.org/download/TheFlyingLapEpisode32HungarianGpDebriefWithF1StatisticianSeanKelly/TheFlyingLapEpisode32HungarianGpDebriefWithF1StatisticianSeanKelly_djvu.xml
72d66c|ERR |       0B/s|http://www.archive.org/download/TheHouse/TheHouse_djvu.xml
32f73b|OK  |   555KiB/s|downloads/aria2//bulletin01queegoog_djvu.xml
633586|OK  |   567KiB/s|downloads/aria2//goethesgedichee01viehgoog_djvu.xml
f37f48|ERR |       0B/s|http://www.archive.org/download/SundaySeriesPlanJune24ThruSept2/SundaySeriesPlanJune24ThruSept2_djvu.xml
945cbc|ERR |       0B/s|http://www.archive.org/download/TheMothers/TheMothers_djvu.xml
14d941|OK  |   479KiB/s|downloads/aria2//railroadsfinanc03riplgoog_djvu.xml
ac1cf9|ERR |       0B/s|http://www.archive.org/download/ThePlaysOfHubertHenryDaviesVol1/ThePlaysOfHubertHenryDaviesVol1_djvu.xml
69bdec|ERR |       0B/s|http://www.archive.org/download/The_Radio/The_Radio_djvu.xml
d12732|ERR |       0B/s|http://www.archive.org/download/the_recipes_in_full/the_recipes_in_full_djvu.xml
9d9db4|ERR |       0B/s|http://www.archive.org/download/TheTurquoiseDream/TheTurquoiseDream_djvu.xml
8afa09|ERR |       0B/s|http://www.archive.org/download/TheWelshRabbitAndSammyTheShrew/TheWelshRabbitAndSammyTheShrew_djvu.xml
68457c|ERR |       0B/s|http://www.archive.org/download/tafreegh_659/tafreegh_659_djvu.xml
3cfea6|OK  |   164KiB/s|downloads/aria2//strafrechtsfael00bauegoog_djvu.xml
d5a04b|OK  |   167KiB/s|downloads/aria2//strafrechtsfael02bauegoog_djvu.xml
60606b|ERR |       0B/s|http://www.archive.org/download/tafreghat2002yahoo.com_594/tafreghat2002yahoo.com_594_djvu.xml
8504b5|ERR |       0B/s|http://www.archive.org/download/Tafregh_3amy_30_quran_drhazemShoman_way2allah.com/Tafregh_3amy_30_quran_drhazemShoman_way2allah.com_djvu.xml
c99574|ERR |       0B/s|http://www.archive.org/download/tafreghat2002yahoo.com_582/tafreghat2002yahoo.com_582_djvu.xml
e58a3d|ERR |       0B/s|http://www.archive.org/download/tafreghat2002yahoo.com_742/tafreghat2002yahoo.com_742_djvu.xml
766ac2|ERR |       0B/s|http://www.archive.org/download/Tafsir_10_akheer_UR/Tafsir_10_akheer_UR_djvu.xml
452487|ERR |       0B/s|http://www.archive.org/download/takouime/takouime_djvu.xml
5d7055|ERR |       0B/s|http://www.archive.org/download/Taklif2012/Taklif2012_djvu.xml
f3957c|ERR |       0B/s|http://www.archive.org/download/TalimaDeenRaheyMehboob/TalimaDeenRaheyMehboob_djvu.xml
5c6289|OK  |   7.9KiB/s|downloads/aria2//tangsihwauikwon1038800_djvu.xml
5a1e9b|ERR |       0B/s|http://www.archive.org/download/TargetLetterMay2005/TargetLetterMay2005_djvu.xml
1258f7|OK  |        n/a|downloads/aria2//tangsihwauikwon1028800_djvu.xml
5f17b1|ERR |       0B/s|http://www.archive.org/download/TechnoKid.tk/TechnoKid.tk_djvu.xml
8fd41f|ERR |       0B/s|http://www.archive.org/download/tema1/tema1_djvu.xml
575bde|ERR |       0B/s|http://www.archive.org/download/te_quiero_poema_poem_in_spanish/te_quiero_poema_poem_in_spanish_djvu.xml
c86cd4|ERR |       0B/s|http://www.archive.org/download/tarjama_mulla_umran1/tarjama_mulla_umran1_djvu.xml
d19092|ERR |       0B/s|http://www.archive.org/download/test-3/test-3_djvu.xml
26cf5c|ERR |       0B/s|http://www.archive.org/download/TesteJava/TesteJava_djvu.xml
f0b132|ERR |       0B/s|http://www.archive.org/download/TestOnReadingWithCall_704/TestOnReadingWithCall_704_djvu.xml
e0cc67|ERR |       0B/s|http://www.archive.org/download/TestOSMTiles001/TestOSMTiles001_djvu.xml
da8093|ERR |       0B/s|http://www.archive.org/download/tetouan-mai2011.pdf/tetouan-mai2011.pdf_djvu.xml
71bf96|ERR |       0B/s|http://www.archive.org/download/thebeat1333/thebeat1333_djvu.xml
21d3ce|OK  |   604KiB/s|downloads/aria2//travelsanirishg04moorgoog_djvu.xml
00a953|ERR |       0B/s|http://www.archive.org/download/PermissionToFail/PermissionToFail_djvu.xml
fec702|ERR |       0B/s|http://www.archive.org/download/diacacahtm/diacacahtm_djvu.xml
aed5a9|ERR |       0B/s|http://www.archive.org/download/RemixingOerAGuideToLicenseCompatibility/RemixingOerAGuideToLicenseCompatibility_djvu.xml
b098ad|ERR |       0B/s|http://www.archive.org/download/PeteOlanskiObituary/PeteOlanskiObituary_djvu.xml
843cad|ERR |       0B/s|http://www.archive.org/download/RepresentativeBritishDramas/RepresentativeBritishDramas_djvu.xml
c0813c|OK  |   178KiB/s|downloads/aria2//christoforusblt00freygoog_djvu.xml
328e46|OK  |   428KiB/s|downloads/aria2//talesmylandlord31scotgoog_djvu.xml
848ec3|ERR |       0B/s|http://www.archive.org/download/ScholarlyElectronicPublishingBibliographyVersion51/ScholarlyElectronicPublishingBibliographyVersion51_djvu.xml
69a1e3|ERR |       0B/s|http://www.archive.org/download/ScholarlyElectronicPublishingBibliographyVersion64/ScholarlyElectronicPublishingBibliographyVersion64_djvu.xml
9ece71|ERR |       0B/s|http://www.archive.org/download/ScholarlyElectronicPublishingBibliographyVersion66/ScholarlyElectronicPublishingBibliographyVersion66_djvu.xml
9f07cf|ERR |       0B/s|http://www.archive.org/download/ScholarlyElectronicPublishingBibliographyVersion67/ScholarlyElectronicPublishingBibliographyVersion67_djvu.xml
4da3b2|OK  |   661KiB/s|downloads/aria2//sborniktovarish00unkngoog_djvu.xml
92f5d2|OK  |   350KiB/s|downloads/aria2//textbookselecti00frangoog_djvu.xml
0e7718|OK  |   605KiB/s|downloads/aria2//reportsunitedst06kniggoog_djvu.xml
14814b|OK  |   156KiB/s|downloads/aria2//theirpilgrimage00warngoog_djvu.xml
896696|ERR |       0B/s|http://www.archive.org/download/salahtm/salahtm_djvu.xml
9d0692|ERR |       0B/s|http://www.archive.org/download/SalaMare-Arhiva1/SalaMare-Arhiva1_djvu.xml
2b5088|ERR |       0B/s|http://www.archive.org/download/salgadohtm/salgadohtm_djvu.xml
57e132|OK  |   5.7KiB/s|downloads/aria2//samgyongsasotaej49asam_djvu.xml
0ded23|OK  |   9.6KiB/s|downloads/aria2//samgyongsasotaej50asam_djvu.xml
35b6f9|OK  |   292KiB/s|downloads/aria2//bulletin41minegoog_djvu.xml
83ba20|OK  |   333KiB/s|downloads/aria2//transactionsame76socigoog_djvu.xml
3f0226|ERR |       0B/s|http://www.archive.org/download/teqdar.ala.a3dabo/teqdar.ala.a3dabo_djvu.xml
1b41ec|ERR |       0B/s|http://www.archive.org/download/SanfordStaabAnIntroductiontoEcconomicsandthenatureofmoneyandcredit/SanfordStaabAnIntroductiontoEcconomicsandthenatureofmoneyandcredit_djvu.xml
eb2a08|ERR |       0B/s|http://www.archive.org/download/SanMateoCounty-PlanningBuilding-BuildingPermitsAndInspections-/SanMateoCounty-PlanningBuilding-BuildingPermitsAndInspections-_djvu.xml
9d107e|ERR |       0B/s|http://www.archive.org/download/santana2htm/santana2htm_djvu.xml
e288df|ERR |       0B/s|http://www.archive.org/download/santanahtm/santanahtm_djvu.xml
d90f5f|OK  |   557KiB/s|downloads/aria2//samladearbeten06blangoog_djvu.xml
0cd7f2|ERR |       0B/s|http://www.archive.org/download/test_html_page/test_html_page_djvu.xml
fe093c|ERR |       0B/s|http://www.archive.org/download/test_php_execute/test_php_execute_djvu.xml
118eca|ERR |       0B/s|http://www.archive.org/download/Satwanti/Satwanti_djvu.xml
5996bb|ERR |       0B/s|http://www.archive.org/download/RisalaAkheekhUlAkheekha/RisalaAkheekhUlAkheekha_djvu.xml
97d6be|ERR |       0B/s|http://www.archive.org/download/saoud/saoud_djvu.xml
93f7f8|OK  |   155KiB/s|downloads/aria2//bulletindelasoc03limogoog_djvu.xml
c1fd97|OK  |   260KiB/s|downloads/aria2//schillerundgoei05braugoog_djvu.xml
97f5e3|OK  |   613KiB/s|downloads/aria2//sciencesociale00unkngoog_djvu.xml
5b569d|OK  |   279KiB/s|downloads/aria2//temptation00clifgoog_djvu.xml
8a9c85|OK  |   637KiB/s|downloads/aria2//treatypeacewith05relagoog_djvu.xml
78ba98|OK  |   241KiB/s|downloads/aria2//sammlungderneue01salogoog_djvu.xml
c605c6|OK  |   243KiB/s|downloads/aria2//schriftendesver06berlgoog_djvu.xml
1e1ff0|OK  |   546KiB/s|downloads/aria2//reportsallcases01casegoog_djvu.xml

Status Legend:
(OK):download completed.(ERR):error occurred.

aria2 will resume download if the transfer is restarted.
If there are any errors, then see the log file. See '-l' option in help/man page for details.


=========> Downloaded in : 114.021801 s


Back in Python
</pre>

## `WGET` statistics

    FINISHED --2013-07-08 00:22:13--
    Total wall clock time: 5m 39s
    Downloaded: 34 files, 319M in 5m 3s (1.05 MB/s)
    =========> Downloaded in : 339.129284 s


## SALT Server disk output
<code>
    -bash-4.1$ df -h
</code>

    Filesystem            Size  Used Avail Use% Mounted on
    /dev/mapper/vg01-root
                           79G  3.1G   72G   5% /
    tmpfs                  24G     0   24G   0% /dev/shm
    /dev/mapper/vg01-salt
                          353G  200G  135G  60% /SALT/salt_local
    /dev/sda1             504M   38M  441M   8% /boot
    /dev/mapper/vg01-tmp 1008M   61M  897M   7% /tmp
    /dev/mapper/vg01-var  4.0G  324M  3.5G   9% /var
    /dev/mapper/vg01-varlib
                          7.9G  305M  7.2G   4% /var/lib
    /dev/mapper/vg01-varlog
                           12G  205M   12G   2% /var/log
    dock2-kure:/vol/sata1/home
                           35T  7.9T   27T  23% /nas02/home
    rc-gridscaler-i.its.unc.edu:/gs1/nfsexport/
                           42T   31T   12T  73% /netscr
    dock2-kure:/vol/sata1/apps
                           35T  7.9T   27T  23% /nas02/apps
    dock2-kure:/vol/sata1/data
                           35T  7.9T   27T  23% /nas02/data
    dock2-kure:/vol/sata2/salt
                           50G     0   50G   0% /SALT/salt_vol

## Book Size Statistics
<code>
    $ python filestats.py --dir="downloads/aria2/" --type="xml"
</code>

    beitrgezurwirth00krgoog_djvu.xml       9319262
    benjaminnoldman00kniggoog_djvu.xml     3151855
    bulletin01queegoog_djvu.xml           21216689
    bulletin16fragoog_djvu.xml             9601477
    bulletin16musegoog_djvu.xml           17590040
    bulletin41minegoog_djvu.xml           21130705
    bulletindelasoc03limogoog_djvu.xml    12957926
    cfgellertssmmtl01heyegoog_djvu.xml     3760495
    choixderapports00lallgoog_djvu.xml    11022941
    christoforusblt00freygoog_djvu.xml     8300111
    goethesgedichee01viehgoog_djvu.xml     5652880
    populationschedu533unit_djvu.xml            89
    railroadsfinanc03riplgoog_djvu.xml    12469989
    reportsallcases01casegoog_djvu.xml    34926467
    reportsunitedst06kniggoog_djvu.xml    12181795
    samgyongsasotaej49asam_djvu.xml             89
    samgyongsasotaej50asam_djvu.xml             89
    samladearbeten06blangoog_djvu.xml      6031871
    sammlungderneue01salogoog_djvu.xml     8946053
    sborniktovarish00unkngoog_djvu.xml     9305122
    schillerundgoei05braugoog_djvu.xml     7533035
    schriftendesver06berlgoog_djvu.xml    13401034
    sciencesociale00unkngoog_djvu.xml     12207825
    strafrechtsfael00bauegoog_djvu.xml     7661140
    strafrechtsfael02bauegoog_djvu.xml     7775676
    talesmylandlord31scotgoog_djvu.xml     3229349
    tangsihwauikwon1028800_djvu.xml             89
    tangsihwauikwon1038800_djvu.xml             89
    temptation00clifgoog_djvu.xml          6081602
    textbookselecti00frangoog_djvu.xml     1293375
    theirpilgrimage00warngoog_djvu.xml     5060260
    transactionsame76socigoog_djvu.xml    14863998
    travelsanirishg04moorgoog_djvu.xml     7570734
    treatypeacewith05relagoog_djvu.xml    39761199
    _______________________________________________________________________________
    Description:
    count          34.000000
    mean      9823686.764706
    std       9017573.197743
    min            89.000000
    25%       4085436.250000
    50%       8037893.500000
    75%      12404448.000000
    max      39761199.000000
    _______________________________________________________________________________
    Median File Size: 8037893.500000
    Total File Size: 334005350.000000


## Wget for 1000 files
    2013-07-08 03:21:37 (7.07 KB/s) - ‘passengercrewlis3253unit_djvu.xml’ saved [89/89]
    FINISHED --2013-07-08 03:21:37--
    Total wall clock time: 23m 51s
    Downloaded: 517 files, 2.8G in 20m 24s (2.30 MB/s)
    =========> Downloaded in : 1431.391540 s
    Back in Python


## aria2 1000 downloads

    c88701|ERR |       0B/s|http://www.archive.org/download/philtrans06478808/philtrans06478808_djvu.xml
    a7c06a|ERR |       0B/s|http://www.archive.org/download/philtrans06859574/philtrans06859574_djvu.xml
    1770d0|ERR |       0B/s|http://www.archive.org/download/philtrans08029176/philtrans08029176_djvu.xml
    24904a|ERR |       0B/s|http://www.archive.org/download/philtrans08431301/philtrans08431301_djvu.xml
    ec681e|ERR |       0B/s|http://www.archive.org/download/TersenyumLyrics/TersenyumLyrics_djvu.xml
    56c11a|ERR |       0B/s|http://www.archive.org/download/SteveNote9.7.05.pdf/SteveNote9.7.05.pdf_djvu.xml
    a372c0|OK  |   727KiB/s|downloads/aria2//christoforusblt00freygoog_djvu.xml
    f9c0f0|ERR |       0B/s|http://www.archive.org/download/The_Effect_Of_A_Quart_Of_Water/The_Effect_Of_A_Quart_Of_Water_djvu.xml
    d166f2|ERR |       0B/s|http://www.archive.org/download/TheFlyingLapEpisode32HungarianGpDebriefWithF1StatisticianSeanKelly/TheFlyingLapEpisode32HungarianGpDebriefWithF1StatisticianSeanKelly_djvu.xml
    d878f9|ERR |       0B/s|http://www.archive.org/download/TheHouse/TheHouse_djvu.xml
    2d84dd|OK  |   667KiB/s|downloads/aria2//bulletin16musegoog_djvu.xml
    340f56|OK  |   735KiB/s|downloads/aria2//bulletin01queegoog_djvu.xml
    b40df3|ERR |       0B/s|http://www.archive.org/download/SundaySeriesPlanJune24ThruSept2/SundaySeriesPlanJune24ThruSept2_djvu.xml
    fba76f|ERR |       0B/s|http://www.archive.org/download/TheMothers/TheMothers_djvu.xml
    af734b|ERR |       0B/s|http://www.archive.org/download/ThePlaysOfHubertHenryDaviesVol1/ThePlaysOfHubertHenryDaviesVol1_djvu.xml
    beeb72|ERR |       0B/s|http://www.archive.org/download/The_Radio/The_Radio_djvu.xml
    ad97f1|ERR |       0B/s|http://www.archive.org/download/the_recipes_in_full/the_recipes_in_full_djvu.xml
    243f1c|ERR |       0B/s|http://www.archive.org/download/TheTurquoiseDream/TheTurquoiseDream_djvu.xml
    8cc94a|ERR |       0B/s|http://www.archive.org/download/TheWelshRabbitAndSammyTheShrew/TheWelshRabbitAndSammyTheShrew_djvu.xml
    aa65d6|OK  |   742KiB/s|downloads/aria2//theirpilgrimage00warngoog_djvu.xml
    3a3552|ERR |       0B/s|http://www.archive.org/download/tafreegh_659/tafreegh_659_djvu.xml
    9684c9|ERR |       0B/s|http://www.archive.org/download/Tafregh_3amy_30_quran_drhazemShoman_way2allah.com/Tafregh_3amy_30_quran_drhazemShoman_way2allah.com_djvu.xml
    fb67c1|ERR |       0B/s|http://www.archive.org/download/tafreghat2002yahoo.com_582/tafreghat2002yahoo.com_582_djvu.xml
    8e7b40|ERR |       0B/s|http://www.archive.org/download/tafreghat2002yahoo.com_594/tafreghat2002yahoo.com_594_djvu.xml
    8faae9|OK  |   358KiB/s|downloads/aria2//goethesgedichee01viehgoog_djvu.xml
    11ea6a|ERR |       0B/s|http://www.archive.org/download/tafreghat2002yahoo.com_742/tafreghat2002yahoo.com_742_djvu.xml
    478134|ERR |       0B/s|http://www.archive.org/download/Tafsir_10_akheer_UR/Tafsir_10_akheer_UR_djvu.xml
    092471|ERR |       0B/s|http://www.archive.org/download/Taklif2012/Taklif2012_djvu.xml
    6adcc2|ERR |       0B/s|http://www.archive.org/download/takouime/takouime_djvu.xml
    ddc921|ERR |       0B/s|http://www.archive.org/download/TalimaDeenRaheyMehboob/TalimaDeenRaheyMehboob_djvu.xml
    24dc99|OK  |        n/a|downloads/aria2//tangsihwauikwon1028800_djvu.xml
    4bd04a|OK  |        n/a|downloads/aria2//tangsihwauikwon1038800_djvu.xml
    de4749|ERR |       0B/s|http://www.archive.org/download/TargetLetterMay2005/TargetLetterMay2005_djvu.xml
    6a903d|ERR |       0B/s|http://www.archive.org/download/tarjama_mulla_umran1/tarjama_mulla_umran1_djvu.xml
    23ee6f|ERR |       0B/s|http://www.archive.org/download/TechnoKid.tk/TechnoKid.tk_djvu.xml
    0b6db7|ERR |       0B/s|http://www.archive.org/download/tema1/tema1_djvu.xml
    b520ed|ERR |       0B/s|http://www.archive.org/download/te_quiero_poema_poem_in_spanish/te_quiero_poema_poem_in_spanish_djvu.xml
    dc1085|ERR |       0B/s|http://www.archive.org/download/test-3/test-3_djvu.xml
    eb00ff|ERR |       0B/s|http://www.archive.org/download/TesteJava/TesteJava_djvu.xml
    e9e2f3|ERR |       0B/s|http://www.archive.org/download/TestOnReadingWithCall_704/TestOnReadingWithCall_704_djvu.xml
    3899d1|ERR |       0B/s|http://www.archive.org/download/TestOSMTiles001/TestOSMTiles001_djvu.xml
    06b9b9|ERR |       0B/s|http://www.archive.org/download/tetouan-mai2011.pdf/tetouan-mai2011.pdf_djvu.xml
    495ec4|ERR |       0B/s|http://www.archive.org/download/thebeat1333/thebeat1333_djvu.xml
    441f55|OK  |   900KiB/s|downloads/aria2//travelsanirishg04moorgoog_djvu.xml
    49485b|ERR |       0B/s|http://www.archive.org/download/diacacahtm/diacacahtm_djvu.xml
    301717|ERR |       0B/s|http://www.archive.org/download/PermissionToFail/PermissionToFail_djvu.xml
    1c30c9|ERR |       0B/s|http://www.archive.org/download/PeteOlanskiObituary/PeteOlanskiObituary_djvu.xml
    7531cd|ERR |       0B/s|http://www.archive.org/download/RemixingOerAGuideToLicenseCompatibility/RemixingOerAGuideToLicenseCompatibility_djvu.xml
    e4f78c|OK  |   900KiB/s|downloads/aria2//talesmylandlord31scotgoog_djvu.xml
    fb1a8a|OK  |   266KiB/s|downloads/aria2//bulletin16fragoog_djvu.xml
    a2414e|ERR |       0B/s|http://www.archive.org/download/RepresentativeBritishDramas/RepresentativeBritishDramas_djvu.xml
    a6efd2|OK  |   248KiB/s|downloads/aria2//beitrgezurwirth00krgoog_djvu.xml
    6f1c49|ERR |       0B/s|http://www.archive.org/download/ScholarlyElectronicPublishingBibliographyVersion51/ScholarlyElectronicPublishingBibliographyVersion51_djvu.xml
    2cd293|ERR |       0B/s|http://www.archive.org/download/ScholarlyElectronicPublishingBibliographyVersion64/ScholarlyElectronicPublishingBibliographyVersion64_djvu.xml
    49f79e|ERR |       0B/s|http://www.archive.org/download/ScholarlyElectronicPublishingBibliographyVersion66/ScholarlyElectronicPublishingBibliographyVersion66_djvu.xml
    4753e2|ERR |       0B/s|http://www.archive.org/download/ScholarlyElectronicPublishingBibliographyVersion67/ScholarlyElectronicPublishingBibliographyVersion67_djvu.xml
    aaf08d|OK  |   869KiB/s|downloads/aria2//transactionsame76socigoog_djvu.xml
    3dcd94|OK  |   1.0MiB/s|downloads/aria2//textbookselecti00frangoog_djvu.xml
    3c8fb8|OK  |   0.9MiB/s|downloads/aria2//schillerundgoei05braugoog_djvu.xml
    67942c|ERR |       0B/s|http://www.archive.org/download/salahtm/salahtm_djvu.xml
    ef191a|ERR |       0B/s|http://www.archive.org/download/SalaMare-Arhiva1/SalaMare-Arhiva1_djvu.xml
    c86a9b|ERR |       0B/s|http://www.archive.org/download/salgadohtm/salgadohtm_djvu.xml
    cb9612|OK  |   838KiB/s|downloads/aria2//sborniktovarish00unkngoog_djvu.xml
    46f8ec|OK  |        n/a|downloads/aria2//samgyongsasotaej49asam_djvu.xml
    c1667b|OK  |   7.2KiB/s|downloads/aria2//samgyongsasotaej50asam_djvu.xml
    e370c8|OK  |   840KiB/s|downloads/aria2//temptation00clifgoog_djvu.xml
    550862|OK  |   311KiB/s|downloads/aria2//railroadsfinanc03riplgoog_djvu.xml
    2b0127|ERR |       0B/s|http://www.archive.org/download/teqdar.ala.a3dabo/teqdar.ala.a3dabo_djvu.xml
    97b2c5|ERR |       0B/s|http://www.archive.org/download/SanfordStaabAnIntroductiontoEcconomicsandthenatureofmoneyandcredit/SanfordStaabAnIntroductiontoEcconomicsandthenatureofmoneyandcredit_djvu.xml
    502481|ERR |       0B/s|http://www.archive.org/download/SanMateoCounty-PlanningBuilding-BuildingPermitsAndInspections-/SanMateoCounty-PlanningBuilding-BuildingPermitsAndInspections-_djvu.xml
    efe2e3|ERR |       0B/s|http://www.archive.org/download/santana2htm/santana2htm_djvu.xml
    545c21|ERR |       0B/s|http://www.archive.org/download/santanahtm/santanahtm_djvu.xml
    d90710|ERR |       0B/s|http://www.archive.org/download/saoud/saoud_djvu.xml
    a29cd3|ERR |       0B/s|http://www.archive.org/download/test_html_page/test_html_page_djvu.xml
    ecd9c7|ERR |       0B/s|http://www.archive.org/download/test_php_execute/test_php_execute_djvu.xml
    51f6b6|ERR |       0B/s|http://www.archive.org/download/Satwanti/Satwanti_djvu.xml
    f0a8e9|ERR |       0B/s|http://www.archive.org/download/RisalaAkheekhUlAkheekha/RisalaAkheekhUlAkheekha_djvu.xml
    ca002a|OK  |   821KiB/s|downloads/aria2//schriftendesver06berlgoog_djvu.xml
    b11dd0|ERR |       0B/s|http://www.archive.org/download/robertinlibrarylendingmaryland2011a/robertinlibrarylendingmaryland2011a_djvu.xml
    7c41f3|ERR |       0B/s|http://www.archive.org/download/risohtm/risohtm_djvu.xml
    180b25|ERR |       0B/s|http://www.archive.org/download/tanseq/tanseq_djvu.xml
    9a5c48|ERR |       0B/s|http://www.archive.org/download/tarbiapress-echelle9-bayan12.pdf/tarbiapress-echelle9-bayan12.pdf_djvu.xml
    95d745|OK  |   9.6KiB/s|downloads/aria2//passportapplicat537unit_djvu.xml
    11d394|OK  |    10KiB/s|downloads/aria2//passportapplicat550unit_djvu.xml
    587ec7|OK  |   6.6KiB/s|downloads/aria2//passportapplicat554unit_djvu.xml
    beae6b|OK  |   7.9KiB/s|downloads/aria2//passportapplicat571unit_djvu.xml
    6658d7|OK  |   6.6KiB/s|downloads/aria2//passportapplicat577unit_djvu.xml
    d6153d|OK  |    14KiB/s|downloads/aria2//passportapplicat578unit_djvu.xml
    279025|OK  |   3.1KiB/s|downloads/aria2//passportapplicat580unit_djvu.xml
    9fe3f8|OK  |    21KiB/s|downloads/aria2//passportapplicat581unit_djvu.xml
    4c02a8|OK  |   2.5KiB/s|downloads/aria2//passportapplicat517unit_djvu.xml
    7e9567|OK  |    14KiB/s|downloads/aria2//passportapplicat586unit_djvu.xml
    dd442d|OK  |   5.4KiB/s|downloads/aria2//passportapplicat587unit_djvu.xml
    d2aa82|OK  |   5.1KiB/s|downloads/aria2//passportapplicat588unit_djvu.xml
    54f37b|OK  |   9.6KiB/s|downloads/aria2//passportapplicat592unit_djvu.xml
    aa2864|OK  |        n/a|downloads/aria2//passportapplicat582unit_djvu.xml
    55ad83|OK  |   4.5KiB/s|downloads/aria2//passportapplicat593unit_djvu.xml
    e64992|OK  |    43KiB/s|downloads/aria2//passportapplicat595unit_djvu.xml
    e91d3a|OK  |   8.6KiB/s|downloads/aria2//passportapplicat607unit_djvu.xml
    b52f78|OK  |   6.6KiB/s|downloads/aria2//passportapplicat614unit_djvu.xml
    07826a|OK  |   7.2KiB/s|downloads/aria2//passportapplicat616unit_djvu.xml
    5e2dc3|OK  |    28KiB/s|downloads/aria2//passportapplicat619unit_djvu.xml
    9e1fd4|OK  |   7.2KiB/s|downloads/aria2//passportapplicat620unit_djvu.xml
    5b8136|OK  |    28KiB/s|downloads/aria2//passportapplicat623unit_djvu.xml
    c4025b|OK  |        n/a|downloads/aria2//passportapplicat621unit_djvu.xml
    9dce14|OK  |    21KiB/s|downloads/aria2//passportapplicat628unit_djvu.xml
    2b33f4|OK  |    10KiB/s|downloads/aria2//passportapplicat635unit_djvu.xml
    7bcd09|OK  |    10KiB/s|downloads/aria2//passportapplicat638unit_djvu.xml
    157ae5|OK  |   7.9KiB/s|downloads/aria2//passportapplicat639unit_djvu.xml
    bef873|OK  |   4.8KiB/s|downloads/aria2//passportapplicat630unit_djvu.xml
    d27ee8|OK  |    21KiB/s|downloads/aria2//passportapplicat640unit_djvu.xml
    c86d2c|OK  |    17KiB/s|downloads/aria2//passportapplicat644unit_djvu.xml
    638432|OK  |   5.1KiB/s|downloads/aria2//passportapplicat645unit_djvu.xml
    e1f9f2|OK  |   1.1MiB/s|downloads/aria2//sammlungderneue01salogoog_djvu.xml
    b48e15|OK  |     399B/s|downloads/aria2//passportapplicat641unit_djvu.xml
    17b2cb|OK  |   2.8KiB/s|downloads/aria2//passportapplicat657unit_djvu.xml
    b9bb99|OK  |   9.6KiB/s|downloads/aria2//passportapplicat658unit_djvu.xml
    b0c243|OK  |    86KiB/s|downloads/aria2//passportapplicat684unit_djvu.xml
    44c55b|ERR |       0B/s|http://www.archive.org/download/PaulJ.MckenzieObituary_726/PaulJ.MckenzieObituary_726_djvu.xml
    21bf3c|ERR |       0B/s|http://www.archive.org/download/PaulKeathObituary/PaulKeathObituary_djvu.xml
    30027b|ERR |       0B/s|http://www.archive.org/download/PennsylvaniaBuildingAndZoningLawsAnAlleghenyCountyAppraisal/PennsylvaniaBuildingAndZoningLawsAnAlleghenyCountyAppraisal_djvu.xml
    9e6f59|ERR |       0B/s|http://www.archive.org/download/SapOpcionAltaGama/SapOpcionAltaGama_djvu.xml
    06f02f|ERR |       0B/s|http://www.archive.org/download/PedroHuffprimeirostextos/PedroHuffprimeirostextos_djvu.xml
    477fff|ERR |       0B/s|http://www.archive.org/download/Script_353/Script_353_djvu.xml
    0d7840|ERR |       0B/s|http://www.archive.org/download/sdfdfdsaas5/sdfdfdsaas5_djvu.xml
    231c13|ERR |       0B/s|http://www.archive.org/download/gov.uscourts.azb.549601/gov.uscourts.azb.549601_djvu.xml
    b05329|ERR |       0B/s|http://www.archive.org/download/DasEstatisticasDeCorAoEstatudoDasRacas/DasEstatisticasDeCorAoEstatudoDasRacas_djvu.xml
    25a541|OK  |   436KiB/s|downloads/aria2//reportsunitedst06kniggoog_djvu.xml
    e26093|OK  |   394KiB/s|downloads/aria2//samladearbeten06blangoog_djvu.xml
    07fd52|OK  |   301KiB/s|downloads/aria2//bulletin41minegoog_djvu.xml
    a286c5|OK  |   537KiB/s|downloads/aria2//peersorpeopleho00steagoog_djvu.xml
    87021a|OK  |   417KiB/s|downloads/aria2//sciencesociale00unkngoog_djvu.xml
    747f2d|OK  |   873KiB/s|downloads/aria2//dieteutschenins00stegoog_djvu.xml
    9becfa|OK  |   1.0MiB/s|downloads/aria2//scottsnewreport02chamgoog_djvu.xml
    4f1250|OK  |   0.9MiB/s|downloads/aria2//diewerkedertrou00mahngoog_djvu.xml
    67c709|OK  |   240KiB/s|downloads/aria2//dieschottischen00gembgoog_djvu.xml
    2b80e6|OK  |   133KiB/s|downloads/aria2//choixderapports00lallgoog_djvu.xml
    2afedc|OK  |   714KiB/s|downloads/aria2//dieverfassungun11prusgoog_djvu.xml
    6dbbf5|OK  |   506KiB/s|downloads/aria2//dieevangelische01nebegoog_djvu.xml
    c3c062|OK  |   648KiB/s|downloads/aria2//duchristianisme00librgoog_djvu.xml
    b3ccca|OK  |   252KiB/s|downloads/aria2//productivefeedi00wilhgoog_djvu.xml
    ee2833|ERR |       0B/s|http://www.archive.org/download/ebert/ebert_djvu.xml
    990eaa|ERR |       0B/s|http://www.archive.org/download/proibirhtm/proibirhtm_djvu.xml
    d4a19d|ERR |       0B/s|http://www.archive.org/download/ProjectPatmos-First5Minutes/ProjectPatmos-First5Minutes_djvu.xml
    6ca68f|ERR |       0B/s|http://www.archive.org/download/ProjectQuranBacaquran.tk/ProjectQuranBacaquran.tk_djvu.xml
    9f5f30|ERR |       0B/s|http://www.archive.org/download/ProjetDeLegliseBaptisteDeLevangileDeValDor/ProjetDeLegliseBaptisteDeLevangileDeValDor_djvu.xml
    b2796c|OK  |   719KiB/s|downloads/aria2//dublinjournalme46unkngoog_djvu.xml
    4b105f|OK  |   734KiB/s|downloads/aria2//droitcivilinter12laurgoog_djvu.xml
    22054f|OK  |   346KiB/s|downloads/aria2//ebbandflow01ebbgoog_djvu.xml
    fd2158|ERR |       0B/s|http://www.archive.org/download/Resurrection/Resurrection_djvu.xml
    faa61c|ERR |       0B/s|http://www.archive.org/download/Revista_Agricola_1872-14/Revista_Agricola_1872-14_djvu.xml
    63ad21|ERR |       0B/s|http://www.archive.org/download/t7P2a0c/t7P2a0c_djvu.xml
    0061e1|ERR |       0B/s|http://www.archive.org/download/tafreghat20022YAHOO.COM/tafreghat20022YAHOO.COM_djvu.xml
    144089|ERR |       0B/s|http://www.archive.org/download/tafreghat2002yahoo.com_1275/tafreghat2002yahoo.com_1275_djvu.xml
    bd8b52|ERR |       0B/s|http://www.archive.org/download/tafreghat2002yahoo.com_1036/tafreghat2002yahoo.com_1036_djvu.xml
    b836df|ERR |       0B/s|http://www.archive.org/download/tafreghat2002yahoo.com_347/tafreghat2002yahoo.com_347_djvu.xml
    f28b40|ERR |       0B/s|http://www.archive.org/download/tafreghat2002yahoo.com_381/tafreghat2002yahoo.com_381_djvu.xml
    099656|ERR |       0B/s|http://www.archive.org/download/tafreghat2002yahoo.com_515/tafreghat2002yahoo.com_515_djvu.xml
    00592c|ERR |       0B/s|http://www.archive.org/download/tafreghat2002yahoo.com_781/tafreghat2002yahoo.com_781_djvu.xml
    bf1d6d|ERR |       0B/s|http://www.archive.org/download/RewawatSakhenah.zip/RewawatSakhenah.zip_djvu.xml
    1d0547|OK  |   578KiB/s|downloads/aria2//projetsdeprnesp02grisgoog_djvu.xml
    aa78e3|ERR |       0B/s|http://www.archive.org/download/tahthibe-1_715/tahthibe-1_715_djvu.xml
    ccd59d|ERR |       0B/s|http://www.archive.org/download/Se.1-Review/Se.1-Review_djvu.xml
    a63e51|ERR |       0B/s|http://www.archive.org/download/Seating_Plan/Seating_Plan_djvu.xml
    c0010f|ERR |       0B/s|http://www.archive.org/download/petitorio14bispdf/petitorio14bispdf_djvu.xml
    558e4f|ERR |       0B/s|http://www.archive.org/download/tafreghat2002yahoo.com_257/tafreghat2002yahoo.com_257_djvu.xml
    62a260|ERR |       0B/s|http://www.archive.org/download/SolucionC50AlgebraLineal/SolucionC50AlgebraLineal_djvu.xml
    cccbb7|ERR |       0B/s|http://www.archive.org/download/PhilipHoutzObituary/PhilipHoutzObituary_djvu.xml
    4969a1|ERR |       0B/s|http://www.archive.org/download/Letras_sob_merda_0/Letras_sob_merda_0_djvu.xml
    4dc514|ERR |       0B/s|http://www.archive.org/download/way2allah.com_828/way2allah.com_828_djvu.xml
    d8eccc|ERR |       0B/s|http://www.archive.org/download/Levitan_files/Levitan_files_djvu.xml
    7b9b38|ERR |       0B/s|http://www.archive.org/download/Lewis_Sutton_Civil_War_Pension_Papers/Lewis_Sutton_Civil_War_Pension_Papers_djvu.xml
    9b86c1|ERR |       0B/s|http://www.archive.org/download/HistoryOfFriedrichIiOfPrussiaVolIII/HistoryOfFriedrichIiOfPrussiaVolIII_djvu.xml
    70bc92|ERR |       0B/s|http://www.archive.org/download/Mfaseeh/Mfaseeh_djvu.xml
    f1387a|ERR |       0B/s|http://www.archive.org/download/Hi-techTranslation-CareerTimes/Hi-techTranslation-CareerTimes_djvu.xml
    3e6652|ERR |       0B/s|http://www.archive.org/download/MinutobasketMagazineN2/MinutobasketMagazineN2_djvu.xml
    078afc|ERR |       0B/s|http://www.archive.org/download/MinutobasketMagazineN3/MinutobasketMagazineN3_djvu.xml
    b6fc1a|ERR |       0B/s|http://www.archive.org/download/MinutobasketMagazineNo3/MinutobasketMagazineNo3_djvu.xml
    1fb578|OK  |   848KiB/s|downloads/aria2//entomologistsmo26compgoog_djvu.xml
    bbac60|ERR |       0B/s|http://www.archive.org/download/HohenheichenVerlagProtestantishceRompilgerProtestantRomePilgrim/HohenheichenVerlagProtestantishceRompilgerProtestantRomePilgrim_djvu.xml
    1ba59d|ERR |       0B/s|http://www.archive.org/download/HoldYourPeaceRemainAtRest/HoldYourPeaceRemainAtRest_djvu.xml
    a1bdfb|OK  |   780KiB/s|downloads/aria2//dieverfassungun12prusgoog_djvu.xml
    d23a9b|ERR |       0B/s|http://www.archive.org/download/ModernEloquenceVolX/ModernEloquenceVolX_djvu.xml
    6b567a|OK  |   577KiB/s|downloads/aria2//dvadtsatipiatil03igoog_djvu.xml
    0bfa5e|ERR |       0B/s|http://www.archive.org/download/reportaje_cuba/reportaje_cuba_djvu.xml
    fd4037|ERR |       0B/s|http://www.archive.org/download/LaDistribuzioneNormale/LaDistribuzioneNormale_djvu.xml
    2d0639|ERR |       0B/s|http://www.archive.org/download/La_Cronaca_di_Mantova__Intervista_a_Fabrizio_Paterlini/La_Cronaca_di_Mantova__Intervista_a_Fabrizio_Paterlini_djvu.xml
    07db80|ERR |       0B/s|http://www.archive.org/download/reloj/reloj_djvu.xml
    f5f13b|ERR |       0B/s|http://www.archive.org/download/MagazinSaff_257_br/MagazinSaff_257_br_djvu.xml
    345f43|ERR |       0B/s|http://www.archive.org/download/ManoirPapierartisanal/ManoirPapierartisanal_djvu.xml
    cc388a|ERR |       0B/s|http://www.archive.org/download/LhupaCastawebber505PodcastCatalogBilinguale-f2ndEdition/LhupaCastawebber505PodcastCatalogBilinguale-f2ndEdition_djvu.xml
    832f4b|ERR |       0B/s|http://www.archive.org/download/lhzaa/lhzaa_djvu.xml
    47e3e0|ERR |       0B/s|http://www.archive.org/download/LIBELULA_525/LIBELULA_525_djvu.xml
    d09559|ERR |       0B/s|http://www.archive.org/download/CurseoftheFro/CurseoftheFro_djvu.xml
    9e7ae9|OK  |   435KiB/s|downloads/aria2//reportsallcases01casegoog_djvu.xml
    695237|ERR |       0B/s|http://www.archive.org/download/Empowerment_through_Tecnology__Paper_ICVET_2005/Empowerment_through_Tecnology__Paper_ICVET_2005_djvu.xml
    5dc30b|ERR |       0B/s|http://www.archive.org/download/FAmily_Junior/FAmily_Junior_djvu.xml
    4c8ff7|ERR |       0B/s|http://www.archive.org/download/LigaProvincialSub15ResultadosCuartosDeFinalJuegoIi/LigaProvincialSub15ResultadosCuartosDeFinalJuegoIi_djvu.xml
    804630|ERR |       0B/s|http://www.archive.org/download/JesusIstheLife_John14.6_342/JesusIstheLife_John14.6_342_djvu.xml
    612b3f|ERR |       0B/s|http://www.archive.org/download/rodolfoberrettiphage5composition/rodolfoberrettiphage5composition_djvu.xml
    ae7d79|ERR |       0B/s|http://www.archive.org/download/LeccionesParaRedesDeCrecimiento/LeccionesParaRedesDeCrecimiento_djvu.xml
    30d23d|OK  |   1.0MiB/s|downloads/aria2//hochelagadepict00goog_djvu.xml
    1a4f49|ERR |       0B/s|http://www.archive.org/download/Lecture6_757/Lecture6_757_djvu.xml
    85aaf7|ERR |       0B/s|http://www.archive.org/download/LecturaEnColombia/LecturaEnColombia_djvu.xml
    04bf98|OK  |   681KiB/s|downloads/aria2//rulingroast01woodgoog_djvu.xml
    73c3b7|ERR |       0B/s|http://www.archive.org/download/tofolah_472/tofolah_472_djvu.xml
    636019|ERR |       0B/s|http://www.archive.org/download/ia11110/ia11110_djvu.xml
    bfd00d|ERR |       0B/s|http://www.archive.org/download/LukeBrittMark1.1-15/LukeBrittMark1.1-15_djvu.xml
    e15f84|OK  |   745KiB/s|downloads/aria2//taxlawnewjersey00jersgoog_djvu.xml
    444b2a|ERR |       0B/s|http://www.archive.org/download/philtrans02986382/philtrans02986382_djvu.xml
    123e25|ERR |       0B/s|http://www.archive.org/download/philtrans05783717/philtrans05783717_djvu.xml
    e0089f|ERR |       0B/s|http://www.archive.org/download/philtrans09947023/philtrans09947023_djvu.xml
    465cc0|OK  |   695KiB/s|downloads/aria2//histoiregnralee15flasgoog_djvu.xml
    e2f610|OK  |   826KiB/s|downloads/aria2//playspoemsshake10malogoog_djvu.xml
    b81ff7|OK  |   571KiB/s|downloads/aria2//playswilliamsha13fleigoog_djvu.xml
    e31ccd|OK  |   853KiB/s|downloads/aria2//historyfederalg03freegoog_djvu.xml
    3f48fd|OK  |   817KiB/s|downloads/aria2//politicalcodest01haymgoog_djvu.xml
    1a6461|ERR |       0B/s|http://www.archive.org/download/LuzYArteProyecto/LuzYArteProyecto_djvu.xml
    718483|OK  |   567KiB/s|downloads/aria2//petroleumlawsal00minegoog_djvu.xml
    4ff935|ERR |       0B/s|http://www.archive.org/download/LyfeliekHerobladeOrderoftheJSSPodcast_Episode2/LyfeliekHerobladeOrderoftheJSSPodcast_Episode2_djvu.xml
    cf988e|ERR |       0B/s|http://www.archive.org/download/maanyalhoroof/maanyalhoroof_djvu.xml
    606c17|ERR |       0B/s|http://www.archive.org/download/MACROPROYECTOS/MACROPROYECTOS_djvu.xml
    62a67b|ERR |       0B/s|http://www.archive.org/download/madrassaty.com_302/madrassaty.com_302_djvu.xml
    2a3920|ERR |       0B/s|http://www.archive.org/download/madrassaty.com_509/madrassaty.com_509_djvu.xml
    af31aa|ERR |       0B/s|http://www.archive.org/download/madrassaty.com_552/madrassaty.com_552_djvu.xml
    54eca9|ERR |       0B/s|http://www.archive.org/download/gov.uscourts.mieb.639643/gov.uscourts.mieb.639643_djvu.xml
    64feae|ERR |       0B/s|http://www.archive.org/download/tafregh_108/tafregh_108_djvu.xml
    4b9739|OK  |   246KiB/s|downloads/aria2//preservationtim00boulgoog_djvu.xml
    a217cc|ERR |       0B/s|http://www.archive.org/download/LisaYeoh10Roses10roses1pps/LisaYeoh10Roses10roses1pps_djvu.xml
    ec2fc5|ERR |       0B/s|http://www.archive.org/download/ListaDePreciosIngenieriaOptica2011/ListaDePreciosIngenieriaOptica2011_djvu.xml
    388a78|OK  |   338KiB/s|downloads/aria2//lesrecueilsdeju17courgoog_djvu.xml
    1191e3|ERR |       0B/s|http://www.archive.org/download/ShriGitamritaBodhini/ShriGitamritaBodhini_djvu.xml
    059e75|ERR |       0B/s|http://www.archive.org/download/TahqeeqUlHaqueMaeWithMuzammana/TahqeeqUlHaqueMaeWithMuzammana_djvu.xml
    5c070b|ERR |       0B/s|http://www.archive.org/download/sandwichleft/sandwichleft_djvu.xml
    9ea46f|ERR |       0B/s|http://www.archive.org/download/bacteria00magnrich/bacteria00magnrich_djvu.xml
    24e704|ERR |       0B/s|http://www.archive.org/download/LosZombiesDentroDeNuestraCulturaMediatica/LosZombiesDentroDeNuestraCulturaMediatica_djvu.xml
    10227f|ERR |       0B/s|http://www.archive.org/download/cbarchive_114041_mosquitobreedingonfarringtonla1941/cbarchive_114041_mosquitobreedingonfarringtonla1941_djvu.xml
    db40c6|OK  |   1.4MiB/s|downloads/aria2//descausespremir00moregoog_djvu.xml
    acba93|ERR |       0B/s|http://www.archive.org/download/saopstenje/saopstenje_djvu.xml
    97a0ab|OK  |   839KiB/s|downloads/aria2//politicalscienc03woolgoog_djvu.xml
    46cf18|ERR |       0B/s|http://www.archive.org/download/LoveYou_275/LoveYou_275_djvu.xml
    ab889d|ERR |       0B/s|http://www.archive.org/download/nigmeDuMarie-carole/nigmeDuMarie-carole_djvu.xml
    376cfe|ERR |       0B/s|http://www.archive.org/download/love.poem.002_1/love.poem.002_1_djvu.xml
    b8807c|ERR |       0B/s|http://www.archive.org/download/petabox08arch/petabox08arch_djvu.xml
    a4547b|ERR |       0B/s|http://www.archive.org/download/rubric5-82/rubric5-82_djvu.xml
    36e601|ERR |       0B/s|http://www.archive.org/download/pfuipadsustainablemediaformission/pfuipadsustainablemediaformission_djvu.xml
    7b9cea|ERR |       0B/s|http://www.archive.org/download/LaTorreBellot/LaTorreBellot_djvu.xml
    510fb6|ERR |       0B/s|http://www.archive.org/download/philtrans01629531/philtrans01629531_djvu.xml
    0a8289|ERR |       0B/s|http://www.archive.org/download/philtrans03263154/philtrans03263154_djvu.xml
    85a019|ERR |       0B/s|http://www.archive.org/download/philtrans03309519/philtrans03309519_djvu.xml
    711fc2|ERR |       0B/s|http://www.archive.org/download/philtrans07860482/philtrans07860482_djvu.xml
    644ba5|ERR |       0B/s|http://www.archive.org/download/philtrans00026355/philtrans00026355_djvu.xml
    9d4701|ERR |       0B/s|http://www.archive.org/download/philtrans08282305/philtrans08282305_djvu.xml
    ac13aa|ERR |       0B/s|http://www.archive.org/download/philtrans08349813/philtrans08349813_djvu.xml
    81bf28|ERR |       0B/s|http://www.archive.org/download/philtrans08698938/philtrans08698938_djvu.xml
    67146e|ERR |       0B/s|http://www.archive.org/download/philtrans09046264/philtrans09046264_djvu.xml
    7a8751|ERR |       0B/s|http://www.archive.org/download/philtrans03211289/philtrans03211289_djvu.xml
    3054fd|OK  |   286KiB/s|downloads/aria2//planosEquivalentes_djvu.xml
    bb6837|ERR |       0B/s|http://www.archive.org/download/LawZanbWahdMaghafarsh_chunk_3.doc/LawZanbWahdMaghafarsh_chunk_3.doc_djvu.xml
    b4b797|ERR |       0B/s|http://www.archive.org/download/randy_894/randy_894_djvu.xml
    75f4ed|ERR |       0B/s|http://www.archive.org/download/philtrans09150048/philtrans09150048_djvu.xml
    57b78d|OK  |   315KiB/s|downloads/aria2//treatypeacewith05relagoog_djvu.xml
    d2749b|ERR |       0B/s|http://www.archive.org/download/JuanDeFucaGroup/JuanDeFucaGroup_djvu.xml
    4d3fba|ERR |       0B/s|http://www.archive.org/download/JuanMiguelTejedaChatoelchicoperuanoep2script_1/JuanMiguelTejedaChatoelchicoperuanoep2script_1_djvu.xml
    251a32|OK  |   1.3MiB/s|downloads/aria2//newjalasat_djvu.xml
    67b610|ERR |       0B/s|http://www.archive.org/download/newsletter-apple-hebdo-30/newsletter-apple-hebdo-30_djvu.xml
    fb99f4|ERR |       0B/s|http://www.archive.org/download/GiveADonkeyAndChangeLivesAnOxfamCharitableGiftDoesTheWorldGood/GiveADonkeyAndChangeLivesAnOxfamCharitableGiftDoesTheWorldGood_djvu.xml
    4b05e6|OK  |   0.9MiB/s|downloads/aria2//democritusoderd07webegoog_djvu.xml
    dae836|ERR |       0B/s|http://www.archive.org/download/BillyXThreeKings/BillyXThreeKings_djvu.xml
    ded241|ERR |       0B/s|http://www.archive.org/download/GlasgowSouthernMedicalSociety-MinuteBook1TypewrittenTranscript-1844/GlasgowSouthernMedicalSociety-MinuteBook1TypewrittenTranscript-1844_djvu.xml
    5817ea|OK  |    73KiB/s|downloads/aria2//CDBABY-POSTER-A3_djvu.xml
    84405b|ERR |       0B/s|http://www.archive.org/download/CabanaGrillAtShadowlakeMenu/CabanaGrillAtShadowlakeMenu_djvu.xml
    2d6bef|ERR |       0B/s|http://www.archive.org/download/GlobalIslam/GlobalIslam_djvu.xml
    14260b|ERR |       0B/s|http://www.archive.org/download/GoingTheSmsWayToSpreadTheWord/GoingTheSmsWayToSpreadTheWord_djvu.xml
    425921|ERR |       0B/s|http://www.archive.org/download/gov.uscourts.cand.231385/gov.uscourts.cand.231385_djvu.xml
    7d0372|ERR |       0B/s|http://www.archive.org/download/gov.uscourts.casd.354609/gov.uscourts.casd.354609_djvu.xml
    d4a9a1|ERR |       0B/s|http://www.archive.org/download/GoseaLagunLaguna/GoseaLagunLaguna_djvu.xml
    0dea0d|ERR |       0B/s|http://www.archive.org/download/ComunidadVinoNuevoApocalipsis/ComunidadVinoNuevoApocalipsis_djvu.xml
    6a4756|ERR |       0B/s|http://www.archive.org/download/Four_Brothers_1/Four_Brothers_1_djvu.xml
    cc9591|ERR |       0B/s|http://www.archive.org/download/HalfHours/HalfHours_djvu.xml
    dd69df|OK  |   342KiB/s|downloads/aria2//miscellaniesphi02britgoog_djvu.xml
    31e821|OK  |   511KiB/s|downloads/aria2//refugiumbotanic03bakegoog_djvu.xml
    d65aec|OK  |   0.9MiB/s|downloads/aria2//minutesconventi00convgoog_djvu.xml
    6957ab|OK  |   464KiB/s|downloads/aria2//mmissonsmemoirs00ozelgoog_djvu.xml
    968ba1|ERR |       0B/s|http://www.archive.org/download/HaciaNuevosModelosDeDesarrolloBasadosEnLaOptimizacinColaborativa/HaciaNuevosModelosDeDesarrolloBasadosEnLaOptimizacinColaborativa_djvu.xml
    4ec40a|ERR |       0B/s|http://www.archive.org/download/Hausarbeit-Comparison/Hausarbeit-Comparison_djvu.xml
    a8271e|OK  |   735KiB/s|downloads/aria2//harryandlucycon00edgegoog_djvu.xml
    a2fc2c|ERR |       0B/s|http://www.archive.org/download/Interview_20120410/Interview_20120410_djvu.xml
    e30c95|OK  |   419KiB/s|downloads/aria2//magyarnyelvr09unkngoog_djvu.xml
    a0aac1|ERR |       0B/s|http://www.archive.org/download/BullockAlternativePower/BullockAlternativePower_djvu.xml
    fd34c9|OK  |   574KiB/s|downloads/aria2//harryandlucycon05edgegoog_djvu.xml
    99b158|OK  |   788KiB/s|downloads/aria2//introductiontoc00karrgoog_djvu.xml
    961b76|OK  |   554KiB/s|downloads/aria2//iole01chamgoog_djvu.xml
    a087ce|OK  |   693KiB/s|downloads/aria2//harleianmiscell04malhgoog_djvu.xml
    1e45a9|ERR |       0B/s|http://www.archive.org/download/MushaheerUnaanORooma/MushaheerUnaanORooma_djvu.xml
    ae5c9c|OK  |   575KiB/s|downloads/aria2//investigationso00mincgoog_djvu.xml
    1b5bdb|ERR |       0B/s|http://www.archive.org/download/hotmai/hotmai_djvu.xml
    6d2c90|ERR |       0B/s|http://www.archive.org/download/How_God_communicates_with_you/How_God_communicates_with_you_djvu.xml
    eb04fd|ERR |       0B/s|http://www.archive.org/download/How-to-Change-Your-IA-EMail_Picture/How-to-Change-Your-IA-EMail_Picture_djvu.xml
    54bd76|ERR |       0B/s|http://www.archive.org/download/HowToGetRidOfScalpAcne/HowToGetRidOfScalpAcne_djvu.xml
    0faa2f|ERR |       0B/s|http://www.archive.org/download/httpwww.apple.com.br/httpwww.apple.com.br_djvu.xml
    b9d504|ERR |       0B/s|http://www.archive.org/download/HajjOfTheProphet-IslamicRussianBook.doc/HajjOfTheProphet-IslamicRussianBook.doc_djvu.xml
    43b3a8|ERR |       0B/s|http://www.archive.org/download/HurufTerbalik_784/HurufTerbalik_784_djvu.xml
    b36bb4|ERR |       0B/s|http://www.archive.org/download/OseidoXorg.confNvidia/OseidoXorg.confNvidia_djvu.xml
    924e03|ERR |       0B/s|http://www.archive.org/download/HypatiaVolII/HypatiaVolII_djvu.xml
    208540|ERR |       0B/s|http://www.archive.org/download/Outline2006/Outline2006_djvu.xml
    bcc71d|OK  |   0.9MiB/s|downloads/aria2//POSTER-01_djvu.xml
    4fa754|OK  |    13KiB/s|downloads/aria2//POSTER-02_djvu.xml
    37d038|ERR |       0B/s|http://www.archive.org/download/Handout_from_32507_message/Handout_from_32507_message_djvu.xml
    0f6948|ERR |       0B/s|http://www.archive.org/download/IbnA2sher/IbnA2sher_djvu.xml
    0a0367|OK  |   342KiB/s|downloads/aria2//dmonstrationsva15dmgoog_djvu.xml
    149c6f|ERR |       0B/s|http://www.archive.org/download/iBot_Project_Report/iBot_Project_Report_djvu.xml
    8cdbf7|ERR |       0B/s|http://www.archive.org/download/IchUpdate022-January2011/IchUpdate022-January2011_djvu.xml
    8c9f15|ERR |       0B/s|http://www.archive.org/download/IdentityWeek2pwrPnt/IdentityWeek2pwrPnt_djvu.xml
    329e5d|ERR |       0B/s|http://www.archive.org/download/IconJobsInfo.or.id/IconJobsInfo.or.id_djvu.xml
    a7b17b|ERR |       0B/s|http://www.archive.org/download/RevistaDigitalGeekN1Noviembre2008-Enero2010_139/RevistaDigitalGeekN1Noviembre2008-Enero2010_139_djvu.xml
    f0b3ba|ERR |       0B/s|http://www.archive.org/download/InformeDeLaAuditoraAlPadronOea/InformeDeLaAuditoraAlPadronOea_djvu.xml
    a304f0|ERR |       0B/s|http://www.archive.org/download/Hermes_RVA_10__Paper_model__stand/Hermes_RVA_10__Paper_model__stand_djvu.xml
    bba3a3|OK  |   822KiB/s|downloads/aria2//reportsdecision07howagoog_djvu.xml
    8d7850|ERR |       0B/s|http://www.archive.org/download/HidayatAlMomineen/HidayatAlMomineen_djvu.xml
    86f5f8|ERR |       0B/s|http://www.archive.org/download/IntelignciaSolidria/IntelignciaSolidria_djvu.xml
    7a8c15|ERR |       0B/s|http://www.archive.org/download/HellenicHistory/HellenicHistory_djvu.xml
    984ecd|ERR |       0B/s|http://www.archive.org/download/JuanMiguelTejedaChatoelchicoperuanoep1script/JuanMiguelTejedaChatoelchicoperuanoep1script_djvu.xml
    c24983|ERR |       0B/s|http://www.archive.org/download/JuanMiguelTejedaPodcuentoGr81_1/JuanMiguelTejedaPodcuentoGr81_1_djvu.xml
    0cf327|ERR |       0B/s|http://www.archive.org/download/JulioCattaniEntrevistaRogerSchank/JulioCattaniEntrevistaRogerSchank_djvu.xml
    6ad017|ERR |       0B/s|http://www.archive.org/download/hilia/hilia_djvu.xml
    7d3954|OK  |   436KiB/s|downloads/aria2//instructionconc00jarrgoog_djvu.xml
    663a6b|ERR |       0B/s|http://www.archive.org/download/himen/himen_djvu.xml
    a39724|ERR |       0B/s|http://www.archive.org/download/ImgLibros/ImgLibros_djvu.xml
    92cfc6|ERR |       0B/s|http://www.archive.org/download/ImplicationsOf1330-1270MaTectono-thermalImprintsOnUranium/ImplicationsOf1330-1270MaTectono-thermalImprintsOnUranium_djvu.xml
    abfeac|ERR |       0B/s|http://www.archive.org/download/ImportantTipsWhileSearchingAPerfectHome/ImportantTipsWhileSearchingAPerfectHome_djvu.xml
    57983c|ERR |       0B/s|http://www.archive.org/download/HeTalk-ApplyingToUcas/HeTalk-ApplyingToUcas_djvu.xml
    14267f|ERR |       0B/s|http://www.archive.org/download/HealthTalk0003TuberculosisEnglishText/HealthTalk0003TuberculosisEnglishText_djvu.xml
    2aeee7|ERR |       0B/s|http://www.archive.org/download/HealthyHappyCitiesExhibitionCatalogue/HealthyHappyCitiesExhibitionCatalogue_djvu.xml
    f8235d|ERR |       0B/s|http://www.archive.org/download/IndividualDifferencesAndFamilyResemblancesInAnimalBehavior/IndividualDifferencesAndFamilyResemblancesInAnimalBehavior_djvu.xml
    9cf4c7|ERR |       0B/s|http://www.archive.org/download/HelenNurtonHPSauce_0/HelenNurtonHPSauce_0_djvu.xml
    b8b457|OK  |    33KiB/s|downloads/aria2//RechtenVanDeMens_djvu.xml
    04d766|ERR |       0B/s|http://www.archive.org/download/GuiaSoluciones_508/GuiaSoluciones_508_djvu.xml
    cbfe2a|ERR |       0B/s|http://www.archive.org/download/DossierBiutzNov11/DossierBiutzNov11_djvu.xml
    1d2676|ERR |       0B/s|http://www.archive.org/download/grafikler_593/grafikler_593_djvu.xml
    9ffaf4|ERR |       0B/s|http://www.archive.org/download/GrandAngelsUtilityAssistanceForm/GrandAngelsUtilityAssistanceForm_djvu.xml
    adc3bb|ERR |       0B/s|http://www.archive.org/download/Gyljen/Gyljen_djvu.xml
    4acb97|OK  |   391KiB/s|downloads/aria2//hippolytodesene00triggoog_djvu.xml
    b44ea6|OK  |   1.1MiB/s|downloads/aria2//ValuationIfudofhumanrights_djvu.xml
    27f3e2|ERR |       0B/s|http://www.archive.org/download/IesIntercultural/IesIntercultural_djvu.xml
    1b45b2|ERR |       0B/s|http://www.archive.org/download/Illusions_of_Sobriety/Illusions_of_Sobriety_djvu.xml
    dd846f|ERR |       0B/s|http://www.archive.org/download/Illustratorand039SResourceFile/Illustratorand039SResourceFile_djvu.xml
    a3c4df|OK  |   539KiB/s|downloads/aria2//iowajournalhist12iowagoog_djvu.xml
    091736|ERR |       0B/s|http://www.archive.org/download/kletter/kletter_djvu.xml
    504a9f|OK  |   725KiB/s|downloads/aria2//investigationme02fallgoog_djvu.xml
    18a25b|OK  |    11MiB/s|downloads/aria2//rosettaproject_spl_ortho-1_djvu.xml
    0e17a0|OK  |   602KiB/s|downloads/aria2//konradvonschwab00zimmgoog_djvu.xml
    456212|OK  |   1.4MiB/s|downloads/aria2//kirk2_djvu.xml
    3a8e6d|ERR |       0B/s|http://www.archive.org/download/JoeGarreckSpecialEducationResources_DaveEdyburn/JoeGarreckSpecialEducationResources_DaveEdyburn_djvu.xml
    c0ea89|OK  |   249KiB/s|downloads/aria2//instructionsfor00moorgoog_djvu.xml
    af1e2c|ERR |       0B/s|http://www.archive.org/download/KtabEnglishInHorob/KtabEnglishInHorob_djvu.xml
    0388c3|OK  |   781KiB/s|downloads/aria2//recordsbuckingh03socigoog_djvu.xml
    1cf34e|ERR |       0B/s|http://www.archive.org/download/KudzaiChikomoInterior/KudzaiChikomoInterior_djvu.xml
    86c73a|OK  |   489KiB/s|downloads/aria2//leconversazioni00ggoog_djvu.xml
    3ba205|OK  |    24KiB/s|downloads/aria2//rosettaproject_tur_color-1_djvu.xml
    af11c5|ERR |       0B/s|http://www.archive.org/download/KyefTatasarafEzaWaqatFelAlasr.zip/KyefTatasarafEzaWaqatFelAlasr.zip_djvu.xml
    3a4407|ERR |       0B/s|http://www.archive.org/download/JohnMaherCampaignFinanceReport/JohnMaherCampaignFinanceReport_djvu.xml
    a4280f|OK  |   298KiB/s|downloads/aria2//registrodelegis01spaigoog_djvu.xml
    b5e054|ERR |       0B/s|http://www.archive.org/download/Jay_C_Alternative_paper/Jay_C_Alternative_paper_djvu.xml
    dc78aa|OK  |   741KiB/s|downloads/aria2//lescheminsdefer00moyagoog_djvu.xml
    6e12b3|OK  |   750KiB/s|downloads/aria2//lehrbuchderverg01stengoog_djvu.xml
    91510f|OK  |   246KiB/s|downloads/aria2//e00goog_djvu.xml
    db34be|OK  |   313KiB/s|downloads/aria2//thewilliamsrecord_vol31_djvu.xml
    9ead03|OK  |   601KiB/s|downloads/aria2//hofratjcschubar00schugoog_djvu.xml
    515067|ERR |       0B/s|http://www.archive.org/download/khtma/khtma_djvu.xml
    a17e02|OK  |   1.2MiB/s|downloads/aria2//rosettaproject_mbi_phon-1_djvu.xml
    8f39f0|ERR |       0B/s|http://www.archive.org/download/JeremyRitchJeremyRitchBio/JeremyRitchJeremyRitchBio_djvu.xml
    583c83|OK  |   534KiB/s|downloads/aria2//historiadaunive07lisbgoog_djvu.xml
    34d68c|OK  |   326KiB/s|downloads/aria2//dasgesetzderpol00wilbgoog_djvu.xml
    d43ab0|OK  |   234KiB/s|downloads/aria2//pediatricshygie02rotcgoog_djvu.xml
    f14214|OK  |   633KiB/s|downloads/aria2//historyeighteen09schlgoog_djvu.xml
    2a629d|OK  |   389KiB/s|downloads/aria2//jahresberichtub58unkngoog_djvu.xml
    e5aeb9|OK  |   648KiB/s|downloads/aria2//journalannualco52churgoog_djvu.xml
    2ccfec|OK  |   608KiB/s|downloads/aria2//historischpolit01unkngoog_djvu.xml
    df7d45|OK  |   234KiB/s|downloads/aria2//deepithetorumco01roemgoog_djvu.xml
    de712c|ERR |       0B/s|http://www.archive.org/download/Italy_revision_dingbats_lesson_1/Italy_revision_dingbats_lesson_1_djvu.xml
    5a0f32|OK  |   394KiB/s|downloads/aria2//legislativedocu15assegoog_djvu.xml
    f798ef|OK  |   871KiB/s|downloads/aria2//journaldupalais09appgoog_djvu.xml
    251f5a|OK  |   446KiB/s|downloads/aria2//journalphiladel04phargoog_djvu.xml
    e815a8|OK  |   701KiB/s|downloads/aria2//deutschesarchiv17unkngoog_djvu.xml
    f08a64|OK  |   0.9MiB/s|downloads/aria2//reportofclerkofh1988unit_djvu.xml
    e66c31|OK  |   237KiB/s|downloads/aria2//dedichtwerken03bildgoog_djvu.xml
    8bbebe|OK  |   824KiB/s|downloads/aria2//jurisprudencegn01unkngoog_djvu.xml
    3220fc|OK  |   523KiB/s|downloads/aria2//deutschesarchiv11unkngoog_djvu.xml
    ed1a03|ERR |       0B/s|http://www.archive.org/download/doencahtm/doencahtm_djvu.xml
    b98691|ERR |       0B/s|http://www.archive.org/download/ItsPossibleToFindWholesaleFoodSuppliersWhoAreAlsoGourmetFood/ItsPossibleToFindWholesaleFoodSuppliersWhoAreAlsoGourmetFood_djvu.xml
    84330b|ERR |       0B/s|http://www.archive.org/download/jquery.css_348/jquery.css_348_djvu.xml
    1d9f42|OK  |   0.9MiB/s|downloads/aria2//journalssenateg03senagoog_djvu.xml
    ccc822|OK  |   296KiB/s|downloads/aria2//diechemieundphy00sachgoog_djvu.xml
    60fd15|ERR |       0B/s|http://www.archive.org/download/Iyengehelaxmi/Iyengehelaxmi_djvu.xml
    1911e3|OK  |   767KiB/s|downloads/aria2//documentssenate102senagoog_djvu.xml
    d94cb6|ERR |       0B/s|http://www.archive.org/download/rodolfoberrettigp48D29andM.smegmatis/rodolfoberrettigp48D29andM.smegmatis_djvu.xml
    0e8ba0|ERR |       0B/s|http://www.archive.org/download/rodolfoberrettiPFGEprotocol/rodolfoberrettiPFGEprotocol_djvu.xml
    bceaba|ERR |       0B/s|http://www.archive.org/download/rodolfoberrettiscientificpaper/rodolfoberrettiscientificpaper_djvu.xml
    93b92f|ERR |       0B/s|http://www.archive.org/download/JuanMiguelTejedaPodcuentoGr71_0/JuanMiguelTejedaPodcuentoGr71_0_djvu.xml
    287645|ERR |       0B/s|http://www.archive.org/download/JuanMiguelTejedaPodcuentoGr81_0/JuanMiguelTejedaPodcuentoGr81_0_djvu.xml
    0d48b9|ERR |       0B/s|http://www.archive.org/download/JuanMiguelTejedaPodcuentoGr82_0/JuanMiguelTejedaPodcuentoGr82_0_djvu.xml
    d3492d|ERR |       0B/s|http://www.archive.org/download/JuanMiguelTejedaChatoelchicoperuanoep2script_0/JuanMiguelTejedaChatoelchicoperuanoep2script_0_djvu.xml
    dec634|OK  |   1.2MiB/s|downloads/aria2//elior1_djvu.xml
    9e246a|OK  |   0.9MiB/s|downloads/aria2//elior2_djvu.xml
    78598f|ERR |       0B/s|http://www.archive.org/download/JCIBMSuaraBukit1PDF/JCIBMSuaraBukit1PDF_djvu.xml
    bc90e3|ERR |       0B/s|http://www.archive.org/download/JCIBMSuaraBukit3SuaraBukit3pdf/JCIBMSuaraBukit3SuaraBukit3pdf_djvu.xml
    328a04|OK  |   596KiB/s|downloads/aria2//dublinjournalme53unkngoog_djvu.xml
    f400b7|OK  |   345KiB/s|downloads/aria2//eagleamagazines07goog_djvu.xml
    c41646|ERR |       0B/s|http://www.archive.org/download/JDLasicaRemixingtheDigitalFuture/JDLasicaRemixingtheDigitalFuture_djvu.xml
    0bfbed|OK  |   744KiB/s|downloads/aria2//englischestudie11wagngoog_djvu.xml
    9434cb|OK  |   812KiB/s|downloads/aria2//documentssenate13senagoog_djvu.xml
    6e090d|OK  |   0.9MiB/s|downloads/aria2//essaisdepolitiq05prgoog_djvu.xml
    a0f1dd|ERR |       0B/s|http://www.archive.org/download/Just-if-ication/Just-if-ication_djvu.xml
    83d340|ERR |       0B/s|http://www.archive.org/download/justinbieber_177/justinbieber_177_djvu.xml
    97e830|OK  |   782KiB/s|downloads/aria2//romaallafrancia00unkngoog_djvu.xml
    8fb10c|OK  |   284KiB/s|downloads/aria2//decisionsdepart43offigoog_djvu.xml
    186515|ERR |       0B/s|http://www.archive.org/download/LaHoraDada-PoderososMantras_352/LaHoraDada-PoderososMantras_352_djvu.xml
    eb78a1|ERR |       0B/s|http://www.archive.org/download/LAGARDELLE_Hubert_Revolutsionnyi_sindikalizm_otryvok/LAGARDELLE_Hubert_Revolutsionnyi_sindikalizm_otryvok_djvu.xml
    b5d992|ERR |       0B/s|http://www.archive.org/download/LaimaMockusDeGloriaGaitnEspecialParaNnNotisanNoticias/LaimaMockusDeGloriaGaitnEspecialParaNnNotisanNoticias_djvu.xml
    06cd22|ERR |       0B/s|http://www.archive.org/download/LaIsameic/LaIsameic_djvu.xml
    ad9ded|ERR |       0B/s|http://www.archive.org/download/meisok_Blackbook/meisok_Blackbook_djvu.xml
    f20f43|OK  |    63KiB/s|downloads/aria2//mensenrechten_djvu.xml
    8057c7|OK  |   311KiB/s|downloads/aria2//fictionalramble01pringoog_djvu.xml
    ef933f|OK  |   834KiB/s|downloads/aria2//drjohannesleuni01unkngoog_djvu.xml
    9370a5|OK  |   149KiB/s|downloads/aria2//mercuredefrance64unkngoog_djvu.xml
    1ccbe0|OK  |   246KiB/s|downloads/aria2//decisionsdepart81offigoog_djvu.xml
    1638d0|OK  |   890KiB/s|downloads/aria2//romania09romagoog_djvu.xml
    cd9cb3|ERR |       0B/s|http://www.archive.org/download/JoseLuisMedinaRodriguezFeericoOlvido/JoseLuisMedinaRodriguezFeericoOlvido_djvu.xml
    054dad|OK  |   497KiB/s|downloads/aria2//journalssenateg02senagoog_djvu.xml
    061ea9|ERR |       0B/s|http://www.archive.org/download/IslamAndItsComparisonWithOterReligions/IslamAndItsComparisonWithOterReligions_djvu.xml
    751fe7|OK  |   700KiB/s|downloads/aria2//englishreportsi16benngoog_djvu.xml
    c6b26c|OK  |   213KiB/s|downloads/aria2//cequtaitlaprovi00bertgoog_djvu.xml
    9e1565|OK  |   409KiB/s|downloads/aria2//christophercolu00dickgoog_djvu.xml
    6f8a5c|OK  |   365KiB/s|downloads/aria2//correspondance08sandgoog_djvu.xml
    2d4c8f|OK  |   765KiB/s|downloads/aria2//executivedocume01minngoog_djvu.xml
    127269|OK  |   826KiB/s|downloads/aria2//couradhomoepath00pommgoog_djvu.xml
    bbd26f|ERR |       0B/s|http://www.archive.org/download/JacobCreekGourp/JacobCreekGourp_djvu.xml
    e1604b|OK  |   499KiB/s|downloads/aria2//constitutionalh18maygoog_djvu.xml
    8fd5f9|OK  |   414KiB/s|downloads/aria2//journalandlette00wardgoog_djvu.xml
    a867d0|ERR |       0B/s|http://www.archive.org/download/JamEJam/JamEJam_djvu.xml
    4ff759|OK  |   235KiB/s|downloads/aria2//criticalhistori01unkngoog_djvu.xml
    7a804a|ERR |       0B/s|http://www.archive.org/download/Karl_Williamson_CV_1/Karl_Williamson_CV_1_djvu.xml
    bba6e0|ERR |       0B/s|http://www.archive.org/download/KashafulHajaahMalaBadmana/KashafulHajaahMalaBadmana_djvu.xml
    a64f9b|OK  |   249KiB/s|downloads/aria2//dieheiligeschri01meyegoog_djvu.xml
    59d003|OK  |   724KiB/s|downloads/aria2//commentariesonl00shargoog_djvu.xml
    e89a0d|OK  |   0.9MiB/s|downloads/aria2//goodhousingthat00waldgoog_djvu.xml
    131cb7|ERR |       0B/s|http://www.archive.org/download/GenelJeolojiSunumlar/GenelJeolojiSunumlar_djvu.xml
    0893c4|ERR |       0B/s|http://www.archive.org/download/AnguloEntreVectores_147/AnguloEntreVectores_147_djvu.xml
    05f953|ERR |       0B/s|http://www.archive.org/download/GoodNeighbourAgreement/GoodNeighbourAgreement_djvu.xml
    316200|ERR |       0B/s|http://www.archive.org/download/AnteprimaLibro01/AnteprimaLibro01_djvu.xml
    18497c|ERR |       0B/s|http://www.archive.org/download/GotToHaveHope/GotToHaveHope_djvu.xml
    97f44f|OK  |    56KiB/s|downloads/aria2//Audio-rarities4.516226.1_djvu.xml
    aeb8e1|ERR |       0B/s|http://www.archive.org/download/raysabdulwahid/raysabdulwahid_djvu.xml
    d7c7b1|ERR |       0B/s|http://www.archive.org/download/Gerry_1/Gerry_1_djvu.xml
    b27539|ERR |       0B/s|http://www.archive.org/download/Cultura_Libre/Cultura_Libre_djvu.xml
    5261b6|ERR |       0B/s|http://www.archive.org/download/GreaterKnowledgeATrueValue-CareerTimes/GreaterKnowledgeATrueValue-CareerTimes_djvu.xml
    ea478f|ERR |       0B/s|http://www.archive.org/download/DeStranding/DeStranding_djvu.xml
    decf0a|ERR |       0B/s|http://www.archive.org/download/DemostracionAnguloEntreVectoresAlgebraLineal/DemostracionAnguloEntreVectoresAlgebraLineal_djvu.xml
    b294b9|ERR |       0B/s|http://www.archive.org/download/Group3...10/Group3...10_djvu.xml
    fedcf0|ERR |       0B/s|http://www.archive.org/download/Group_2_Amis_/Group_2_Amis__djvu.xml
    0cd615|ERR |       0B/s|http://www.archive.org/download/DesignacionesLigaCordobesaCrelechFechaDoce/DesignacionesLigaCordobesaCrelechFechaDoce_djvu.xml
    35718d|ERR |       0B/s|http://www.archive.org/download/DeterminantesAlgebraLinealDiegoAlvarez/DeterminantesAlgebraLinealDiegoAlvarez_djvu.xml
    3894c8|ERR |       0B/s|http://www.archive.org/download/GruhaVaasthuSaaramu/GruhaVaasthuSaaramu_djvu.xml
    0cb39f|ERR |       0B/s|http://www.archive.org/download/EmmanLaxtonAboriginalissues/EmmanLaxtonAboriginalissues_djvu.xml
    b8a90d|ERR |       0B/s|http://www.archive.org/download/EncuentroContinentalDeLosPueblosDelAbyaYala-PorElAguaYLaPachamama/EncuentroContinentalDeLosPueblosDelAbyaYala-PorElAguaYLaPachamama_djvu.xml
    f2132e|ERR |       0B/s|http://www.archive.org/download/group2group2radiocommlpaper/group2group2radiocommlpaper_djvu.xml
    30414b|OK  |   890KiB/s|downloads/aria2//gographieuniver00descgoog_djvu.xml
    182b38|ERR |       0B/s|http://www.archive.org/download/GuardianKissesGerryGablesArse/GuardianKissesGerryGablesArse_djvu.xml
    856afa|ERR |       0B/s|http://www.archive.org/download/EuropaJupiterWhitePaperv3/EuropaJupiterWhitePaperv3_djvu.xml
    b2a0fa|ERR |       0B/s|http://www.archive.org/download/FCLCMembersLentDailyDevotionalBooklet2009/FCLCMembersLentDailyDevotionalBooklet2009_djvu.xml
    a7b5d8|OK  |   501KiB/s|downloads/aria2//goethesleben00viehgoog_djvu.xml
    2a865a|ERR |       0B/s|http://www.archive.org/download/GundamnCallInShowSkypeChatLog/GundamnCallInShowSkypeChatLog_djvu.xml
    c60472|ERR |       0B/s|http://www.archive.org/download/FloatHomePage/FloatHomePage_djvu.xml
    119fc1|ERR |       0B/s|http://www.archive.org/download/HaithamContinentalAljdani/HaithamContinentalAljdani_djvu.xml
    45ddf6|ERR |       0B/s|http://www.archive.org/download/guyinatiesurvivingextremesjungle/guyinatiesurvivingextremesjungle_djvu.xml
    00e2ff|ERR |       0B/s|http://www.archive.org/download/Tarbiapress-bayanMo9ata3atIdmaj-25-09-2011.pdf/Tarbiapress-bayanMo9ata3atIdmaj-25-09-2011.pdf_djvu.xml
    4ce540|ERR |       0B/s|http://www.archive.org/download/HajjTawheedThai.doc/HajjTawheedThai.doc_djvu.xml
    ab1542|OK  |   381KiB/s|downloads/aria2//TeMerecesMs_djvu.xml
    8388a0|OK  |   0.9MiB/s|downloads/aria2//friendsintellig01assogoog_djvu.xml
    c19dcb|OK  |   686KiB/s|downloads/aria2//jahresberichtbe10vetegoog_djvu.xml
    b59ce7|OK  |   915KiB/s|downloads/aria2//recreationsinag03andegoog_djvu.xml
    c382a9|OK  |   775KiB/s|downloads/aria2//anessayoneducat00atwagoog_djvu.xml
    0936bf|OK  |   787KiB/s|downloads/aria2//angelapisaniano01unkngoog_djvu.xml
    af4889|OK  |   769KiB/s|downloads/aria2//medicaltimesand07unkngoog_djvu.xml
    4bb9bd|OK  |   594KiB/s|downloads/aria2//ivors00sewegoog_djvu.xml
    29bdf6|OK  |   758KiB/s|downloads/aria2//friendsintellig00assogoog_djvu.xml
    ee7afd|OK  |   847KiB/s|downloads/aria2//annalenderliter06unkngoog_djvu.xml
    c7b7e7|OK  |   0.9MiB/s|downloads/aria2//annalesdelinsti02belggoog_djvu.xml
    34359d|OK  |   768KiB/s|downloads/aria2//annalesdelasoci77frangoog_djvu.xml
    270825|OK  |   671KiB/s|downloads/aria2//janetalbot00browgoog_djvu.xml
    b62975|OK  |   915KiB/s|downloads/aria2//annalesdegograp04fragoog_djvu.xml
    afb551|OK  |   0.9MiB/s|downloads/aria2//appalachia08clubgoog_djvu.xml
    15fd16|OK  |   270KiB/s|downloads/aria2//geschichtederde06schmgoog_djvu.xml
    ccd502|ERR |       0B/s|http://www.archive.org/download/JauhareRiyazee/JauhareRiyazee_djvu.xml
    690411|ERR |       0B/s|http://www.archive.org/download/OurTownNarberthPA19300214/OurTownNarberthPA19300214_djvu.xml
    5eaac9|OK  |   272KiB/s|downloads/aria2//columbianmagazi01unkngoog_djvu.xml
    0561f3|OK  |   305KiB/s|downloads/aria2//fursealarbitrat05arbigoog_djvu.xml
    672817|ERR |       0B/s|http://www.archive.org/download/bannnn/bannnn_djvu.xml
    a87066|OK  |   0.9MiB/s|downloads/aria2//annualreportswa112deptgoog_djvu.xml
    9bec62|OK  |   892KiB/s|downloads/aria2//beitrgezurnhere00gegegoog_djvu.xml
    5df06c|OK  |   599KiB/s|downloads/aria2//beitrgezuderleh00diesgoog_djvu.xml
    2a0848|OK  |   343KiB/s|downloads/aria2//archivfrdiephys01reilgoog_djvu.xml
    23cc52|OK  |   746KiB/s|downloads/aria2//bibliographiede06nijhgoog_djvu.xml
    80102b|OK  |   649KiB/s|downloads/aria2//jean00margoog_djvu.xml
    88e082|OK  |   809KiB/s|downloads/aria2//belehrungenunde00plesgoog_djvu.xml
    a116a9|ERR |       0B/s|http://www.archive.org/download/Zhai_Yongming_Sorgere_e_cadere_delle_parole_distanza_tra_le_cose_2006/Zhai_Yongming_Sorgere_e_cadere_delle_parole_distanza_tra_le_cose_2006_djvu.xml
    b22408|OK  |   304KiB/s|downloads/aria2//annalesdesponts09chaugoog_djvu.xml
    c4bb15|OK  |   488KiB/s|downloads/aria2//bibliothquedelh02chagoog_djvu.xml
    f8e0a6|OK  |   477KiB/s|downloads/aria2//abrahamlincolna03choagoog_djvu.xml
    1dd208|OK  |   834KiB/s|downloads/aria2//bibliographisch03schlgoog_djvu.xml
    3f7d45|OK  |   145KiB/s|downloads/aria2//critiskhistorie03suhmgoog_djvu.xml
    6de725|ERR |       0B/s|http://www.archive.org/download/Incidental_Dispatch_1/Incidental_Dispatch_1_djvu.xml
    81aa15|ERR |       0B/s|http://www.archive.org/download/InclusiveLearningEnvironment/InclusiveLearningEnvironment_djvu.xml
    c98e1b|OK  |   682KiB/s|downloads/aria2//atreatiseonfede02fostgoog_djvu.xml
    53abad|OK  |   708KiB/s|downloads/aria2//achronicleengla01hamigoog_djvu.xml
    a17fb2|OK  |   738KiB/s|downloads/aria2//bibliographiede22dietgoog_djvu.xml
    4de2d0|OK  |   380KiB/s|downloads/aria2//archivfuergynae03unkngoog_djvu.xml
    669d3f|OK  |   702KiB/s|downloads/aria2//acollectionallt02britgoog_djvu.xml
    a5baa7|OK  |   731KiB/s|downloads/aria2//acollectionacts04elligoog_djvu.xml
    ca59f5|OK  |   722KiB/s|downloads/aria2//acollectionacts05elligoog_djvu.xml
    625626|OK  |   719KiB/s|downloads/aria2//abridgmentconta26presgoog_djvu.xml
    68c2c0|OK  |   647KiB/s|downloads/aria2//abridgmentconta32presgoog_djvu.xml
    47f70f|OK  |   330KiB/s|downloads/aria2//abodydivinitywi00ridggoog_djvu.xml
    c6f18b|OK  |   0.9MiB/s|downloads/aria2//acompletehistor05smolgoog_djvu.xml
    a1eda7|OK  |   234KiB/s|downloads/aria2//annualreportswa101deptgoog_djvu.xml
    4fd0ad|OK  |   641KiB/s|downloads/aria2//acompletehistor02smolgoog_djvu.xml
    522728|OK  |   1.0MiB/s|downloads/aria2//acorrespondence00labegoog_djvu.xml
    f13a10|OK  |   859KiB/s|downloads/aria2//acordialforlows05gordgoog_djvu.xml
    e32214|OK  |   199KiB/s|downloads/aria2//abridgmentconta37presgoog_djvu.xml
    92a904|OK  |   584KiB/s|downloads/aria2//annotatedcasesa00greegoog_djvu.xml
    c041e8|OK  |   265KiB/s|downloads/aria2//acompletehistor01smolgoog_djvu.xml
    7b774d|ERR |       0B/s|http://www.archive.org/download/alasem/alasem_djvu.xml
    76b7f6|OK  |   537KiB/s|downloads/aria2//acompletesystem09corngoog_djvu.xml
    34b989|ERR |       0B/s|http://www.archive.org/download/Indymedia_bookmarks/Indymedia_bookmarks_djvu.xml
    4b2dcb|OK  |   837KiB/s|downloads/aria2//aloysblumauersg01blumgoog_djvu.xml
    c6b4c8|OK  |   666KiB/s|downloads/aria2//algemeenekerkel01hamegoog_djvu.xml
    af6413|OK  |   417KiB/s|downloads/aria2//acollectionstat04evangoog_djvu.xml
    b08ad8|ERR |       0B/s|http://www.archive.org/download/Information_Policy_Bibliography/Information_Policy_Bibliography_djvu.xml
    fb3189|ERR |       0B/s|http://www.archive.org/download/IridescenzeAcsi/IridescenzeAcsi_djvu.xml
    822968|OK  |   465KiB/s|downloads/aria2//acompletesystem07corngoog_djvu.xml
    9f9ce0|ERR |       0B/s|http://www.archive.org/download/HomePage.html/HomePage.html_djvu.xml
    9cf813|ERR |       0B/s|http://www.archive.org/download/HonjoRyogoku/HonjoRyogoku_djvu.xml
    094afa|ERR |       0B/s|http://www.archive.org/download/resalaelatones/resalaelatones_djvu.xml
    2e5766|OK  |   590KiB/s|downloads/aria2//jamesgordonswif01gordgoog_djvu.xml
    ed9167|ERR |       0B/s|http://www.archive.org/download/italysecularisation/italysecularisation_djvu.xml
    483868|ERR |       0B/s|http://www.archive.org/download/SergiSotoJouAdanyEvaEden/SergiSotoJouAdanyEvaEden_djvu.xml
    94c1a8|ERR |       0B/s|http://www.archive.org/download/Internet_Filter/Internet_Filter_djvu.xml
    962bda|OK  |   454KiB/s|downloads/aria2//acollectionstat08evangoog_djvu.xml
    7045d0|OK  |   614KiB/s|downloads/aria2//actspassedatses77kentgoog_djvu.xml
    40e0eb|ERR |       0B/s|http://www.archive.org/download/brnamj_234/brnamj_234_djvu.xml
    a39e65|OK  |   323KiB/s|downloads/aria2//boletndelminist03mexigoog_djvu.xml
    a6625d|OK  |   681KiB/s|downloads/aria2//canadaandunited01moorgoog_djvu.xml
    746839|OK  |   537KiB/s|downloads/aria2//irishmonthly16unkngoog_djvu.xml
    4e045c|OK  |   504KiB/s|downloads/aria2//boletinspainins04unkngoog_djvu.xml
    0d4888|OK  |   600KiB/s|downloads/aria2//castironarecord02keepgoog_djvu.xml
    269414|OK  |   509KiB/s|downloads/aria2//ageneralabridgm23vinegoog_djvu.xml
    165137|OK  |   705KiB/s|downloads/aria2//cataloguedesliv05santgoog_djvu.xml
    b91016|ERR |       0B/s|http://www.archive.org/download/JoeyAirdo20060425_2/JoeyAirdo20060425_2_djvu.xml
    114456|ERR |       0B/s|http://www.archive.org/download/cbarchive_116025_pacificcoastantimosquitoconfer1943/cbarchive_116025_pacificcoastantimosquitoconfer1943_djvu.xml
    5fd116|ERR |       0B/s|http://www.archive.org/download/jogarhtm/jogarhtm_djvu.xml
    e921b9|OK  |   750KiB/s|downloads/aria2//catherineireimp02gottgoog_djvu.xml
    6ac059|ERR |       0B/s|http://www.archive.org/download/InvestForTheFutureTakeActionNow/InvestForTheFutureTakeActionNow_djvu.xml
    09cb18|ERR |       0B/s|http://www.archive.org/download/IS-A-BALLER/IS-A-BALLER_djvu.xml
    f17e3a|OK  |   250KiB/s|downloads/aria2//acompletesystem10corngoog_djvu.xml
    46059d|ERR |       0B/s|http://www.archive.org/download/IanCooperKNockoutholidayclubbadges/IanCooperKNockoutholidayclubbadges_djvu.xml
    d7058b|ERR |       0B/s|http://www.archive.org/download/Ibn8a6lob3aAl7anafi-shar7IbnFara7/Ibn8a6lob3aAl7anafi-shar7IbnFara7_djvu.xml
    28df3d|ERR |       0B/s|http://www.archive.org/download/IbneghaziArtical/IbneghaziArtical_djvu.xml
    ee4cba|ERR |       0B/s|http://www.archive.org/download/UniversityofMichiganUniversityofMichiganurbandesignrecommendationsforDowntownYoungstown/UniversityofMichiganUniversityofMichiganurbandesignrecommendationsforDowntownYoungstown_djvu.xml
    97c1d8|ERR |       0B/s|http://www.archive.org/download/HukumatKhodIqtiyariAurHinduMuslimMaslaKahal/HukumatKhodIqtiyariAurHinduMuslimMaslaKahal_djvu.xml
    4ed1c5|ERR |       0B/s|http://www.archive.org/download/HusnENazel/HusnENazel_djvu.xml
    00bd7e|ERR |       0B/s|http://www.archive.org/download/HyderabadSwatantrodayamaCharithra/HyderabadSwatantrodayamaCharithra_djvu.xml
    295c95|ERR |       0B/s|http://www.archive.org/download/I..._1/I..._1_djvu.xml
    c792f1|ERR |       0B/s|http://www.archive.org/download/TSMCAPosteriori/TSMCAPosteriori_djvu.xml
    014e49|ERR |       0B/s|http://www.archive.org/download/jogohtm/jogohtm_djvu.xml
    739614|ERR |       0B/s|http://www.archive.org/download/3omar-elyas/3omar-elyas_djvu.xml
    d47b39|ERR |       0B/s|http://www.archive.org/download/20110320d/20110320d_djvu.xml
    8217f8|ERR |       0B/s|http://www.archive.org/download/morassala/morassala_djvu.xml
    856ef0|ERR |       0B/s|http://www.archive.org/download/5088829.129/5088829.129_djvu.xml
    ca33f0|ERR |       0B/s|http://www.archive.org/download/5088829.13-17/5088829.13-17_djvu.xml
    f74218|ERR |       0B/s|http://www.archive.org/download/5088829.132/5088829.132_djvu.xml
    616451|ERR |       0B/s|http://www.archive.org/download/5088829.33-34/5088829.33-34_djvu.xml
    b271bd|ERR |       0B/s|http://www.archive.org/download/5088829.4-6/5088829.4-6_djvu.xml
    4241b8|ERR |       0B/s|http://www.archive.org/download/5088829.131/5088829.131_djvu.xml
    c19954|ERR |       0B/s|http://www.archive.org/download/5088829.43/5088829.43_djvu.xml
    a07779|ERR |       0B/s|http://www.archive.org/download/5088829.96-97/5088829.96-97_djvu.xml
    26e935|OK  |   615KiB/s|downloads/aria2//amonographonple02wambgoog_djvu.xml
    009a20|ERR |       0B/s|http://www.archive.org/download/5088829.92-93/5088829.92-93_djvu.xml
    5193ef|OK  |   540KiB/s|downloads/aria2//catalogueannuel06jordgoog_djvu.xml
    87f543|ERR |       0B/s|http://www.archive.org/download/MoyzesIlonaEletrajz/MoyzesIlonaEletrajz_djvu.xml
    f8b304|ERR |       0B/s|http://www.archive.org/download/Egglepple-Summary-ThelesmuseumRtm/Egglepple-Summary-ThelesmuseumRtm_djvu.xml
    c8f4df|ERR |       0B/s|http://www.archive.org/download/Non-publishedWebSite/Non-publishedWebSite_djvu.xml
    0b1a95|ERR |       0B/s|http://www.archive.org/download/EnglishtranslationForLawNo.91Year2005/EnglishtranslationForLawNo.91Year2005_djvu.xml
    d52897|ERR |       0B/s|http://www.archive.org/download/ASRIAA/ASRIAA_djvu.xml
    fb262b|ERR |       0B/s|http://www.archive.org/download/NotasMec.FluidosIi/NotasMec.FluidosIi_djvu.xml
    c27dea|ERR |       0B/s|http://www.archive.org/download/EugenieGrandetAndOtherStories/EugenieGrandetAndOtherStories_djvu.xml
    a261f6|ERR |       0B/s|http://www.archive.org/download/nateq_pcir/nateq_pcir_djvu.xml
    dacdb4|ERR |       0B/s|http://www.archive.org/download/CarlosMoralesSocorroPuestaapuntodeUbuntu5.10/CarlosMoralesSocorroPuestaapuntodeUbuntu5.10_djvu.xml
    90a43e|ERR |       0B/s|http://www.archive.org/download/slamda_nashidin_yeri/slamda_nashidin_yeri_djvu.xml
    67c45d|ERR |       0B/s|http://www.archive.org/download/GunchaENoor/GunchaENoor_djvu.xml
    ec29a5|ERR |       0B/s|http://www.archive.org/download/nayf--0u/nayf--0u_djvu.xml
    914278|ERR |       0B/s|http://www.archive.org/download/HistoireDeLand039Imprimerie/HistoireDeLand039Imprimerie_djvu.xml
    c697ec|ERR |       0B/s|http://www.archive.org/download/HijatulRahman/HijatulRahman_djvu.xml
    3b021f|ERR |       0B/s|http://www.archive.org/download/shreat3/shreat3_djvu.xml
    1f5d5e|ERR |       0B/s|http://www.archive.org/download/CodeUsedByIaForUploading/CodeUsedByIaForUploading_djvu.xml
    9e5284|ERR |       0B/s|http://www.archive.org/download/shwahed/shwahed_djvu.xml
    8a6256|ERR |       0B/s|http://www.archive.org/download/Cume_ibadet_gunudur/Cume_ibadet_gunudur_djvu.xml
    548e3f|ERR |       0B/s|http://www.archive.org/download/New-Forsanelhaq.com/New-Forsanelhaq.com_djvu.xml
    167f6d|ERR |       0B/s|http://www.archive.org/download/Circus_animals_Entertaining_or_inhumane/Circus_animals_Entertaining_or_inhumane_djvu.xml
    650add|ERR |       0B/s|http://www.archive.org/download/NewScotlandYardArsonsInitialResponse/NewScotlandYardArsonsInitialResponse_djvu.xml
    09bde2|ERR |       0B/s|http://www.archive.org/download/ApresentaaoGritoRock2012/ApresentaaoGritoRock2012_djvu.xml
    4be98d|ERR |       0B/s|http://www.archive.org/download/AprhqVol22N3Juin2010/AprhqVol22N3Juin2010_djvu.xml
    a06b73|ERR |       0B/s|http://www.archive.org/download/newsletter-apple-hebdo-38/newsletter-apple-hebdo-38_djvu.xml
    97b241|ERR |       0B/s|http://www.archive.org/download/BarbaraJacksonDestructionbyDesign/BarbaraJacksonDestructionbyDesign_djvu.xml
    84d4d7|ERR |       0B/s|http://www.archive.org/download/Bash-leq/Bash-leq_djvu.xml
    a3d5bb|ERR |       0B/s|http://www.archive.org/download/seyahet/seyahet_djvu.xml
    ea909d|ERR |       0B/s|http://www.archive.org/download/Mr.BrunsCh.4ReviewE-edition/Mr.BrunsCh.4ReviewE-edition_djvu.xml
    9cef51|ERR |       0B/s|http://www.archive.org/download/Mr.BrunsCh.13.4E-edition/Mr.BrunsCh.13.4E-edition_djvu.xml
    1ab5b4|ERR |       0B/s|http://www.archive.org/download/shashinotes/shashinotes_djvu.xml
    44a42d|ERR |       0B/s|http://www.archive.org/download/ActsAndResolvesPassedByTheGeneralCourt/ActsAndResolvesPassedByTheGeneralCourt_djvu.xml
    8a4d58|ERR |       0B/s|http://www.archive.org/download/mujeresproceres/mujeresproceres_djvu.xml
    9aced3|ERR |       0B/s|http://www.archive.org/download/AficheFlisolBogot2008/AficheFlisolBogot2008_djvu.xml
    e7bd89|ERR |       0B/s|http://www.archive.org/download/AmoreFrozenFoodsAmoreFrozenfoods/AmoreFrozenFoodsAmoreFrozenfoods_djvu.xml
    dd3500|OK  |   6.2KiB/s|downloads/aria2//munchwikwon12028800_djvu.xml
    890ed9|ERR |       0B/s|http://www.archive.org/download/MusicalLettersFromAbroad/MusicalLettersFromAbroad_djvu.xml
    651b29|ERR |       0B/s|http://www.archive.org/download/NickRentonBusinessEnglishLacksStyle/NickRentonBusinessEnglishLacksStyle_djvu.xml
    d76174|ERR |       0B/s|http://www.archive.org/download/Night_Sky_Reflections/Night_Sky_Reflections_djvu.xml
    503a85|ERR |       0B/s|http://www.archive.org/download/nikobookmarks01november2k9/nikobookmarks01november2k9_djvu.xml
    df19a8|ERR |       0B/s|http://www.archive.org/download/NicksDjMixes/NicksDjMixes_djvu.xml
    5a4d7d|ERR |       0B/s|http://www.archive.org/download/DocumentoDeCatedra-CulturaYPosdesarrollo/DocumentoDeCatedra-CulturaYPosdesarrollo_djvu.xml
    1a70a0|ERR |       0B/s|http://www.archive.org/download/Documento_Eletronico__Aspectos_Tecnicos_e_Regulamentacao_Legal/Documento_Eletronico__Aspectos_Tecnicos_e_Regulamentacao_Legal_djvu.xml
    5597c7|ERR |       0B/s|http://www.archive.org/download/NiteroiCulturalOnLineAndSobuhir/NiteroiCulturalOnLineAndSobuhir_djvu.xml
    920a36|ERR |       0B/s|http://www.archive.org/download/Nikki_Listening_Comprehension/Nikki_Listening_Comprehension_djvu.xml
    b2fc5f|OK  |   181KiB/s|downloads/aria2//actslegislature15jersgoog_djvu.xml
    d0a63e|ERR |       0B/s|http://www.archive.org/download/FightForAxeloos/FightForAxeloos_djvu.xml
    69e8fc|OK  |   440KiB/s|downloads/aria2//cambrianbibliog00prysgoog_djvu.xml
    d90174|ERR |       0B/s|http://www.archive.org/download/GettingDeals_610/GettingDeals_610_djvu.xml
    457757|ERR |       0B/s|http://www.archive.org/download/BEND.OREGON/BEND.OREGON_djvu.xml
    62315f|ERR |       0B/s|http://www.archive.org/download/MinimaDistanciaEntreDosPuntos/MinimaDistanciaEntreDosPuntos_djvu.xml
    a22aa3|ERR |       0B/s|http://www.archive.org/download/MiscellaneousHaysCountyGopEmphera_126/MiscellaneousHaysCountyGopEmphera_126_djvu.xml
    72f23a|ERR |       0B/s|http://www.archive.org/download/MiscellaneousWritings/MiscellaneousWritings_djvu.xml
    7fa567|ERR |       0B/s|http://www.archive.org/download/MkvMergeTutorialInstallationUbuntu/MkvMergeTutorialInstallationUbuntu_djvu.xml
    7d9e8f|OK  |   517KiB/s|downloads/aria2//cataloguefishes03gngoog_djvu.xml
    420e3d|ERR |       0B/s|http://www.archive.org/download/sermon_624/sermon_624_djvu.xml
    abd11b|ERR |       0B/s|http://www.archive.org/download/moduljd/moduljd_djvu.xml
    c8b686|ERR |       0B/s|http://www.archive.org/download/molta9a_da3awi/molta9a_da3awi_djvu.xml
    2884cc|ERR |       0B/s|http://www.archive.org/download/PenrodEva/PenrodEva_djvu.xml
    b07383|ERR |       0B/s|http://www.archive.org/download/HoytSilas/HoytSilas_djvu.xml
    27e4e9|ERR |       0B/s|http://www.archive.org/download/HylandLeola/HylandLeola_djvu.xml
    a05849|ERR |       0B/s|http://www.archive.org/download/BaxterBessie/BaxterBessie_djvu.xml
    ce7f92|ERR |       0B/s|http://www.archive.org/download/HartmanZetta/HartmanZetta_djvu.xml
    fc654d|ERR |       0B/s|http://www.archive.org/download/FugalMargaret/FugalMargaret_djvu.xml
    5d1e4d|ERR |       0B/s|http://www.archive.org/download/PalmarWilliam/PalmarWilliam_djvu.xml
    4a6ea5|ERR |       0B/s|http://www.archive.org/download/BerryEdnaMorgan/BerryEdnaMorgan_djvu.xml
    8574e3|ERR |       0B/s|http://www.archive.org/download/HindmarshShelby/HindmarshShelby_djvu.xml
    e7baab|ERR |       0B/s|http://www.archive.org/download/HamiltonWilliam/HamiltonWilliam_djvu.xml
    ffa058|ERR |       0B/s|http://www.archive.org/download/MadsenAnnaHardy/MadsenAnnaHardy_djvu.xml
    8a1365|ERR |       0B/s|http://www.archive.org/download/PackardMilliard/PackardMilliard_djvu.xml
    7d03a0|ERR |       0B/s|http://www.archive.org/download/NarinaAmiconeObituary/NarinaAmiconeObituary_djvu.xml
    d48081|ERR |       0B/s|http://www.archive.org/download/ChadwickMaryJoanShepherd/ChadwickMaryJoanShepherd_djvu.xml
    2b4ab9|OK  |   291KiB/s|downloads/aria2//nouveauxromans01genlgoog_djvu.xml
    e474ff|ERR |       0B/s|http://www.archive.org/download/MatnShatibia/MatnShatibia_djvu.xml
    5d6311|OK  |   773KiB/s|downloads/aria2//notulenvandealg10indogoog_djvu.xml
    c3f4c6|ERR |       0B/s|http://www.archive.org/download/mediafire./mediafire._djvu.xml
    817a0f|ERR |       0B/s|http://www.archive.org/download/MediMax_Manual__Chapter_15_Collections/MediMax_Manual__Chapter_15_Collections_djvu.xml
    435ae8|ERR |       0B/s|http://www.archive.org/download/MediMax_Manual__Chapter_6_Guarantor_Records/MediMax_Manual__Chapter_6_Guarantor_Records_djvu.xml
    917fbb|OK  |   0.9MiB/s|downloads/aria2//meditazione01_djvu.xml
    921ae8|OK  |   838KiB/s|downloads/aria2//notulenvandealg09indogoog_djvu.xml
    07227b|ERR |       0B/s|http://www.archive.org/download/mejoramiento_485/mejoramiento_485_djvu.xml
    16e900|ERR |       0B/s|http://www.archive.org/download/mejoramiento_528/mejoramiento_528_djvu.xml
    de1893|ERR |       0B/s|http://www.archive.org/download/MangaRankingsWeekEnding14August2011/MangaRankingsWeekEnding14August2011_djvu.xml
    a187d3|ERR |       0B/s|http://www.archive.org/download/MangaRankingsWeekEnding15May2011/MangaRankingsWeekEnding15May2011_djvu.xml
    4fbe2e|ERR |       0B/s|http://www.archive.org/download/MangaRankingsWeekEnding17April2011/MangaRankingsWeekEnding17April2011_djvu.xml
    1ea0d3|ERR |       0B/s|http://www.archive.org/download/MangaRankingsWeekEnding19June2011/MangaRankingsWeekEnding19June2011_djvu.xml
    69bbd8|ERR |       0B/s|http://www.archive.org/download/MangaRankingsWeekEnding1May2011/MangaRankingsWeekEnding1May2011_djvu.xml
    1003a1|ERR |       0B/s|http://www.archive.org/download/MangaRankingsWeekEnding21August2011/MangaRankingsWeekEnding21August2011_djvu.xml
    d8c1eb|ERR |       0B/s|http://www.archive.org/download/MangaRankingsWeekEnding12June2011/MangaRankingsWeekEnding12June2011_djvu.xml
    796b50|ERR |       0B/s|http://www.archive.org/download/MangaRankingsWeekEnding24April2011/MangaRankingsWeekEnding24April2011_djvu.xml
    4a2a03|ERR |       0B/s|http://www.archive.org/download/MangaRankingsWeekEnding31July2011/MangaRankingsWeekEnding31July2011_djvu.xml
    0798f6|ERR |       0B/s|http://www.archive.org/download/MangaRankingsWeekEnding3April2011/MangaRankingsWeekEnding3April2011_djvu.xml
    904122|ERR |       0B/s|http://www.archive.org/download/MangaRankingsWeekEnding4September2011/MangaRankingsWeekEnding4September2011_djvu.xml
    c645ff|ERR |       0B/s|http://www.archive.org/download/MangaRankingsWeekEnding5June2011/MangaRankingsWeekEnding5June2011_djvu.xml
    b4da5a|ERR |       0B/s|http://www.archive.org/download/MangaRankingsWeekEnding7August2011/MangaRankingsWeekEnding7August2011_djvu.xml
    99040a|ERR |       0B/s|http://www.archive.org/download/MangaRankingsWeekEnding9January2011/MangaRankingsWeekEnding9January2011_djvu.xml
    51e353|ERR |       0B/s|http://www.archive.org/download/MaouseAllahOuakbar/MaouseAllahOuakbar_djvu.xml
    2640c9|ERR |       0B/s|http://www.archive.org/download/MapOSMaticDan/MapOSMaticDan_djvu.xml
    5ddff9|ERR |       0B/s|http://www.archive.org/download/Map_saturne/Map_saturne_djvu.xml
    1520c9|ERR |       0B/s|http://www.archive.org/download/gov.uscourts.mssd.69971/gov.uscourts.mssd.69971_djvu.xml
    477e7f|ERR |       0B/s|http://www.archive.org/download/2012-01-24-whitepowermilk/2012-01-24-whitepowermilk_djvu.xml
    037b92|ERR |       0B/s|http://www.archive.org/download/Merritt-7TransitAdjacentNotTransitOriented/Merritt-7TransitAdjacentNotTransitOriented_djvu.xml
    66fee9|OK  |   278KiB/s|downloads/aria2//revuedelahautea01hautgoog_djvu.xml
    e7236e|ERR |       0B/s|http://www.archive.org/download/securityjustice-se-jasonscott/securityjustice-se-jasonscott_djvu.xml
    e2e39f|ERR |       0B/s|http://www.archive.org/download/Mickey_914/Mickey_914_djvu.xml
    725fa3|ERR |       0B/s|http://www.archive.org/download/securityjustice-se-openotto/securityjustice-se-openotto_djvu.xml
    faf9f5|ERR |       0B/s|http://www.archive.org/download/PicitureOfLiberary/PicitureOfLiberary_djvu.xml
    6b95ab|ERR |       0B/s|http://www.archive.org/download/IekhazUlRakhoodBahawalulYunulMauood/IekhazUlRakhoodBahawalulYunulMauood_djvu.xml
    12c29d|ERR |       0B/s|http://www.archive.org/download/PlanoPueblo25DeAgosto/PlanoPueblo25DeAgosto_djvu.xml
    8067d5|ERR |       0B/s|http://www.archive.org/download/IhsanShahadateenFiRamozAsbateen/IhsanShahadateenFiRamozAsbateen_djvu.xml
    513fdd|ERR |       0B/s|http://www.archive.org/download/IjazulMushtaqeen/IjazulMushtaqeen_djvu.xml
    9eaa51|ERR |       0B/s|http://www.archive.org/download/IkhdamUlMajboob/IkhdamUlMajboob_djvu.xml
    40db18|ERR |       0B/s|http://www.archive.org/download/IhsanUlMawaiz/IhsanUlMawaiz_djvu.xml
    ad5f27|ERR |       0B/s|http://www.archive.org/download/IkhsaAljawab/IkhsaAljawab_djvu.xml
    0a14cc|OK  |   534KiB/s|downloads/aria2//schoolorganizat00ayregoog_djvu.xml
    a31269|ERR |       0B/s|http://www.archive.org/download/ikketekstjetekstjemp3_0/ikketekstjetekstjemp3_0_djvu.xml
    de764c|OK  |   1.2MiB/s|downloads/aria2//acriticaldictio09alligoog_djvu.xml
    b57af7|ERR |       0B/s|http://www.archive.org/download/IlGrandeHjort/IlGrandeHjort_djvu.xml
    6073f0|ERR |       0B/s|http://www.archive.org/download/IlGlossarioDiVerlan_929/IlGlossarioDiVerlan_929_djvu.xml
    8307d2|ERR |       0B/s|http://www.archive.org/download/IlmKiDevi/IlmKiDevi_djvu.xml
    453839|ERR |       0B/s|http://www.archive.org/download/PoemYouWillFindThemEverywhereInEverything/PoemYouWillFindThemEverywhereInEverything_djvu.xml
    e3607e|ERR |       0B/s|http://www.archive.org/download/I_Love_Everything_About_You_2/I_Love_Everything_About_You_2_djvu.xml
    e0bd3d|OK  |    48KiB/s|downloads/aria2//PorAlgoSer...enriqueBugnone_djvu.xml
    ecf02e|OK  |   585KiB/s|downloads/aria2//notulenvandealg14indogoog_djvu.xml
    7ec8ca|ERR |       0B/s|http://www.archive.org/download/Imagine_836/Imagine_836_djvu.xml
    51a0f9|ERR |       0B/s|http://www.archive.org/download/ProcessoDeSeleoParaOCursoDePs-graduaoLatoSensuEmFilosofia_12/ProcessoDeSeleoParaOCursoDePs-graduaoLatoSensuEmFilosofia_12_djvu.xml
    74b3ce|ERR |       0B/s|http://www.archive.org/download/reportofsuperint1964leen/reportofsuperint1964leen_djvu.xml
    1c7fa3|ERR |       0B/s|http://www.archive.org/download/reportofsuperint1947leen/reportofsuperint1947leen_djvu.xml
    106395|ERR |       0B/s|http://www.archive.org/download/reportofsuperint1946leen/reportofsuperint1946leen_djvu.xml
    8a2cae|ERR |       0B/s|http://www.archive.org/download/LeMagasinPitoresque/LeMagasinPitoresque_djvu.xml
    9698b1|ERR |       0B/s|http://www.archive.org/download/reportofsuperint1965leen/reportofsuperint1965leen_djvu.xml
    30d723|ERR |       0B/s|http://www.archive.org/download/LesBoulinard/LesBoulinard_djvu.xml
    40f692|ERR |       0B/s|http://www.archive.org/download/leprocszoladev02zola/leprocszoladev02zola_djvu.xml
    6efdd5|ERR |       0B/s|http://www.archive.org/download/LesAnnes2000UneDecennieMusicaleDecevante/LesAnnes2000UneDecennieMusicaleDecevante_djvu.xml
    89c6fb|ERR |       0B/s|http://www.archive.org/download/Leonida_Lyrics-SenzaVita/Leonida_Lyrics-SenzaVita_djvu.xml
    ab6640|ERR |       0B/s|http://www.archive.org/download/MahHongObituary/MahHongObituary_djvu.xml
    06cffa|OK  |   7.2KiB/s|downloads/aria2//prajasaktiv2n1101unknsher_djvu.xml
    7d6fc6|OK  |   4.5KiB/s|downloads/aria2//prajasaktiv2n11500unknsher_djvu.xml
    4a54a7|OK  |   3.4KiB/s|downloads/aria2//prajasaktiv1n700unknsher_djvu.xml
    8cffbc|ERR |       0B/s|http://www.archive.org/download/MahaPadmam/MahaPadmam_djvu.xml
    8312d0|OK  |    43KiB/s|downloads/aria2//prajasaktiv2n1200unknsher_djvu.xml
    4523f1|OK  |    43KiB/s|downloads/aria2//prajasaktiv1n27300unknsher_djvu.xml
    20f253|OK  |    28KiB/s|downloads/aria2//prajasaktiv2n11400unknsher_djvu.xml
    9cffbe|ERR |       0B/s|http://www.archive.org/download/Makh6o6atHamdiSalafi-4/Makh6o6atHamdiSalafi-4_djvu.xml
    50acf4|OK  |    43KiB/s|downloads/aria2//prajasaktiv2n6900unknsher_djvu.xml
    9c8e44|ERR |       0B/s|http://www.archive.org/download/makhdoom/makhdoom_djvu.xml
    caea77|ERR |       0B/s|http://www.archive.org/download/ManagementOfDyslipidemiaInChildren/ManagementOfDyslipidemiaInChildren_djvu.xml
    7c5993|OK  |   5.7KiB/s|downloads/aria2//passengercrewlis0924unit_djvu.xml
    a55c2b|OK  |    14KiB/s|downloads/aria2//passengercrewlis0940unit_djvu.xml
    3a43d4|OK  |   3.7KiB/s|downloads/aria2//passengercrewlis0944unit_djvu.xml
    1b5d5b|OK  |   6.6KiB/s|downloads/aria2//passengercrewlis0947unit_djvu.xml
    05a1f0|OK  |   6.6KiB/s|downloads/aria2//passengercrewlis0952unit_djvu.xml
    6fa7e2|OK  |   9.6KiB/s|downloads/aria2//passengercrewlis0954unit_djvu.xml
    1a337f|OK  |   3.1KiB/s|downloads/aria2//passengercrewlis0927unit_djvu.xml
    59ca18|OK  |   9.6KiB/s|downloads/aria2//passengercrewlis1021unit_djvu.xml
    994c2d|OK  |   6.6KiB/s|downloads/aria2//passengercrewlis1020unit_djvu.xml
    069d80|OK  |   5.7KiB/s|downloads/aria2//passengercrewlis1025unit_djvu.xml
    472e09|OK  |   6.6KiB/s|downloads/aria2//passengercrewlis1023unit_djvu.xml
    53b0de|OK  |   6.2KiB/s|downloads/aria2//passengercrewlis1028unit_djvu.xml
    bcdb50|OK  |        n/a|downloads/aria2//passengercrewlis1022unit_djvu.xml
    a0e183|OK  |   5.7KiB/s|downloads/aria2//passengercrewlis1026unit_djvu.xml
    21f45b|ERR |       0B/s|http://www.archive.org/download/ChristensenFlorenceMecham/ChristensenFlorenceMecham_djvu.xml
    c7410a|OK  |    86KiB/s|downloads/aria2//passengercrewlis1037unit_djvu.xml
    bf6784|OK  |    28KiB/s|downloads/aria2//passengercrewlis1030unit_djvu.xml
    37eefa|OK  |    17KiB/s|downloads/aria2//passengercrewlis1039unit_djvu.xml
    c8bb97|OK  |     483B/s|downloads/aria2//passengercrewlis1036unit_djvu.xml
    09e971|OK  |    86KiB/s|downloads/aria2//passengercrewlis1043unit_djvu.xml
    b58397|OK  |    43KiB/s|downloads/aria2//passengercrewlis1044unit_djvu.xml
    dbdbac|OK  |   7.2KiB/s|downloads/aria2//passengercrewlis1045unit_djvu.xml
    c2cd26|OK  |    86KiB/s|downloads/aria2//passengercrewlis1046unit_djvu.xml
    be6167|OK  |    17KiB/s|downloads/aria2//passengercrewlis1047unit_djvu.xml
    6dd9d4|OK  |   5.1KiB/s|downloads/aria2//passengercrewlis1048unit_djvu.xml
    8eda86|OK  |    10KiB/s|downloads/aria2//passengercrewlis1059unit_djvu.xml
    8789f9|OK  |    10KiB/s|downloads/aria2//passengercrewlis1121unit_djvu.xml
    037d6f|OK  |   8.6KiB/s|downloads/aria2//passengercrewlis1049unit_djvu.xml
    9cfa42|OK  |   6.6KiB/s|downloads/aria2//passengercrewlis1122unit_djvu.xml
    3512ff|OK  |   5.7KiB/s|downloads/aria2//passengercrewlis1050unit_djvu.xml
    cd7594|OK  |    28KiB/s|downloads/aria2//passengercrewlis1125unit_djvu.xml
    e71fab|OK  |   6.2KiB/s|downloads/aria2//passengercrewlis1126unit_djvu.xml
    a8a61c|OK  |    17KiB/s|downloads/aria2//passengercrewlis1159unit_djvu.xml
    9aac56|OK  |   4.8KiB/s|downloads/aria2//passengercrewlis1158unit_djvu.xml
    e13c38|OK  |   2.8KiB/s|downloads/aria2//passengercrewlis1221unit_djvu.xml
    1108c1|OK  |   6.6KiB/s|downloads/aria2//passengercrewlis1223unit_djvu.xml
    7c8968|OK  |   7.9KiB/s|downloads/aria2//passengercrewlis1222unit_djvu.xml
    a2bb94|OK  |   0.9MiB/s|downloads/aria2//leschevaliersdu05genlgoog_djvu.xml
    bd724a|OK  |    86KiB/s|downloads/aria2//passengercrewlis1220unit_djvu.xml
    dd3b3d|OK  |    43KiB/s|downloads/aria2//passengercrewlis1230unit_djvu.xml
    ee3221|OK  |    12KiB/s|downloads/aria2//passengercrewlis1229unit_djvu.xml
    3494ef|OK  |    28KiB/s|downloads/aria2//passengercrewlis1235unit_djvu.xml
    d51eb3|OK  |        n/a|downloads/aria2//passengercrewlis1224unit_djvu.xml
    ac1018|OK  |   8.6KiB/s|downloads/aria2//passengercrewlis1237unit_djvu.xml
    407b36|OK  |    28KiB/s|downloads/aria2//passengercrewlis1236unit_djvu.xml
    d96bc7|OK  |   8.6KiB/s|downloads/aria2//passengercrewlis1239unit_djvu.xml
    7e5b1c|OK  |    43KiB/s|downloads/aria2//passengercrewlis1242unit_djvu.xml
    83a041|OK  |   4.1KiB/s|downloads/aria2//passengercrewlis1238unit_djvu.xml
    b7fdca|OK  |   7.9KiB/s|downloads/aria2//passengercrewlis1243unit_djvu.xml
    6b0868|OK  |   8.6KiB/s|downloads/aria2//passengercrewlis1244unit_djvu.xml
    4438b5|OK  |   5.7KiB/s|downloads/aria2//passengercrewlis1246unit_djvu.xml
    b5c4f1|OK  |        n/a|downloads/aria2//passengercrewlis1248unit_djvu.xml
    66df53|OK  |    43KiB/s|downloads/aria2//passengercrewlis1249unit_djvu.xml
    70eda6|OK  |    43KiB/s|downloads/aria2//passengercrewlis1251unit_djvu.xml
    5dcf3d|OK  |   4.8KiB/s|downloads/aria2//passengercrewlis1250unit_djvu.xml
    18265f|OK  |    43KiB/s|downloads/aria2//passengercrewlis1253unit_djvu.xml
    e85c33|OK  |   2.1KiB/s|downloads/aria2//passengercrewlis1252unit_djvu.xml
    d6d3fc|OK  |   3.1KiB/s|downloads/aria2//passengercrewlis1256unit_djvu.xml
    b70b99|OK  |   6.2KiB/s|downloads/aria2//passengercrewlis1259unit_djvu.xml
    b75e84|OK  |   6.6KiB/s|downloads/aria2//passengercrewlis1254unit_djvu.xml
    8495ff|OK  |   4.3KiB/s|downloads/aria2//passengercrewlis1321unit_djvu.xml
    9d5281|OK  |   7.9KiB/s|downloads/aria2//passengercrewlis1325unit_djvu.xml
    d4a2ac|OK  |    28KiB/s|downloads/aria2//passengercrewlis1326unit_djvu.xml
    b7cb26|OK  |   5.7KiB/s|downloads/aria2//passengercrewlis1329unit_djvu.xml
    b95ff2|OK  |    86KiB/s|downloads/aria2//passengercrewlis1328unit_djvu.xml
    f97459|OK  |        n/a|downloads/aria2//passengercrewlis1255unit_djvu.xml
    e6bf25|OK  |   5.1KiB/s|downloads/aria2//passengercrewlis1330unit_djvu.xml
    41643a|OK  |   5.4KiB/s|downloads/aria2//passengercrewlis1331unit_djvu.xml
    1ce27f|OK  |   7.2KiB/s|downloads/aria2//passengercrewlis1334unit_djvu.xml
    520f72|OK  |   4.1KiB/s|downloads/aria2//passengercrewlis1335unit_djvu.xml
    9c82d1|OK  |    21KiB/s|downloads/aria2//passengercrewlis1336unit_djvu.xml
    da7208|OK  |    12KiB/s|downloads/aria2//passengercrewlis1338unit_djvu.xml
    fd13d7|OK  |   5.1KiB/s|downloads/aria2//passengercrewlis1337unit_djvu.xml
    4dcbca|OK  |   5.7KiB/s|downloads/aria2//passengercrewlis1339unit_djvu.xml
    e68373|OK  |    21KiB/s|downloads/aria2//passengercrewlis1346unit_djvu.xml
    c5ebd1|OK  |    21KiB/s|downloads/aria2//passengercrewlis1348unit_djvu.xml
    a93da8|OK  |   7.9KiB/s|downloads/aria2//passengercrewlis1350unit_djvu.xml
    83dd44|OK  |   514KiB/s|downloads/aria2//mediaevalphilos00maurgoog_djvu.xml
    cf0481|OK  |    86KiB/s|downloads/aria2//passengercrewlis1355unit_djvu.xml
    decf7d|OK  |    17KiB/s|downloads/aria2//passengercrewlis1358unit_djvu.xml
    e5c045|OK  |   7.9KiB/s|downloads/aria2//passengercrewlis1357unit_djvu.xml
    c27fa2|OK  |   8.6KiB/s|downloads/aria2//passengercrewlis1402unit_djvu.xml
    ea62b3|OK  |    14KiB/s|downloads/aria2//passengercrewlis1403unit_djvu.xml
    cb1bc9|OK  |   6.2KiB/s|downloads/aria2//passengercrewlis1404unit_djvu.xml
    c2a5ba|OK  |   9.6KiB/s|downloads/aria2//passengercrewlis1406unit_djvu.xml
    d406e1|OK  |     412B/s|downloads/aria2//passengercrewlis1351unit_djvu.xml
    26026d|OK  |    12KiB/s|downloads/aria2//passengercrewlis1407unit_djvu.xml
    e29d33|OK  |    10KiB/s|downloads/aria2//passengercrewlis1410unit_djvu.xml
    7bbdd5|OK  |    12KiB/s|downloads/aria2//passengercrewlis1414unit_djvu.xml
    d439fa|OK  |   9.6KiB/s|downloads/aria2//passengercrewlis1409unit_djvu.xml
    5ecb33|OK  |   4.8KiB/s|downloads/aria2//passengercrewlis1413unit_djvu.xml
    bb74ac|OK  |        n/a|downloads/aria2//passengercrewlis1412unit_djvu.xml
    82cfbb|OK  |   5.7KiB/s|downloads/aria2//passengercrewlis1416unit_djvu.xml
    29520f|OK  |   4.8KiB/s|downloads/aria2//passengercrewlis1417unit_djvu.xml
    9614da|OK  |   4.3KiB/s|downloads/aria2//passengercrewlis1418unit_djvu.xml
    71b4fc|ERR |       0B/s|http://www.archive.org/download/PaigamEmohammadiPartI/PaigamEmohammadiPartI_djvu.xml
    625663|OK  |   7.2KiB/s|downloads/aria2//passengercrewlis1460unit_djvu.xml
    bf333e|OK  |   3.1KiB/s|downloads/aria2//passengercrewlis1462unit_djvu.xml
    7a19ea|OK  |    14KiB/s|downloads/aria2//passengercrewlis1463unit_djvu.xml
    ffa544|OK  |    43KiB/s|downloads/aria2//passengercrewlis1466unit_djvu.xml
    d44722|OK  |    12KiB/s|downloads/aria2//passengercrewlis1468unit_djvu.xml
    6b7407|OK  |   5.7KiB/s|downloads/aria2//passengercrewlis1469unit_djvu.xml
    9a4f75|OK  |    86KiB/s|downloads/aria2//passengercrewlis1471unit_djvu.xml
    aba3b5|OK  |   7.9KiB/s|downloads/aria2//passengercrewlis1472unit_djvu.xml
    27c9e6|OK  |   8.6KiB/s|downloads/aria2//passengercrewlis1467unit_djvu.xml
    d9665c|OK  |    86KiB/s|downloads/aria2//passengercrewlis1475unit_djvu.xml
    970039|OK  |    14KiB/s|downloads/aria2//passengercrewlis1474unit_djvu.xml
    6ca7ab|OK  |   7.9KiB/s|downloads/aria2//passengercrewlis1473unit_djvu.xml
    6fc815|OK  |    12KiB/s|downloads/aria2//passengercrewlis1476unit_djvu.xml
    bcc3e7|OK  |    10KiB/s|downloads/aria2//passengercrewlis1599unit_djvu.xml
    8e92b4|OK  |    86KiB/s|downloads/aria2//passengercrewlis1661unit_djvu.xml
    2f236f|OK  |   6.6KiB/s|downloads/aria2//passengercrewlis1662unit_djvu.xml
    4bb938|OK  |    43KiB/s|downloads/aria2//passengercrewlis1664unit_djvu.xml
    71231e|OK  |   4.5KiB/s|downloads/aria2//passengercrewlis1660unit_djvu.xml
    422456|OK  |   9.6KiB/s|downloads/aria2//passengercrewlis1667unit_djvu.xml
    a0aab5|OK  |    28KiB/s|downloads/aria2//passengercrewlis1666unit_djvu.xml
    c52b68|OK  |        n/a|downloads/aria2//passengercrewlis1675unit_djvu.xml
    b0fe06|OK  |    21KiB/s|downloads/aria2//passengercrewlis1676unit_djvu.xml
    bd696e|OK  |   4.5KiB/s|downloads/aria2//passengercrewlis1669unit_djvu.xml
    5dc611|OK  |        n/a|downloads/aria2//passengercrewlis1665unit_djvu.xml
    7c9f29|OK  |    10KiB/s|downloads/aria2//passengercrewlis1680unit_djvu.xml
    deb840|OK  |    14KiB/s|downloads/aria2//passengercrewlis1681unit_djvu.xml
    7389a4|ERR |       0B/s|http://www.archive.org/download/PartyControloftheUSCongressandStateLegislatures/PartyControloftheUSCongressandStateLegislatures_djvu.xml
    3e1b57|OK  |   6.6KiB/s|downloads/aria2//passengercrewlis1619unit_djvu.xml
    3243d1|OK  |   5.7KiB/s|downloads/aria2//passengercrewlis1674unit_djvu.xml
    b7ec7f|OK  |   6.6KiB/s|downloads/aria2//passengercrewlis1682unit_djvu.xml
    2517d0|OK  |        n/a|downloads/aria2//passengercrewlis1684unit_djvu.xml
    c9b61c|OK  |   9.6KiB/s|downloads/aria2//passengercrewlis1683unit_djvu.xml
    af0ec4|OK  |    28KiB/s|downloads/aria2//passengercrewlis1686unit_djvu.xml
    300ff6|OK  |    10KiB/s|downloads/aria2//passengercrewlis1690unit_djvu.xml
    5222f7|OK  |    12KiB/s|downloads/aria2//passengercrewlis1688unit_djvu.xml
    f570c4|OK  |        n/a|downloads/aria2//passengercrewlis1691unit_djvu.xml
    b16391|OK  |    86KiB/s|downloads/aria2//passengercrewlis1693unit_djvu.xml
    9bbcb5|OK  |    86KiB/s|downloads/aria2//passengercrewlis1692unit_djvu.xml
    6612bb|OK  |    86KiB/s|downloads/aria2//passengercrewlis1701unit_djvu.xml
    ab85d3|OK  |    12KiB/s|downloads/aria2//passengercrewlis1704unit_djvu.xml
    6827a6|OK  |   5.1KiB/s|downloads/aria2//passengercrewlis1705unit_djvu.xml
    587f2e|OK  |   574KiB/s|downloads/aria2//70unkngoog_djvu.xml
    41fbb6|OK  |    86KiB/s|downloads/aria2//passengercrewlis1706unit_djvu.xml
    d2bda2|OK  |   4.5KiB/s|downloads/aria2//passengercrewlis1707unit_djvu.xml
    cf243c|OK  |    43KiB/s|downloads/aria2//passengercrewlis1762unit_djvu.xml
    ac3376|OK  |   7.9KiB/s|downloads/aria2//passengercrewlis1807unit_djvu.xml
    436fc4|ERR |       0B/s|http://www.archive.org/download/Pitt_Darl_Test3/Pitt_Darl_Test3_djvu.xml
    127148|OK  |   2.8KiB/s|downloads/aria2//passengercrewlis1875unit_djvu.xml
    f368e9|ERR |       0B/s|http://www.archive.org/download/PlebNewspaper/PlebNewspaper_djvu.xml
    f23f80|ERR |       0B/s|http://www.archive.org/download/PlenoExtraordinario02-03-2012YAudio/PlenoExtraordinario02-03-2012YAudio_djvu.xml
    f4264a|ERR |       0B/s|http://www.archive.org/download/PlenoExtraordinario08-02-2012/PlenoExtraordinario08-02-2012_djvu.xml
    402c17|OK  |   4.8KiB/s|downloads/aria2//passengercrewlis2932unit_djvu.xml
    ad9d5b|OK  |   4.5KiB/s|downloads/aria2//passengercrewlis2938unit_djvu.xml
    262ea6|OK  |   3.6KiB/s|downloads/aria2//passengercrewlis2934unit_djvu.xml
    90ef57|OK  |    21KiB/s|downloads/aria2//passengercrewlis2939unit_djvu.xml
    235e77|OK  |    17KiB/s|downloads/aria2//passengercrewlis2933unit_djvu.xml
    96004e|OK  |    17KiB/s|downloads/aria2//passengercrewlis2937unit_djvu.xml
    97fc2b|OK  |   3.3KiB/s|downloads/aria2//passengercrewlis2940unit_djvu.xml
    17bca6|OK  |   4.8KiB/s|downloads/aria2//passengercrewlis2941unit_djvu.xml
    9451da|OK  |   8.6KiB/s|downloads/aria2//passengercrewlis2945unit_djvu.xml
    ecf8f1|OK  |   717KiB/s|downloads/aria2//mmoires108frangoog_djvu.xml
    8a67ce|OK  |   6.6KiB/s|downloads/aria2//passengercrewlis2948unit_djvu.xml
    a4939e|OK  |   9.6KiB/s|downloads/aria2//passengercrewlis2944unit_djvu.xml
    18ae39|OK  |    12KiB/s|downloads/aria2//passengercrewlis2942unit_djvu.xml
    11f1e8|OK  |   3.2KiB/s|downloads/aria2//passengercrewlis2949unit_djvu.xml
    29e365|OK  |    86KiB/s|downloads/aria2//passengercrewlis2943unit_djvu.xml
    aa1e7f|OK  |   3.9KiB/s|downloads/aria2//passengercrewlis2951unit_djvu.xml
    0c50ce|OK  |        n/a|downloads/aria2//passengercrewlis2955unit_djvu.xml
    456b37|OK  |        n/a|downloads/aria2//passengercrewlis2950unit_djvu.xml
    1ea23e|OK  |   7.2KiB/s|downloads/aria2//passengercrewlis2954unit_djvu.xml
    8e8eb4|OK  |    10KiB/s|downloads/aria2//passengercrewlis2956unit_djvu.xml
    25d77a|OK  |   3.6KiB/s|downloads/aria2//passengercrewlis2953unit_djvu.xml
    77b664|OK  |   7.2KiB/s|downloads/aria2//passengercrewlis3021unit_djvu.xml
    e2119b|OK  |    10KiB/s|downloads/aria2//passengercrewlis2958unit_djvu.xml
    c52a79|OK  |   5.1KiB/s|downloads/aria2//passengercrewlis3024unit_djvu.xml
    d8de68|OK  |   7.2KiB/s|downloads/aria2//passengercrewlis3026unit_djvu.xml
    8a96c2|OK  |   5.7KiB/s|downloads/aria2//passengercrewlis3029unit_djvu.xml
    c61bff|OK  |    43KiB/s|downloads/aria2//passengercrewlis3027unit_djvu.xml
    629adf|OK  |   7.9KiB/s|downloads/aria2//passengercrewlis3025unit_djvu.xml
    b42c87|OK  |   9.6KiB/s|downloads/aria2//passengercrewlis3030unit_djvu.xml
    06fad4|OK  |   4.5KiB/s|downloads/aria2//passengercrewlis3032unit_djvu.xml
    825701|OK  |    10KiB/s|downloads/aria2//passengercrewlis3033unit_djvu.xml
    a94452|OK  |    14KiB/s|downloads/aria2//passengercrewlis3034unit_djvu.xml
    9cbd8a|OK  |        n/a|downloads/aria2//passengercrewlis3036unit_djvu.xml
    794c71|OK  |    21KiB/s|downloads/aria2//passengercrewlis3040unit_djvu.xml
    750478|OK  |    14KiB/s|downloads/aria2//passengercrewlis3041unit_djvu.xml
    10d374|OK  |   4.8KiB/s|downloads/aria2//passengercrewlis3037unit_djvu.xml
    34684c|OK  |    86KiB/s|downloads/aria2//passengercrewlis3042unit_djvu.xml
    ca71c4|OK  |    17KiB/s|downloads/aria2//passengercrewlis3039unit_djvu.xml
    fa154a|OK  |   9.6KiB/s|downloads/aria2//passengercrewlis3043unit_djvu.xml
    b6bba2|OK  |   5.7KiB/s|downloads/aria2//passengercrewlis3044unit_djvu.xml
    ea6c45|OK  |    12KiB/s|downloads/aria2//passengercrewlis3047unit_djvu.xml
    6d5c90|OK  |    17KiB/s|downloads/aria2//passengercrewlis3049unit_djvu.xml
    d1b953|OK  |    10KiB/s|downloads/aria2//passengercrewlis3055unit_djvu.xml
    8d5f37|OK  |   4.8KiB/s|downloads/aria2//passengercrewlis3052unit_djvu.xml
    10dfb6|OK  |    10KiB/s|downloads/aria2//passengercrewlis3048unit_djvu.xml
    cfa3da|OK  |   7.2KiB/s|downloads/aria2//passengercrewlis3056unit_djvu.xml
    db7dac|OK  |    43KiB/s|downloads/aria2//passengercrewlis3053unit_djvu.xml
    97312a|OK  |    43KiB/s|downloads/aria2//passengercrewlis3058unit_djvu.xml
    7abf58|OK  |    86KiB/s|downloads/aria2//passengercrewlis3054unit_djvu.xml
    2f3455|OK  |    12KiB/s|downloads/aria2//passengercrewlis3120unit_djvu.xml
    ca7dda|OK  |        n/a|downloads/aria2//passengercrewlis3122unit_djvu.xml
    476c79|OK  |   7.9KiB/s|downloads/aria2//passengercrewlis3121unit_djvu.xml
    44a71e|OK  |    17KiB/s|downloads/aria2//passengercrewlis3059unit_djvu.xml
    50675b|OK  |        n/a|downloads/aria2//passengercrewlis3123unit_djvu.xml
    4b057b|OK  |   7.9KiB/s|downloads/aria2//passengercrewlis3124unit_djvu.xml
    0074fa|OK  |        n/a|downloads/aria2//passengercrewlis3128unit_djvu.xml
    2f5fa9|OK  |   5.7KiB/s|downloads/aria2//passengercrewlis3129unit_djvu.xml
    753e97|OK  |    10KiB/s|downloads/aria2//passengercrewlis3130unit_djvu.xml
    05c17a|OK  |   7.9KiB/s|downloads/aria2//passengercrewlis3131unit_djvu.xml
    cdd9c1|OK  |    43KiB/s|downloads/aria2//passengercrewlis3132unit_djvu.xml
    790c09|OK  |   5.4KiB/s|downloads/aria2//passengercrewlis3133unit_djvu.xml
    c3e4c2|OK  |    10KiB/s|downloads/aria2//passengercrewlis3137unit_djvu.xml
    3fac90|OK  |   8.6KiB/s|downloads/aria2//passengercrewlis3139unit_djvu.xml
    1896d6|OK  |   4.3KiB/s|downloads/aria2//passengercrewlis3136unit_djvu.xml
    57c684|OK  |    14KiB/s|downloads/aria2//passengercrewlis3140unit_djvu.xml
    361491|OK  |    43KiB/s|downloads/aria2//passengercrewlis3141unit_djvu.xml
    b211d2|OK  |    43KiB/s|downloads/aria2//passengercrewlis3142unit_djvu.xml
    665509|OK  |    14KiB/s|downloads/aria2//passengercrewlis3149unit_djvu.xml
    cc6de1|OK  |   9.6KiB/s|downloads/aria2//passengercrewlis3143unit_djvu.xml
    ec1db6|OK  |   6.6KiB/s|downloads/aria2//passengercrewlis3146unit_djvu.xml
    ea21b2|OK  |   4.5KiB/s|downloads/aria2//passengercrewlis3154unit_djvu.xml
    45395f|OK  |   8.6KiB/s|downloads/aria2//passengercrewlis3153unit_djvu.xml
    e4fa16|OK  |   8.6KiB/s|downloads/aria2//passengercrewlis3151unit_djvu.xml
    614935|OK  |   7.9KiB/s|downloads/aria2//passengercrewlis3150unit_djvu.xml
    4ed742|OK  |        n/a|downloads/aria2//passengercrewlis3157unit_djvu.xml
    798934|OK  |        n/a|downloads/aria2//passengercrewlis3145unit_djvu.xml
    34caad|OK  |   9.6KiB/s|downloads/aria2//passengercrewlis3159unit_djvu.xml
    7b802d|OK  |    43KiB/s|downloads/aria2//passengercrewlis3224unit_djvu.xml
    742f62|ERR |       0B/s|http://www.archive.org/download/PolinomioDeGradoDosPorCarrascal/PolinomioDeGradoDosPorCarrascal_djvu.xml
    e89e8d|OK  |    21KiB/s|downloads/aria2//passengercrewlis3221unit_djvu.xml
    efccc5|OK  |    17KiB/s|downloads/aria2//passengercrewlis3227unit_djvu.xml
    5b2356|OK  |   3.9KiB/s|downloads/aria2//passengercrewlis3223unit_djvu.xml
    68e33b|OK  |    86KiB/s|downloads/aria2//passengercrewlis3228unit_djvu.xml
    fbf833|OK  |   7.2KiB/s|downloads/aria2//passengercrewlis3155unit_djvu.xml
    c477a5|OK  |        n/a|downloads/aria2//passengercrewlis3156unit_djvu.xml
    e6d7fe|OK  |   9.6KiB/s|downloads/aria2//passengercrewlis3229unit_djvu.xml
    ece47b|OK  |   5.7KiB/s|downloads/aria2//passengercrewlis3230unit_djvu.xml
    82c604|OK  |        n/a|downloads/aria2//passengercrewlis3231unit_djvu.xml
    7038d3|OK  |   7.9KiB/s|downloads/aria2//passengercrewlis3234unit_djvu.xml
    ac1b8f|OK  |    43KiB/s|downloads/aria2//passengercrewlis3235unit_djvu.xml
    02db7f|OK  |   7.9KiB/s|downloads/aria2//passengercrewlis3236unit_djvu.xml
    538338|OK  |    10KiB/s|downloads/aria2//passengercrewlis3237unit_djvu.xml
    97e2fc|OK  |   4.8KiB/s|downloads/aria2//passengercrewlis3240unit_djvu.xml
    c16ce3|OK  |   2.8KiB/s|downloads/aria2//passengercrewlis3244unit_djvu.xml
    42c72a|OK  |   5.1KiB/s|downloads/aria2//passengercrewlis3247unit_djvu.xml
    e9da2c|OK  |    12KiB/s|downloads/aria2//passengercrewlis3246unit_djvu.xml
    bb0aa9|OK  |    12KiB/s|downloads/aria2//passengercrewlis3248unit_djvu.xml
    fe1a4b|OK  |    12KiB/s|downloads/aria2//passengercrewlis3250unit_djvu.xml
    edadce|OK  |    86KiB/s|downloads/aria2//passengercrewlis3251unit_djvu.xml
    074e8c|OK  |    43KiB/s|downloads/aria2//passengercrewlis3239unit_djvu.xml
    37c59a|OK  |   5.7KiB/s|downloads/aria2//passengercrewlis3253unit_djvu.xml
    68a782|OK  |    14KiB/s|downloads/aria2//passengercrewlis3242unit_djvu.xml
    0d580a|OK  |   472KiB/s|downloads/aria2//biographieunive01fellgoog_djvu.xml
    d3161c|OK  |   1.0MiB/s|downloads/aria2//illinoisschoolj00unkngoog_djvu.xml

    Status Legend:
    (OK):download completed.(ERR):error occurred.

    aria2 will resume download if the transfer is restarted.
    If there are any errors, then see the log file. See '-l' option in help/man page for details.


    =========> Downloaded in : 617.796431 s
