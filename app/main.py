import os
import waitress as waitress
from flask import Flask, render_template, request

from app.products import ProductManager, CarRent, Tours, Tickets


def start():
    app = Flask(__name__)
    product_manager = ProductManager()

    product_manager.add(CarRent('Hyundai Solaris', 1200, 'https://www.hyundai-avtomir.ru/upload/iblock/28b/28bcc2eded8a2046dde5b20f9f5465ea.jpg'))
    product_manager.add(CarRent('Nissan X-Trail', 1500, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-CTWVq8HGUSap9RfZmwzz4PNO71SBFdqjNLLp_yrcqr-rcw-nXg'))
    product_manager.add(CarRent('Mercedes S600', 2500, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-CTWVq8HGUSap9RfZmwzz4PNO71SBFdqjNLLp_yrcqr-rcw-nXg'))
    product_manager.add(CarRent('Nissan GTR', 4500, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRixgkHVyiFO8Ok4WW2PJ4M52ODO1KETC4Jfm2OufDDqbIhtbxB9Q'))

    product_manager.add(Tours('Turkey, Akra Hotel', 20_990, '3*', 7))
    product_manager.add(Tours('Greece, Zevs Hotel', 41_990, '4*', 8))
    product_manager.add(Tours('Egypt, Kleopatra Hotel', 45_290, '5*', 10))
    product_manager.add(Tours('China, Lundzin Hotel', 60_590, '5*', 9))

    product_manager.add(Tickets('Moscow-Kazan', 3590, '6 August'))
    product_manager.add(Tickets('Moscow-Kyiv', 4790, '12 August'))
    product_manager.add(Tickets('Ekaterinburg-Blagoveshensk', 5590, '3 September'))
    product_manager.add(Tickets('Kazan-London', 17590, '23 August'))

    @app.route('/')
    def index():

        return render_template('index.html')

    @app.route('/carrent')
    def carrent():
        cars = product_manager.cars()
        result = []
        for item in cars:
            result.append(item)

        search = request.args.get('search')
        if search:
            items = product_manager.search_products(search)

            return render_template('carrent.html', search=items)
        return render_template('carrent.html', result=result)

    @app.route('/tours')
    def tours():
        tour = product_manager.tours()
        result = []
        for item in tour:
            result.append(item)
        return render_template('tours.html', result=result)

    @app.route('/tickets')
    def tickets():
        ticket = product_manager.tickets()
        result = []
        for item in ticket:
            result.append(item)
        return render_template('tickets.html', result=result)

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9877, debug=True)


if __name__ == '__main__':
    start()
