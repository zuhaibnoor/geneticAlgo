import random

# Default genes set
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

class Individual:
    def __init__(self, chromosome, target):
        self.chromosome = chromosome
        self.target = target
        self.fitness = self.cal_fitness()

    @classmethod
    def mutated_genes(cls, genes):
        return random.choice(genes)

    @classmethod
    def create_gnome(cls, target, genes):
        return [cls.mutated_genes(genes) for _ in range(len(target))]

    def mate(self, par2, genes):
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):
            prob = random.random()
            if prob < 0.45:
                child_chromosome.append(gp1)
            elif prob < 0.90:
                child_chromosome.append(gp2)
            else:
                child_chromosome.append(self.mutated_genes(genes))
        return Individual(child_chromosome, self.target)

    def cal_fitness(self):
        fitness = sum(gs != gt for gs, gt in zip(self.chromosome, self.target))
        return fitness

# Driver code
def main():
    print("Welcome to the Genetic Algorithm!")
    target = input("Enter the target string: ").strip()
    
    while True:
        try:
            population_size = int(input("Enter the population size (e.g., 100): ").strip())
            if population_size <= 0:
                raise ValueError("Population size must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")
    
    generation = 1
    found = False
    population = []

    # Create initial population
    for _ in range(population_size):
        gnome = Individual.create_gnome(target, GENES)
        population.append(Individual(gnome, target))
    
 

    while not found:
        population = sorted(population, key=lambda x: x.fitness)

        if population[0].fitness <= 0:
            found = True
            break

        new_generation = []

        # Elitism: 10% of the fittest individuals
        elite_size = int(0.1 * population_size)
        new_generation.extend(population[:elite_size])

        # Generate new individuals
        for _ in range(population_size - elite_size):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = parent1.mate(parent2, GENES)
            new_generation.append(child)

        population = new_generation

        print(f"Generation: {generation}\tString: {''.join(population[0].chromosome)}\tFitness: {population[0].fitness}")
        generation += 1

    print(f"\nTarget achieved in Generation {generation}: {''.join(population[0].chromosome)}     Fitness: {population[0].fitness}")

if __name__ == "__main__":
    main()
