# !pip install feedparser
import feedparser
import pandas as pd
import pytz
from bs4 import BeautifulSoup
import unicodedata


def getCampusLabsFromRSS():
    url = 'https://uncw.campuslabs.com/engage/events.rss'
    feed = feedparser.parse(url)

    data = []
    for entry in feed.entries:
        title = entry.title
        host = entry.host
        soup = BeautifulSoup(entry.summary, 'html.parser')
        description = soup.find('div', {'class': 'p-description description'}).text.strip()
        description = unicodedata.normalize('NFKD', description).replace("\n", " ")
        link = entry.link
        location = entry.location
        start = pd.to_datetime(entry.start).tz_localize(None)
        end = pd.to_datetime(entry.start).tz_localize(None)

        data.append({'Title': title, 'Host': host, 'Description': description, 'Link': link, 'Location': location,
                     'Start': start, 'End': end})

    WaveLink = pd.DataFrame(data)
    # WaveLink

    # est_tz = pytz.timezone('US/Eastern')
    # WaveLink['Start'] = pd.to_datetime(WaveLink['Start']).dt.tz_convert(est_tz)
    # WaveLink['End'] = pd.to_datetime(WaveLink['End']).dt.tz_convert(est_tz)
    # WaveLink.info()

    return WaveLink

def getSportsFromRSS():
    url = 'https://uncwsports.com/calendar.ashx/calendar.rss?sport_id=0&_=clg75i7gn0001359j7snfrdpa'
    feed = feedparser.parse(url)

    data = []
    for entry in feed.entries:
        title = entry.title
        description = entry.summary.replace('/n', '')
        link = entry.link
        location = entry.ev_location
        start = pd.to_datetime(entry.ev_startdate).dt.tz_localize(None)
        end = pd.to_datetime(entry.ev_enddate).dt.tz_localize(None)

        data.append({'Title': title, 'Description': description, 'Link': link, 'Location': location, 'Start': start,
                     'End': end})

    SportsCalendar = pd.DataFrame(data)
    # SportsCalendar.head()

    return SportsCalendar
def getLibraryFromRSS():
    url = 'https://library.uncw.edu/events_exhibits/events/feed'
    feed = feedparser.parse(url)

    data = []
    for entry in feed.entries:
        title = entry.title
        description = entry.summary.replace('/n', '')
        link = entry.link
        location = entry.ev_location
        # start = pd.to_datetime(entry.ev_startdate)
        # end = pd.to_datetime(entry.ev_enddate)
        start, end = 0, 0


        data.append({'Title': title, 'Description': description, 'Link': link, 'Location': location, 'Start': start,
                     'End': end})

    LibraryCalendar = pd.DataFrame(data)
    # SportsCalendar.head()

    return LibraryCalendar