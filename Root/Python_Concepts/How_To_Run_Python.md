# Running the Retail Dataset Generator in VS Code

## Overview

The uploaded file is a Python script that generates a large retail dataset containing approximately **1.4 million records** across multiple CSV files.

Before running the script, ensure that:

* Python 3.9 or later is installed
* VS Code is installed
* Required Python libraries are installed

---

# Step 1: Save the File as a Python Script

Rename the file from:

```text
Pasted text.txt
```

to:

```text
generate_retail_capstone_dataset.py
```

---

# Step 2: Verify Python Installation

Open a terminal and run:

```bash
python --version
```

or

```bash
python3 --version
```

Expected output:

```text
Python 3.x.x
```

---

# Step 3: Open the Project in VS Code

1. Launch VS Code
2. Select **File → Open Folder**
3. Open the folder containing:

```text
generate_retail_capstone_dataset.py
```

---

# Step 4: Create a Virtual Environment (Recommended)

Open the VS Code terminal and execute:

```bash
python -m venv venv
```

---

## Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

After activation, the terminal should display:

```text
(venv)
```

---

# Step 5: Install Required Dependencies

The script requires:

* pandas
* numpy
* faker
* pyarrow (optional for Parquet output)

Install them using:

```bash
pip install pandas numpy faker pyarrow
```

Verify installation:

```bash
pip list
```

---

# Step 6: Execute the Script

The script requires an output directory using the `--out` argument.

## Basic Execution

```bash
python generate_retail_capstone_dataset.py --out ./retail_capstone_v2
```

---

## Execute with Custom Seed

```bash
python generate_retail_capstone_dataset.py --out ./retail_capstone_v2 --seed 23
```

---

## Generate CSV + Parquet Files

```bash
python generate_retail_capstone_dataset.py --out ./retail_capstone_v2 --parquet
```

---

## Disable Progress Messages

```bash
python generate_retail_capstone_dataset.py --out ./retail_capstone_v2 --no-progress
```

---

# Step 7: Expected Output Structure

After successful execution:

```text
retail_capstone_v2/
│
├── data/
│   └── merged/
│       ├── customers_merged.csv
│       ├── products_merged.csv
│       ├── orders_merged.csv
│       ├── order_items_merged.csv
│       └── payments_merged.csv
│
└── logs/
    ├── profiling_summary.json
    └── generation_config.json
```

---

# Step 8: Run Using VS Code Debugger

Create a file:

```text
.vscode/launch.json
```

Add the following configuration:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Retail Dataset Generator",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/generate_retail_capstone_dataset.py",
            "args": [
                "--out",
                "./retail_capstone_v2",
                "--seed",
                "23"
            ],
            "console": "integratedTerminal"
        }
    ]
}
```

Press:

```text
F5
```

to execute the script.

---

# Common Errors and Fixes

## Error: ModuleNotFoundError

Example:

```text
ModuleNotFoundError: No module named 'faker'
```

Solution:

```bash
pip install faker
```

---

## Error: No module named pandas

Solution:

```bash
pip install pandas
```

---

## Error: Permission Denied

Run VS Code as administrator or choose a writable output directory.

---

## Error: Out of Memory

The script generates approximately:

| Entity      |          Rows |
| ----------- | ------------: |
| Customers   |       244,000 |
| Products    |        15,000 |
| Orders      |       205,000 |
| Order Items |       798,000 |
| Payments    |       138,000 |
| **Total**   | **1,400,000** |

Recommendations:

* Minimum 8 GB RAM
* Recommended 16 GB RAM
* At least 5 GB free disk space

---

# Example Complete Execution

```bash
# Create virtual environment
python -m venv venv

# Activate environment
source venv/bin/activate

# Install dependencies
pip install pandas numpy faker pyarrow

# Run generator
python generate_retail_capstone_dataset.py \
    --out ./retail_capstone_v2 \
    --seed 23 \
    --parquet
```

---

# Successful Execution Output

Example:

```text
Generating customers ...
Generating products ...
Generating orders ...
Generating order_items ...
Generating payments ...
Writing shuffled merged CSVs ...
Done. Files written to:
.../retail_capstone_v2
```

The generated datasets will be available under:

```text
retail_capstone_v2/data/merged/
```
