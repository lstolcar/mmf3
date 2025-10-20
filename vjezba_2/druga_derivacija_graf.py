import numpy as np
import matplotlib.pyplot as plt

def druga_derivacija(f, x, h):
    return (f(x + h) - 2*f(x) + f(x - h)) / (h**2)

f = np.exp
df_true = np.exp


x_values = [1, 5, 10]
h_values = np.array([1e-1, 1e-2, 1e-3,1e-4,1e-5,1e-6])


errors = {x: [] for x in x_values}
for x in x_values:
    for h in h_values:
        approx = druga_derivacija(f, x, h)
        err = abs(approx - df_true(x))
        errors[x].append(err)


plt.figure(figsize=(8,5))
for x in x_values:
    plt.loglog(h_values, errors[x], marker='o', label=f"x = {x}")

plt.xlabel("Korak h (log-skala)")
plt.ylabel("Apsolutna pogreška (log-skala)")
plt.title("Pogreška druge derivacije e^x u ovisnosti o koraku h")
plt.grid(True, which="both", ls="--", lw=0.5)
plt.legend()

plt.subplots_adjust(bottom=0.2)

plt.figtext(
    0.1, 0.1,
    "Za velike vrijednosti h pogreška je veća zbog grube aproksimacije , dok za vrlo male h raste zbog numeričkog zaokruživanja i oduzimanja gotovo jednakih brojeva.",
    wrap=True, ha='center', fontsize=9
)

plt.show()


print("Procijenjeni red točnosti (nagib u log–log skali):")
for x in x_values:
    logh = np.log(h_values)
    loge = np.log(errors[x])
    slope, _ = np.polyfit(logh, loge, 1)
    print(f"  x = {x}: p ≈ {slope:.3f}")
