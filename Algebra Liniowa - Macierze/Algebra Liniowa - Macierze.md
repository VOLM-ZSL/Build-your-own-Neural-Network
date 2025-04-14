Poniżej prezentuję tłumaczenie tekstu na język polski:

# 2) Ekspresowy kurs o macierzach

Macierze są zwięzłym sposobem reprezentowania układów równań. Kiedy musisz przetwarzać setki liczb jednocześnie (co często ma miejsce w uczeniu maszynowym), macierze są kluczem do tego, by wszystko było zrozumiałe.

Na przykład, jak zwięźle przedstawić (2×1)+(3×5)+(2×2)(2 \times 1) + (3 \times 5) + (2 \times 2)? W ten sposób:

## Iloczyn skalarny

Iloczyn skalarny to operacja, w której mnożymy dwa wektory, a następnie sumujemy ich iloczyny elementów. Jeśli masz dwa wektory:

(2,3,2)⋅(1,5,2)(2, 3, 2) \cdot (1, 5, 2)

To proces wygląda tak:

1. Mnożymy pierwszy element pierwszego wektora przez pierwszy element drugiego wektora: 2×12 \times 1.
2. Mnożymy drugi element pierwszego wektora przez drugi element drugiego wektora: 3×53 \times 5.
3. Mnożymy trzeci element pierwszego wektora przez trzeci element drugiego wektora: 2×22 \times 2.
4. Sumujemy wyniki:

(2×1)+(3×5)+(2×2)=2+15+4=21(2 \times 1) + (3 \times 5) + (2 \times 2) = 2 + 15 + 4 = 21

Ostateczny wynik to pojedyncza liczba, czyli skalar. Dlatego nazywa się to **iloczynem skalarnym**.

Pamiętaj, że iloczyn skalarny można wykonać tylko wtedy, gdy oba wektory mają tę samą liczbę elementów.

## Wektory i macierze

Wektory to w zasadzie macierze jednokolumnowe lub jednowierszowe. Macierze natomiast są bardziej ogólną strukturą, mają wiersze i kolumny. Przykładowa macierz wygląda tak:

A=[2314]A = \begin{bmatrix} 2 & 3 \\ 1 & 4 \end{bmatrix}

## Mnożenie macierzy

Mnożenie macierzy to proces bardziej skomplikowany niż iloczyn skalarny. Każdy element wynikowej macierzy jest sumą iloczynów odpowiednich elementów wiersza jednej macierzy i kolumny drugiej. Przykład:

[2314]×[5678]=[(2×5+3×7)(2×6+3×8)(1×5+4×7)(1×6+4×8)]=[31363338]\begin{bmatrix} 2 & 3 \\ 1 & 4 \end{bmatrix} \times \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} = \begin{bmatrix} (2 \times 5 + 3 \times 7) & (2 \times 6 + 3 \times 8) \\ (1 \times 5 + 4 \times 7) & (1 \times 6 + 4 \times 8) \end{bmatrix} = \begin{bmatrix} 31 & 36 \\ 33 & 38 \end{bmatrix}

Każdy element nowej macierzy jest wynikiem sumy iloczynów elementów z wiersza pierwszej macierzy i odpowiadających im elementów kolumny drugiej macierzy.

## Wymiarowość mnożenia macierzy

Aby pomnożyć dwie macierze, liczba kolumn pierwszej macierzy musi być równa liczbie wierszy drugiej macierzy. Jeśli pierwsza macierz ma wymiary a×ba \times b, a druga macierz ma wymiary b×cb \times c, to wynikowa macierz będzie miała wymiary a×ca \times c.

**Przykład niepoprawnego mnożenia:**

[1234]×[5678910111213]\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \times \begin{bmatrix} 5 & 6 & 7 \\ 8 & 9 & 10 \\ 11 & 12 & 13 \end{bmatrix}

Nie można wykonać tej operacji, ponieważ liczba kolumn pierwszej macierzy (2) nie zgadza się z liczbą wierszy drugiej macierzy (3).

## Transpozycja macierzy

Transpozycja macierzy polega na zamianie wierszy na kolumny. Oznaczamy ją jako ATA^T. Przykład:

AT=[2314]T=[2134]A^T = \begin{bmatrix} 2 & 3 \\ 1 & 4 \end{bmatrix}^T = \begin{bmatrix} 2 & 1 \\ 3 & 4 \end{bmatrix}

Transpozycja jest użyteczna w wielu operacjach, zwłaszcza w mnożeniu macierzy. Istnieje ważna własność transpozycji:

(A×B)T=BT×AT(A \times B)^T = B^T \times A^T

## Podsumowanie

- **Iloczyn skalarny** dwóch wektorów daje pojedynczą liczbę.
- **Mnożenie macierzy** jest możliwe tylko wtedy, gdy liczba kolumn pierwszej macierzy zgadza się z liczbą wierszy drugiej.
- **Transpozycja macierzy** zamienia wiersze z kolumnami.
- **Rozmiar wynikowej macierzy** w mnożeniu to a×ca \times c, jeśli pierwsza macierz ma rozmiar a×ba \times b, a druga b×cb \times c.
$$ \begin{bmatrix} 2 & 3 \\ 1 & 4 \end{bmatrix} \times \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} = \begin{bmatrix} (2 \times 5 + 3 \times 7) & (2 \times 6 + 3 \times 8) \\ (1 \times 5 + 4 \times 7) & (1 \times 6 + 4 \times 8) \end{bmatrix} = \begin{bmatrix} 31 & 36 \\ 33 & 38 \end{bmatrix} $$
$$ a \times b $$
$$ \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \times \begin{bmatrix} 5 & 7 & 9 \\ 6 & 8 & 10 \end{bmatrix}=\begin{bmatrix} 28 & 38 & 48 \\ 29 & 39 & 49\end{bmatrix} $$
$$
(2 \times 5 + 3 \times 7)
$$

$$
(2 \times 6 + 3 \times 8)
$$

$$
(1 \times 5 + 4 \times 7)
$$

$$
a \times b, \quad b \times c \quad \Rightarrow \quad a \times c
$$

$$
3 \times 2 \times 2 \times 2
$$

$$
4 \times 8 \times 8 \times 3
$$
$$ \begin{bmatrix} 5 & 6 \\ 7 & 8 \\ 9 & 10 \end{bmatrix} \times \begin{bmatrix}2 & 3 \\ 1 & 4 \end{bmatrix}=Git=\begin{bmatrix} 10+6 & 15+24 \\ 14 + 8 & 21+32 \\ 18+10 & 27+40 \end{bmatrix} = \begin{bmatrix} 16 & 39 \\ 22 & 53 \\ 28 & 67 \end{bmatrix}$$
$$ \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \times \begin{bmatrix} 5 & 7 \\ 6 & 7 \end{bmatrix}=\begin{bmatrix} 5+14 & 6+16 \\ 15 + 28 & 18+32 \end{bmatrix} = \begin{bmatrix} 19 & 22 \\ 43 & 50\end{bmatrix}$$
$$ \begin{bmatrix} 5 & 7 \\ 6 & 7 \end{bmatrix} \times \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}=\begin{bmatrix} 5+18 & 10+24 \\ 7 + 24 & 14+32 \end{bmatrix} = \begin{bmatrix} 23 & 34 \\ 31 & 46\end{bmatrix}$$
$$ \begin{bmatrix} 5 & 6 \\ 7 & 8 \\ 9 & 10 \end{bmatrix} ^{T}=\begin{bmatrix} 5 & 7 & 9 \\ 6 & 8 & 10\end{bmatrix} $$

$$W^{T}X=XW$$