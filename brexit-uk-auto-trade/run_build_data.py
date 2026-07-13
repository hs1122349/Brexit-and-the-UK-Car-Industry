"""Write the three reconstructed index CSVs into data/.

The two official CSVs (uk_production_2022.csv, fta_count_post_brexit.csv)
are already committed and do not need this script.

Usage:
    python run_build_data.py
"""
from src.reconstruct import main

if __name__ == "__main__":
    main()
