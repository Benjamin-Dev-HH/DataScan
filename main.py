import os
from modules.scanner import scan_library
from modules.sorter import sort_data
from modules.analyzer import analyze_data

def main():
    # ...existing code...
    input_dir = input("Enter the directory to scan: ")
    sort_criteria = input("Enter sorting criteria (e.g., name, size, date): ")
    
    print("Scanning library...")
    data = scan_library(input_dir)
    
    print("Sorting data...")
    sorted_data = sort_data(data, sort_criteria)
    
    print("Analyzing data...")
    analysis_results = analyze_data(sorted_data)
    
    print("Analysis complete. Results:")
    print(analysis_results)

if __name__ == "__main__":
    main()
