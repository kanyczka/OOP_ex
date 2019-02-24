
1. Swórz klasę 'Product', której obiekty powinny mieć następujące:
POLA:
code -> unikalny tekst
name -> tekst
price -> liczba
weight -> liczba

2. Stwórz klasę 'Shop' reprezentującą sklep z niekończoncymi się produktami, 	która powinna mieć:
POLA:
products -> lista dostępnych produktów
METODY:
add_product -> metoda powinna przyjmować w argumencie obiekt typu 'Product', i dodawać go do listy produktów. Jeżeli jednak produkt o takim samym kodzie (pole 'code') już istniał, to rzucamy wybrany wyjątek z informacją, że nie można dodać produktu, ponieważ w sklepie już jest produkt o podaym kodzie.

3. Stwórz funkcję main, która będzie się wykonywać od razu po uruchomieniu skryptu.

4. W funkcji 'main', stwórz kilka produktów i dodaj je do listy dostępnych produktów klasy 'Shop' (za pomocą metody 'add_product'). Spróbuj sprawić, aby metoda add_product rzuciła wyjątek, który przechwycisz, aby program się nie wysypał, a do tego wypiszesz informacje, że taki wyjątek przechwyciłaś.

5. Stwósz klasę 'Cart', której obiekty powinny mieć:
POLA:
products (produkty) -> lista produktów
capacity -> liczba reprezentująca maksymalną ładowność wózka
METODY:
add_product -> metoda powinna przyjmować w argumencie obiekt typu 'Product', i dodawać go do listy produktów. Jeżeli produktu o takim samym kodzie (pole 'code') nie było wcześniej na liście, to do dodawanego na listę produktu powinniśmy dodać nowe pole liczbowe 'count' o wartości 1. Jeżeli jednak produkt o takim samym kodzie już istniał to powinniśmy zwiększyć wartość atrybutu 'count' o 1.
UWAGA. Podczas dodawania produktu należy sprawdzać czy sumaryczna waga wszytkich produktów nie przekracza wartości w polu 'capacity' wózka. Jeżeli przekracza to powinniśmy rzucić odpowiedni wyjątek.

remove_product -> metoda powinna móc przyjąć albo kod produktu, albo obiekt typu 'Product' i w obu przypadkach powinna zadziałać. Jeżeli produktu nie było na liście to powinna zwrócić False, jeżeli produkt był na liście to powinna go z listy usunąć, tzn. zmniejszyć wartość atrybutu 'count' o 1, natomiast gdyby po zmniejszeniu wartość 'count' była równa 0, to należy ten produkt kompletnie usunąć z listy, a następnie zwrócić True.


6. Stwórz klasę 'DebitCard', której obiekty powinny mieć:
POLA:
number -> numer karty
balance -> kwota na karcie
METODY:
withdraw -> metoda będzie przyjmowała tylko wartość liczbową 'amount' i zmniejszała balance o 'amount', chyba, ze na koncie jest mniej kasy, niz wynosi argument, wtedy powinnismy rzucic wyjatkiem.



7. Stwórz klasę 'Person' reprezentującą osobę. Obiekty tej klasy powinny mieć:
POLA:
name (imie) -> text
surname (nazwisko) -> text
birth_date (data_urodzenia) -> data
debit_card -> DebitCard | None
cart -> Cart | None
METODY:
buy - metoda powinna wyczyścić koszyk ('cart') oraz zmniejszyć środki na karcie o tyle ile wynosi suma produktów z koszyka. Płatność odbywa się za pomocą metody 'withdraw' karty.


8. Poproś użytkownika o podanie imienia, nazwiska oraz daty urodzenia, ładowności koszyka, oraz kwoty na koncie a gdy użytkownik je poda, stwórz instance klas 'Cart', 'DebitCard', a następnie 'Person', gdzie do konstruktora klasy person przekażesz odpowiednie dane (w tym 2 uprzednio utworzone obiekty).

9. Następnie wywołaj funkcję print, a w argumencie przekaż utworzoną instancję.
Dostosuj klasę 'Person', aby wywołanie funkcji print zadziałało mniej więcej tak:

>>> print(person)
Patryk Kowalski (wiek: 20)

10. Przetestuj wszystkie metody, w tym dodaj do koszyka trochę produktów, a następnie kup je używając metody 'buy'.


