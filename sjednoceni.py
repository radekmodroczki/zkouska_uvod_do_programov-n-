import sys

class UnionFinder:
# Class for finding the union of two numerical sequences.
    def __init__(self):
        self.sequence_a = []
        self.sequence_b = []
        self.result_union = []

    def load_from_file(self, filename):
# Loads two sequences from file, with the expected format of two lines of numbers separated by spaces.
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
                # Singular case treatment: file has to have at least two lines (even if empty).
                if len(lines) < 2:
                    raise ValueError("File has too little lines.")

                # First line
                self.sequence_a = self._parse_line(lines[0])
                # Second line
                self.sequence_b = self._parse_line(lines[1])
                
                print(f"Loaded A: {len(self.sequence_a)} features, B: {len(self.sequence_b)} features.")

        except FileNotFoundError:
            raise FileNotFoundError(f"File '{filename}' not found.")

    def _parse_line(self, line):
    # Method for parsing the lines to integers.
        numbers = []
        parts = line.strip().split()
        for p in parts:
            try:
                numbers.append(int(p))
            except ValueError:
                # Ignores non-numerical values.
                continue
        return numbers

    def compute_union(self):
        # Computes the union.
        merged = self.sequence_a + self.sequence_b
        
        # Singular case: both are empty.
        if not merged:
            self.result_union = []
            return

        # Sorting
        merged.sort()

        # Removal of duplicates
        unique_list = []
        
        # Adding the first feature
        if merged:
            unique_list.append(merged[0])

        # Go through the rest of the features
        for i in range(1, len(merged)):
            # If the feature is different from the last one, it gets added.
            if merged[i] != merged[i-1]:
                unique_list.append(merged[i])

        self.result_union = unique_list

    def print_result(self):
# Prints the new sequence
        print("-" * 30)
        print("The result sequence (sorted, unique):")
        # Turns into string
        print(", ".join(map(str, self.result_union)))
        print(f"Number of features: {len(self.result_union)}")
        print("-" * 30)

# Main program
if __name__ == "__main__":
    app = UnionFinder()
    input_file = "sequences.txt"

    try:
        # Data loading
        app.load_from_file(input_file)
        
        # Calculation
        app.compute_union()
        
        # Print
        app.print_result()

    except Exception as e:

        print(f:"Error: {e}")
