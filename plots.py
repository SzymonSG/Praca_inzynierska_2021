import matplotlib.pyplot as plt
import numpy as np

def reverse_plot(reversed_time):
    alg = ['Bąbelkowe','Wybieranie','Wstawianie','Szybkie','Iter.Szybkie' ]
    time_rev = reversed_time
    xpos= np.arange(len(alg))
    plt.xticks(xpos,alg)
    plt.ylabel("czas w sekudnach")
    plt.title("Wydajność algorytmów sortowania dla danych odwróconych")
    plt.bar(xpos,time_rev,width=0.3,label="Odwórcona lista",color="blue")
    plt.legend()

def shuffle_python_plot(random_time):
    alg = ['Bąbelkowe','Wybieranie','Wstawianie','Szybkie','Iter.Szybkie' ]
    rand_schuff= random_time
    xpos= np.arange(len(alg))
    plt.xticks(xpos,alg)
    plt.ylabel("czas w sekundach")
    plt.title("Wydajność algorytmów sortowania dla danych tasowanych \n funkcją schuffle() z biblioteki random (python)")
    plt.bar(xpos,rand_schuff,width=0.3,label="Lista tasowana funkcją random.shuffle().",color="red")
    plt.legend()


def random_reps_plot(random_reps_time):
    alg = ['Bąbelkowe','Wybieranie','Wstawianie','Szybkie','Iter.Szybkie' ]
    rand_reps = random_reps_time
    xpos= np.arange(len(alg))
    plt.xticks(xpos,alg)
    plt.ylabel("czas w sekundach")
    plt.title("Wydajność algorytmów sortowania \n dla losowych danych z powtórzeniami")
    plt.bar(xpos,rand_reps,width=0.3,label="Lista z losowymi elem.-możliwe powtórzenia",color = "green")
    plt.legend()

def rev_and_shuff_plot(rev_and_shuff):
    alg = ['Bąbelkowe','Wybieranie','Wstawianie','Szybkie','Iter.Szybkie' ]
    control_schuff = rev_and_shuff
    xpos= np.arange(len(alg))
    plt.xticks(xpos,alg)
    plt.ylabel("czas w sekundach")
    plt.title("Wydajność algorytmów sortowania, danych generowanych\n przy pomocy własnego algorytmu tasowania.")
    plt.bar(xpos,control_schuff,width=0.3,label="Unikalna lista-(odwórcona i potasowana)",color = "orange")
    plt.legend()

