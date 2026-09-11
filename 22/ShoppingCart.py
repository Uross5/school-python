class ShoppingCart:


    def __init__(self):
        self.items=[]

    def add_item(self,item):
        self.items.append(item)



    def show_products(self):
        for item in self.items:
            print(item.name)
