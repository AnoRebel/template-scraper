#!usr/bin/python

########################################################################################################################
# This little code scrapes all Tanzanian schools, primary and secondary and saving it
# in a .json file for later use
#
# author = Adam Salehe
#
# This program is written in pure python 3.5.2, and uses, bs4, lxml, json, requests(or urllib2)
# the requisites are the above mention.
#
# questions = hacker4rebel@gmail.com
#
# created on 26/03/2017
#
# You can use this as a template for any scraping project using beautifulsoup4 and lxml
# this works even for a beginner coz its a step by step program
#
# Thanks to that prick Maotora for making a noob like me do this without any help and even having the guts to give me a
# deadline
########################################################################################################################
import requests
from bs4 import BeautifulSoup
import time

# Regions
regions = ['Arusha', 'Dar es Salaam', 'Dodoma', 'Iringa', 'Kagera', 'Kigoma', 'Kilimanjaro', 'Lindi', 'Manyara', 'Mara',
           'Mbeya', 'Morogoro', 'Mtwara', 'Mwanza', 'Pwani', 'Rukwa', 'Ruvuma', 'Shinyanga', 'Singida', 'Tabora',
           'Tanga']

# Districts
Arusha = ['Arumeru', 'Arusha', 'Karatu', 'Longido', 'Monduli', 'Ngorogoro']
Dar_es_Salaam = ['Ilala', 'Kinondoni', 'Temeke']
Dodoma = ['Bahi', 'Buigiri', 'Chamwino', 'Dodoma', 'Dodoma+(V)', 'Kondoa', 'Kongwa', 'Mpwapwa']
Iringa = ['Iringa', 'Iringa+(V)', 'Kilolo', 'Ludewa', 'Makete', 'Mufindi', 'Njombe']
Kagera = ['Biharamulo', 'Bukoba', 'Bukoba+(V)', 'Chato', 'Kahama', 'Karagwe', 'Misenyi', 'Muleba', 'Ngara']
Kigoma = ['Kasulu', 'Kibondo', 'Kigoma', 'Kigoma+(V)']
Kilimanjaro = {'Hai', 'Himo', 'Moshi', 'Moshi+(V)', 'Mwanga', 'Rombo', 'Same', 'Siha'}
Lindi = ['Kilwa', 'Lindi', 'Lindi+(V)', 'Liwale', 'Nachingwea', 'Ruangwa']
Manyara = ['Babati', 'Babati+(V)', 'Hanang', 'Kiteto', 'Manyara', 'Mbulu', 'Simanjiro']
Mara = ['Bunda', 'Musoma', 'Musoma+(V)', 'Rorya', 'Serengeti', 'Tarime']
Mbeya = ['Chunya', 'Ileje', 'Kyela', 'Mbarali', 'Mbeya', 'Mbeya+(V)', 'Mbozi', 'Rujewa', 'Rungwe']
Morogoro = ['Ifakara', 'Kilombero', 'Kilosa', 'Mahenge', 'Morogoro', 'Morogoro+(V)', 'Mvomero', 'Ulanga']
Mtwara = ['Masasi', 'Mtwara', 'Mtwara+(V)', 'Namtumbo', 'Newala', 'Tandahimba']
Mwanza = ['Geita', 'Ilemela', 'Kwimba', 'Magu', 'Misungwi', 'Mwanza', 'Mwanza+(V)', 'Nyamagana', 'Sengerema', 'Ukerewe']
Pwani = ['Bagamoyo', 'Kibaha', 'Kisarawe', 'Mafia', 'Mkuranga', 'Rufiji']
Rukwa = ['Mpanda', 'Mpanda+(V)', 'Nkasi', 'Sumbawanga', 'Sumbawanga+(V)']
Ruvuma = ['Mbinga', 'Namtumbo', 'Ruvuma', 'Songea', 'Songea+(V)', 'Tunduru']
Shinyanga = ['Bariadi', 'Bukombe', 'Kahama', 'Kishapu', 'Maswa', 'Meatu', 'Shinyanga', 'Shinyanga+(V)']
Singida = ['Iramba', 'Manyoni', 'Singida', 'Singida+(V)']
Tabora = ['Igunga', 'Nzega', 'Sikonge', 'Tabora', 'Tabora+(V)', 'Urambo', 'Uyui']
Tanga = ['Handeni', 'Kilindi', 'Korogwe', 'Lushoto', 'Mkinga', 'Muheza', 'Pangani', 'Tanga']

