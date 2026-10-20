# Conference Company Shortlist

A Python command-line tool for reviewing high-priority companies
before a career fair or networking event.

## Features

- Reads company priorities and reference details from CSV files.
- Matches records using company IDs.
- Displays selected companies and booth numbers.
- Handles priority capitalization and surrounding spaces.
- Reports unmatched IDs and an empty shortlist.
- Includes a public demo using fictional data.

## Requirements

Python 3. No additional packages required.

## Run the demo

Open a terminal in the project folder:

```bash
python3 company_shortlist.py --demo
```

The demo uses sample_companies.csv and sample_reference.csv.

## Example demo output

```text
High-Priority Companies

DEMO001 — Example Software — Booth 101
DEMO003 — Demo Systems — Booth 103

Total high-priority companies: 2
```

## Use personal data

Create a data folder containing these two files.

company_reference.csv:

```csv
company_id,company,booth
C001,Your chosen company,123
```

my_shortlist.csv:

```csv
company_id,target_role,priority,notes
C001,,High,
```

Use matching company IDs in both files, then run:

```bash
python3 company_shortlist.py
```

The data folder is excluded from Git. Keep a separate backup
of personal research if needed.

Company IDs connect records; they do not anonymize identifying
details if those details are published.

## Checks performed

- Demo mode displays two high-priority companies.
- Uppercase priorities and surrounding spaces are accepted.
- No high-priority entries produces a friendly message.
- Confirmed personal data files are excluded from Git.

## What I practiced

- Reading CSV files with csv.DictReader.
- Filtering records and using dictionary lookups.
- Matching records across two files using IDs.
- Selecting demo mode with a command-line argument.
- Separating personal data from public examples.

## Limitations

- Files must contain the expected column headings.
- Results follow shortlist file order.
- Target roles and notes are stored but not displayed yet.
- Missing files produce an error.
- Personal exhibitor details require manual updates.

## Data source

Public demo records are fictional.

Personal conference research was sourced from the official WE26
exhibitor list and checked on October 19, 2026:

https://we26.swe.org/exhibitor-partner/list-of-committed-exhibitors/

Exhibitor attendance does not confirm specific job openings.