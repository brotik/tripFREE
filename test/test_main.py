from app.products import CarRent, ProductManager, Tours, Tickets
product_manager = ProductManager

def test_carrent():
    data = CarRent(
        'Hyundai Solaris',
            1200,
            'http://www.avtomir.ru/upload/photo_bank/hyundai/solaris_hcr/active_%D1%81%D0%B5%D0%B4%D0%B0%D0%BD/MZH_1.png',
            'Комфортный и недорогой седан'
    )
    result = ('Hyundai Solaris',
              1200,
              'http://www.avtomir.ru/upload/photo_bank/hyundai/solaris_hcr/active_%D1%81%D0%B5%D0%B4%D0%B0%D0%BD/MZH_1.png',
              'Комфортный и недорогой седан'
              )

    assert data.name in result
    assert data.price in result
    assert data.image in result
    assert data.description in result


def test_tours():
    data = Tours('Turkey, Akra Hotel', 20_990,
                 'https://gursesintour.com/wp-content/uploads/2013/12/u_wdg2HsNCk.jpg', '3*', 7)
    result = ('Turkey, Akra Hotel', 20_990,
              'https://gursesintour.com/wp-content/uploads/2013/12/u_wdg2HsNCk.jpg', '3*', 7)

    assert data.image in result
    assert data.name in result
    assert data.price in result
    assert data.comfort in result
    assert data.days_qty in result


def test_tickets():
    data = Tickets('Moscow-Kazan', 3590, 'https://www.s7-airlines.com/images/icons/icon-600x400.jpg', '6 August')
    result = ('Moscow-Kazan', 3590, 'https://www.s7-airlines.com/images/icons/icon-600x400.jpg', '6 August')

    assert data.image in result
    assert data.price in result
    assert data.name in result
    assert data.date in result


def test_add():
    product_manager = ProductManager()
    excepted = product_manager.add(CarRent('Hyundai Solaris', 1200,
                                'http://www.avtomir.ru/upload/photo_bank/hyundai/solaris_hcr/active_%D1%81%D0%B5%D0%B4%D0%B0%D0%BD/MZH_1.png',
                                'Комфортный и недорогой седан'))
    result = product_manager.add(CarRent('Hyundai Solaris',
                                         1200,
                                         'http://www.avtomir.ru/upload/photo_bank/hyundai/solaris_hcr/active_%D1%81%D0%B5%D0%B4%D0%B0%D0%BD/MZH_1.png',
                                         'Комфортный и недорогой седан'))

    assert excepted == result


def test_search_cars():
    pass