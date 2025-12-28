import matplotlib.pyplot as plt
import numpy as np

ns = [8, 10, 12, 15, 20, 30, 40, 50, 100]

times_cp_bool = [0.0150, 0.0560, 0.0240, 0.0430, 0.0600, 0.1670, 0.4090, 0.3630, 7.3820]
times_cp_int  = [0.0004, 0.0003, 0.0007, 0.0003, 0.0012, 0.0010, 0.0015, 0.0057, 0.0052]
times_qubo    = [1.1588, 1.1519, 1.1203, 1.1179, 1.1154, 1.2332, 1.2297, 1.5197, 4.3496]
times_local   = [0.0001, 0.0010, 0.0715, 0.0010, 0.0001, 0.0094, 0.0278, 0.0028, 0.0443]

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(ns, times_cp_bool, marker='o', label='CP Boolean (Coin-BC)')
plt.plot(ns, times_cp_int,  marker='s', label='CP Integer (Gecode)')
plt.plot(ns, times_qubo,    marker='^', label='QUBO (Total Time)')
plt.plot(ns, times_local,   marker='x', label='Local Search')

plt.title('Performance Comparison (Linear Scale)')
plt.xlabel('N (Board Size)')
plt.ylabel('Time (seconds)')
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(ns, times_cp_bool, marker='o', label='CP Boolean (Coin-BC)')
plt.plot(ns, times_cp_int,  marker='s', label='CP Integer (Gecode)')
plt.plot(ns, times_qubo,    marker='^', label='QUBO (Total Time)')
plt.plot(ns, times_local,   marker='x', label='Local Search')

plt.yscale('log') 
plt.title('Performance Comparison (Log Scale)')
plt.xlabel('N (Board Size)')
plt.ylabel('Time (seconds) - Log Scale')
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.legend()

plt.tight_layout()
plt.savefig('nqueens_benchmark.png', dpi=300)
print("Grafico salvato come 'nqueens_benchmark.png'")
plt.show()