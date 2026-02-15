# Wasserverbrauch Analyse (Water Consumption Analysis)

Dieses Repository behandelt das **Einlesen → Bereinigung → Analyse/Visualisierung → (optional) Forecasting** von realen Wasserverbrauchsdaten (Monatsverbräuche).

## Quickstart

### 1) Repo klonen / öffnen
- Lokal: ZIP entpacken und mit **GitHub Desktop** als Repository hinzufügen (oder neues Repo daraus erstellen).
- Terminal:
```bash
git init
git add .
git commit -m "Initial commit: Wasserverbrauch Analyse"
```

### 2) Python-Umgebung
Empfohlen: Python **3.10+**
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate

pip install -U pip
pip install -r requirements-dev.txt
```

### 3) Notebooks
Die bereitgestellten Notebooks liegen unter `notebooks/`.
```bash
jupyter lab
```

## Daten

- Rohdaten gehören nach `data/raw/` (werden standardmäßig **nicht** committed).
- Ergebnisse/Exports: `exports/` (standardmäßig ignoriert; bei Bedarf `.gitignore` anpassen).

## Projektstruktur (Kurz)
- `notebooks/` – explorative Analyse & Prototyping
- `src/` – wiederverwendbarer Code (load/clean/features/plots)
- `reports/` – Reports & Abbildungen
- `data/` – Roh-/Zwischen-/aufbereitete Daten

## Reproduzierbare Runs (Optional)
CLI-Skelett:
```bash
python -m src.cli train --config configs/config.yaml
python -m src.cli predict --config configs/config.yaml
```

## Lizenz
Siehe `LICENSE`.