# Schooltypes which will be looped on later
schooltyp = ['Govt', 'Private']

# School gender also to  be looped on in the secondary schools
schoolgen = ['Coed', 'boys', 'girls']

# Main loop for the general app to loop from, first primary, then secondary.
all_schools = ['primary', 'secondary']


# This function scrapes the pages and calls the mongodb function in secondary school loop
def scrapes(urls):
    print('Opening the urls for parsing')
    print('...........')
    try:
        # req = urllib.request.Request(url, headers={'User-Agent': "Magic Browser"})
        # use above if the site blocks or refuses your connection(when using urllib.request)
        r = requests.get(urls)
    except:
        time.sleep(4)
        r = requests.get(urls)

    print('Reading the page')
    print('..............')
    html = r.text

    print('Creating our soup')
    print('..............')
    soup = BeautifulSoup(html, 'lxml')

    td = {}

    tables = soup.findAll('table')

    print('parsing through our data and taking the needed')
    print('...............')
    for i in range(len(tables)):
        table_rows = tables[i].select('tr')

        td['Name'] = table_rows[0].findAll('td')[0].text.strip()

        td['Level'] = table_rows[2].findAll('td')[2].text.strip()

        td['District'] = table_rows[3].findAll('td')[2].text.strip()

        td['Region'] = table_rows[4].findAll('td')[2].text.strip()

        td['Gender'] = gender

        td['Type'] = typ

        print('{0}, {1}'.format(td['Name'], td['Level']))
        print('{0}, {1}'.format(td['Region'], td['District']))
        print('{0}, {1}'.format(td['Gender'], td['Type']))

        print('Creating and Opening an append file to dump the data in a JSON format:secondary.json')
        print('.............')
        import json
        file = open("secondary.json", "a")
        print('Dumping the data')
        print('........')
        json.dump(td, file, separators=(',', ':'))
        print('Done dumping, closing file')
        print('')
        file.close()


# This function scrapes the pages and calls the mongodb function in primary school loop
def scrapep(urls):
    print('Opening the urls for parsing')
    print('...........')
    try:
        # req = urllib.request.Request(url, headers={'User-Agent': "Magic Browser"})
        # use above if the site blocks or refuses your connection(when using urllib.request)
        r = requests.get(urls)
    except:
        time.sleep(4)
        r = requests.get(urls)

    print('Reading the page')
    print('..............')
    html = r.text

    print('Creating our soup')
    print('............')
    soup = BeautifulSoup(html, 'lxml')

    td = {}

    tables = soup.findAll('table')

    print('parsing through our data and taking the needed')
    print('.........')
    for i in range(len(tables)):
        table_rows = tables[i].select('tr')

        td['Name'] = table_rows[0].findAll('td')[0].text.strip()

        td['Type'] = table_rows[2].findAll('td')[0].text.strip()

        td['District'] = table_rows[3].findAll('td')[2].text.strip()

        td['Region'] = table_rows[4].findAll('td')[2].text.strip()

        print('Data extracted is:')
        print('')
        print('{0}, {1}'.format(td['Name'], td['Type']))
        print('{0}, {1}'.format(td['Region'], td['District']))
        print('')

        print('Creating and Opening an append file to dump the data in a JSON format:primary.json')
        print('......')
        import json
        file = open("primary.json", "a")
        print('Dumping the data')
        print('......')
        json.dump(td, file, separators=(',', ':'))
        print('Done dumping, closing file')
        print('')
        file.close()


