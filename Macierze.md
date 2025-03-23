# Kurs o macierzach

Macierze są zwięzłym sposobem reprezentowania układów równań. Kiedy musisz przetwarzać setki liczb jednocześnie (co często ma miejsce w uczeniu maszynowym), macierze są kluczem do tego, by wszystko było zrozumiałe.

Na przykład, jak zwięźle przedstawić $$(2 \times 1) + (3 \times 5) + (2 \times 2)$$
?   
Można tak:  
$$(2, 3, 2) \cdot(1, 5, 2)$$


## Iloczyn skalarny
Tutaj mnożymy dwa wektory (wyjaśnię później) w operacji zwanej iloczynem skalarnym, która przebiega w następujących krokach:
$$(2 \times 1) + (3 \times 5) + (2 \times 2) = 2 + 15 + 4 = 21$$
1. Dla pierwszego elementu w pierwszym wektorze, pomnóż go przez pierwszy element w drugim wektorze.
2. Dla drugiego elementu w pierwszym wektorze, pomnóż go przez drugi element w drugim wektorze.
3. Dla trzeciego elementu w pierwszym wektorze, pomnóż go przez trzeci element w drugim wektorze.
4. Teraz zsumuj te trzy liczby i to jest iloczyn skalarny.

Łączysz każdy element z obu wektorów w kolejności, mnożysz je, a następnie dodajesz te wynikowe liczby, więc przejdźmy przez matematykę:

- Pierwsza para: 2*1
- Druga para: 3*5
- Trzecia para: 2*2

Dodając wszystko razem, otrzymujesz 2 + 15 + 4 = 21. Więc gdy wykonujesz iloczyn skalarny dwóch wektorów, otrzymujesz pojedynczą liczbę (sumę), którą nazywamy skalarem.

Pamiętaj, że nie możesz wykonać iloczynu skalarnego dwóch wektorów, jeśli mają różne długości. Co jeśli jeden wektor ma 2 elementy, a drugi wektor ma 3 elementy? Ten trzeci element w drugim wektorze nie ma się z czym sparować, co prowadzi do błędu (ok, nie aż tak dramatycznego).

Wektory to po prostu jednowymiarowe macierze, co oznacza, że działają po prostu jak lista liczb.

