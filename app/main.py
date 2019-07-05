import os
import waitress as waitress
from flask import Flask, render_template, request

from app.products import ProductManager, CarRent, Tours, Tickets


def start():
    app = Flask(__name__)
    product_manager = ProductManager()

    product_manager.add(CarRent('Hyundai Solaris', 1200, 'http://www.avtomir.ru/upload/photo_bank/hyundai/solaris_hcr/active_%D1%81%D0%B5%D0%B4%D0%B0%D0%BD/MZH_1.png'))
    product_manager.add(CarRent('Nissan X-Trail', 1500, 'http://www.avtomir.ru/upload/photo_bank/nissan/x-trail/se+_%D0%BA%D1%80%D0%BE%D1%81%D1%81%D0%BE%D0%B2%D0%B5%D1%80/QAB_1.png'))
    product_manager.add(CarRent('Mercedes S600', 2500, 'https://www.toulineprestige.com/file/location-voiture-casablanca-mercedes-class-s.png'))
    product_manager.add(CarRent('Nissan GTR', 4500, 'https://img.sm360.ca/ir/w600h400c/images/newcar/ca/2018/nissan/gt-r/premium-/coupe/exteriorColors/11818_cc0640_032_KAB.png'))

    product_manager.add(Tours('Turkey, Akra Hotel', 20_990, 'https://gursesintour.com/wp-content/uploads/2013/12/u_wdg2HsNCk.jpg', '3*', 7))
    product_manager.add(Tours('Greece, Zevs Hotel', 41_990, 'http://flagger.ru/wp-content/uploads/2017/12/greece.png', '4*', 8))
    product_manager.add(Tours('Egypt, Kleopatra Hotel', 45_290, 'http://ogeraldike.ru/news/item/f00/s01/n0000198/pic/000004.jpg', '5*', 10))
    product_manager.add(Tours('China, Lundzin Hotel', 60_590, 'http://ogeraldike.ru/news/item/f00/s00/n0000058/pic/000000.jpg', '5*', 9))

    product_manager.add(Tickets('Moscow-Kazan', 3590, 'https://www.s7-airlines.com/images/icons/icon-600x400.jpg', '6 August'))
    product_manager.add(Tickets('Moscow-Kyiv', 4790, 'https://i2.wp.com/thesuitelife.blog/wp-content/uploads/2018/05/600x600wa.jpg?resize=600%2C400&ssl=1', '12 August'))
    product_manager.add(Tickets('Ekaterinburg-Blagoveshensk', 5590, 'https://d2osdnqd2igqfx.cloudfront.net/AcuCustom/Sitename/DAM/124/Turkish_Airline_logo_600x400.png', '3 September'))
    product_manager.add(Tickets('Kazan-London', 17590, 'http://www.etbtravelnews.global/wp-content/uploads/2016/01/Swiss-International-Air-Lines-logo.png', '23 August'))

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
