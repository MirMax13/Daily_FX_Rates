########### Python 3.2 #############
import urllib.request, json, time


def fetch_and_save_latest_observation(series_id, cursor, conn, retries=5, delay=15):
    url = f"https://api.riksbank.se/swea/v1/Observations/Latest/{series_id[0]}"
    hdr = {
        # Request headers
        "Cache-Control": "no-cache",
    }
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=hdr)

            req.get_method = lambda: "GET"
            response = urllib.request.urlopen(req)
            if response.getcode() != 200:
                raise Exception(f"HTTP {response.getcode()}")
            # Save results into observations table
            data = json.loads(response.read())

            cursor.execute(
                """
                    INSERT OR IGNORE INTO observations (seriesId, date, value)
                    VALUES (?, ?, ?)
                """,
                (series_id[0], data["date"], data["value"]),
            )
            conn.commit()
            print(f"✅ {series_id[0]}: {data['date']} saved successfully.")
            return
        except Exception as e:
            print(e)
            if "429" in str(e):
                print(
                    f"❌ {series_id[0]}: Rate limit exceeded, retrying in {delay} seconds..."
                )
                time.sleep(delay)


####################################
