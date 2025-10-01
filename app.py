import argparse, os, sqlite3, random
from datetime import datetime, timedelta
import pandas as pd

DB_PATH = os.path.join(os.path.dirname(__file__), "app.db")
REPORT_SQL_PATH = os.path.join(os.path.dirname(__file__), "report.sql")

def seed():
    # Start fresh
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Schema
    cur.executescript("""
    DROP TABLE IF EXISTS "order";
    DROP TABLE IF EXISTS "shippackage";

    CREATE TABLE "order"(
        id INTEGER PRIMARY KEY,
        xid TEXT,
        CustomPartnerId TEXT,
        SortedOnUtc TEXT,             -- ISO8601 datetime
        TotalWeightLbs REAL,
        ShippingBase REAL,
        ShippingAmount REAL,
        FactoryId INTEGER,
        ShippingPriority INTEGER,
        IsInvoiced INTEGER,           -- 0/1
        IsShippingInvoiced INTEGER,   -- 0/1
        ShippingCarrier TEXT,
        InvoiceWeek TEXT              -- e.g., '2024-W14'
    );

    CREATE TABLE "shippackage"(
        id INTEGER PRIMARY KEY,
        OrderId INTEGER,
        TrackingNumber TEXT,
        FOREIGN KEY(OrderId) REFERENCES "order"(id)
    );
    """)

    # Deterministic fake data so results are reproducible
    random.seed(42)
    carriers = ["DHLGM", "UPS", "FedEx"]
    partners = ["printify", "teepublicvip", "brewcity", "acme"]
    start = datetime(2023, 11, 1)

    orders = []
    pkgs = []
    oid = 1
    pid = 1

    for day in range(0, 365):
        d = start + timedelta(days=day)
        for _ in range(random.randint(1, 6)):
            partner = random.choice(partners)
            factory = random.choice([1, 2, 3])
            carrier = random.choice(carriers)
            is_inv = int(random.random() < 0.8)
            is_ship_inv = int(random.random() < 0.7)
            total_weight = round(random.uniform(0.2, 25.0), 2)
            ship_base = round(random.uniform(2.00, 20.00), 2)
            ship_amt = round(ship_base + random.uniform(0.5, 5.0), 2)
            prio = random.choice([1, 2, 3])
            iw = f"{d.isocalendar().year}-W{d.isocalendar().week:02d}" if is_inv else None

            xid = f"{d.strftime('%y%m%d')}{oid:06d}"
            orders.append((oid, xid, partner, d.isoformat(), total_weight, ship_base, ship_amt,
                           factory, prio, is_inv, is_ship_inv, carrier, iw))

            for p in range(random.randint(1, 3)):
                tracking = f"{carrier}-{oid:06d}-{p+1:02d}"
                pkgs.append((pid, oid, tracking))
                pid += 1

            oid += 1

    cur.executemany("""
        INSERT INTO "order"(id, xid, CustomPartnerId, SortedOnUtc, TotalWeightLbs, ShippingBase,
                            ShippingAmount, FactoryId, ShippingPriority, IsInvoiced,
                            IsShippingInvoiced, ShippingCarrier, InvoiceWeek)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, orders)

    cur.executemany("""
        INSERT INTO "shippackage"(id, OrderId, TrackingNumber) VALUES (?, ?, ?);
    """, pkgs)

    conn.commit()
    conn.close()
    print("Seeded fake data into", DB_PATH)

def run_report(carrier, factory, start, out_csv=None):
    conn = sqlite3.connect(DB_PATH)
    with open(REPORT_SQL_PATH, "r") as f:
        sql = f.read()
    params = {"carrier": carrier, "factory": factory, "start": start}
    df = pd.read_sql_query(sql, conn, params=params)
    conn.close()

    print("\n=== Report Parameters ===")
    print(params)
    print("\n=== Sample Rows (first 10) ===")
    print(df.head(10).to_string(index=False))

    print("\n=== Summary ===")
    if df.empty:
        print("No rows found.")
    else:
        total_orders = df['id'].nunique()
        total_pkgs = len(df)
        total_ship_base = df['ShippingBase'].sum()
        total_ship_amount = df['ShippingAmount'].sum()
        print(f"Orders: {total_orders:,} | Packages: {total_pkgs:,}")
        print(f"ShippingBase: ${total_ship_base:,.2f} | ShippingAmount: ${total_ship_amount:,.2f}")

    if out_csv:
        df.to_csv(out_csv, index=False)
        print(f"\nSaved CSV to {out_csv}")

def main():
    parser = argparse.ArgumentParser(description="Shipping invoice report (SQLite + Python).")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("seed", help="Create/refresh SQLite DB with fake data.")

    pr = sub.add_parser("report", help="Run the invoiced shipments report.")
    pr.add_argument("--carrier", default="DHLGM")
    pr.add_argument("--factory", type=int, default=2)
    pr.add_argument("--start", default="2023-12-01")
    pr.add_argument("--out", dest="out_csv")

    args = parser.parse_args()
    if args.cmd == "seed":
        seed()
    elif args.cmd == "report":
        run_report(args.carrier, args.factory, args.start, args.out_csv)

if __name__ == "__main__":
    main()
