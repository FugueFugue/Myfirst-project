import random
class eightQ:
    def __init__(self):
        self.sample_chromosome = [i + 1 for i in range(8)]
        self.t = []
        self.pop = []
        for i in range(20):
            random.shuffle(self.sample_chromosome)
            t = self.sample_chromosome.copy()
            self.pop.append(t)

    def fitness(self, x):
        # number of queens that hit eachother
        cost = 0
        for i in range(len(x) - 1):
            for j in range(i + 1, len(x)):
                if (x[i] == x[j]):
                    cost += 1
                elif (abs(x[i] - x[j]) == abs(i - j)):
                    cost += 1

        return cost

    def cross_over(self, x1, x2):
        t = random.randint(0, 8)
        child = x1[:t]
        for i in x2:
            if i not in child:
                child.append(i)
        return child

    def mutation(self, x):
        t1 = random.randint(0, 7)
        t2 = random.randint(0, 7)
        x[t1], x[t2] = x[t2], x[t1]
        return x

    def cross_over_and_mutate(self, x):
        pop = []
        k = 0
        for i in range(len(x)):
            for j in range(len(x)):
                k += 1
                temp = self.cross_over(x[i], x[j])
                if k % 1 == 0:
                    pop.append(self.mutation(temp))
                else:
                    pop.append(temp)
        return pop[:15]


def main():
    t = eightQ()
    pop = t.pop
    for generation in range(1000):
        pop = [[t.fitness(i), i] for i in pop]
        pop = sorted(pop)
        elitisms = pop[:5]
        pop2 = [elitisms[j][1] for j in range(len(elitisms))]
        after_mut_cross = [i[1] for i in pop[5:11]]
        after_mut_cross = t.cross_over_and_mutate(after_mut_cross)
        pop2 += after_mut_cross
        pop = pop2.copy()
        print(f"the best chromosome in the {generation} generation:", pop[0], "And the Cost Is:", t.fitness(pop[0]))
        if t.fitness(pop[0]) == 0:
            break
    print("The Best Chromosome at the End:", pop[0], "And the Cost is:", t.fitness(pop[0]))
    
    

if __name__ == "__main__":
    main()