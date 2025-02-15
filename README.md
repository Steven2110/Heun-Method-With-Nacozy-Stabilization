# Heun-Method-With-Nacozy-Stabilization
Laboratory Assignment for Computational Methods of Celestial Mechanics

# Task
Find numerically the solution of the system of differential equations of the plane two-body problem:

$$
x_1' = x_3, \quad x_2' = x_4,
$$

$$
x_3' = -\frac{x_1}{r^3}, \quad x_4' = -\frac{x_2}{r^3},
$$

$$
r = \sqrt{x_1^2 + x_2^2}, \quad v = \sqrt{x_3^2 + x_4^2}
$$

$$
\vec{x} = (x_1, x_2, x_3, x_4), \quad \vec{x_0} = \left( x_1(t_0), x_2(t_0), x_3(t_0), x_4(t_0) \right)
$$

Initial conditions:

$$
x_1(t_0) = 1, \quad x_2(t_0) = 0,
$$

$$
x_3(t_0) = 0, \quad x_4(t_0) = 1.
$$

Integration interval: 
$\left[ t_0; t_0+1000T \right]$, where $T = 2\pi$

Timestep:
$h=\frac{T}{2^i}$ , where $i = (4, 5,..., 12)$

Energy integral:

$$
I(\vec{x}) = \frac{v^2}{2} - \frac{1}{r}
$$

Using [Heun's method](https://en.wikipedia.org/wiki/Heun%27s_method) with Nacozy stabilization.

## Heun's method
**Prediction step:**

$$
k_1=f(t_0,x_0)
$$

**Second estimate:**

$$
k_2=f(t_0+h,x_0+h \cdot k_1)
$$

**Correction step:**

$$
x_1 = x_0 + \frac{h}{2} \left( k_1+k_2 \right)
$$

## Nacozy stabilization

**Position stabilization:**

$$
\bar{\mathbf{x}} = \mathbf{x} \left( 1 - \frac{\mathcal{H}}{D} \frac{\mu}{|\mathbf{x}|^3} \right)
$$

**Velocity stabilization:**

$$
\dot{\bar{\mathbf{x}}} = \dot{\mathbf{x}} \left( 1 - \frac{\mathcal{H}}{D} \right)
$$

Where,

$$
\mathcal{H} = H - I_0, \\
H = \frac{v^2}{2} - \frac{\mu}{r}, \\
D = v^2 + \frac{\mu^2}{|\mathbf{x}|^4}, \\
$$

This step is done iteratively with stopping criteria:

$$
|\mathcal{H}| < \text{tolerance}
$$

## Error and Energy Deviation

**Error:**

$$
\lvert \Delta \vec{r} \rvert = \sqrt{\left( \vec{r}_1 - \vec{r}_1^* \right)^2 + \left( \vec{r}_2 - \vec{r}_2^* \right)^2}
$$

where

$$
\vec{r}_1^* = \cos(t), \quad \vec{r}_2^* = \sin(t)
$$

**Energy Deviation:**

$$
\Delta I = \lvert I(\vec{x}) - I(\vec{x}_0) \rvert
$$


# Result:
## Without Nacozy Stabilization
![Error Evolution Without Nacozy Stabilization](/Error_Evolution_Without_Nacozy.png)

*Figure 1: Error Evolution Without Nacozy Stabilization*

![Energy Deviation Evolution Without Nacozy Stabilization](/Energy_Deviation_Evolution_Without_Nacozy.png)

*Figure 2: Energy Deviation Evolution Without Nacozy Stabilization*

## With Nacozy stabilization every step
![Error Evolution With Nacozy Stabilization Every Step](/Error_Evolution_Nacozy_Every_Step.png)

*Figure 3: Error Evolution With Nacozy Stabilization Every Step*

![Energy Deviation Evolution With Nacozy Stabilization Every Step](/Energy_Deviation_Evolution_Nacozy_Every_Step.png)

*Figure 4: Energy Deviation Evolution With Nacozy Stabilization Every Step*

## With Nacozy stabilization on several step
![Error Evolution With Nacozy Stabilization on Several Step](/Error_Evolution.png)

*Figure 5: Error Evolution With Nacozy Stabilization  on Several Step*

![Energy Deviation Evolution With Nacozy Stabilization on Several Step](/Energy_Deviation_Evolution.png)

*Figure 6: Energy Deviation Evolution With Nacozy Stabilization on Several Step*

# How to run this project
1. Clone this repository.
2. Open terminal and open the folder. 
    ```sh
    cd path/Heun-Method-With-Nacozy-Stabilization
    ```
3. Run this command to install all necessary libraries.
    ```sh
    pip install -r requirements.txt
    ```
4. Then run this command.
    ```sh
    python main.py
    ```
5. You can find all the results of the image in the same folder.

    a. **Error evolution**:

    - Without Nacozy stabilization: `Error_Evolution_Without_Nacozy.png`.
    
    - With Nacozy stabilization on every step: `Error_Evolution_Nacozy_Every_Step.png`.

    - With Nacozy stabilization on several steps: `Error_Evolution.png`.

    b. **Energy deviation**:

    - Without Nacozy stabilization: `Energy_Deviation_Evolution_Without_Nacozy.png`.
    
    - With Nacozy stabilization on every step: `Energy_Deviation_Evolution_Nacozy_Every_Step.png`.

    - With Nacozy stabilization on several steps: `Energy_Deviation_Evolution.png`.
