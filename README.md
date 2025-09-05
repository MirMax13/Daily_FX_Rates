# 📊 Daily FX Rates Fetcher

A Python application that fetches **daily FX rates from the Swedish Riksbank (SWEA API)** and stores them into a local **SQLite database** for further analysis.  

This project was built as a test assignment for a Junior Python Engineer position.  

---

## 🚀 Features

- Fetches the list of all available **series** (exchange rates, interest rates, etc.) via the Riksbank SWEA API.  
- Downloads the **latest observation** (daily rate) for each series.  
- Saves data into a local **SQLite** database.  
- Prevents duplicate inserts with database constraints.  
- Runs inside an isolated Python environment managed by **Poetry**.  
- Code is formatted with **Black** for consistent style.  

---

## 🛠 Requirements

- Python **3.10.8** (or compatible `>=3.10.8,<3.11`)  
- [Poetry](https://python-poetry.org/) package manager  

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MirMax13/Daily_FX_Rates.git
   cd daily-fx-rates
   ```

2. Install dependencies with Poetry:
   ```bash
   poetry install
   ```

---

## ▶️ Usage
Run the main script: 
```bash
poetry run python main.py
```
This will:
1. Ensure the SQLite database (`fx_rates.db`) contains the required tables (`series`, `observations`).  
2. Fetch the list of series from the Riksbank SWEA API.  
3. For each series, fetch the latest available observation.  
4. Insert results into the database, skipping duplicates automatically.

# ⚠️ **Important:**
For best performance, run the script in one go without interruptions.
Stopping and re-running may cause unnecessary API calls and waste the limited number of requests.

## 📂 Project Structure
```
daily-fx-rates/
│
├── main.py             # Orchestrates the workflow
├── sql.py              # Database initialization
├── series.py           # Fetch & save series from API
├── observation.py      # Fetch & save observations
├── database.py         # View database content
│
├── fx_rates.db         # SQLite database (created locally, ignored in git)
│
├── pyproject.toml      # Poetry project config
├── poetry.lock         # Locked dependencies
├── README.md           # Project documentation
└── .gitignore          # Ignored files (db, venv, caches)
```

---

## 🗄 Database Schema
### Table: `series`
| Column             | Type    | Notes                         |
|--------------------|---------|-------------------------------|
| id                 | INTEGER | Primary key                   |
| seriesId           | TEXT    | Unique identifier from API    |
| source             | TEXT    | Data source                   |
| shortDescription   | TEXT    | Short description             |
| midDescription     | TEXT    | Medium description            |
| longDescription    | TEXT    | Detailed description          |
| groupID            | INTEGER | Group identifier              |
| observationMaxDate | TEXT    | Latest available date         |
| observationMinDate | TEXT    | Earliest available date       |
| seriesClosed       | INTEGER | Whether the series is closed  |

### Table: `observations`
| Column   | Type    | Notes                                  |
|----------|---------|----------------------------------------|
| id       | INTEGER | Primary key                            |
| seriesId | TEXT    | Foreign key → `series(seriesId)`       |
| date     | TEXT    | Date of observation                    |
| value    | REAL    | Observed value                         |
| UNIQUE(seriesId, date)     |         |  to avoid duplicates |

---

## 📝 Example Output

When running main.py, you should see logs like:
```bash
💾 SEKEURPMI: 2025-08-29 inserted.
⏩ SEKATSPMI: Already up-to-date (2002-02-28)
💾 USDSEKPMI: 2025-08-29 inserted.

---

```
## ⚡ Development
Format code:
```bash
poetry run black .
```

---

## 🛑 Notes

- **API data from Riksbank is usually delayed by one banking day.**  
  For example, running the script on a weekend may still return data from the last weekday (e.g. Friday).  
- If you exceed API limits (`HTTP 429 Too Many Requests`), the script retries up to **5 times** with a fixed **15s delay**.  

---