# This function opens each page, checks the total results, calculates the amount of pages
# and loops through these pages per district
def pagnums(urls):
    try:
        # req = urllib.request.Request(url, headers={'User-Agent': "Magic Browser"})
        # use above if the site blocks or refuses your connection(when using urllib.request)
        r = requests.get(urls)
    except:
        time.sleep(4)
        r = requests.get(urls)

    html = r.text

    soup = BeautifulSoup(html, 'lxml')

    results = soup.findAll('b')

    total_schools = int(results[2].text)

    print('Opening the page and getting page no for total pages to parse')
    print('...........')
    if total_schools < 10:
        pageno = 1
    elif total_schools == 0:
        pass
    else:
        pagenum = round(int(results[2].text) / 10)

        pageno = pagenum + 1

    print('Total pages to parse in this area are: ' + str(pageno))
    print('')
    return pageno


# This function opens each page, checks the total results, calculates the amount of pages
# and loops through these pages per district
def pagnump(urls):
    try:
        # req = urllib.request.Request(url, headers={'User-Agent': "Magic Browser"})
        # use above if the site blocks or refuses your connection(when using urllib.request)
        r = requests.get(urls)
    except:
        time.sleep(4)
        r = requests.get(urls)

    html = r.text

    soup = BeautifulSoup(html, 'lxml')

    results = soup.findAll('b')

    total_schools = int(results[1].text)

    print('Opening the page and getting page no for total pages to parse')
    print('........')
    if total_schools < 10:
        pageno = 1
    elif total_schools == 0:
        pass
    else:
        pagenum = round(int(results[1].text) / 10)

        pageno = pagenum + 1

    print('Total pages to parse in this area are: ' + str(pageno))
    print('')
    return pageno


