import timeit
import matplotlib.pyplot as plt
import logical_matrix_without_numpy as lv
import logical_matrix_numpy as ln

sizes = [10, 100, 500, 1000]


def benchmark():
    results = {"vanilla": {}, "numpy": {}}
    for size in sizes:
        time_taken_numpy = timeit.timeit(
            lambda: ln.generate_matrix((size, size)), number=10
        )
        time_taken_vanilla = timeit.timeit(
            lambda: lv.generate_matrix(size, size, val_min=1, val_max=20),
            number=10,
        )
        results["vanilla"].update({size: time_taken_vanilla})
        results["numpy"].update({size: time_taken_numpy})
    return results


def plot_results(results):
    plt.figure(figsize=(10, 6))

    vanilla_sizes = list(results["vanilla"].keys())
    vanilla_times = list(results["vanilla"].values())
    numpy_sizes = list(results["numpy"].keys())
    numpy_times = list(results["numpy"].values())

    plt.plot(vanilla_sizes, vanilla_times, label="Vanilla Python", marker="o")
    plt.plot(numpy_sizes, numpy_times, label="NumPy", marker="o")

    plt.xlabel("Taille de la matrice (n x n)")
    plt.ylabel("Temps d'exécution (secondes)")
    plt.title("Comparaison des performances : Vanilla Python vs NumPy")
    plt.legend()
    plt.grid(True)

    # Enregistrer le graphique dans un fichier
    plt.savefig("benchmark_results.png", format="png", dpi=200, bbox_inches="tight")
    plt.close()  # Fermer la figure pour libérer la mémoire


if __name__ == "__main__":
    results = benchmark()
    plot_results(results)
