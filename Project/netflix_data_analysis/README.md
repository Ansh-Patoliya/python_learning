# 🎬 Netflix Data Analysis — Quick Guide

## Description
Beginner‑friendly EDA of Netflix titles using Pandas and Matplotlib. Load the CSV, do light cleaning, explore trends (movies vs shows, years, countries, genres, ratings), and plot simple visuals — all in one notebook.

---

## Files
- Notebook: `netflix_data_analysis.ipynb`
- Dataset: `netflix_titles.csv` (kept in the same folder)

---

## Setup (Windows)
```
python -m venv .venv
.venv\Scripts\activate
pip install -U pip
pip install -r ..\..\requirements.txt
```
Optional (if needed):
```
pip install scipy
```

---

## Run
```
jupyter notebook
```
Open: `Project/netflix_data_analysis/netflix_data_analysis.ipynb`

Tip: VS Code or PyCharm Jupyter support works too.

---

## What you’ll learn
- Quick data overview: head/info/shape, missing values
- Cleaning basics: dates, ratings, simple text fields
- Feature columns: added_year/month/weekday, release_decade
- Explorations: movies vs shows, year/country/genre/rating counts
- Visuals: bars, hist, pie, simple line (Matplotlib)

---

## Troubleshooting
- File not found: open the notebook from the repo root or correct the path.
- Encoding: CSV loads with `encoding='latin1'` in the notebook; keep the file as‑is.
- Extra imports: if you see errors for optional libraries (e.g., SciPy), install them or remove the unused import lines.

---

Learning-focused project. Keep plots simple and labels clear.
