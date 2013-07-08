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