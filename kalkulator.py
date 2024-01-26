from kalkulatordodawanie import dodawanie
from kalkulatorodejmowanie import odejmowanie
from kalkulatormnozenie import mnozenie
from kalkulatordzielenie import dzielenie
from kalkulatorpierwiastek import pierwiastek
from kalkulatorprocent import procent

def kalkulator():
    while True:
        print("Wybierz operację:")
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnożenie")
        print("4. Dzielenie")
        print("5. Pierwiastkowanie")
        print("6. Procent z liczby")

        wybor = input("Podaj numer operacji (1/2/3/4/5/6): ")

        if wybor in ('1', '2', '3', '4', '5', '6'):
            if wybor not in ('5', '6'):
                liczba1 = float(input("Podaj pierwszą liczbę: "))

            if wybor in ('1', '2', '3', '4'):
                liczba2 = float(input("Podaj drugą liczbę: "))

            if wybor == '1':
                wynik = dodawanie(liczba1, liczba2)
            elif wybor == '2':
                wynik = odejmowanie(liczba1, liczba2)
            elif wybor == '3':
                wynik = mnozenie(liczba1, liczba2)
            elif wybor == '4':
                wynik = dzielenie(liczba1, liczba2)
            elif wybor == '5':
                liczba1 = float(input("Podaj liczbę do pierwiastkowania: "))
                wynik = pierwiastek(liczba1)
            elif wybor == '6':
                liczba1 = float(input("Podaj liczbę: "))
                procentu = float(input("Podaj procent: "))
                wynik = procent(liczba1, procentu)

            print(f"Wynik: {wynik}")

            kontynuacja = input("Czy chcesz kontynuować? (tak/nie): ")
            if kontynuacja.lower() != 'tak':
                break
        else:
            print("Nieprawidłowy numer operacji.")

if __name__ == "__main__":
    kalkulator()
