# Download Script & Estimation
via Utilities: `wget`, `curl`, `aria2`

This is performance evaluation of the download script. The download script depends on `wget`, `curl`, and `aria2` ([a download manager for *NIX systems](http://aria2.sourceforge.net/) )

Short summary of advantages of using a download manager like `aria2`:

- __Multi Connection Download__ which enables use of full bandwidth
- __Resume Interrupted Downloads__ : it automatically resumes interrupted downloads, unlike `wget` and `curl` where you have to specifically specify flags like `--c` for resuming downloads
- Easier management of downloads
    - It can parse a text file for the URLs and start downloading
    - We can specify a target directory (which I think is missing in `wget` or `curl` allowing us to manage our downloads better)

## Usage of the script `dnld.py`
    $python dnld.py --input="src/source.csv" --utility="wget" --format="djvu"

- `--input` [MANDATORY] : specify a csv file with `book-ids` for the books to be downloaded from [National Archives Advanced Search interface](http://archive.org/advancedsearch.php?q=mediatype:texts)
- `--utility` [OPTIONAL] : The script provides provision for downloading using `wget`, `curl` and `aria2` utilities that must be pre-installed in the environment.
    - DEFAULT value is `aria2`
- `--format` [OPTIONAL]: To specify the xml format of files that we are interested in.

#### Note:

- `time` module has been used to timestamp the download process
- `curl` utility output isn't working exactly as expected. It keeps downloading ~0B files. It may be a silly mistake. I shall correct that in the future.
- `wget` option downloads the files in the current directory, whereas `aria2` downloads it in the appropriate `./downloads/aria2/` directory. I am still trying to do a workaround in python
- The script downloads the files and then comes back to python, to do any post-processing that we might need to do (like the `XSLT` Transformation)


## Download Performance

<table>
    <tr>
        <th>Computer Station</th>
        <th>Files Requested</th>
        <th>Files Downloaded</th>
        <th>Total Download Size</th>
        <th><code>wget</code></th>
        <th><code>aria2</code></th>
        <th><code>curl</code></th>
    </tr>
    <tr>
        <td>Personal Laptop</td>
        <td>100</td>
        <td>34</td>
        <td>334 MB</td>
        <td>5m 39s (= 339 s)</td>
        <td>1m 54.02 s (114.02 s)</td>
        <td>-</td>
    </tr>
    <tr>
        <td>Personal Laptop</td>
        <td>1000</td>
        <td>517</td>
        <td>2.8G</td>
        <td>23m 51.39s (=1431.391540 s)</td>
        <td>10m 29s (=617.796431 s)</td>
        <td>-</td>
    </tr>
    <tr>
        <td>UNC Server</td>
        <td>100</td>
        <td>34</td>
        <td>334 MB</td>
        <td>2m 48s (= 223.842660 s)</td>
        <td>-</td>
        <td>-</td>
    </tr>
</table>

## File Statistics
via `filestats.py` script

    $ python filestats.py --dir="downloads/aria2/" --type="xml"


<table>
    <tr>
        <th>Files Requested</th>
        <th>File Count</th>
        <th>Total Size</th>
        <th>Mean File Size</th>
        <th>Minimum</th>
        <th>Maximum</th>
        <th>75 percentile</th>
    </tr>
    <tr>
        <td>100</td>
        <td>34</td>
        <td>334 MB</td>
        <td>9.82 MB </td>
        <td>89 B</td>
        <td>39.76 MB</td>
        <td>12.404 MB</td>
    </tr>
    <tr>
        <td>1000</td>
        <td>517</td>
        <td>2.96 GB</td>
        <td>5.71 MB </td>
        <td>89 B</td>
        <td>105.18 MB</td>
        <td>7.78 MB</td>
    </tr>
</table>

## Estimation
Here is my estimation of file size and download time for the given corpus.

Considering the 1000 book-id sample, the query response was

    4614983 results (first 1000 shown) for query: mediatype:texts

And from the above sample of book ids, we were able to get `517` books. So, assuming for the entire sample we would be able to get 50% of the books from the total results returned.

    total_books = 4614983 * 0.5

Then, considering our dispersion of file size,

    best case scenario      : file_size = mean file size
    conservative case scenario   : file_size = 75 % file size + 25% large file

Therefore, __Total Download Size__ becomes:

    [BEST CASE]
    downloadable file size : total_book * mean file size
    downloadable file size : ~ 13.175 TB

    [GENERAL CASE]
    downloadable file size : total_book * 0.75 * (75percentile file size) + total_book * 0.25 * an estimated large file size
    Estimating an average of ~40 MB for larger books
    downloadable file size : ~ 44.541 TB


And then, the download time: (via `aria` speeds)

    [BEST CASE]
    Estimated time : 33.6 days  i.e. 806.446 hours (for one system)

    [GENERAL CASE]
    Estimated time: 107.59 days i.e. 2582.29 hours (for one system)


## SALT Server disk output

    -bash-4.1$ df -h

    Filesystem            Size  Used Avail Use% Mounted on
    /dev/mapper/vg01-root
                           79G  3.1G   72G   5% /tmpfs
                           24G     0   24G   0% /dev/shm



    <!-- this should our SALT Directory drive -->
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









