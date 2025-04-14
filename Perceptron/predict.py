from simple_perceptron import SimplePerceptron
import argparse
import numpy as np

if __name__ == '__main__':

    # Parsowanie argumentów wiersza poleceń
    # Argumenty mogą być również wczytane z pliku (@plik.par)
    ap = argparse.ArgumentParser(fromfile_prefix_chars='@')
    ap.add_argument('-t', '--testset', help='Ścieżka do zbioru testowego',
        metavar='plik', required=True)
    ap.add_argument('-m', '--model', help='Ścieżka do wytrenowanego modelu',
        metavar='plik', required=True)

    args = vars(ap.parse_args())

    test_dataset_filename = args['testset']
    model_filename = args['model']

    # Utworzenie instancji klasy SimplePerceptron
    # (bez argumentów, ponieważ będzie używana tylko do predykcji)
    perceptron = SimplePerceptron()

    # Wczytanie zapisanego wcześniej modelu
    perceptron.load_model(model_filename)

    # Wczytanie danych testowych i przetestowanie perceptronu
    # z wykorzystaniem wytrenowanych wag
    Xtest, Yexpected = perceptron.read_input_data(test_dataset_filename)
    Yout = perceptron.test(Xtest)

    # Denormalizacja wyników
    Xtest, Yout, Yexpected = perceptron.unnormalize(Xtest, Yout, Yexpected)

    print('\nWyniki testów:')

    correct_predictions = 0
    for i in range(len(Yout)):
        # Dla funkcji sumowania:
        expected_rounded = round(Yexpected[i], 1)
        predicted_rounded = round(Yout[i], 1)
        is_correct = abs(expected_rounded - predicted_rounded) < 0.25
        
        if is_correct:
            correct_predictions += 1
            
        print(f'{Xtest[i][0]:.3f} + {Xtest[i][1]:.3f} = {Yout[i]:.3f} (oczekiwano {Yexpected[i]:.3f})')

    # Obliczenie dokładności (accuracy)
    accuracy = (correct_predictions / len(Yout)) * 100
    
    # Metryki jakości: RMSE, współczynnik determinacji R^2 i dokładność
    sse = sum((np.array(Yexpected) - np.array(Yout))**2)
    tse = (len(Yexpected) - 1) * np.var(Yexpected, ddof=1)
    rmse = np.sqrt(sse / len(Yout))
    r2_score = 1 - (sse / tse)
    
    print(f"\nBłąd RMSE       = {rmse:.2f}")
    print(f"Współczynnik R^2 = {r2_score:.2f}")
    print(f"Accuracy       = {accuracy:.2f}%")