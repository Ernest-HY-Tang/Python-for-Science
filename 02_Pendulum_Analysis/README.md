# Project: Pendulum Motion & Model Analysis

## Overview:
As I was deriving the simple harmonic motion equation for a simple pendulum:

$$T = 2\pi\sqrt{\frac{L}{g}}$$

I noticed that we benefit from the small-angle approximation, which makes me wonder how this equation deviates from the actual time period in relation to the length of the string and the angle from which it is being pulled.

This leads me to use the correction factor:

$$T_{Actual} \approx T_{Ideal}\left(1+\frac{\theta^2}{16}\right)$$

Which comes from the binomial expansion of an elliptic integral.*

## Key Features of the Project: 
* **Numerical Modelling:** The user can input an angle to get the ideal and actual periods across a list of preselected lengths of the pendulum.
* **Error Analysis:** With respect to the actual period, there is a percentage error associated with the angle chosen. 
* **Data Formatting:** Uses Python `zip()` and `f-strings` to generate a clean result table consisting of the lengths, periods and errors.

## What I Learnt:
* **Functional Programming:** Neat ways to condense my code for efficient data processing (e.g., using the `[x for x in list]` style and `zip()`).
* **Avoid Early Rounding:** At the beginning stage of the code, the percentage errors varied across different lengths (which raised suspicion as the error analysis is independent of length), as I had mistakenly used the rounded lists for the error calculations.
* **Pythonic Logic:** In functions, empty lists should be defined within such that they are restored upon calling.

> *Within the binomial expansion, I have only used the first two terms (as the following terms are negligible). What drew my attention was how we used the small-angle approximation once again within this approximation, which defeats the whole purpose of the error analysis. I then realised that this simplification is used to provide a more intuitive, linearised interpretation of how period changes in moderate amplitudes. However, at larger angles, the divergence between $\theta$ and $\sin\theta$ becomes the dominant source of inaccuracy.