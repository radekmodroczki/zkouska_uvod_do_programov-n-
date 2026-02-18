import math

class StatisticsCalculator:
# Class for statistical calculations on a pair of data sets.        
    def __init__(self):
        self.data_x = []
        self.data_y = []

    def load_data(self, list_x, list_y):
# Reads and validates input data. Handles singular cases, where the lines are different lenghts
        if len(list_x) != len(list_y):
            raise ValueError("Error: Input sequences must be the same length")
        if len(list_x) < 2:
            raise ValueError("Error: At least 2 values are needed to calculate correlation.")
        
        self.data_x = list_x
        self.data_y = list_y

    def _calculate_mean(self, data):
 # Method to calculate means.
        if not data:
            return 0.0
        return sum(data) / len(data)

    def calculate_pearson_correlation(self):
# Calculates the pearson correlation coefficient.
        n = len(self.data_x)
        mean_x = self._calculate_mean(self.data_x)
        mean_y = self._calculate_mean(self.data_y)

        numerator = 0.0      
        denom_x_sq = 0.0     
        denom_y_sq = 0.0     

        for i in range(n):
            diff_x = self.data_x[i] - mean_x
            diff_y = self.data_y[i] - mean_y

            numerator += diff_x * diff_y
            denom_x_sq += diff_x ** 2
            denom_y_sq += diff_y ** 2

        # Denominator calculation
        denominator = math.sqrt(denom_x_sq * denom_y_sq)

        # Singular case: division by zero
        if denominator == 0:
            raise ArithmeticError("Cannot calculate correlation, of of the sequence has zero variance (all numbers are the same).")

        return numerator / denominator

# Main program
if __name__ == "__main__":
    try:
        # Entry data example
        study_hours = [10, 5, 2, 8, 7] 
        grade_points = [90, 60, 40, 85, 80]

        calc = StatisticsCalculator()
        calc.load_data(study_hours, grade_points)
        
        result = calc.calculate_pearson_correlation()
        
        print(f"Entry X: {studium_hodiny}")
        print(f"Entry Y: {znamky_body}")
        print(f"Pearson correlation coefficient: {result:.4f}")
        
        # Interpretace výsledku
        if result > 0.7:
            print("REsult: Strong direct dependence")
        elif result < -0.7:
            print("Result: Strong indirect dependence.")
        else:
            print("Result: no correlaction.")

    except (ValueError, ArithmeticError) as e:

        print(f"An error occured: {e}")
