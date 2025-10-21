import os
from validator import validate_and_clean

def main():
    print("🚀 Starting Data Lighthouse System...\n")

    # Folder to store your datasets
    data_folder = "data"
    os.makedirs(data_folder, exist_ok=True)

    # Input and output file paths
    input_file = os.path.join(data_folder, "sample.csv")
    output_file = os.path.join(data_folder, "cleaned_sample.csv")

    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"⚠️ No input file found at {input_file}")
        print("Please add a 'sample.csv' file in the 'data' folder and rerun.")
        return

    # Run the validation and cleaning process
    validate_and_clean(input_file, output_file)

    print("\n🏁 Process completed successfully!")

if __name__ == "__main__":
    main()
