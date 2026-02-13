import math

class StatisticsCalculator:
    """
    Třída pro statistické výpočty nad dvojicí datových sad.
    """
    def __init__(self):
        self.data_x = []
        self.data_y = []

    def load_data(self, list_x, list_y):
        """
        Načte a validuje vstupní data.
        Ošetřuje singulární případ: Různé délky polí.
        """
        if len(list_x) != len(list_y):
            raise ValueError("Chyba: Vstupní posloupnosti musí mít stejnou délku.")
        if len(list_x) < 2:
            raise ValueError("Chyba: Pro výpočet korelace jsou potřeba alespoň 2 hodnoty.")
        
        self.data_x = list_x
        self.data_y = list_y

    def _calculate_mean(self, data):
        """Pomocná metoda pro výpočet aritmetického průměru."""
        if not data:
            return 0.0
        return sum(data) / len(data)

    def calculate_pearson_correlation(self):
        """
        Vypočte Pearsonův korelační koeficient r.
        Vrací hodnotu v intervalu <-1, 1>.
        """
        n = len(self.data_x)
        mean_x = self._calculate_mean(self.data_x)
        mean_y = self._calculate_mean(self.data_y)

        numerator = 0.0      # Čitatel
        denom_x_sq = 0.0     # Část jmenovatele pro X
        denom_y_sq = 0.0     # Část jmenovatele pro Y

        for i in range(n):
            diff_x = self.data_x[i] - mean_x
            diff_y = self.data_y[i] - mean_y

            numerator += diff_x * diff_y
            denom_x_sq += diff_x ** 2
            denom_y_sq += diff_y ** 2

        # Výpočet jmenovatele
        denominator = math.sqrt(denom_x_sq * denom_y_sq)

        # Ošetření singulárního případu: Dělení nulou
        # Nastane, pokud jsou všechna čísla v jedné sadě stejná (rozptyl je 0).
        if denominator == 0:
            raise ArithmeticError("Nelze vypočítat korelaci: Jedna z posloupností má nulový rozptyl (všechna čísla jsou stejná).")

        return numerator / denominator

# --- Hlavní program (Main) ---
if __name__ == "__main__":
    try:
        # Příklad vstupních dat (např. čas studia vs. známka)
        studium_hodiny = [10, 5, 2, 8, 7] 
        znamky_body =    [90, 60, 40, 85, 80]

        calc = StatisticsCalculator()
        calc.load_data(studium_hodiny, znamky_body)
        
        result = calc.calculate_pearson_correlation()
        
        print(f"Vstup X: {studium_hodiny}")
        print(f"Vstup Y: {znamky_body}")
        print(f"Pearsonův koeficient: {result:.4f}")
        
        # Interpretace výsledku
        if result > 0.7:
            print("Závěr: Silná přímá závislost.")
        elif result < -0.7:
            print("Závěr: Silná nepřímá závislost.")
        else:
            print("Závěr: Nízká nebo žádná lineární závislost.")

    except (ValueError, ArithmeticError) as e:
        print(f"Nastala chyba při zpracování: {e}")