Aby głębiej zrozumieć wektory, obejrzyj następujące filmy (nie są wymagane do zbudowania sieci, ale są niezwykle pomocne):
- Dowiedz się, co reprezentują wektory [tutaj](https://www.youtube.com/watch?v=fNk_zzaMoSs&t=2s)

Macierze są bardziej skomplikowane. Są dwuwymiarowe i mogą mieć wiele wierszy i kolumn. Oto przykład macierzy:

**Macierz 2 na 2**  
*Macierz z 2 wierszami i 2 kolumnami* 

![$$A = \begin{bmatrix} 2 & 3 \\ 1 & 4 \end{bmatrix}$$](https://github.com/user-attachments/assets/604d8cde-b1b1-476c-af29-9bc30622b76e)
  
Podsumujmy terminologię:
- Gdy myślisz o skalarze, wyobraź sobie pojedynczą liczbę.
- Gdy myślisz o wektorze, wyobraź sobie listę liczb.
- Gdy myślisz o macierzy, wyobraź sobie tabelę liczb.

Dlaczego tak bardzo dbamy o macierze? Ponieważ mnożenie macierzy może zamienić wiele obliczeń liczbowych w proste wyrażenia. Na przykład, co jeśli chcę pomnożyć wiele liczb razem, ale nie chcę jednej końcowej sumy — chcę nową macierz jako wynik?

**Przykład mnożenia dwóch macierzy**
  
![$$ \begin{bmatrix} 2 & 3 \\ 1 & 4 \end{bmatrix} \times \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} = \begin{bmatrix} (2 \times 5 + 3 \times 7) & (2 \times 6 + 3 \times 8) \\ (1 \times 5 + 4 \times 7) & (1 \times 6 + 4 \times 8) \end{bmatrix} = \begin{bmatrix} 31 & 36 \\ 33 & 38 \end{bmatrix} $$](https://github.com/user-attachments/assets/db2f968b-980c-40ea-b1e7-f5a1f1ba29ab)

Mnożenie macierzy działa następująco:
1. W pierwszej macierzy weź pierwszy wiersz pierwszej macierzy (zauważ, że to wektor, ponieważ jest jednowymiarowy, po prostu lista liczb) i pierwszą kolumnę drugiej macierzy (również wektor!) i wykonaj ich iloczyn skalarny. To jest pierwszy wpis wynikowej macierzy. To jest obliczenie (2*5 + 3*7).
2. W pierwszej macierzy weź pierwszy wiersz pierwszej macierzy i drugą kolumnę drugiej macierzy i wykonaj ich iloczyn skalarny. To jest drugi wpis wynikowej macierzy. To jest obliczenie (2*6 + 3*8).
3. W pierwszej macierzy weź drugi wiersz pierwszej macierzy i pierwszą kolumnę drugiej macierzy i wykonaj ich iloczyn skalarny. To jest trzeci wpis wynikowej macierzy. To jest obliczenie (1*5+ 4*7).
4. W pierwszej macierzy weź... czy w ogóle jeszcze słuchasz?

Tak, rozumiem. Mnożenie macierzy jest wyczerpujące i szczerze mówiąc, mylące. Dobra wiadomość jest taka, że nie musisz rozumieć, jak wykonać mnożenie macierzy, tylko kiedy jest ono możliwe.

Najważniejszym czynnikiem mnożenia macierzy jest zrozumienie wymiarowości każdej macierzy i jak będzie wyglądać macierz wynikowa.

Jeśli nie nauczysz się niczego innego z tego artykułu, naucz się przynajmniej tego, co następuje:

## Wymiarowość mnożenia macierzy
Jeśli macierz ma 2 wiersze i 2 kolumny, jest to macierz 2 x 2 (czytaj "x" jako "na").

Jeśli macierz ma 3 wiersze i 4 kolumny, jest to macierz 3 x 4.

Więc ogólny wzór na opisanie wymiarowości macierzy to wiersze x kolumny, zawsze. Ta notacja ma znaczenie dla zrozumienia, które kombinacje macierzy możemy, a których nie możemy mnożyć.

Dwie macierze można ze sobą pomnożyć, jeśli pierwsza macierz ma wymiary a x b, a druga macierz ma wymiary b x c, a wtedy macierz wynikowa będzie miała wymiary a x c.

Co mam na myśli? Cóż, liczba kolumn w pierwszej macierzy musi być dokładnie równa liczbie wierszy w drugiej macierzy.

Spróbujmy kombinacji mnożenia macierzy, która nie może być porządnie wykonana:

**Przykład niemożliwego mnożenia macierzy między macierzą 2 x 2 a macierzą 3 x 2.**  
![$$ \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \times \begin{bmatrix} 5 & 6 \\ 7 & 8 \\ 9 & 10 \end{bmatrix}=Niemożliwe $$](https://github.com/user-attachments/assets/5e3505ee-7a0a-4dfe-82c0-4be4ba1955db)

Jeśli spróbujemy wykonać iloczyn skalarny między pierwszym wierszem pierwszej macierzy a pierwszą kolumną drugiej macierzy, zobaczysz, że 9 jest samo. Z czym mamy je sparować i pomnożyć — z pustką? Widzisz, nie da się tego zrobić.

Ogólna zasada, którą być może zauważyłeś, polega na tym, że wiersze w pierwszej macierzy muszą mieć ten sam rozmiar (taką samą liczbę elementów) jak kolumny w drugiej macierzy. Nie możesz wykonać iloczynu skalarnego dwóch wektorów, jeśli mają różne rozmiary.

A co, jeśli zamienimy te dwie macierze miejscami?  
![$$ \begin{bmatrix} 5 & 6 \\ 7 & 8 \\ 9 & 10 \end{bmatrix} \times \begin{bmatrix}2 & 3 \\ 1 & 4 \end{bmatrix}=Git=\begin{bmatrix} 10+6 & 15+24 \\ 14 + 8 & 21+32 \\ 18+10 & 27+40 \end{bmatrix} = \begin{bmatrix} 16 & 39 \\ 22 & 53 \\ 28 & 67 \end{bmatrix}$$](https://github.com/user-attachments/assets/94f4574f-7fa2-4d85-bc15-700ffa43c869)


**Mnożenie macierzy 3 x 2 przez macierz 2 x 2 daje prawidłową macierz 3 x 2**

Teraz wymiary mnożenia poprawnie podążają za wzorem a x b i b x c, dając macierz wynikową a x c. Przyjrzyjmy się wymiarom:

- a: Liczba wierszy w pierwszej macierzy, czyli 3
- b: Liczba kolumn w pierwszej macierzy, czyli 2
- c: Liczba kolumn w drugiej macierzy, czyli 2

Więc macierz 3 x 2 razy macierz 2 x 2 daje macierz 3 x 2. Lubię myśleć o tej operacji jako o swoistym "zgniataniu" i łączeniu środkowych dwóch liczb, tak jak:

3 x 2 razy 2 x 2  
3 x 2oojejjestemzgniatany2 x 2  
wymiary macierzy wynikowej: 3 x 2

Zróbmy jeszcze jeden przykład dla utrwalenia.

4 x 8 razy 8 x 3  
4 x 8oojejjestemzgniatany8 x 3  
wymiary macierzy wynikowej: 4 x 3

Ostatnia rzecz do zapamiętania to to, że przy mnożeniu macierzy kolejność ma znaczenie. Oto przykład, gdzie mnożymy dwie macierze 2 x 2 razem (więc ich wymiary zawsze będą prawidłowe), ale robimy to w dwóch różnych kolejnościach i otrzymujemy zupełnie różne wyniki.

**Przykład, jak mnożenie macierzy NIE jest przemienne**  
![$$ \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \times \begin{bmatrix} 5 & 7 \\ 6 & 7 \end{bmatrix}=\begin{bmatrix} 5+14 & 6+16 \\ 15 + 28 & 18+32 \end{bmatrix} = \begin{bmatrix} 19 & 22 \\ 43 & 50\end{bmatrix}$$
$$ \begin{bmatrix} 5 & 7 \\ 6 & 7 \end{bmatrix} \times \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}=\begin{bmatrix} 5+18 & 10+24 \\ 7 + 24 & 14+32 \end{bmatrix} = \begin{bmatrix} 23 & 34 \\ 31 & 46\end{bmatrix}$$
](https://github.com/user-attachments/assets/9a2c75c3-e1c3-4b80-a0f5-ed31a11c4371)


W kontekście uczenia maszynowego kolejność mnożenia macierzy może być bardzo myląca, ale jak zobaczysz później, najważniejszą częścią jest po prostu dopasowanie wymiarów. Ta nieprzemienna właściwość mnożenia macierzy jest ważna do zapamiętania, ale nie będziesz musiał się nią zajmować.

Świetnie. Teraz, gdy już wiesz, jak działają wymiary macierzy, pozostaje jeszcze jeden krok, zanim pomyślnie nauczysz się całej algebry liniowej potrzebnej do stworzenia sieci neuronowej.

Aby uzyskać bardziej szczegółowe zrozumienie, obejrzyj te dwa świetne filmy:  
[Transformacje Liniowe](https://www.youtube.com/watch?v=kYB8IZa5AuE&t=2s)  
[Mnożenie macierzy](https://www.youtube.com/watch?v=XkY2DOUCWMU&t=1s)

## Transpozycja
Transpozycja to prosta koncepcja. Transponujesz macierz, po prostu zamieniając miejscami jej wiersze i kolumny.

W poniższym przykładzie transponujemy macierz 3 x 2 w macierz 2 x 3. Symbol "T" oznacza po prostu, że transponujemy macierz.

**Przykład transponowania macierzy 3 x 2 w macierz 2 x 3 poprzez zamianę wierszy i kolumn.**  
![$$ \begin{bmatrix} 5 & 6 \\ 7 & 8 \\ 9 & 10 \end{bmatrix} ^{T}=\begin{bmatrix} 5 & 7 & 9 \\ 6 & 8 & 10\end{bmatrix} $$](https://github.com/user-attachments/assets/0b2d526e-1805-450c-9196-2c22bbf26955)

Pierwsza kolumna macierzy staje się pierwszym wierszem w nowej transponowanej macierzy.

Druga kolumna macierzy staje się drugim wierszem w nowej transponowanej macierzy i ten wzorzec jest kontynuowany.

Dlaczego transpozycja jest ważna? Ponieważ pozwala nam pomnożyć dwie macierze, których w przeciwnym razie nie moglibyśmy pomnożyć.

Wróćmy do poprzedniego przykładu:

**2 x 2 razy macierz 3 x 2 jest niemożliwe**  
![$$ \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \times \begin{bmatrix} 5 & 6 \\ 7 & 8 \\ 9 & 10 \end{bmatrix}=Niemożliwe $$](https://github.com/user-attachments/assets/5e3505ee-7a0a-4dfe-82c0-4be4ba1955db)  
Ale co jeśli transponujemy tę macierz 3 x 2 w macierz 2 x 3?  
![$$ \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \times \begin{bmatrix} 5 & 7 & 9 \\ 6 & 8 & 10 \end{bmatrix}=\begin{bmatrix} 28 & 38 & 48 \\ 29 & 39 & 49\end{bmatrix} $$](https://github.com/user-attachments/assets/4a489376-bd7b-45b1-a2fd-4d9f0378cea0)

**Transpozycja pozwala nam pomnożyć dwie macierze razem bez zmiany kolejności (co, jak się nauczyłeś wcześniej, ma znaczenie).**

Transpozycja macierzy daje nam również dużą elastyczność w mnożeniu macierzy według następującego prawa:

**Prawo transpozycji**  
$$W^{T}X=XW$$   

Dlaczego nie spróbujesz udowodnić tego samodzielnie? Użyj poniższych macierzy.

**Spróbuj pomnożyć te macierze, aby udowodnić powyższe prawo.**  
![$$ \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \times \begin{bmatrix} 5 & 7 & 9 \\ 6 & 8 & 10 \end{bmatrix}=\begin{bmatrix} 28 & 38 & 48 \\ 29 & 39 & 49\end{bmatrix} $$](https://github.com/user-attachments/assets/4a489376-bd7b-45b1-a2fd-4d9f0378cea0)
## Podsumowanie
- Iloczyn skalarny dwóch wektorów daje pojedynczą liczbę.
- Przy mnożeniu macierzy kolejność ma znaczenie.
- Możesz pomnożyć dwie macierze tylko wtedy, gdy pierwsza macierz ma wymiary a x b, a druga ma wymiary b x c, co daje macierz o wymiarach a x c.
- Transponowanie macierzy zamienia jej kolumny i wiersze. Sprawia, że macierz o wymiarach a x b zmienia się w macierz o wymiarach b x a.
