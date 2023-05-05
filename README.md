# Knapsack Problem using Genetic Algorithm
Đồ án Trí Tuệ Nhân Tạo (23D1INF50904203) UEH - Knapsack Problem using Genetic Algorithm

https://user-images.githubusercontent.com/96617645/236198151-29795b1f-3666-4dc3-856e-d5a9beb4168a.mov

This project is an implementation of the Knapsack Problem using Genetic Algorithm in Python. The Knapsack Problem is a combinatorial optimization problem that involves selecting a set of items to maximize the total value while keeping the total weight below a certain limit. The Genetic Algorithm is a heuristic optimization method that is inspired by the process of natural selection.

## Getting Started
To get started with this project, you will need to have Python 3 installed on your machine. You can download Python 3 from the official website: https://www.python.org/downloads/

Once you have Python 3 installed, you can clone the repository and install the required packages by running the following commands:

`git clone https://github.com/quocviethere/Knapsack-Problem-using-Genetic-Algorithm/`

## Code Description
The `ga_algorithm2.py` file contains the following functions:

- `generate_random_value()`: generates a random binary value (0 or 1).
- `create_individual(n_items)`: creates an individual chromosome of length n_items by calling generate_random_value() for each bit.
- `compute_fitness(chromosome, values, weights, max_weight)`: computes the fitness of the chromosome by calculating the total value and weight of the selected -items. If the total weight is above max_weight, the fitness score is 0.
- `compute_weight(chromosome, weights)`: computes the total weight of the chromosome.
- `selection(population, fitness_scores)`: selects the top chromosomes based on their fitness scores for reproduction.
- `crossover(parent1, parent2)`: performs a single-point crossover between parent1 and parent2 to create two new offspring.
- `mutate(chromosome, mutation_rate)`: randomly mutates a chromosome by flipping the value of a bit with probability mutation_rate.
- `genetic_algorithm(n_items, values, weights, max_weight, population_size=100, generations=100, mutation_rate=0.1)`: runs the genetic algorithm to find the best solution.






