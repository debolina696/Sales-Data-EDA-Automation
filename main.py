# ==========================================
# SALES DATA AUTOMATION MAIN PIPELINE
# ==========================================

import os
import sys

print("🚀 Starting Sales Data Automation Pipeline...")

# ==========================================
# DEFINE PROJECT PATHS
# ==========================================

# Root project path
base_path = os.path.dirname(os.path.abspath(__file__))

# Scripts folder
scripts_path = os.path.join(base_path, "scripts")

# Data folders
data_path = os.path.join(base_path, "data")

raw_path = os.path.join(data_path, "raw")

cleaned_path = os.path.join(data_path, "cleaned")

# Reports folder
reports_path = os.path.join(base_path, "reports")

# Add scripts to system path
sys.path.append(scripts_path)

# ==========================================
# IMPORT MODULES
# ==========================================

try:
    from data_cleaning import run_data_cleaning
    from eda import run_eda
    from sales_analysis import run_statistics
    from report_generator import generate_pdf_report

except Exception as e:
    print("❌ Import Error:", e)

# ==========================================
# MAIN FUNCTION
# ==========================================

def main():

    print("\n🧹 Step 1: Data Cleaning Started")
    run_data_cleaning(raw_path, cleaned_path)

    print("\n📊 Step 2: Running EDA")
    run_eda(cleaned_path, reports_path)

    print("\n📈 Step 3: Running Statistical Analysis")
    run_statistics(cleaned_path, reports_path)

    print("\n📄 Step 4: Generating PDF Report")
    generate_pdf_report(reports_path)

    print("\n✅ Pipeline Completed Successfully!")

# ==========================================
# EXECUTE MAIN
# ==========================================

if __name__ == "__main__":
    main()
