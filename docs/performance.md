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
