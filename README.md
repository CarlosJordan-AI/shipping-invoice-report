# Shipping Invoice Report (SQLite + Python)

This demo simulates a real operations/3PL report:
**Find all invoiced shipments for a carrier from a start date and factory**, including tracking numbers and invoice week.

## Why this matters
- Finance: reconcile shipping charges per carrier/site
- Ops: monitor volumes and package counts
- Customer Care: quickly fetch tracking numbers

## How to run in GitHub

### Option 1 — Codespaces (interactive)
1. Open this repo → Code (green button) → **Create codespace on main**.
2. In the Codespace terminal:
   ```bash
   pip install -r requirements.txt
   python app.py seed
   python app.py report --carrier DHLGM --factory 2 --start 2023-12-01 --out shipments.csv
