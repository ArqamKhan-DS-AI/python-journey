import csv

def process_data(input_file: str, output_file: str) -> None:
    """Reads a CSV, filters for Engineers, and writes a new CSV."""
    try:
        # Open the input file for reading
        with open(input_file, mode="r", encoding="utf-8") as infile:
            reader = csv.DictReader(infile) # DictReader turns each row into a dictionary
            
            engineers = []

            for row in reader:
                
                if row["role"] == "Engineer":
                    engineers.append(row)
                    
    except FileNotFoundError:
        print(f"Error: Could not find the file '{input_file}'.")
        return

    # Open the output file for writing
    with open(output_file, mode="w", newline="", encoding="utf-8") as outfile:
        # We need to know the column names for the new file
        fieldnames = ["id", "name", "role", "salary"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader() # Write the top row (id, name, role, salary)
        writer.writerows(engineers) # Write all the filtered data
        
    print(f"Success! Found {len(engineers)} engineers. Saved to {output_file}.")

if __name__ == "__main__":
    process_data("day04/data.csv", "day04/engineers_only.csv")