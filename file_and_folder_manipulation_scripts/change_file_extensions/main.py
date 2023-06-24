from pathlib import Path

root_dir = Path('files')

for path in root_dir.rglob("*.txt"):
# for path in root_dir.rglob("*.csv"): << change from csv to txt
# for path in root_dir.glob("*"): << this will change all files in the root directory "files"
    if path.is_file():
        new_filepath = path.with_suffix(".csv")
        # new_filepath = path.with_suffix(".txt") change back from csv to txt
        path.rename(new_filepath)