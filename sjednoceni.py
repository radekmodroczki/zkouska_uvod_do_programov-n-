import sys

class UnionFinder:
    """
    Třída pro nalezení sjednocení dvou číselných posloupností
    bez použití vestavěných množinových typů (set).
    """
    def __init__(self):
        self.sequence_a = []
        self.sequence_b = []
        self.result_union = []

    def load_from_file(self, filename):
        """
        Načte dvě posloupnosti čísel ze souboru.
        Očekávaný formát:
        1. řádek: čísla první posloupnosti oddělená mezerou
        2. řádek: čísla druhé posloupnosti oddělená mezerou
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
                # Ošetření: Soubor musí mít alespoň 2 řádky (i když prázdné)
                if len(lines) < 2:
                    raise ValueError("Soubor musí obsahovat alespoň dva řádky.")

                # Zpracování 1. řádku
                self.sequence_a = self._parse_line(lines[0])
                # Zpracování 2. řádku
                self.sequence_b = self._parse_line(lines[1])
                
                print(f"Načteno A: {len(self.sequence_a)} prvků, B: {len(self.sequence_b)} prvků.")

        except FileNotFoundError:
            raise FileNotFoundError(f"Soubor '{filename}' nebyl nalezen.")

    def _parse_line(self, line):
        """Pomocná metoda pro převod textového řádku na seznam int."""
        numbers = []
        parts = line.strip().split()
        for p in parts:
            try:
                numbers.append(int(p))
            except ValueError:
                # Ignorujeme nečíselné hodnoty
                continue
        return numbers

    def compute_union(self):
        # 1. Spojení obou posloupností do jedné
        merged = self.sequence_a + self.sequence_b
        
        # Singulární případ: Obě jsou prázdné
        if not merged:
            self.result_union = []
            return

        # 2. Setřídění
        merged.sort()

        # 3. Odstranění duplicit
        # Princip: V setříděném poli jsou stejná čísla vedle sebe.
        unique_list = []
        
        # První prvek přidáme vždy (pokud existuje)
        if merged:
            unique_list.append(merged[0])

        # Procházíme od druhého prvku dál
        for i in range(1, len(merged)):
            # Pokud se aktuální prvek liší od předchozího, je unikátní; přidáme ho
            if merged[i] != merged[i-1]:
                unique_list.append(merged[i])

        self.result_union = unique_list

    def print_result(self):
        """Vytiskne výslednou posloupnost."""
        print("-" * 30)
        print("Výsledné sjednocení (seřazené, unikátní):")
        # Převedení na string
        print(", ".join(map(str, self.result_union)))
        print(f"Počet prvků: {len(self.result_union)}")
        print("-" * 30)

# Hlavní program
if __name__ == "__main__":
    app = UnionFinder()
    input_file = "sequences.txt"

    try:
        # 1. Načtení dat
        app.load_from_file(input_file)
        
        # 2. Výpočet
        app.compute_union()
        
        # 3. Výpis
        app.print_result()

    except Exception as e:
        print(f"Chyba: {e}")