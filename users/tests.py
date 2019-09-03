# Вход и выход из системы являются
# частью Django и зависят от внутренних представлений и url маршрутов. Поэтому они уже
# имеют тестовое покрытие. Если мы внесем существенные изменения в них в будущем, то
# мы захотели бы добавить тесты и для этого. Но, как правило, вам не нужно добавлять тесты
# для основной функциональности Django.

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class SignupPageTests(TestCase):
    def test_signup_page_status_code(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_form(self):
        get_user_model().objects.create_user('test', 'test@test.com')
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, 'test')
        self.assertEqual(get_user_model().objects.all()[0].email, 'test@test.com')