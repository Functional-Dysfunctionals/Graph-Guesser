import numpy as np
import matplotlib.pyplot as plt
import os
import random
import inspect

# Define the range of x values
x_values = np.linspace(-10, 10, 1024)

# Define the number of graphs for each equation type
num_graphs_per_type = 20

# Create a directory to save the images
if not os.path.exists('equation_images'):
    os.makedirs('equation_images')

# Define the equations to be plotted
equations = [
    (lambda x, a, b: a * x + b, 'Linear: y = {:.0f}x + {:.0f}'),  # Linear equation
    (lambda x, a, b, c: a * (x + b) ** 2 + c, 'Quadratic: y = {:.0f}(x + {:.0f})^2 + {:.0f}'),
    # Quadratic equation (shift along x and y)
    (lambda x, a, b, c: a * np.sin(b * (x + c)), 'Sine: y = {:.0f}sin({:.0f}(x + {:.0f}))'),
    # Sine wave (shift along x, stretch/compress along x)
    (lambda x, a, b: a * np.exp(b * x), 'Exponential: y = {:.0f}exp({:.0f}x)'),
    # Exponential function (stretch/compress along x)
    (lambda x, a, b: a * np.sqrt(np.abs(x) + np.abs(b)), 'Square Root: y = {:.0f}sqrt(|x| + |{:.0f}|)'),
    # Square root function (stretch/compress along x)
    (lambda x, *coefficients: np.polyval(coefficients[::-1], x), 'Polynomial: y = {}')
    # Polynomial equation
]

# Loop over equations
for idx, (equation, equation_label_template) in enumerate(equations):
    # Generate one graph for each equation type
    for i in range(num_graphs_per_type):
        # Generate random parameters or coefficients with variability
        params = []
        for param in inspect.signature(equation).parameters.values():
            if param.name == 'x':
                continue
            if param.annotation == int:
                if idx == len(equations) - 1:  # For polynomial equation
                    params.append(random.randint(-10, -1))  # Avoiding zero
                else:
                    params.append(random.randint(-5, -1))  # Avoiding zero
            else:
                if idx == len(equations) - 1:  # For polynomial equation
                    params.append(random.uniform(-10, -1))  # Avoiding zero
                else:
                    params.append(random.uniform(-5, -1))  # Avoiding zero

        # Ensure the polynomial starts from a higher degree to avoid x^0 term
        if idx == len(equations) - 1:
            degree = random.randint(2, 5)  # Random degree between 2 and 5
            params = [random.randint(-10, 10) for _ in range(degree - 1)] + [random.randint(-10, 10)]  # Random coefficients and a constant transformation

        print(f"Equation {idx + 1}_{i + 1} Parameters: {params}")

        # Generate (x, y) pairs
        try:
            y_values = equation(x_values, *params)
        except ValueError:
            print(f"Invalid parameter combination for Equation {idx + 1}_{i + 1}. Skipping.")
            continue

        print(f"Equation {idx + 1}_{i + 1} y-values: {y_values}")

        # Plot the function within the limits of -10 to 10 for both axes
        plt.figure(figsize=(6, 6))
        plt.plot(x_values, y_values)
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        plt.xticks(np.arange(-10, 11, 2))
        plt.yticks(np.arange(-10, 11, 2))
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.xlabel('x')
        plt.ylabel('y')

        # Format the equation label with actual parameter values
        if idx == len(equations) - 1:
            equation_label = equation_label_template.format(' + '.join([f'{coeff}x^{len(params) - i - 1}' for i, coeff in enumerate(params[:-1])]) + f' + {params[-1]}')
        else:
            equation_label = equation_label_template.format(*map(round, params))

        # Annotate with the equation and parameters to the right of the graph
        plt.text(9, 9, equation_label, fontsize=8, verticalalignment='top', horizontalalignment='right')

        # Save the plot as an image
        image_path = f'equation_images/equation_{idx + 1}_{i + 1}.png'
        plt.savefig(image_path, dpi=150)
        plt.close()
