import sqlite3
from sql import init_db
from series import fetch_series, save_series
from observation import fetch_and_save_latest_observation


def main():

    conn = sqlite3.connect("fx_rates.db")
    cursor = conn.cursor()

    init_db(cursor)

    series_list = fetch_series()
    save_series(series_list, cursor, conn)

    cursor.execute("SELECT seriesId FROM series")
    series_ids = cursor.fetchall()
    for series_id in series_ids:
        fetch_and_save_latest_observation(series_id, cursor, conn)

    conn.close()


if __name__ == "__main__":
    main()
