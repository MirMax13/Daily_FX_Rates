import sqlite3
from sql import init_db
from series import fetch_series, save_series
from observation import fetch_and_save_latest_observation, needs_update


def main():

    conn = sqlite3.connect("fx_rates.db")
    cursor = conn.cursor()

    init_db(cursor)

    series_list = fetch_series()
    save_series(series_list, cursor, conn)

    cursor.execute('SELECT seriesId, observationMaxDate FROM series')
    series_data = cursor.fetchall()
    print(series_data)

    for sid, latest_date in series_data:
        if needs_update(sid, latest_date, cursor):
            fetch_and_save_latest_observation((sid,), cursor, conn)
        else:
            print(f"⏩ {sid}: Already up-to-date ({latest_date})")

    conn.close()


if __name__ == "__main__":
    main()
