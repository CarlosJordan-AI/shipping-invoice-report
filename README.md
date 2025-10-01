# 📦 Shipping Invoice Report (SQLite + Python)

> **Portfolio project** — This demo uses **fake but realistic data** to simulate a real-world **operations & finance report**:  
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

---

### 🧠 Key highlights
- Parameterized SQL query (`:carrier`, `:factory`, `:start`)  
- Reproducible fake dataset seeded automatically  
- Outputs `shipments.csv` with order, carrier, and invoice data  
- Optional: run interactively in **Codespaces**, or trigger via **GitHub Actions**  
