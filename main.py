"""
Job Market Pulse Analyzer
=========================
Run this single file to execute the entire project pipeline:
  1. Generate dataset
  2. Clean data
  3. Run analysis
  4. Generate all visualizations
"""

import subprocess
import sys

def install_requirements():
    print("[*] Installing required libraries...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "-q"])
    print("[OK] Libraries ready!\n")

def main():
    install_requirements()

    print("=" * 55)
    print("   STEP 1: Generating Dataset")
    print("=" * 55)
    import generate_dataset

    print("\n" + "=" * 55)
    print("   STEP 2: Cleaning Data")
    print("=" * 55)
    from data_cleaning import clean_data
    clean_data()

    print("\n" + "=" * 55)
    print("   STEP 3: Running Analysis")
    print("=" * 55)
    from analysis import run_analysis
    run_analysis()

    print("\n" + "=" * 55)
    print("   STEP 4: Generating Visualizations")
    print("=" * 55)
    import visualizations

    print("\n" + "=" * 55)
    print("   PROJECT COMPLETE!")
    print("=" * 55)
    print("\nCheck these folders:")
    print("   data/      -> raw + cleaned CSV files")
    print("   outputs/   -> 10 charts + Excel summary")
    print("\nReady to add to your resume & GitHub!")

if __name__ == "__main__":
    main()
