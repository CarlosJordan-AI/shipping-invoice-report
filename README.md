# 📦 Shipping Invoice Report (SQLite + Python)

> This project showcases how SQL + Python automation can generate reports used in real-world logistics or finance workflows.
> This demo uses **fake but realistic data** to simulate a real-world **operations & finance report**:  


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
### Option 2 — Workflows (interactive)
Run the below Workflow:
> _“Find all invoiced shipments for a carrier from a start date and factory, with tracking numbers and invoice weeks.”_

[![Run Report](https://github.com/CarlosJordan-AI/shipping-invoice-report/actions/workflows/run-report.yml/badge.svg)](https://github.com/CarlosJordan-AI/shipping-invoice-report/actions/workflows/run-report.yml)

The above link redirects you to:
<img width="1285" height="526" alt="image" src="https://github.com/user-attachments/assets/7cc3b2f5-3156-4417-b75c-7d9312ef84cb" />

After it completes (about 15 seg), enter in the workflow and download the file for preview:

<img width="1530" height="537" alt="image" src="https://github.com/user-attachments/assets/643ad323-d871-46fc-81d8-93b4677c0555" />


Output preview:

<img width="1355" height="655" alt="image" src="https://github.com/user-attachments/assets/a511fe24-6067-4cb1-b333-25373899b242" />


### 🧠 Key highlights
- Parameterized SQL query (`:carrier`, `:factory`, `:start`)  
- Reproducible fake dataset seeded automatically  
- Outputs `shipments.csv` with order, carrier, and invoice data  
- Optional: run interactively in **Codespaces**, or trigger via **GitHub Actions**  
