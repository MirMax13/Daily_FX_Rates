def init_db(cursor):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS series (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            seriesId TEXT NOT NULL UNIQUE,
            source TEXT NOT NULL,
            shortDescription TEXT NOT NULL,
            midDescription TEXT NOT NULL,
            longDescription TEXT NOT NULL,
            groupID INTEGER NOT NULL,
            observationMaxDate TEXT NOT NULL,
            observationMinDate TEXT NOT NULL,
            seriesClosed INTEGER NOT NULL
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS observations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            seriesId TEXT NOT NULL,
            date TEXT NOT NULL,
            value REAL NOT NULL,
            FOREIGN KEY (seriesId) REFERENCES series(seriesId),
            UNIQUE(seriesId, date)
        )
    """
    )
