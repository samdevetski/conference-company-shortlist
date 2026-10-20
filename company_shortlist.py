import csv
import sys
from pathlib import Path

project_folder = Path(__file__).parent
demo_mode = "--demo" in sys.argv
#python3 company_shortlist.py --demo
#python3 company_shortlist.py

if demo_mode:
    shortlist_path = project_folder / "sample_companies.csv"
    reference_path = project_folder / "sample_reference.csv"
else:
    shortlist_path = project_folder / "data" / "my_shortlist.csv"
    reference_path = project_folder / "data" / "company_reference.csv"

company_reference = {}

with open(reference_path, newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        company_reference[row["company_id"]] = row


with open(shortlist_path, newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    high_priority = []

    for row in reader:
        if row["priority"].strip().lower() == "high":
            high_priority.append(row)
            
if len(high_priority) == 0:
    print("No high-priority companies selected.")
else:
    print("High-Priority Companies")
    print()

    for company in high_priority:
        company_id = company["company_id"]
        details = company_reference.get(company_id)

        if details is None:
            print(f"{company_id}: No matching company reference.")
        else:
            print(
                f"{company_id} — {details['company']} "
                f"— Booth {details['booth']}"
            )

    print()
    print("Total high-priority companies:", len(high_priority))