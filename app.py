"""Marks Tool - print a short report for a list of marks."""
from config import load_env
# Remove highest and lowest from this import
from stats import average 

MARKS = [72, 65, 88, 91, 54] 

def main():
    settings = load_env()
    print(settings["APP_NAME"])
    print("Count  :", len(MARKS))
    print("Average:", average(MARKS))
    print("Highest:", max(MARKS))  # Changed to built-in max()
    print("Lowest :", min(MARKS))  # Changed to built-in min()

if __name__ == "__main__":
    main()


