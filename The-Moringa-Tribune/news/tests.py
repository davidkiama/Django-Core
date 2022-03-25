from django.test import TestCase
from .models import Editor, Article, Tags
import datetime as dt

# Create your tests here.


class EditorTestClass(TestCase):
    def setUp(self):
        self.kiama = Editor(first_name='David',
                            last_name='Kiama', email='davidkiama@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.kiama, Editor))

    def test_save(self):
        self.kiama.save_editor()
        editors = Editor.objects.all()

        self.assertTrue(len(editors) > 0)

     # Creating a new tag and saving it
        self.new_tag = Tags(name='testing')
        self.new_tag.save()

        self.new_article = Article(
            title='Test Article', post='This is a random test Post', editor=self.kiama)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        Tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news) > 0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
