from parser import parse_data
from DataCleaning import clean_data
from write import write_to_sheets

def main():
    raw = parse_data()
    clean = clean_data(raw)
    write_to_sheets(clean)

if __name__ == "__main__":
    main()
