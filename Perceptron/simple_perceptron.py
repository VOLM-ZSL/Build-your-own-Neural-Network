import numpy as np
import csv
import pickle
import matplotlib.pyplot as plt
from time import time

class SimplePerceptron:
    def __init__(self, epochs=100, learning_rate=0.1, activation='tanh'):
        """
        Inicjalizacja prostego perceptronu
        
        Parametry:
        - epochs: liczba epok treningowych
        - learning_rate: współczynnik uczenia
        - activation: funkcja aktywacji ('tanh', 'sigmoid', 'relu')
        """
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.activation = activation
        self.weights = None
        self.bias = None
        self.normalize_params = {}
        
    def read_input_data(self, filename):
        """
        Wczytanie danych z pliku CSV
        
        Format pliku:
        - Dwie pierwsze kolumny: dane wejściowe X
        - Trzecia kolumna: oczekiwane wyjście Y
        
        Zwraca:
        - X: lista wektorów wejściowych
        - Y: lista oczekiwanych wyjść
        """
        X = []
        Y = []
        
        # Implementuj wczytywanie danych z pliku CSV
        # Wskazówka: Otwórz plik, użyj csv.reader, przetwórz każdy wiersz
        # Konwertuj stringi na float i przypisz odpowiednie kolumny do X i Y
        # Kod powinien pomijać puste wiersze
        # Pierwsze dwie kolumny to dane wejściowe X, trzecia kolumna to Y
        # #implementuj
        
        # Konwersja list do tablic numpy
        X = np.array(X)  # #implementuj - np.array() zamienia listę na tablicę numpy
        Y = np.array(Y)  # #implementuj
        
        # Normalizacja danych
        X, Y = self.normalize_data(X, Y)
        
        return X, Y
    
    def normalize_data(self, X, Y):
        """
        Normalizacja danych wejściowych i wyjściowych
        do zakresu [-1, 1] lub [0, 1] w zależności od funkcji aktywacji
        """
        if not self.normalize_params:
            # Zapisanie parametrów normalizacji tylko podczas trenowania
            # #implementuj - zapisz min i max wartości dla X i Y do słownika self.normalize_params
            self.normalize_params['X_min'] = np.min(X, axis=0)  # minimum dla każdej kolumny X
            self.normalize_params['X_max'] = np.max(X, axis=0)  # maksimum dla każdej kolumny X
            self.normalize_params['Y_min'] = # #implementuj - minimum dla Y
            self.normalize_params['Y_max'] = # #implementuj - maksimum dla Y
            
        # Zakres normalizacji zależny od funkcji aktywacji
        if self.activation == 'sigmoid':
            # Dla funkcji sigmoid normalizujemy do [0, 1]
            # Użyj formuły: (wartość - min) / (max - min)
            # #implementuj
            X_norm = # #implementuj - normalizacja X do zakresu [0, 1]
            Y_norm = # #implementuj - normalizacja Y do zakresu [0, 1]
        else:
            # Dla funkcji tanh i relu normalizujemy do [-1, 1]
            # Użyj formuły: 2 * (wartość - min) / (max - min) - 1
            # #implementuj
            X_norm = # #implementuj - normalizacja X do zakresu [-1, 1]
            Y_norm = # #implementuj - normalizacja Y do zakresu [-1, 1]
            
        return X_norm, Y_norm
    
    def unnormalize(self, X, Y_pred, Y_true):
        """
        Denormalizacja danych wyjściowych
        """
        if self.activation == 'sigmoid':
            # Dla funkcji sigmoid denormalizujemy z [0, 1]
            # Użyj formuły: wartość * (max - min) + min
            # #implementuj
            X_denorm = # #implementuj - denormalizacja X z zakresu [0, 1]
            Y_pred_denorm = # #implementuj - denormalizacja Y_pred z zakresu [0, 1]
            Y_true_denorm = # #implementuj - denormalizacja Y_true z zakresu [0, 1]
        else:
            # Dla funkcji tanh i relu denormalizujemy z [-1, 1]
            # Użyj formuły: (wartość + 1) / 2 * (max - min) + min
            # #implementuj
            X_denorm = # #implementuj - denormalizacja X z zakresu [-1, 1]
            Y_pred_denorm = # #implementuj - denormalizacja Y_pred z zakresu [-1, 1]
            Y_true_denorm = # #implementuj - denormalizacja Y_true z zakresu [-1, 1]
            
        return X_denorm, Y_pred_denorm, Y_true_denorm
    
    def train_validation_split(self, X, Y, split=0.2, shuffle=False):
        """
        Podział danych na zbiór treningowy i walidacyjny
        
        Parametry:
        - X: dane wejściowe
        - Y: oczekiwane wyjścia
        - split: proporcja podziału (domyślnie 0.2 = 20% danych jako walidacyjne)
        - shuffle: czy przemieszać dane przed podziałem
        
        Zwraca:
        - X_train, Y_train: dane treningowe
        - X_valid, Y_valid: dane walidacyjne
        """
        if shuffle:
            # Przemieszanie danych
            # #implementuj - utwórz tablicę indeksów, przemieszaj ją i użyj do przemieszania X i Y
            indices = # #implementuj - np.arange() tworzy tablicę indeksów od 0 do len(X)-1
            np.random.shuffle(indices)  # przemieszanie indeksów
            X = # #implementuj - użyj indeksów do przemieszania X
            Y = # #implementuj - użyj indeksów do przemieszania Y

        # Punkt podziału - NAJPIERW określamy punkt podziału, a DOPIERO POTEM dzielimy dane
        split_idx = int(len(X) * (1 - split))
        
        # #implementuj - podziel X i Y na części treningowe i walidacyjne
        X_train = # #implementuj - użyj indeksów od 0 do split_idx
        Y_train = # #implementuj - użyj indeksów od 0 do split_idx
        X_valid = # #implementuj - użyj indeksów od split_idx do końca
        Y_valid = # #implementuj - użyj indeksów od split_idx do końca
        
        return X_train, Y_train, X_valid, Y_valid
    
    def calculate_accuracy(self, predictions, targets): #W sumie accuracy to 
        """
        Obliczenie dokładności (accuracy) jako procent poprawnych predykcji
        Przyjmujemy, że predykcja jest poprawna, jeśli po zaokrągleniu
        do jednego miejsca po przecinku różni się od wartości oczekiwanej o mniej niż 0.1
        """
        correct = 0
        # #implementuj - policz liczbę poprawnych predykcji
    
        return (correct / len(predictions)) * 100
    
    def activate(self, x):
        """
        Funkcja aktywacji
        """
        if self.activation == 'sigmoid':
            # #implementuj funkcję sigmoid: 1 / (1 + np.exp(-x))
            return # #implementuj
        elif self.activation == 'tanh':
            # #implementuj funkcję tanh, możesz użyć np.tanh(x)
            return # #implementuj
        elif self.activation == 'relu':
            # #implementuj funkcję ReLU: max(0, x), możesz użyć np.maximum(0, x)
            return # #implementuj
        else:
            raise ValueError(f"Nieznana funkcja aktywacji: {self.activation}")
    
    def derivative(self, x):
        """
        Pochodna funkcji aktywacji
        """
        if self.activation == 'sigmoid':
            # #implementuj pochodną funkcji sigmoid: sigmoid(x) * (1 - sigmoid(x))
            sig = self.activate(x)
            return # #implementuj
        elif self.activation == 'tanh':
            # #implementuj pochodną funkcji tanh: 1 - tanh(x)^2
            return # #implementuj
        elif self.activation == 'relu':
            # #implementuj pochodną funkcji ReLU: 1 dla x > 0, 0 dla x <= 0
            # Wskazówka: użyj np.where(warunek, wartość_gdy_prawda, wartość_gdy_fałsz)
            return # #implementuj
        else:
            raise ValueError(f"Nieznana funkcja aktywacji: {self.activation}")
    
    def forward(self, X):
        """
        Propagacja w przód (forward pass)
        """
        # #implementuj - oblicz iloczyn skalarny wejść i wag + bias
        # Wskazówka: użyj np.dot()
        z = # #implementuj
        
        # Zastosowanie funkcji aktywacji
        # #implementuj - zwróć parę (wynik aktywacji, z)
        return # #implementuj
    
    def train(self, X_train, Y_train):
        """
        Trenowanie perceptronu
        
        Parametry:
        - X_train, Y_train: dane treningowe
        """
        n_features = X_train.shape[1]
        
        # Inicjalizacja wag i biasu
        if self.weights is None:
            # #implementuj - losowa inicjalizacja wag
            # Wskazówka: użyj np.random.randn(n_features) * 0.1
            self.weights = # #implementuj
        if self.bias is None:
            # #implementuj - inicjalizacja biasu zerami
            self.bias = # #implementuj
        
        # Listy do zapisywania błędów i dokładności
        train_errors = []
        train_accuracy = []
        
        print("Rozpoczęcie trenowania...")
        start_time = time()
        
        for epoch in range(self.epochs):
            # Forward pass
            # #implementuj - oblicz predykcje dla danych treningowych
            predictions, _ = # #implementuj
            
            # Obliczenie błędu MSE
            # #implementuj - oblicz błąd średniokwadratowy (MSE) między predykcjami a Y_train
            # Wskazówka: użyj np.mean((predictions - Y_train)**2)
            train_error = # #implementuj
            train_errors.append(train_error)
            
            # Obliczenie dokładności
            # #implementuj - oblicz dokładność dla danych treningowych
            train_acc = # #implementuj
            train_accuracy.append(train_acc)
            
            
            # Wyświetlanie postępu co 10 epok
            if (epoch + 1) % 10 == 0:
                print(f"Epoka {epoch+1}/{self.epochs}, Błąd: {train_error:.4f}, Dokładność: {train_acc:.2f}%, ")
            
            # Propagacja wsteczna
            for i in range(len(X_train)):
                # Forward dla pojedynczego przykładu
                # #implementuj - oblicz predykcję dla pojedynczego przykładu
                # Wskazówka: użyj reshape(1, -1) aby przekształcić wektor na macierz 1xn
                prediction, z = # #implementuj
                
                # Obliczenie gradientu
                # #implementuj - oblicz błąd i gradient
                error = # #implementuj - różnica między predykcją a oczekiwaną wartością
                gradient = # #implementuj - iloczyn błędu i pochodnej funkcji aktywacji
                
                # Aktualizacja wag i biasu
                # #implementuj - zaktualizuj wagi i bias
                # Wskazówka: wagi -= learning_rate * gradient * X_train[i]
                # bias -= learning_rate * gradient
                # #implementuj
        
        training_time = time() - start_time
        print(f"\nTrening zakończony w {training_time:.2f} sekund")
        
        # Wykres błędów i dokładności
        # #implementuj - stwórz wykres błędów i dokładności
        plt.figure(figsize=(12, 5))
        
        # Wykres błędów
        plt.subplot(1, 2, 1)
        # #implementuj - narysuj wykres błędów treningowych i walidacyjnych
        
        # Wykres dokładności
        plt.subplot(1, 2, 2)
        # #implementuj - narysuj wykres dokładności treningowej i walidacyjnej
        
        plt.tight_layout()
        plt.savefig('training_progress.png')
        plt.close()
        
        print(f"Wykres przebiegu trenowania zapisany jako 'training_progress.png'")
        
        # Wyświetlenie końcowych wyników
        # #implementuj - wyświetl końcową dokładność dla zbiorów treningowego i walidacyjnego
        final_train_accuracy = # #implementuj
        print(f"Końcowa dokładność - zbiór treningowy: {final_train_accuracy:.2f}%")
    
    def test(self, X):
        """
        Testowanie perceptronu na nowych danych
        """
        predictions, _ = self.forward(X)
        return predictions
    
    def save_model(self, filename):
        """
        Zapisanie wytrenowanego modelu do pliku
        """
        model_data = {
            'weights': self.weights,
            'bias': self.bias,
            'activation': self.activation,
            'normalize_params': self.normalize_params
        }
        
        with open(filename, 'wb') as file:
            pickle.dump(model_data, file)
    
    def load_model(self, filename):
        """
        Wczytanie modelu z pliku
        """
        with open(filename, 'rb') as file:
            model_data = pickle.load(file)
            
        self.weights = model_data['weights']
        self.bias = model_data['bias']
        self.activation = model_data['activation']
        self.normalize_params = model_data['normalize_params']