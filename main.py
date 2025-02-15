import numpy as np
import matplotlib.pyplot as plt

def calculate_r(x1, x2):
    return np.sqrt(x1**2 + x2**2)

def calculate_v(x1, x2):
    return np.sqrt(x1**2 + x2**2)

# System of differential equations
def f(x):
    x1, x2, x3, x4 = x
    r = calculate_r(x1, x2)
    dx1 = x3
    dx2 = x4
    dx3 = -x1 / r**3
    dx4 = -x2 / r**3
    
    return np.array([dx1, dx2, dx3, dx4])

# Energy Integral
def I(x):
    x1, x2, x3, x4 = x
    v2 = calculate_v(x3, x4) ** 2
    r = calculate_r(x1, x2)

    return v2 / 2 - 1 / r

# Delta X |∆x|
def delta_r(x, t):
    x1, x2 = x[:2]
    
    r1 = np.cos(t)
    r2 = np.sin(t)

    return np.sqrt((r1 - x1)**2 + (r2 - x2)**2)

def nacozy_stabilization(I_0, x, tolerance=1E-8, max_iter=1000):
    x_temp = x
    for i in range(max_iter):
        x1, x2, x3, x4 = x
        r = calculate_r(x1, x2)
        v2 = calculate_v(x3, x4) ** 2

        H = v2 / 2 - 1 / r
        D = v2 + 1 / r**4

        # H caligraphy
        H_cal = H - I_0

        if abs(H_cal) < tolerance:
            break

        correction_factor = 1 - (H_cal / D) * (1 / r**3)
        x1_stabilized = x1 * correction_factor
        x2_stabilized = x2 * correction_factor
        x3_stabilized = x3 * (1 - H_cal / D)
        x4_stabilized = x4 * (1 - H_cal / D)
        x_temp = np.array([x1_stabilized, x2_stabilized, x3_stabilized, x4_stabilized])

    return x_temp

def heun(f, x0, t0, t_end, h, stabilization_interval=10):
    I_0 = I(x0)
    r_delta = delta_r(x0, t0)
    t = t0
    x = x0
    trajectory = [x]
    times = [t]
    r_deltas = [r_delta]
    energy_deltas = [0]

    iter_count = 0
    while t < t_end:
        k1 = f(x)
        k2 = f(x + h * k1)
        x_next = x + 0.5 * h * (k1 + k2)

        # If you want to stabilize the system every several iterations then uncomment the following lines.
        # if iter_count % stabilization_interval == 0:
        #     x_next = nacozy_stabilization(I_0, x_next)
        
        # Stabilization on every iterations
        x_next = nacozy_stabilization(I_0, x_next)

        x = x_next
        t += h
        trajectory.append(x)
        times.append(t)

        # Calculate r delta |∆x|
        r_deltas.append(delta_r(x, t))

        # Calculate energy delta
        energy_deltas.append(abs(I(x) - I_0))

        iter_count += 1

    print(f"Completed Heun's method with step size {h} in {iter_count} iterations.")
    
    return np.array(times), np.array(trajectory), np.array(r_deltas), np.array(energy_deltas)

if __name__ == '__main__':
    # Initial conditions
    x0 = np.array([1.0, 0.0, 0.0, 1.0])
    t0 = 0
    T = 2 * np.pi
    t_end = t0 + 1000 * T

    all_r_deltas = []
    all_energy_deltas = []
    step_sizes = []

    for i in range(4, 13): # i = [4, 12]
        h = T / 2**i
        times, trajectory, r_delta, energy_delta = heun(f, x0, t0, t_end, h)

        all_r_deltas.append((times, r_delta))
        all_energy_deltas.append((times, energy_delta))
        step_sizes.append(h)

    plt.figure(figsize=(12, 8))

    for (times, errors), h in zip(all_r_deltas, step_sizes):
        plt.plot(times, errors, label=f'h = T / 2^{int(np.log2(T / h))}')

    plt.title("Error Evolution Over Time (Heun's method without Nacozy stabilization)")
    plt.xlabel("Time")
    plt.ylabel("Error |∆x|")
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()
    plt.grid(True)
    plt.savefig("Error_Evolution_Without_Nacozy.png")
    plt.show()

    # Plot energy delta over time for each step size
    plt.figure(figsize=(12, 8))
    for (times, energy_deltas), h in zip(all_energy_deltas, step_sizes):
        plt.plot(times, energy_deltas, label=f"h = T / 2^{int(np.log2(T / h))}")

    plt.title("Energy Deviation Over Time (Heun's Method)")
    plt.xlabel("Time")
    plt.ylabel("Energy Deviation |ΔI|")
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()
    plt.grid(True)
    plt.savefig("Energy_Deviation_Evolution_Without_Nacozy.png")
    plt.show()