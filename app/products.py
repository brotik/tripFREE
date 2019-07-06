class CarRent:
    def __init__(self, name, price, image, description):
        self.name = name
        self.price = price
        self.image = image
        self.description = description


class Tours:
    def __init__(self, name, price, image, comfort, days_qty):
        self.name = name
        self.price = price
        self.days_qty = days_qty
        self.comfort = comfort
        self.image = image


class Tickets:
    def __init__(self, name, price, image, date):
        self.name = name
        self.price = price
        self.date = date
        self.image = image


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

    def search_products_car(self, search):
        search_lowercase = search.strip().lower()
        result = []
        cars = self.cars()
        for item in cars:
            if search_lowercase in item.name.lower():
                result.append(item)
        return result

    def search_products_tour(self, search):
        search_lowercase = search.strip().lower()
        result = []
        tours = self.tours()
        for item in tours:
            if search_lowercase in item.name.lower():
                result.append(item)
        return result

    def search_products_ticket(self, search):
        search_lowercase = search.strip().lower()
        result = []
        tickets = self.tickets()
        for item in tickets:
            if search_lowercase in item.name.lower():
                result.append(item)
        return result
