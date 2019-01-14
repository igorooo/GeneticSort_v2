from ArrayOps import *
from random import *

class GenObject(object):

    # (real number, weight, index)

    def __init__(self,ar_ARRAY):
        self.ar_TABLE = []
        self.i_ARR_LEN = len(ar_ARRAY)
        for i in range(0, self.i_ARR_LEN):
            self.ar_TABLE.append((ar_ARRAY[i],0,i))
        self.i_FITNESS = 0
        self.ar_RES_ARR = []


    def __lt__(self, other):
        return self.i_FITNESS < other.i_FITNESS


    def create_randomly(self):
        for i in range(0,self.i_ARR_LEN):
            self.ar_TABLE[i] = (self.ar_TABLE[i][0], randint( 0 , 10 * self.i_ARR_LEN-1 ), i)
        self.implement_moves()
        self.i_FITNESS = i_check_array_fitness(self.ar_RES_ARR)

    def crossover(self,MOTHER,FATHER):

        for i in range(0,self.i_ARR_LEN):
            self.ar_TABLE[i] =(self.ar_TABLE[i][0] ,round((3*MOTHER.ar_TABLE[i][1] + FATHER.ar_TABLE[i][1] ) / 4) , i)

        self.mutation()
        self.implement_moves()
        self.i_FITNESS = i_check_array_fitness(self.ar_RES_ARR)

    def mutation(self):
        for i in range(0,self.i_ARR_LEN):
            if (randint(0, 100) < 5):
                self.ar_TABLE[i] = (self.ar_TABLE[i][0], randint(0, 10 * self.i_ARR_LEN - 1), i)

    def implement_moves(self):
        self.ar_RES_ARR = self.ar_TABLE[:]
        self.ar_RES_ARR.sort(key= lambda x:x[1])







class GenSort(object):

    def __init__(self,ar_ARRAY,i_POP_SIZE):
        self.ar_ARRAY = ar_ARRAY[:]
        self.i_POP_SIZE = i_POP_SIZE
        self.ar_FST_GEN = []
        self.ar_SND_GEN = []
        self.f_LOGS = open("logs.txt","w")
        self.f_LOGS.close()
        self.i_NO_GEN = 0

        if(self.i_POP_SIZE % 2 == 1):
            self.i_POP_SIZE += 1


    def create_fst_gen(self):
        for i in range(0,self.i_POP_SIZE):
            TEMP = GenObject(self.ar_ARRAY)
            TEMP.create_randomly()
            self.ar_FST_GEN.append(TEMP)
        self.save_logs_from_fstgen()

    def get_parent(self):
        RANDOM_1 = self.ar_FST_GEN[randint(0, self.i_POP_SIZE-1)]
        RANDOM_2 = self.ar_FST_GEN[randint(0, self.i_POP_SIZE-1)]

        if( RANDOM_1 < RANDOM_2):
            return RANDOM_2
        else:
            return RANDOM_1

    def next_gen(self):
        self.ar_SND_GEN = []
        for i in range(0, int(self.i_POP_SIZE/2)):
            CHILD_A = GenObject(self.ar_ARRAY)
            CHILD_B = GenObject(self.ar_ARRAY)

            PARENT_A = self.get_parent()
            PARENT_B = self.get_parent()

            CHILD_A.crossover(PARENT_A,PARENT_B)
            CHILD_B.crossover(PARENT_B,PARENT_A)

            self.ar_SND_GEN.append( CHILD_A )
            self.ar_SND_GEN.append( CHILD_B )

        self.ar_FST_GEN = []
        self.ar_FST_GEN = self.ar_SND_GEN[:]
        self.save_logs_from_fstgen()


    def save_logs_from_fstgen(self):
        # saving generation in logs.txt file
        self.f_LOGS = open("logs.txt","a")
        for ELEM in self.ar_FST_GEN:
            self.f_LOGS.write("{")
            for i in range(0,len(ELEM.ar_RES_ARR)):
                self.f_LOGS.write(str(ELEM.ar_RES_ARR[i][0]))
                self.f_LOGS.write(" ")
            self.f_LOGS.write("}")
            self.f_LOGS.write("(")
            for i in range(0,len(ELEM.ar_RES_ARR)):
                self.f_LOGS.write(str(ELEM.ar_RES_ARR[i][1]))
                self.f_LOGS.write(" ")
            self.f_LOGS.write(")")
            self.f_LOGS.write("[")
            self.f_LOGS.write(str(ELEM.i_FITNESS))
            self.f_LOGS.write("]")
            self.f_LOGS.write(" ")
        self.f_LOGS.write("\n")
        self.f_LOGS.close()