# This is the actual program
# it 1st loops the schools
for school in all_schools:
    # then checks for appropriate value
    print('Starting with Primary schools now: ')
    print('Scraping primary schools into primary.json now: ')
    print('..........')
    if school is 'primary':
        # this is a nested loop for the actual values, that is, region, then district then page no.
        for region in regions:
            if region is regions[0]:
                for district in Arusha:
                    # urls = []
                    urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                        1) + "&region=" + region + "&district=" + district

                    for pgno in range(pagnump(urls)):
                        # urls = []
                        urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                            pgno + 1) + "&region=" + region + "&district=" + district
                        # print(urls)
                        scrapep(urls)
                        time.sleep(1)

            if region is regions[1]:
                daregion = 'Dar+es+Salaam'
                for district in Dar_es_Salaam:
                    urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                        1) + "&region=" + daregion + "&district=" + district
                    for pgno in range(pagnump(urls)):
                        # urls = []
                        urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                            pgno + 1) + "&region=" + daregion + "&district=" + district
                        # print(urls)
                        scrapep(urls)
                        time.sleep(1)

            if region is regions[2]:
                for district in Dodoma:
                    # urls = []
                    urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                        1) + "&region=" + region + "&district=" + district

                    for pgno in range(pagnump(urls)):
                        # urls = []
                        urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                            pgno + 1) + "&region=" + region + "&district=" + district
                        # print(urls)
                        scrapep(urls)
                        time.sleep(1)

            if region is regions[3]:
                for district in Iringa:
                    # urls = []
                    urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                        1) + "&region=" + region + "&district=" + district

                    for pgno in range(pagnump(urls)):
                        # urls = []
                        urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                            pgno + 1) + "&region=" + region + "&district=" + district
                        # print(urls)
                        scrapep(urls)
                        time.sleep(1)

            if region is regions[4]:
                for district in Kagera:
                    # urls = []
                    urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                        1) + "&region=" + region + "&district=" + district

                    for pgno in range(pagnump(urls)):
                        # urls = []
                        urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                            pgno + 1) + "&region=" + region + "&district=" + district
                        # print(urls)
                        scrapep(urls)
                        time.sleep(1)

            if region is regions[5]:
                for district in Kigoma:
                    # urls = []
                    urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                        1) + "&region=" + region + "&district=" + district

                    for pgno in range(pagnump(urls)):
                        # urls = []
                        urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                            pgno + 1) + "&region=" + region + "&district=" + district
                        # print(urls)
                        scrapep(urls)
                        time.sleep(1)

            if region is regions[6]:
                for district in Kilimanjaro:
                    # urls = []
                    urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                        1) + "&region=" + region + "&district=" + district

                    for pgno in range(pagnump(urls)):
                        # urls = []
                        urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                            pgno + 1) + "&region=" + region + "&district=" + district
                        # print(urls)
                        scrapep(urls)
                        time.sleep(1)

            if region is regions[7]:
                for district in Lindi:
                    # urls = []
                    urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                        1) + "&region=" + region + "&district=" + district

                    for pgno in range(pagnump(urls)):
                        # urls = []
                        urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                            pgno + 1) + "&region=" + region + "&district=" + district
                        # print(urls)
                        scrapep(urls)
                        time.sleep(1)

            if region is regions[8]:
                for district in Manyara:
                    # urls = []
                    urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                        1) + "&region=" + region + "&district=" + district

                    for pgno in range(pagnump(urls)):
                        # urls = []
                        urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                            pgno + 1) + "&region=" + region + "&district=" + district
                        # print(urls)
                        scrapep(urls)
                        time.sleep(1)

            if region is regions[9]:
                for district in Mara:
                    # urls = []
                    urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                        1) + "&region=" + region + "&district=" + district

                    for pgno in range(pagnump(urls)):
                        # urls = []
                        urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                            pgno + 1) + "&region=" + region + "&district=" + district
                        # print(urls)
                        scrapep(urls)
                        time.sleep(1)

            if region is regions[10]:
                for district in Mbeya:
                    # urls = []
                    urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                        1) + "&region=" + region + "&district=" + district

                    for pgno in range(pagnump(urls)):
                        # urls = []
                        urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                            pgno + 1) + "&region=" + region + "&district=" + district
                        # print(urls)
                        scrapep(urls)
                        time.sleep(1)

            if region is regions[11]:
                for district in Morogoro:
                    # urls = []
                    urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                        1) + "&region=" + region + "&district=" + district

                    for pgno in range(pagnump(urls)):
                        # urls = []
                        urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                            pgno + 1) + "&region=" + region + "&district=" + district
                        # print(urls)
                        scrapep(urls)
                        time.sleep(1)

            if region is regions[12]:
                for district in Mtwara:
                    # urls = []
                    urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                        1) + "&region=" + region + "&district=" + district

                    for pgno in range(pagnump(urls)):
                        # urls = []
                        urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                            pgno + 1) + "&region=" + region + "&district=" + district
                        # print(urls)
                        scrapep(urls)
                        time.sleep(1)

            if region is regions[13]:
                for district in Mwanza:
                    # urls = []
                    urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                        1) + "&region=" + region + "&district=" + district

                    for pgno in range(pagnump(urls)):
                        # urls = []
                        urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                            pgno + 1) + "&region=" + region + "&district=" + district
                        # print(urls)
                        scrapep(urls)
                        time.sleep(1)

            if region is regions[14]:
                for district in Pwani:
                    # urls = []
                    urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                        1) + "&region=" + region + "&district=" + district

                    for pgno in range(pagnump(urls)):
                        # urls = []
                        urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                            pgno + 1) + "&region=" + region + "&district=" + district
                        # print(urls)
                        scrapep(urls)
                        time.sleep(1)

            if region is regions[15]:
                for district in Rukwa:
                    # urls = []
                    urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                        1) + "&region=" + region + "&district=" + district

                    for pgno in range(pagnump(urls)):
                        # urls = []
                        urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                            pgno + 1) + "&region=" + region + "&district=" + district
                        # print(urls)
                        scrapep(urls)
                        time.sleep(1)

            if region is regions[16]:
                for district in Ruvuma:
                    # urls = []
                    urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                        1) + "&region=" + region + "&district=" + district

                    for pgno in range(pagnump(urls)):
                        # urls = []
                        urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                            pgno + 1) + "&region=" + region + "&district=" + district
                        # print(urls)
                        scrapep(urls)
                        time.sleep(1)

            if region is regions[17]:
                for district in Shinyanga:
                    # urls = []
                    urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                        1) + "&region=" + region + "&district=" + district

                    for pgno in range(pagnump(urls)):
                        # urls = []
                        urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                            pgno + 1) + "&region=" + region + "&district=" + district
                        # print(urls)
                        scrapep(urls)
                        time.sleep(1)

            if region is regions[18]:
                for district in Singida:
                    # urls = []
                    urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                        1) + "&region=" + region + "&district=" + district

                    for pgno in range(pagnump(urls)):
                        # urls = []
                        urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                            pgno + 1) + "&region=" + region + "&district=" + district
                        # print(urls)
                        scrapep(urls)
                        time.sleep(1)

            if region is regions[19]:
                for district in Tabora:
                    # urls = []
                    urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                        1) + "&region=" + region + "&district=" + district

                    for pgno in range(pagnump(urls)):
                        # urls = []
                        urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                            pgno + 1) + "&region=" + region + "&district=" + district
                        # print(urls)
                        scrapep(urls)
                        time.sleep(1)

            if region is regions[20]:
                for district in Tanga:
                    # urls = []
                    urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                        1) + "&region=" + region + "&district=" + district

                    for pgno in range(pagnump(urls)):
                        # urls = []
                        urls = "http://www.schoolsinfo.co.tz/?SchType=primary&Page=" + str(
                            pgno + 1) + "&region=" + region + "&district=" + district
                        # print(urls)
                        scrapep(urls)
                        time.sleep(1)

    # this checks for appropriate value also.
    print('Going on with Secondary schools now: ')
    print('Scraping secondary schools to secondary.json now: ')
    print('.............')
    if school is 'secondary':
        # this is a nested loop for the actual values, that is, region, gender, type, then district then page no.
        for region in regions:
            for gender in schoolgen:
                for typ in schooltyp:
                    if region is regions[0]:
                        for district in Arusha:
                            # urls = []
                            urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ

                            for pgno in range(pagnums(urls)):
                                # urls = []
                                urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                    1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ
                                # print(urls)
                                scrapes(urls)
                                time.sleep(1)

                    if region is regions[1]:
                        daregion = 'Dar+es+Salaam'
                        for district in Dar_es_Salaam:
                            # urls = []
                            urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                1) + "&region=" + daregion + "&district=" + district + "&gender=" + gender + "&status=" + typ

                            for pgno in range(pagnums(urls)):
                                # urls = []
                                urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                    1) + "&region=" + daregion + "&district=" + district + "&gender=" + gender + "&status=" + typ
                                # print(urls)
                                scrapes(urls)
                                time.sleep(1)

                    if region is regions[2]:
                        for district in Dodoma:
                            # urls = []
                            urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ

                            for pgno in range(pagnums(urls)):
                                # urls = []
                                urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                    1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ
                                # print(urls)
                                scrapes(urls)
                                time.sleep(1)

                    if region is regions[3]:
                        for district in Iringa:
                            # urls = []
                            urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ

                            for pgno in range(pagnums(urls)):
                                # urls = []
                                urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                    1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ
                                # print(urls)
                                scrapes(urls)
                                time.sleep(1)

                    if region is regions[4]:
                        for district in Kagera:
                            # urls = []
                            urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ

                            for pgno in range(pagnums(urls)):
                                # urls = []
                                urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                    1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ
                                # print(urls)
                                scrapes(urls)
                                time.sleep(1)

                    if region is regions[5]:
                        for district in Kigoma:
                            # urls = []
                            urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ

                            for pgno in range(pagnums(urls)):
                                # urls = []
                                urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                    1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ
                                # print(urls)
                                scrapes(urls)
                                time.sleep(1)

                    if region is regions[6]:
                        for district in Kilimanjaro:
                            # urls = []
                            urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ

                            for pgno in range(pagnums(urls)):
                                # urls = []
                                urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                    1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ
                                # print(urls)
                                scrapes(urls)
                                time.sleep(1)

                    if region is regions[7]:
                        for district in Lindi:
                            # urls = []
                            urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ

                            for pgno in range(pagnums(urls)):
                                # urls = []
                                urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                    1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ
                                # print(urls)
                                scrapes(urls)
                                time.sleep(1)

                    if region is regions[8]:
                        for district in Manyara:
                            # urls = []
                            urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ

                            for pgno in range(pagnums(urls)):
                                # urls = []
                                urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                    1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ
                                # print(urls)
                                scrapes(urls)
                                time.sleep(1)

                    if region is regions[9]:
                        for district in Mara:
                            # urls = []
                            urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ

                            for pgno in range(pagnums(urls)):
                                # urls = []
                                urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                    1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ
                                # print(urls)
                                scrapes(urls)
                                time.sleep(1)

                    if region is regions[10]:
                        for district in Mbeya:
                            # urls = []
                            urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ

                            for pgno in range(pagnums(urls)):
                                # urls = []
                                urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                    1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ
                                # print(urls)
                                scrapes(urls)
                                time.sleep(1)

                    if region is regions[11]:
                        for district in Morogoro:
                            # urls = []
                            urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ

                            for pgno in range(pagnums(urls)):
                                # urls = []
                                urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                    1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ
                                # print(urls)
                                scrapes(urls)
                                time.sleep(1)

                    if region is regions[12]:
                        for district in Mtwara:
                            # urls = []
                            urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ

                            for pgno in range(pagnums(urls)):
                                # urls = []
                                urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                    1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ
                                # print(urls)
                                scrapes(urls)
                                time.sleep(1)

                    if region is regions[13]:
                        for district in Mwanza:
                            # urls = []
                            urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ

                            for pgno in range(pagnums(urls)):
                                # urls = []
                                urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                    1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ
                                # print(urls)
                                scrapes(urls)
                                time.sleep(1)

                    if region is regions[14]:
                        for district in Pwani:
                            # urls = []
                            urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ

                            for pgno in range(pagnums(urls)):
                                # urls = []
                                urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                    1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ
                                # print(urls)
                                scrapes(urls)
                                time.sleep(1)

                    if region is regions[15]:
                        for district in Rukwa:
                            # urls = []
                            urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ

                            for pgno in range(pagnums(urls)):
                                # urls = []
                                urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                    1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ
                                # print(urls)
                                scrapes(urls)
                                time.sleep(1)

                    if region is regions[16]:
                        for district in Ruvuma:
                            # urls = []
                            urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ

                            for pgno in range(pagnums(urls)):
                                # urls = []
                                urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                    1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ
                                # print(urls)
                                scrapes(urls)
                                time.sleep(1)

                    if region is regions[17]:
                        for district in Shinyanga:
                            # urls = []
                            urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ

                            for pgno in range(pagnums(urls)):
                                # urls = []
                                urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                    1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ
                                # print(urls)
                                scrapes(urls)
                                time.sleep(1)

                    if region is regions[18]:
                        for district in Singida:
                            # urls = []
                            urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ

                            for pgno in range(pagnums(urls)):
                                # urls = []
                                urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                    1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ
                                # print(urls)
                                scrapes(urls)
                                time.sleep(1)

                    if region is regions[19]:
                        for district in Tabora:
                            # urls = []
                            urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ

                            for pgno in range(pagnums(urls)):
                                # urls = []
                                urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                    1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ
                                # print(urls)
                                scrapes(urls)
                                time.sleep(1)

                    if region is regions[20]:
                        for district in Tanga:
                            # urls = []
                            urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ

                            for pgno in range(pagnums(urls)):
                                # urls = []
                                urls = "http://www.schoolsinfo.co.tz/?Page=" + str(
                                    1) + "&region=" + region + "&district=" + district + "&gender=" + gender + "&status=" + typ
                                # print(urls)
                                scrapes(urls)
                                time.sleep(1)
                            print('Finishing some things.')
                            print('Now exiting......')
                            raise SystemExit('Done.!')
