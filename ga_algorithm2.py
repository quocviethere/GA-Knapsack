#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def generate_random_value():
    return random.randint(0, 1)

def create_individual(n_items):
    return [generate_random_value() for _ in range(n_items)]

def compute_fitness(chromosome, values, weights, max_weight):
    value = sum([chromosome[i] * values[i] for i in range(len(chromosome))])
    weight = sum([chromosome[i] * weights[i] for i in range(len(chromosome))])
    if weight > max_weight:
        return 0
    else:
        return value

def compute_weight(chromosome, weights):
    return sum([chromosome[i] * weights[i] for i in range(len(chromosome))])

def selection(population, fitness_scores):
    selected_chromosomes = []
    population_size = len(population)
    for i in range(population_size // 2):
        max_fitness_index = fitness_scores.index(max(fitness_scores))
        selected_chromosomes.append(population[max_fitness_index])
        fitness_scores[max_fitness_index] = 0
    return selected_chromosomes

def crossover(parent1, parent2):
    split_index = random.randint(1, len(parent1)-1)
    child1 = parent1[:split_index] + parent2[split_index:]
    child2 = parent2[:split_index] + parent1[split_index:]
    return child1, child2

def mutate(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.uniform(0, 1) < mutation_rate:
            chromosome[i] = 1 - chromosome[i]
    return chromosome

def genetic_algorithm(n_items, values, weights, max_weight, population_size=100, generations=100, mutation_rate=0.1):
    # create the initial population
    population = [create_individual(n_items) for i in range(population_size)]

    # run the genetic algorithm for the specified number of generations
    for generation in range(generations):
        # calculate the fitness of each chromosome in the population
        fitness_scores = [compute_fitness(chromosome, values, weights, max_weight) for chromosome in population]

        # select the top chromosomes for reproduction
        selected_chromosomes = selection(population, fitness_scores)

        # crossover the selected chromosomes to create new offspring
        offspring = []
        for i in range(population_size // 2):
            parent1 = selected_chromosomes[random.randint(0, len(selected_chromosomes)-1)]
            parent2 = selected_chromosomes[random.randint(0, len(selected_chromosomes)-1)]
            child1, child2 = crossover(parent1, parent2)
            offspring.extend([child1, child2])

        # mutate the offspring
        for i in range(len(offspring)):
            offspring[i] = mutate(offspring[i], mutation_rate)

        # replace the old population with the new offspring
        population = offspring

    # find the chromosome with the highest fitness score
    best_chromosome = population[0]
    best_fitness_score = compute_fitness(best_chromosome, values, weights, max_weight)
    for chromosome in population:
        fitness_score = compute_fitness(chromosome, values, weights, max_weight)
        if fitness_score > best_fitness_score:
            best_chromosome = chromosome
            best_fitness_score = fitness_score

    # return the solution
    selected_items = [i+1 for i in range(n_items) if best_chromosome[i] == 1]
    solution = {
        'items': selected_items,
        'value': best_fitness_score,
        'weight': compute_weight(best_chromosome, weights)
    }
    return solution

