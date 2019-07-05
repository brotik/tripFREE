class CarRent:
    def __init__(self, name, price, image):
        self.name = name
        self.price = price
        self.image = image


class Tours:
    def __init__(self, name, price, comfort, days_qty):
        self.name = name
        self.price = price
        self.days_qty = days_qty
        self.comfort = comfort


class Tickets:
    def __init__(self, name, price, date):
        self.name = name
        self.price = price
        self.date = date


class ProductManager:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def cars(self):
        return list(filter(lambda cars: isinstance(cars, CarRent), self.items))

    def tours(self):
        return list(filter(lambda tours: isinstance(tours, Tours), self.items))

    def tickets(self):
        return list(filter(lambda tickets: isinstance(tickets, Tickets), self.items))

    def search_products(self, search):
        search_lowercase = search.strip().lower()
        result = []
        if search_lowercase:
            result.append(self)
        return result



        # return list(filter(lambda o: name.lower() in o.name.lower(), self.items))
#
# def search_products(container, search):
#     search_lowercase = search.strip().lower()
#     result = []
#     for item in container:
#         if search_lowercase in item.name.lower():
#             result.append(item)

