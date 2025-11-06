import  json
from array import array


class Product:
    def __init__(self, pid, name, quantity, price):
        self.pid=pid
        self.name=name
        self.quantity=quantity
        self.price=price
    def total_value(self):
        return self.quantity * self.price


    def __str__(self):
        return f"ID: {self.pid}  {self.name} {self.quantity} total :{self.total_value()}"



class Inventory:
    def __init__(self):
        self.product = []
        self.load_data()

    def load_data(self):

        try:
            with open('inventory.json','r') as f:
                data= json.load(f)
                for d in data:
                    self.product.append(Product(d['pid'], d['name'], d['quantity'], d['price']))

        except FileNotFoundError:
            print("no saved data found")
        except json.JSONDecoder:
            print(" Corrupted file, starting new inventory")
    def save_data(self):
        with open('inventory.Json','w') as f:
            json.dump([vars(p) for p in self.product],f, indent=4)


    def add_product(self):
        try:
            pid=int(input("enter Product ID"))
            name=int(input("enter product name"))
            quantity=int(input("enter qunantity"))
            price = int(input("enter price"))

            for p in self.product:
                if p.pid==pid:
                    print("product id already exited")
                    return
            new_product=Product(pid,name,price,quantity)
            self.product.append(new_product)
            self.save_data()
            print("product save succesfully")
        except ValueError:
            print("invalid id")

    def show_all(self):
        if not self.product:
            print("inventoty empty")
        else:
            for p in self.product:
                print(p)
        print(f"\n💰 Total Stock Value: {sum(p.total_value() for p in self.product)}")


    def search_product(self):
        name=input("enter your product").lower()
        result=[p for p in self.product if name in p.name.lower () ]
        if result:
            print("search result :")
            for p in result:
                print(p)
        else:
            print("not found")


    def update_product(self):
        pid=int(input("enter product id"))
        for p in self.product:
            if p.pid==pid:
                print(F" editing {p.name}")
                p.quantity=int(input("new qunatity"))
                p.price=int(input("enter price"))
                self.save_data()
                print("update succesfully")
                return
        print("Product not found")

    def delete_product(self):
        pid=int(input("Enter product Id"))
        for p in self.product:
            if p.pid == pid:
                self.product.remove(p)
                self.save_data()
                print("Product delete successfully")
                return
        print("Product not found")

    def sort_by(self):
        sorted_product = sorted(self.product, key=lambda x: x.price)
        print('product sorted')
        for p in sorted_product:
            print(p)


    def show_statistic(self):
        if not self.product:
            print("no daata analyze")
            return
        price = array('f',[p.price for p in self.product])
        ava_price=sum(price)
        max_price=sum(price)
        min_price=sum(price)
        print(f"\n📈 Average Price: {ava_price:.2f}")
        print(f"💰 Highest Price: {max_price}")
        print(f"🪙 Lowest Price: {min_price}")

def main( ):
        inventory=Inventory()

        while True:
            print("_________________________")
            print("1.show product")
            print("2.add_product")
            print("3.search Product")
            print("4. update product")
            print("5.delete product")
            print("6.sorted by  product")
            print("7.show statistic product")
            print("8.exit")
            choice=input("enter your choice : ")

            if choice == '1':
                inventory.add_product()
            elif  choice =='2':
                inventory.show_all()
            elif choice =='3':
                inventory.sort_by()
            elif choice =='4':
                inventory.search_product()
            elif choice == '5':
                inventory.save_data()
            elif choice == '6':
                inventory.delete_product()
            elif choice == '7':
                 inventory.show_statistic()
            else:
                print("❌ Invalid choice. Try again!")



if __name__ == "__main__":
        main()