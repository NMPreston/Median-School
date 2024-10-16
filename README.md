# Median Computation Tool

This project is designed to compute the median of a series of numbers from a text file. The code reads numbers from a file, processes them, and returns the median value, which is a key statistical measure.

## Project Structure
- `compute_median.py`: The Python script that reads numbers from a text file, computes the median, and outputs the result.
- `numbers.txt`, `numbers2.txt`, `numbers6.txt`, `numbers7.txt`: Sample text files containing lists of numbers. Each file contains a different set of numbers to test the median computation.

## How to Use

1. **Run the Median Computation**:
   - Ensure you have Python installed (version 3.x).
   - To run the script with one of the provided number files, use the following command in your terminal:
     ```bash
     python compute_median.py numbers.txt
     ```
     Replace `numbers.txt` with the name of the file you want to use (e.g., `numbers2.txt`, `numbers6.txt`, `numbers7.txt`).

2. **Input Files**:
   - The script reads numbers from a text file where each number is placed on a new line.
   - Sample input files:
     - `numbers.txt`: Contains a short list of integers&#8203;:contentReference[oaicite:0]{index=0}.
     - `numbers2.txt`: Contains a list of integers, including negative numbers&#8203;:contentReference[oaicite:1]{index=1}.
     - `numbers6.txt`: Contains a smaller set of numbers with duplicates&#8203;:contentReference[oaicite:2]{index=2}.
     - `numbers7.txt`: Contains a larger, varied list of integers, including both positive and negative values&#8203;:contentReference[oaicite:3]{index=3}.
