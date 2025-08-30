########### Python 3.2 #############
import urllib.request, json
import sqlite3
conn = sqlite3.connect('fx_rates.db')
cursor = conn.cursor()

#For every seriesid in series table do API call
cursor.execute('SELECT seriesId FROM series')
series_ids = cursor.fetchall()

for series_id in series_ids:
    try:
        url = f"https://api.riksbank.se/swea/v1/Observations/Latest/{series_id[0]}"

        hdr = {
            # Request headers
            'Cache-Control': 'no-cache',
        }

        req = urllib.request.Request(url, headers=hdr)

        req.get_method = lambda: 'GET'
        response = urllib.request.urlopen(req)
        # Save results into observations table
        data = json.loads(response.read())
        cursor.execute('''
                INSERT OR IGNORE INTO observations (seriesId, date, value)
                VALUES (?, ?, ?)
            ''', (
                series_id[0],
                data['date'],
                data['value']
            ))
        conn.commit()

        print(response.getcode())
        print(response.read())
    except Exception as e:
        print(e)
####################################


# Close connection
conn.close()