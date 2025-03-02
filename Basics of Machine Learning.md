# Wprowadzenie
Czy kiedykolwiek zastanawiałeś się, jak ChatGPT wydaje się rozumieć, co do niego mówisz? Albo jak Gemini, gdy pokażesz mu zdjęcie węża, potrafi sklasyfikować, jakiego rodzaju to wąż?

Pomimo tego, jak bardzo ludzkie wydają się maszyny i jak niemożliwe byłoby udawanie takiej wiedzy, właśnie to robią maszyny – udają, aż im się uda.

Przypomnij sobie, kiedy byłeś małym dzieckiem, które nic nie wiedziało. Nauczyłeś się klasyfikować ludzi, zwierzęta, drzewa itp., ale jak?

Jeśli urodziłeś się w Polsce, jedynymi osobami, z którymi miałeś kontakt, byli twoi rodzice czy rodzeństwo. Musiałeś myśleć, że wszyscy ludzie są biali, dopóki nie zobaczyłeś innych żywych istot. Miały te same cechy co twoi rodzice, ale miały brązową, czarną lub żółtawą skórę.

Nie wyglądały jak psy, koty czy zebry. Musiałeś rozszerzyć swoją definicję człowieka, aby objąć coraz więcej ludzi – niskich, wysokich, szczupłych, grubych, z nogami lub bez. Poszerzyłeś swoją wiedzę, ponieważ otrzymałeś więcej danych.

W skrócie, dokładnie tak samo uczy się maszyna. Jeśli pokażesz komputerowi zdjęcie Jerry'ego Seinfelda i sklasyfikujesz go jako człowieka, komputer będzie myślał, że Jerry Seinfeld jest jedynym człowiekiem istniejącym na świecie. Nie uda mu się sklasyfikować żadnej innej osoby jako człowieka.

Ale jeśli dasz maszynie zdjęcia 100 000 ludzi, mówiąc za każdym razem „to jest człowiek, to jest człowiek", wtedy komputer stworzy szerszą definicję tego, jak wygląda człowiek – twarz, ramiona, około 150-180 cm wzrostu, ubrany, różne kolory skóry itp.

Maszyny uczą się z danych, dokładnie tak jak ludzie. Im więcej danych ma maszyna, tym bardziej poszerza się jej "światopogląd" i wiedza.

Oczywiście jakość danych ma znaczenie. Jeśli wychowasz dziecko, mówiąc mu, że każdy banan, który widzi, to w rzeczywistości jabłko, to za każdym razem, gdy wskaże na banana, będzie naprawdę wierzyło, że ten długi żółty owoc nazywa się jabłko.

Jak kolega z klasy tego nieszczęsnego dziecka mógłby skorygować to zachowanie? Cóż, powiedziałby mu: "stary, to jest banan". Wystarczająco często poprawiaj to zdezorientowane dziecko, a w końcu nauczy się prawidłowych nazw bananów i jabłek.

Co więc się stało? Dziecko uczyło się na swoich błędach i korygowało je. Znowu, dokładnie tak samo uczy się maszyna.
## Uczenie maszynowe składa się z następujących kroków:
1. Zbieranie poprawnie oznaczonych danych, na których maszyna będzie się uczyć.
2. Stworzenie metryki opisującej, ile błędów maszyna popełnia, próbując przewidzieć, czym coś jest.
3. Iteracyjne szkolenie w celu zmniejszenia tego błędu.

# Intuicja kosztu
Gdy po raz pierwszy używasz maszyny do uczenia maszynowego, przewidywania, które generuje, są całkowitą porażką. Więc "karamy" model, podobnie jak "karamy" dziecko, mówiąc mu, że się myli. Ale w przypadku maszyn idziemy o krok dalej – mówimy im, jak bardzo się mylą, co nazywamy kosztem modelu.

Powiedzmy, że trenujemy model do klasyfikacji kotów i psów, a testujemy go, podając trzy zdjęcia psów. Zamiast tego klasyfikuje je wszystkie jako koty.

**Ile więc odpowiedzi było poprawnych?**

Model miał 0/3 poprawnych odpowiedzi, więc oczywiście wypadł dość słabo. Ale 1/3 to lepszy wynik niż 0/3, a 2/3 jest jeszcze lepszy. Możemy określić ilościowo wskaźnik błędów poprzez koszt, z podstawową implementacją w następujący sposób:

**Koszt = liczba błędów / całkowita liczba przewidywań**  

Więc w przypadku naszego bardzo słabego modelu, z 3 przewidywań wykonał 3 błędne, więc koszt = 3/3 = 1, co jest najwyższym kosztem dla modelu.

**Całe uczenie maszynowe polega na próbie zminimalizowania tej metryki kosztu tak bardzo, jak to możliwe.** Koszt wynoszący 0 oznacza, że mamy 0 błędnych przewidywań z łącznie 3 przewidywań (0/3), co oznacza, że nasz model wszystko przewiduje poprawnie.

Zrozum to: **Niski koszt = dobry model, wysoki koszt = zły model**

Możesz myśleć o koszcie jako synonimie oceny – dostajesz D w klasie, niezbyt dobrze znasz materiał, ale jeśli dostajesz A, radzisz sobie świetnie.

Ale jak właściwie minimalizujemy ten koszt? Tu wkracza skomplikowana matematyka, a my wkrótce się jej nauczymy.

Na razie stwórzmy analogię do sieci neuronowych. Jak sugeruje nazwa, sieci neuronowe próbują naśladować to, co robi ludzki mózg, w nadziei na stworzenie sztucznej inteligencji dorównującej ludzkiej.

Ludzki mózg ma 100 miliardów neuronów, więc maszynowy model ludzkiego mózgu (sieć neuronowa) będzie miał 100 miliardów elementów obliczeniowych, które dla uproszczenia nazwiemy parametrami.

Jeśli koszt jest miarą tego, jak słabo radzi sobie model, to najpierw potrzebuje on wyniku modelu, który wymaga 100 miliardów parametrów do obliczenia ostatecznego wyniku. To sprawia, że koszt jest potężną funkcją, przyjmującą 100 miliardów zmiennych i generującą pojedynczą liczbę.

1. Czy możesz zminimalizować, a nawet zrozumieć funkcję tej wielkości? 
2. Czy możesz zminimalizować koszt ręcznie? 
Oto odpowiedzi na oba pytania:

1. Możesz. 
2. Nie możesz – dlatego używamy komputerów.
# Podsumowanie uczenia maszynowego
Teraz już wiesz, czym jest uczenie maszynowe. Kiedy próbujemy sprawić, by model uczenia maszynowego klasyfikował rzeczy takie jak obrazy lub dane, mówimy mu, jakie są poprawne odpowiedzi i testujemy go na danych.

Z tego testowania otrzymujemy metrykę kosztu, która pokazuje, jak słabo model przewiduje, i przeprowadzamy iteracyjny proces obejmujący skomplikowaną matematykę, aby zminimalizować ten koszt.

Kiedy koszt jest zminimalizowany, oznacza to, że model przewiduje rzeczy poprawnie, prawie tak dobrze jak człowiek.
