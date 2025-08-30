########### Python 3.2 #############
import urllib.request, json

def fetch_series():
    try:
        url = "https://api.riksbank.se/swea/v1/Series?language=en"

        hdr ={
        # Request headers
        'Cache-Control': 'no-cache',
        }

        req = urllib.request.Request(url, headers=hdr)

        req.get_method = lambda: 'GET'
        response = urllib.request.urlopen(req)
        if response.getcode() != 200:
            raise Exception(f"Error fetching series: {response.getcode()}")

        data = json.loads(response.read())
    except Exception as e:
        print(e)
    return data
####################################


def save_series(data, cursor, conn):
    # Save results into series table
    for item in data:
        cursor.execute('''
            INSERT OR IGNORE INTO series (seriesId, source, shortDescription, midDescription, longDescription, groupID, observationMaxDate, observationMinDate, seriesClosed)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            item['seriesId'],
            item['source'],
            item['shortDescription'],
            item['midDescription'],
            item['longDescription'],
            item['groupId'],
            item['observationMaxDate'],
            item['observationMinDate'],
            int(item.get('seriesClosed'))
        ))
    conn.commit()