# 📦 Shipping Invoice Report (SQLite + Python)

> This project showcases how SQL + Python automation can generate reports used in real-world logistics or finance workflows.
> This demo uses **fake but realistic data** to simulate a real-world **operations & finance report**:  
> _“Find all invoiced shipments for a carrier from a start date and factory, with tracking numbers and invoice weeks.”_

[![Run Report](https://github.com/CarlosJordan-AI/shipping-invoice-report/actions/workflows/run-report.yml/badge.svg)](https://github.com/CarlosJordan-AI/shipping-invoice-report/actions/workflows/run-report.yml)


---

### 🔍 Why this project matters
- **Finance:** reconciles shipping charges per carrier/site  
- **Operations:** monitors volumes and package counts  
- **Customer Care:** provides tracking data quickly  

---

### ⚙️ How it works
This small pipeline combines:
- 🗃️ **SQLite** (lightweight fake database)
- 💡 **SQL** report (`report.sql`)
- 🐍 **Python CLI** (`app.py`) to:
  - seed fake data  
  - execute the report  
  - export the results as a CSV  
- ⚡ **GitHub Actions workflow** for one-click report generation directly on GitHub  

## How to run (in GitHub)

### Option 1 — Codespaces (interactive)
1) Code (green button) → **Create codespace on main**  
2) Terminal:
```bash
pip install -r requirements.txt
python app.py seed
python app.py report --carrier DHLGM --factory 2 --start 2023-12-01 --out shipments.csv
```


---

### 🧠 Key highlights
- Parameterized SQL query (`:carrier`, `:factory`, `:start`)  
- Reproducible fake dataset seeded automatically  
- Outputs `shipments.csv` with order, carrier, and invoice data  
- Optional: run interactively in **Codespaces**, or trigger via **GitHub Actions**  
