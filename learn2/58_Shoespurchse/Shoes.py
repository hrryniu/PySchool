from traceback import print_tb


class Shoes:
    def __init__(self,name,price):
        self.name = name
        self.price = float(price)

    def budget_check(self,budget):
        if not isinstance(budget, (int,float)):
            print("Invalid entry")
            exit()

    def change(self, budget):
        return (budget - self.price)

    def buy(self,budget):
        self.budget_check(budget)

        if budget >= self.price:
            print(f"You can cop some {self.name}")

            if budget ++ self.price:
                print("You have exactly enough money for these shoes")
            else:
                print(f"You can buy these and have $ {self.change(budget)} left over")

            exit("Thank for using my app!")