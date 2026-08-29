class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"[{self.product_id}] {self.name} - ${self.price} x{self.quantity}"


class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Added: {product}")

    def remove_product(self, product_id):
        self.products = [p for p in self.products if p.product_id != product_id]
        print(f"Removed product with ID: {product_id}")

    def update_product(self, product_id, name=None, price=None, quantity=None):
        for p in self.products:
            if p.product_id == product_id:
                if name: p.name = name
                if price is not None: p.price = price
                if quantity is not None: p.quantity = quantity
                print(f"Updated: {p}")
                return
        print("Product not found.")

    def list_products(self):
        if not self.products:
            print("No products available.")
        for p in self.products:
            print(p)


if __name__ == "__main__":
    manager = ProductManager()
    manager.add_product(Product(1, "Laptop", 55000, 5))
    manager.add_product(Product(2, "Mouse", 500, 20))

    manager.list_products()

    manager.update_product(1, price=52000)
    manager.remove_product(2)

    manager.list_products()