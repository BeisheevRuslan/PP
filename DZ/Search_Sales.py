import sqlalchemy
from sqlalchemy.orm import sessionmaker

# Импортируем наши модели
from Models import Publisher, Book, Stock, Sale, Shop

DSN = 'postgresql://postgres:<.l;tncnhfys888@localhost:5432/netology_db'

engine = sqlalchemy.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()


def find_publisher_sales():
    publisher_name = input("Введите имя издателя: ").strip()

    query = (
        session.query(
            Shop.name.label('shop_name'),
            Book.title.label('book_title'),
            Sale.date_sale,
            Sale.price,
            Sale.count
        )
        .join(Stock, Sale.id_stock == Stock.id)
        .join(Book, Stock.id_book == Book.id)
        .join(Publisher, Book.id_publisher == Publisher.id)
        .join(Shop, Stock.id_shop == Shop.id)
        .filter(Publisher.name.ilike(f"%{publisher_name}%"))
    )

    results = query.all()

    print("\n" + "=" * 50)
    if not results:
        print(f"Продаж книг издателя '{publisher_name}' не найдено.")
    else:
        print(f"Найдено продаж: {len(results)}\n")
        for row in results:
            print(f"Магазин:   {row.shop_name}")
            print(f"Книга:     {row.book_title}")
            print(f"Дата:      {row.date_sale.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Цена:      {row.price} руб.")
            print(f"Кол-во:    {row.count} шт.")
            print("-" * 50)

    session.close()


if __name__ == '__main__':
    find_publisher_sales()
