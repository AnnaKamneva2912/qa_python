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
        collector1 = BooksCollector()
        collector1.add_new_book('Гордость и предубеждение и зомби')
        assert (collector1.get_book_rating('Гордость и предубеждение и зомби')) == 1

    def test_set_book_rating_from_1_to_10(self):
        collector2 = BooksCollector()
        collector2.add_new_book('Гордость и предубеждение и зомби')
        collector2.set_book_rating('Гордость и предубеждение и зомби', 3)
        assert collector2.get_book_rating('Гордость и предубеждение и зомби') == 3

    def test_set_book_rating_more_than_10(self):
        collector3 = BooksCollector()
        collector3.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector3.set_book_rating('Что делать, если ваш кот хочет вас убить', 15)
        assert collector3.get_book_rating('Что делать, если ваш кот хочет вас убить') == 1

    def test_set_book_rating_no_title_in_BooksCollector(self):
        collector4 = BooksCollector()
        collector4.add_new_book('Гордость и предубеждение и зомби')
        collector4.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector4.set_book_rating('Bible', 7)
        assert collector4.get_book_rating('Bible') == None


    def test_get_book_rating(self):
        collector5 = BooksCollector()
        collector5.add_new_book('Гордость и предубеждение и зомби')
        collector5.set_book_rating('Гордость и предубеждение и зомби', 3)
        assert collector5.get_book_rating('Гордость и предубеждение и зомби') == 3

    def test_get_books_with_specific_rating_3(self):
         collector6 = BooksCollector()
         collector6.add_new_book('Гордость и предубеждение и зомби')
         collector6.set_book_rating('Гордость и предубеждение и зомби', 3)
         collector6.get_books_with_specific_rating(3)
         assert len(collector6.get_books_with_specific_rating(3)) == 1

    def test_get_books_rating(self):
         collector7 = BooksCollector()
         collector7.add_new_book('Гордость и предубеждение и зомби')
         collector7.add_new_book('Что делать, если ваш кот хочет вас убить')
         collector7.add_new_book('Wolfs')
         collector7.get_books_rating()
         assert len(collector7.get_books_rating()) == 3

    def test_add_book_in_favorites(self):
        collector8 = BooksCollector()
        collector8.add_new_book('Гордость и предубеждение и зомби')
        collector8.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector8.add_new_book('Wolfs')
        collector8.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(collector8.favorites) == 1


    def test_get_list_of_favorites_books(self):
        collector9 = BooksCollector()
        collector9.add_new_book('Гордость и предубеждение и зомби')
        collector9.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector9.add_new_book('Wolfs')
        collector9.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector9.get_list_of_favorites_books()
        assert len(collector9.favorites)==1

    def test_delete_book_from_favorites(self):
        collector10 = BooksCollector()
        collector10.add_new_book('Гордость и предубеждение и зомби')
        collector10.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector10.add_new_book('Wolfs')
        collector10.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector10.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(collector10.favorites) == 0