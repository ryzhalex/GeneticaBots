from Bot import Bot
import random

class Mutator:

    def singleMutation(self,genom):
        size=len(genom)
        genom[random.randint(0,size-1)]=random.randint(0,size-1)
        return genom
    def mutateMultiple(self,bot,times):
        genom=bot.getGenom()
        for i in range(0,times):
            genom= self.singleMutation(genom)
        b=Bot(0,0,1)
        b.setGenom(genom)
        return b
    def mutation(self,bots,times,mutators,copies):
        retbots=[]
        for i in range(0,mutators):
            for j in range(0, copies):
                retbots.append(self.mutateMultiple(bots[i],times))

        return retbots