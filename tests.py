from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    def test_add_new_book_add_three_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Wolfs')

        assert len(collector.get_books_rating()) == 3

    def test_default_new_book_rating_1(self):
        collector = BooksCollector()
        assert (collector.books_rating['Гордость и предубеждение и зомби']) == 1

    def test_set_book_rating_from_1_to_10(self):

        collector = BooksCollector()

        collector.set_book_rating('Гордость и предубеждение и зомби', 3)
        assert (collector.books_rating['Гордость и предубеждение и зомби']) == 3

    def test_set_book_rating_more_than_10(self):

        collector = BooksCollector()

        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 15)

        assert (collector3.books_rating['Что делать, если ваш кот хочет вас убить']) == None



    def test_set_book_rating_no_title_in_BooksCollector(self):

        collector = BooksCollector()

        collector.set_book_rating('Bible', 7)

        assert (collector.books_rating['Bible']) == None


    def test_get_book_rating(self):
        collector = BooksCollector()
        assert (collector.books_rating['Гордость и предубеждение и зомби']) == 3

    def test_get_books_with_specific_rating_3(self):
         collector = BooksCollector()
         collector.get_books_with_specific_rating(3)
         assert len(collector.get_books_with_specific_rating()) == 1


    def test_get_books_rating_3(self):
         collector = BooksCollector()
         collector.get_books_rating()
         assert collector.get_books_rating

    def test_add_book_in_favorites(self):

        collector = BooksCollector()
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(collector.favorites()) == 1


    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.get_list_of_favorites_books()
        assert favorites()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(collector.favorites()) == None