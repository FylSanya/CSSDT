from abc import ABC, abstractmethod
import datetime
import time
import json

class AbstractArray(ABC):
    
    @abstractmethod
    def __del__(self):
        print('Deleted class example.')

    @abstractmethod 
    def print(self):
        pass

class Products(AbstractArray):
    
    def __init__(self):
        self.list_of_products = []
        self.num_of_nice_products = 0

    def __del__(self):
        return super().__del__()

    def fillProduct(self, n):
        for i in range(n):
            self.list_of_products.append({
                'name': checkForString(input('Enter product name: ')),
                'count': checkForInt(input('Enter count of product: ')),
                'price': checkForInt(input('Enter price of product: ')),
                'date': datetime.date(2021, checkForInt(input('Enter the month of receipt of the product: ')), \
                    checkForInt(input('Enter the day of receipt of the product: '))).timetuple(),
                'today': datetime.date.today().timetuple()
            })

    def edit_list(self):
        products.print()
        temp = input("What do you want to do? (delete/add)")
        if temp == 'delete':
            n = int(input("Which item you want to delete? "))
            del self.list_of_products[n-1]
            products.print()
        elif temp == 'add':
            n = int(input("How much item you want to add? "))
            products.fillProduct(n)
            products.run()
            products.print()

        if int(input("Want to edit your list? 0 - no, 1 - yes ")) == 1:
            return products.edit_list()


    def run(self):
        i = 0
        border = len(self.list_of_products)
        while i < border:
            if self.list_of_products[i]["date"][1] < self.list_of_products[i]["today"][1] and \
                self.list_of_products[i]["date"][2] < self.list_of_products[i]["today"][2] and \
                int(self.list_of_products[i]["price"]) > 100:
                i += 1
            else:
                del self.list_of_products[i]
                border -= 1
            
        self.list_of_products = sorted(self.list_of_products, key=lambda item: item['name'])

    def recordToFile(self):
        str_to_record = ''
        for i in range(len(self.list_of_products)):
            str_to_record += (f'Name: {self.list_of_products[i]["name"]} ' 
                + f'Count of product: {self.list_of_products[i]["count"]} '
                + f'Price of product: {self.list_of_products[i]["price"]} '
                + 'Date: ' + time.strftime("%d %b", self.list_of_products[i]["date"]) + '; ')
        json.dump(str_to_record, open(f'D:\python\CSSDT\cssdt7.txt', 'w'))

    def print(self):
        super().print()
        for i in range(len(self.list_of_products)):
                print('\n' + f'Name: {self.list_of_products[i]["name"]}\n' 
                + f'Count of product: {self.list_of_products[i]["count"]}\n'
                + f'Price of product: {self.list_of_products[i]["price"]}' + '\n'
                + 'Date: ' + time.strftime("%d %b", self.list_of_products[i]["date"]))

    
def checkForInt(data):
    if data.isdigit():
        return int(data)
    else:
        data = input("Enter number!\n")
        return checkForInt(data)

def checkForString(data):
    if not data:
        data = input('Enter current name!\n')
        return checkForString(data)
    else:
        return data

products = Products()
products.fillProduct(checkForInt(input('Number of products: ')))
products.run()
products.print()
if checkForInt(input("Want to edit your list? 0 - no, 1 - yes ")) == 1:
    products.edit_list()
products.recordToFile()