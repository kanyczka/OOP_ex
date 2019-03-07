##### Moduł shoper.py:

1. Klasa 'Product', której obiekty mają:<br  /> POLA:<br  /> 
code -> unikalny tekst<br  />
name -> tekst<br  />
price -> liczba<br  />
weight -> liczba<br  />
METODY:<br  />
  show_codes -> lista istniejących unikalnych kodów<br  />
  show_products -> lista istniejących produktów

2. Klasa 'Shop' - sklep z niekończącymi się produktami:<br  />
POLA:<br  />
products -> lista dostępnych produktów<br  />
METODY:<br  />
 add_product -> dodaje obiekt typu 'Product'. Jeżeli jednak produkt o takim samym kodzie (pole 'code') już istniał, 
to rzucamy wybrany wyjątek z informacją, że nie można dodać produktu, ponieważ w sklepie już jest produkt o podaym kodzie.<br  />
  change_quantity -> metoda przyjmuje w argumencie obiekt typu 'Product' i jego nową ilość.<br  />
  show_products_list -> wyświetla listę wszystkich dodanych do sklepu produktów<br  />
  show_product -> wyświetla dany produkt wraz z jego ilością w sklepie<br  />
 
3. Klasa 'Cart' - koszyk z produktami:<br  />
POLA:<br  />
products (produkty) -> lista produktów<br  />
capacity -> liczba reprezentująca maksymalną ładowność wózka<br  />
METODY:<br  />
  add_products -> metoda dodaje dowolną ilość produktów do koszyka. Sprawdza czy produkt był już wcześniej na liście, jeżeli nie to go dodaje, 
jeżeli tak - zwiększa jego ilość w koszyku. Podczas dodawania produktu sprawdzamy czy sumaryczna waga wszytkich produktów nie przekracza wartości w polu 'capacity' wózka. 
Jeżeli przekracza to rzucany jest odpowiedni wyjątek.<br  />
  remove_product -> metoda usuwa obiekt typu 'Product' z koszyka.<br  />
  show_cart -> wyświetla wszystkie produkty dodane do koszyka wraz z ich wagą.<br  />
 

<b>go_script.py - skrypt sprawdzający działanie klas<br  />
shoper_func.py - moduł z metodami<br  /></b>

