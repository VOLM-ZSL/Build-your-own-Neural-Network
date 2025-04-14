from simple_perceptron import SimplePerceptron
import argparse

if __name__ == '__main__':

    # Domyślne hiperparametry
    EPOCHS = 100
    LEARNING_RATE = 0.1
    ACTIVATION = 'tanh'
    SPLIT = 0.2
    SHUFFLE = False

    # Parsowanie argumentów wiersza poleceń
    # Argumenty mogą być również wczytane z pliku (@plik.par)
    ap = argparse.ArgumentParser(fromfile_prefix_chars='@')
    ap.add_argument('-d', '--dataset', help='Ścieżka do zbioru treningowego',
        metavar='plik', required=True)
    ap.add_argument('-e', '--epochs', help='Liczba epok treningowych',
        type=int, default=EPOCHS, metavar='liczba')
    ap.add_argument('-l', '--learning_rate', help='Współczynnik uczenia',
        type=float, default=LEARNING_RATE, metavar='float')
    ap.add_argument('-a', '--activation', help='Funkcja aktywacji',
        choices=['tanh', 'sigmoid', 'relu'], metavar='funkcja', default=ACTIVATION)
    ap.add_argument('-s', '--split', help='Podział dane treningowe/walidacyjne',
        type=float, default=SPLIT, metavar='float')
    ap.add_argument('-f', '--shuffle', help='Włącz mieszanie danych',
        action='store_true', default=SHUFFLE)

    args = vars(ap.parse_args())

    input_filename = args['dataset']
    epochs = args['epochs']
    activation = args['activation']
    learning_rate = args['learning_rate']
    split = args['split']
    shuffle = args['shuffle']

    # Inicjalizacja instancji klasy SimplePerceptron
    perceptron = SimplePerceptron(epochs=epochs,
                                  learning_rate=learning_rate,
                                  activation=activation)

    # Wczytanie danych z pliku CSV
    X, Y = perceptron.read_input_data(input_filename)

    # Podział na dane treningowe i walidacyjne
    Xtrain, Ytrain, Xvalid, Yvalid = perceptron.train_validation_split(X, Y, split=split, shuffle=shuffle)

    # Trenowanie perceptronu
    perceptron.train(Xtrain, Ytrain, Xvalid, Yvalid)

    # Zapisanie modelu do pliku (z rozszerzeniem .model)
    model_filename = input_filename.rsplit('.', 1)[0] + '.model'
    perceptron.save_model(model_filename)
    
    print(f"Model został zapisany jako: {model_filename}")