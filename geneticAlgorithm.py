# Import modules and dependencies
import random
import string

# Options
populationSize = 1000
mutationRate   = 0.01
targetString   = 'To be or not to be.'

print('Press enter to continue with default settings, or type in a target word to make custom settings.')
targetString_ = str(input('> '))
if targetString_ != '':
    targetString = targetString_
    try:
        print('Enter a population size.')
        populationSize = int(input('> '))
        print('Enter a mutation rate(suggested 0.01 to 0.05)')
        mutationRate = float(input('> '))
    except Exception:
        print('Please make sure to use the correct types when inputting values.')

# Setup
chars = string.ascii_letters + string.punctuation + string.whitespace
targetLength = len(targetString)

# Initialise population as a list of random strings, called 'individuals'
def initialisePopulation():
    population = []
    for i in range(populationSize):
        population.append(''.join(random.choice(chars) for j in range(targetLength)))
    print('Population of length {}, with a target word of {} initialised.'.format(populationSize, targetString))
    return population

# Calculate fitness of the population, using the number of characters in common with the target to calculate fitness
def calculateFitness(population):
    populationFitness = []
    for individual in population:
        fitness = 0
        for char in range(targetLength):
            if targetString[char] == individual[char]:
                fitness += 1
        if fitness == targetLength:
            print('Individual with a value of "{}" is a match!'.format(individual))
            return False
        populationFitness.append(fitness)
    print('Fitness calculated for {} individuals. There have been no matches yet...'.format(populationSize))
    return populationFitness

# Generate a 'gene pool' based on the population and the fitness of all individuals in that population
def createGenePool(population, populationFitness):
    genePool = []
    for individual in range(populationSize):
        for i in range(populationFitness[individual]):
            genePool.append(population[individual])
    genePoolLength = len(genePool)
    print('Created a gene pool containing {} individuals.'.format(genePoolLength))
    return genePool

# Create a new population by randomly selecting pairs of individuals in the 'gene pool', and creating a daughter to add to the new population
def createNewPopulation(genePool):
    newPopulation = []
    for individual in range(populationSize):
        mother = random.choice(genePool)
        father = random.choice(genePool)
        daughter = ''
        for i in range(targetLength):
            if random.random() < mutationRate:
                daughter += random.choice(chars)
            else:
                daughter += random.choice([mother[i], father[i]])
        newPopulation.append(daughter)
    print('Created a new population of {} individuals.'.format(populationSize))
    return newPopulation

# Repeatedly calculate fitness, create gene pool, and generate a new population until a match has been found
def runGeneration(population):
    populationFitness = calculateFitness(population)
    if populationFitness:
        genePool = createGenePool(population, populationFitness)
        return createNewPopulation(genePool)
    return False

if __name__ == '__main__':
    population = initialisePopulation()
    generation = 0

    while population:
        print('\n\nRunning generation {}.'.format(generation))
        population = runGeneration(population)
        generation += 1
