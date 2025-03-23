# Pochodne

Rachunek różniczkowy to tajny składnik, który pozwala nam zminimalizować funkcję kosztu, o której mówiliśmy wcześniej. Tak, dobrze czytasz — koszt modelu uczenia maszynowego to po prostu funkcja matematyczna.

Wejdziemy w szczegóły później, ale zrozum, że funkcja kosztu jest ogromna, przyjmując tysiące zmiennych jako dane wejściowe. Aby zminimalizować koszt, musimy znaleźć jego nachylenie, żebyśmy mogli ustalić, w którym kierunku zmierzać.

Pochodne to sposób na znalezienie nachylenia dowolnej funkcji. Jeśli spojrzysz na wykres liniowy poniżej, możemy stwierdzić, że ma nachylenie 2 (pamiętasz wzrost dzielony przez przebieg?).

![image](https://github.com/user-attachments/assets/97f6da77-9258-40f0-be2e-437b299ed831)


Ale jak możemy znaleźć nachylenie bardziej złożonej funkcji, takiej jak parabola? Tutaj wkraczają pochodne.

![image](https://github.com/user-attachments/assets/6b5b9b56-d789-48cf-b960-5774a4990567)


Stary, jak znaleźć nachylenie tej rzeczy? Gdzie jest wzrost dzielony przez przebieg?

Zwykle cały semestr rachunku różniczkowego poświęca się nauczaniu, czym są pochodne i jak je obliczać, ale będę się streszczać.

## Wyjaśnienie, czym jest pochodna

Wróćmy do wcześniejszego przykładu paraboli: to nie jest linia, więc nie ma wzrostu dzielonego przez przebieg. Możesz myśleć, że obliczenie nachylenia paraboli jest niemożliwe, ale przyjrzyj się bliżej — dużo bliżej.

Przybliż wystarczająco jedną sekcję paraboli, powiedzmy od x = 3,0 do x = 3,001, a będzie się wydawać prostą linią. Teraz możesz obliczyć to nachylenie.

![image](https://github.com/user-attachments/assets/a251c285-ef75-491f-8ca1-c0b1854c3b81)

Ta sama koncepcja przybliżania dotyczy wszystkich kiedykolwiek stworzonych funkcji. Przybliż wystarczająco, a ta sekcja staje się linią, której nachylenie możesz uzyskać.

Jednakże jest haczyk: nachylenie zmienia się w zależności od tego, gdzie jesteś na wykresie. Nie jest statyczne jak w przypadku linii. Nachylenie między x = 3,0 a x = 3,001 różni się od nachylenia między x = 1,0 a x = 1,001.

To właśnie jest pochodna — równanie algebraiczne, które reprezentuje nachylenie wykresu we wszystkich punktach wykresu.

Dla paraboli pochodna byłaby równaniem algebraicznym reprezentującym linię y = 2x. Możesz też myśleć o pochodnej jako równaniu algebraicznym stycznym (prostopadłym) do wykresu we wszystkich punktach.

![image](https://github.com/user-attachments/assets/c9deeb95-533c-4717-b56a-b9051ca9866d)

Jeśli nadal nie rozumiesz, nie martw się. Wszystko, co musisz wiedzieć, to jak obliczać pochodne.

## Obliczanie pochodnych: Reguła potęgowa

Jak znaleźliśmy pochodną y=x² wcześniej? Cóż, użyjmy reguły potęgowej:

1. Przenieś wykładnik x² — 2 — w dół przed podstawę i pomnóż go przez podstawę, dając ci 2x²
2. Odejmij jeden od wykładnika, dając ci 2x¹
3. Uśmiechnij się z radości z ostatecznym wynikiem = 2x.

Spróbujmy znaleźć pochodną y = 3x²:
1. Przenieś 2 w dół, dając ci (3 * 2)x² = 6x²
2. Odejmij 1 od wykładnika, dając ci 6x¹ = 6x.

Dla bardziej zwięzłej notacji zamieniamy y na f(x), ponieważ lepiej myśleć w kategoriach funkcji dla uczenia maszynowego.

Więc jeśli f(x) = 4x², reprezentujemy pochodną f(x) notacją f'(x) — nazywaną f prim x — jest f'(x) = 8x.

Ok, przejdźmy do sytuacji, gdy reguła potęgowa nie jest tak oczywista.

Jak znalazłbyś f'(x) dla f(x) = 2x? Reguła potęgowa nadal ma zastosowanie.

1. Wykładnik przy x wynosi 1, więc przenieś 1 w dół, dając ci (2 * 1)x¹
2. Odejmij 1 od wykładnika, co daje ci 2x⁰. Następnie zdaj sobie sprawę, że cokolwiek na świecie do potęgi 0 jest równe 1, co daje ci 2 * 1 = 2.

Więc jeśli f(x) = 2x, pochodna f'(x) = 2, co było po prostu stałą mnożącą x. Więc dla każdego f(x) = cx, gdzie c jest stałą, f'(x) = c. To ma intuicyjny sens:

![image](https://github.com/user-attachments/assets/9eca2cf0-99d5-43e7-ba68-bc112bea0c7a)

Linia prosta ma to samo nachylenie wszędzie na linii.

Reprezentujemy linię o nachyleniu równym 2 jako y = 2x, a czym innym jest pochodna, jak nie nachyleniem funkcji? Pochodna jest tutaj po prostu równa nachyleniu, czyli f'(x) = 2.

A ostatnim przypadkiem do rozważenia jest pochodna stałej. Nie możemy użyć reguły potęgowej do znalezienia pochodnej stałej, takiej jak f(x) = 5, ale przeskoczę od razu do odpowiedzi:

Dla wszystkich f(x) = c, gdzie c jest jakąś stałą liczbą rzeczywistą, f'(x) = 0. Więc pochodna każdej stałej wynosi 0. To ma intuicyjny sens:

![image](https://github.com/user-attachments/assets/d47e7b42-788d-4fd6-9223-b662066014db)

Linia f(x) = c, gdzie c jest stałą, reprezentuje po prostu płaską linię. Weźmy na przykład f(x) = 3. To płaska linia, co oznacza brak wzrostu i tylko przebieg, dając nachylenie = 0. Zatem ma sens, że pochodna f'(x) równa się 0.

## Obliczanie pochodnych: Wiele składników

Jeśli f(x) = x + 5, jak znaleźć f'(x)? Reguła jest prosta: po prostu znajdź pochodną każdego pojedynczego składnika.

Pochodna x wynosi 1, a pochodna stałej 5 wynosi 0, więc otrzymujemy f'(x) = 1.

Jeśli f(x) = 2x² — 3x + 8, pochodna to po prostu 4x-3 + 0 = 4x-3.

## Obliczanie pochodnych: Reguła iloczynu

Powiedzmy, że mnożymy dwie funkcje f(x) i g(x) razem jako h(x) = f(x)g(x) i chcemy znaleźć pochodną tego.

Oto ogólny wzór:

h'(x) = f'(x)g(x) + f(x)g'(x)

Zanim pośpiesznie podbiegniecie do najbliższej krawędzi i spróbujecie z niej skoczyć, posłuchajcie mnie — omówmy przykład.

1. f(x) = 3x, g(x) = 2x²
2. więc pochodne to f'(x) = 3, g'(x) = 4x
3. To prowadzi do h'(x) = 3(2x²) + 3x(4x) = 6x² + 12x² = 18x²

Udowodnijmy, że to działa, mnożąc f(x) i g(x) razem, a następnie biorąc pochodną:
1. f(x) * g(x) = 6x³
2. Pochodna 6x³ to 18x², więc udowodniliśmy to!

Jeśli chcesz zrozumieć, dlaczego to działa i jak ludzie się o tym dowiedzieli, ja też. Ale jesteśmy już 20 minut i w ogóle nie rozmawialiśmy o sieciach neuronowych.

Przejdźmy dalej.

## Obliczanie pochodnych: Suma

Budując na tej samej idei, jak pochodna sumy to po prostu pochodne każdej pojedynczej części, wszystkie zsumowane razem, możemy zrobić to samo z sumowaniem.

Jak znaleźlibyśmy f'(x) dla tego?

```
∑(x) od i=1 do 10
```

Można by po prostu najpierw wykonać sumę, a następnie wziąć pochodną, co dałoby f(x) = 10x, co czyni f'(x) = 10. Pomyślmy nieco mądrzej.

Ponieważ suma po prostu sumuje wszystkie składniki, możemy po prostu użyć reguły pochodnych sumy, aby wziąć pochodną wszystkich pojedynczych części tych sum, a następnie zsumować je wszystkie.

Więc pierwszym krokiem jest znalezienie pochodnej x, która wynosi 1. Następnie po prostu sumujemy te jedynki.

```
∑(1) od i=1 do 10
```

Pochodna x = 1, a następnie sumujemy 1 dziesięć razy, aby uzyskać końcową odpowiedź = 10.

## Obliczanie pochodnych: Reguła łańcuchowa

Reguła łańcuchowa jest zdecydowanie najistotniejszą częścią nauki o pochodnych. Możesz w ogóle nic nie zrozumieć, a omówienie intuicji wymagałoby, abym uczył cię o granicach, liniach siecznych itp., więc będziemy uczyć się tylko, jak stosować regułę łańcuchową.

Gorąco polecam obejrzenie tego filmu, jeśli masz czas, aby zbudować intuicję poza "tak stary, po prostu f prim x".

Reguła łańcuchowa dotyczy znajdowania pochodnych, gdy funkcje są złożone, jak f(g(x)). Jak znaleźć pochodną tego? Właśnie to mówi reguła łańcuchowa:

f(g(x)) = f'(g(x)) * g'(x)

Najpierw zróbmy to po staremu z f(x) = 4x² i g(x) = 3x³.

1. f(g(x)) = f(3x³) = 4(3x³)² = 4(9x⁶) = 36x⁶.
2. Pochodna 36x⁶ to (gorączkowo szuka 36 razy 6) 216x⁵.

Teraz zróbmy to z regułą łańcuchową:

1. f(g(x)) = f'(3x³) * g'(x) = f'(3x³) * 9x²
2. Aby dowiedzieć się, co to jest f'(3x³), musimy najpierw znaleźć f'(x).
3. f'(x) = 8x, więc f'(3x³) = 8*3x³ = 24x³.
4. Więc f'(3x³) * 9x² = 24x³ * 9x² = 216x⁵.

Świetnie, udowodniliśmy to! Teraz czas nauczyć się notacji, której będziemy używać do uczenia maszynowego.

Możemy przepisać regułę łańcuchową w następujący sposób:

```
d/dx f(g(x)) = df/dg * dg/dx
```

![Ilustracja reguły łańcuchowej]

Składnia d/dx oznacza po prostu wzięcie pochodnej równania względem x. To inny sposób na przepisanie f'(x). Na przykład d/dx dla 2x to po prostu pochodna 2x, która równa się 2.

Ta notacja jest ważna, ponieważ pokazuje łańcuch, czego nie można zrobić za pomocą notacji f prim.

Rozbijmy to:

1. d/dx f(g(x)) oznacza, że próbujemy znaleźć f'(g(x)), tak jak w regule łańcuchowej.
2. df/dg to zwięzły sposób na zapisanie df(x)/dg(x), co oznacza, że chcemy znaleźć pochodną f(x) względem g(x), co zapisujemy jako f'(g(x)).
3. dg/dx to nasz stary przyjaciel g'(x).

Więc wróćmy i wykonajmy obliczenia z f(x) = 4x² i g(x) = 3x³.

1. df/dg: f'(g(x)), a f'(x) = 8x, co równa się f'(3x³) = 8(3x³) = 24x³
2. dg/dx: g'(x) = 9x²
3. Następnie mnożymy te dwa terminy razem, aby ponownie uzyskać odpowiedź: 216x⁵.

Jedną z użytecznych cech tej notacji jest ilustracja łańcucha, zwłaszcza jeśli myślimy o mnożeniu ułamków. To może być zbyt mylące, aby o tym myśleć teraz, więc zajmiemy się tym ponownie, gdy będziemy mówić o pochodnych cząstkowych.

## Obliczanie pochodnych: Specjalne pochodne

Istnieje kilka specjalnych pochodnych, które powinieneś umieć obliczać, ponieważ będą one używane w obliczeniach wstecznej propagacji. Wszystkie one używają reguły łańcuchowej.

Jeśli f(x) = ln(x), czyli naturalny logarytm x, to f'(x) = 1/x * 1 = 1/x. To po prostu 1 podzielona przez cokolwiek było w środku, a następnie, z powodu reguły łańcuchowej, mnożysz przez pochodną wewnętrznego składnika.

Zróbmy inny przykład, ale mając na uwadze regułę łańcuchową: Jeśli f(x) = ln(2x²), to f'(x) = (1/2x²) * 4x = 2/x. Pomnożyliśmy przez 4x, ponieważ to jest pochodna 2x².

Ok, to jest naprawdę dziwne — jeśli f(x) = e^x, to f'(x) = e^x. To po prostu to samo.

Ale z regułą łańcuchową, jeśli f(x) = e^{2x}, to f'(x) = e^{2x}*2 = 2e^{2x}. Mnożymy przez pochodną 2x, która wynosi po prostu 2 z powodu reguły łańcuchowej.

# Podstawy: Pochodne cząstkowe

![Zdjęcie autorstwa Chris Liverani na Unsplash](https://source.unsplash.com/Chris-Liverani)

Gratulacje, to ostatni element podstawowej wiedzy matematycznej, którego potrzebujesz, zanim będziesz mógł zbudować sieć neuronową od podstaw.

Jeśli mamy funkcję, która istnieje w trzech wymiarach, jak z = 2x + 3y, jak możemy znaleźć jej nachylenie? Pytanie z pułapką — nie możemy.

Ale możemy to sfałszować. Możesz uzyskać pochodną funkcji wielowymiarowej względem jednej zmiennej na raz, traktując wszystkie inne zmienne jako stałe.

To nazywa się pochodną cząstkową, gdzie traktujemy tylko jedną zmienną w równaniu wielozmiennym jako faktyczną zmienną, a wszystko inne jako stałą.

Jeśli funkcja f przyjmuje dwie zmienne x i y, jak f(x, y), możemy reprezentować pochodną cząstkową f względem x jako ∂f/∂x (wymawiane "del f del x").

Jak możemy obliczyć ∂f/∂x, jeśli f(x, y) = 2x + 3y?

1. Ponieważ próbujemy znaleźć pochodną cząstkową f względem x, traktujemy x jako zmienną, a y jako stałą.
2. Jaka jest pochodna 2x, traktując x jako zmienną? To po prostu 2.
3. Jaka jest pochodna 3y, traktując y jako stałą? Cóż, 3 razy stała to nadal stała, a pochodna każdej stałej równa się 0.
4. Uzyskujemy ∂f/∂x = 2 + 0 = 2

Spróbujmy znaleźć ∂f/∂y, jeśli f(x, y) = 2x + 3y.

1. Traktuj y jako zmienną, a x jako stałą.
2. ∂f/∂y = 0 + 3 = 3.

## Intuicja gradientu spadkowego

Intuicja stojąca za pochodnymi cząstkowymi polega na zastanowieniu się, jak pojedyncza zmienna w funkcji wielowymiarowej wpływa na wynik tej funkcji. ∂f/∂x pyta: "jeśli zmieniam tylko x i utrzymuję wszystkie inne zmienne jako stałe, jak ta zmiana x wpływa na wynik mojej funkcji f?".

To jest najważniejsze pytanie w uczeniu maszynowym.

Co, jeśli mógłbym znaleźć pochodną cząstkową kosztu mojego modelu uczenia maszynowego względem pojedynczej zmiennej? Wtedy mógłbym odpowiednio dostosować tę zmienną, aby zminimalizować koszt tak bardzo, jak to możliwe.

Powtórzę: Rachunek różniczkowy to tajny składnik tego, jak maszyna się uczy. Pochodne cząstkowe pozwalają nam znaleźć, jak każda zmienna wpływa na koszt modelu i odpowiednio ją dostosować, aby koszt był mniejszy lub większy według naszej woli.

Jeśli ∂f/∂x jest dodatnie, powiedzmy ∂f/∂x = 2, wtedy tłumaczy się to na: "jeśli x wzrasta o pewną małą wartość, to funkcja f wzrasta o tę małą wartość pomnożoną przez 2".

Jeśli ∂f/∂x jest ujemne, powiedzmy ∂f/∂x = -2, wtedy tłumaczy się to na: "jeśli x wzrasta o pewną małą wartość, to funkcja f maleje o tę małą wartość pomnożoną przez 2".

Powiedzmy, że funkcja kosztu modelu ma pewną zmienną/parametr o nazwie w. Jeśli ∂C/∂w jest dodatnie, oznacza to, że jeśli w wzrasta, to koszt C również wzrasta. Zróbmy więc coś mądrego — zmniejszmy wartość w. Jeśli w maleje, to C również.

Pozwolę ci samodzielnie ustalić, czy powinniśmy zwiększyć czy zmniejszyć w, aby zminimalizować koszt, jeśli ∂C/∂w jest ujemne.

To jest serce uczenia maszynowego — gradient spadkowy. Powiedzmy, że nasza funkcja kosztu C ma 1000 zmiennych, nazwanych w_1, w_2, itd., co czyni ją ogromną funkcją 1000-wymiarową. Notujemy C jako C(w_1, w_2, …, w_n)

Gradient C jest oznaczony jako ∇C, co jest po prostu zbiorem wszystkich pochodnych cząstkowych C względem każdej z jego 1000 zmiennych:

```
∇C = [∂C/∂w_1, ∂C/∂w_2, ..., ∂C/∂w_1000]
```

![Gradient C, wymawiany "nabla" C, to po prostu zbiór jego 1000 pochodnych cząstkowych, ponieważ ma 1000 zmiennych jako dane wejściowe]

Wygląda znajomo? To po prostu wektor. Pochodna cząstkowa kosztu względem jego pierwszej zmiennej, ∂C/∂w_1, staje się pierwszym wpisem, i tak dalej aż do ∂C/∂w_1000.

Gradient daje nam panowanie nad niegdyś bestialską funkcją kosztu — teraz wiemy, jak dostosowanie każdej zmiennej zmienia funkcję kosztu.

Możesz myśleć o każdej pochodnej cząstkowej jako o pokrętle, gdzie obracanie go w lewo (zmniejszanie) lub w prawo (zwiększanie) odpowiednio dostosowuje koszt. Dzięki potędze uczenia maszynowego masz teraz tysiąc pokręteł do dostosowania według swojej woli, pozwalając ci wszechmocnie zmieniać koszt.

Ale żaden człowiek nie może zarządzać 1000 pokrętłami, a co dopiero 100 miliardami, które ma typowa sieć neuronowa. Zamiast tego, sprawiamy, że sieć sama to rozwiązuje.

Jeśli model uczenia maszynowego ma ∇C, dokładnie wie, jak każde pokrętło zmienia koszt i jak bardzo każde z nich obracać.

Na przykład, jeśli ∂C/∂w_1 = 1 i ∂C/∂w_2 = 9, to możemy zobaczyć, że ∂C/∂w_2 ma większy wpływ na funkcję kosztu. Zwiększysz zmienną w_2 o 1 jednostkę, a koszt C wzrośnie o 9!

Tym samym pokrętło ∂C/∂w_2 daje nam największą wartość za nasze pieniądze pod względem zmiany kosztu.

Jeśli to wyjaśnienie nie trafiło do ciebie, zachęcam do ponownego przeczytania. Pochodne cząstkowe są podstawą całej intuicji stojącej za tym, jak działają sieci neuronowe.

## Reguła łańcuchowa z pochodnymi cząstkowymi

Obiecuję, że to ostatni kawałek matematyki, którego potrzebujemy, zanim będziemy mogli w pełni zrozumieć sieci neuronowe.

Reguła łańcuchowa z pochodnymi cząstkowymi opiera się na normalnej idei reguły łańcuchowej. Trudno to wyjaśnić, ale łatwo pokazać.

Powiedzmy, że mam funkcję v = 3x + 4y, x = 3a², i y = 4b². Jak mogę uzyskać ∂v/∂a lub ∂v/∂b, jeśli mam do czynienia ze złożonymi funkcjami zagnieżdżonymi w sobie?

Mógłbyś próbować podstawić x w kategoriach a i y w kategoriach b, aby bezpośrednio obliczyć ∂v/∂a i ∂v/∂b, ale co jeśli v było bardziej skomplikowane, jak 3x⁵ — 4y²? Wtedy skończyłbyś z 9a¹⁰ + 64b⁴, dużo bałaganiarskie niż praca z każdym równaniem osobno.

Reguła łańcuchowa upraszcza obliczenia ze złożonymi wyrażeniami algebraicznymi, zajmując się nimi kawałek po kawałku.

Zbudujmy graf obliczeń:

![Graf obliczeń pokazujący związki między v, x, y, a i b]

Funkcja v składa się ze zmiennych x i y, a x składa się z a, a y składa się z b. To drzewo jest pojedynczym najbardziej pomocnym diagramem do narysowania przed obliczeniem jakichkolwiek pochodnych cząstkowych.

Jeśli chcę znaleźć ∂v/∂a, muszę podróżować od v do x, dając mi ∂v/∂x, a następnie od x do a, dając mi ∂x/∂a. Następnie mnożysz je razem, aby stworzyć regułę łańcuchową:

```
∂v/∂a = ∂v/∂x * ∂x/∂a
```

![Podróż od v do x, a następnie do a]

Inny sposób, który ma sens, to idea mnożenia ułamków. Chociaż wcale nie masz do czynienia z ułamkami, możesz jakby zobaczyć, jak mianownik ∂v/∂x i licznik ∂x/∂a są takie same — ∂x — i dlatego "skracają się".

To jest łańcuch, moja osobista metoda wyboru do obliczania pochodnych cząstkowych. Łańcuch i drzewo są najłatwiejszym sposobem obliczenia tych istotnych pochodnych.

Spróbujmy jeszcze raz: jaka jest ∂v/∂b?

Najpierw używamy łańcucha i drzewa, aby skonstruować, jak powinno wyglądać obliczenie pochodnej cząstkowej:

1. podróż od v do y, a następnie b
   ![podróż od v do y, a następnie b]
2. Skonstruuj łańcuch: ∂v/∂b = (∂v/∂y) * (∂y/∂b)
3. Oblicz ∂v/∂y: v = 3x + 4y, więc ∂v/∂y traktuje y jako zmienną, a wszystko inne jako stałą, dlatego ∂v/∂y = 0 + 4(1) = 4
4. Oblicz ∂y/∂b: y = 4b², więc ∂y/∂b traktuje b jako zmienną, a wszystko inne jako stałą, dlatego ∂v/∂y = 8b
5. Pomnóż łańcuch razem: ∂v/∂b = 4(8b) = 32b

Gdy przyzwyczaisz się do notacji, zdajesz sobie sprawę, że rachunek różniczkowy nie jest taki trudny. Jeśli rozumiesz metodę łańcucha i drzewa oraz jesteś w stanie wykonać te obliczenia, jesteś w świetnym miejscu, aby zbudować własną sieć neuronową.
