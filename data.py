from dataclasses import dataclass
from typing import Optional


class FaqAnswers:
    answer_0 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    answer_1 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    answer_2 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    answer_3 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    answer_4 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    answer_5 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    answer_6 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    answer_7 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'


@dataclass
class User:
    name: str
    surname: str
    address: str
    phone: str
    comment: Optional[str] = None


user_1 = User(
    name='Те',
    surname='Ст',
    address='Москв',
    phone='81234567890',
    comment='тестовый заказ')

user_2 = User(
    name='БорисБорисБорис',
    surname='БорисоввБорисов',
    address='Москва, проспект Мира,  д. 26, вход со стороны ул',
    phone='+123456789012')
