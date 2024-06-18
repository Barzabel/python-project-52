from django.test import TestCase


from django.test import TestCase
from django.contrib.messages import get_messages
from django.urls import reverse_lazy
from task_manager.users.models import User
from task_manager.status.models import Status
from task_manager.tasks.models import Task
# Create your tests here.


class SetUpTestCase(TestCase):

    def setUp(self):
        # Create user author
        self.user = User.objects.create(

            first_name='user_name', last_name='user_last_name',
            username='Test_user1',
        )
        self.user.set_password('dqweRty21')
        self.user.save()

        # Create user executor
        self.user2 = User.objects.create(
            first_name='Cris', last_name='Moltisanti',
            username='Test_user2',
        )
        self.user2.set_password('Alsfkqwo21')
        self.user2.save()

        # Create status

        self.status = Status.objects.create(name='status')
        self.status.save()

        self.status_for_delete = Status.objects.create(name='status_for_delete')
        self.status_for_delete.save()

        # Create task
        self.task = Task.objects.create(
            name='test tasks',
            description='a description test tasks',
            status=Status.objects.get(pk=self.status.pk),
            executor=User.objects.get(pk=self.user.pk),
            author=self.user
        )
        self.client.login(
            username='Test_user1', password='dqweRty21',
        )



class CreateUserTest(SetUpTestCase):
    def test_status_create_view(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('singup'))
        self.assertEqual(response.status_code, 200)

    def test_status_create_success(self):
        self.client.logout()
        response = self.client.post(reverse_lazy('singup'), {
            "first_name": 'testUserVasya',
            "last_name": 'testUserIvanov',
            "username": 'testUser',
            "password1": '123test123',
            "password2": '123test123',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'the new user has been successfully created',
            'Пользователь успешно зарегистрирован',
        ])
        response = self.client.get(reverse_lazy('singup'))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse_lazy('login'),
            {'username': 'testUser', 'password':'123test123',})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('home'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'You are logged in !',
            'Вы залогинены',
        ])


class UserUpdateTest(SetUpTestCase):
    def test_label_update_view(self):
        response = self.client.get(reverse_lazy('update_user',
                                                kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 200)


    def test_user_update_success(self):
        new_data = {
            "first_name": 'testUserVasya',
            "last_name": 'testUserIvanov',
            "username": 'testUser',
            "password1": '123test123',
            "password2": '123test123',
        }
        response = self.client.post(reverse_lazy('update_user', 
                                    kwargs={'pk': self.user.pk}), 
                                    new_data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'the user has been successfully changed',
            'Пользователь успешно изменен'
        ])

    def test_protect_user_update(self):
        response = self.client.post(reverse_lazy('update_user',
                                                 kwargs={'pk': self.user2.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            "You can't change this profile, this is not you",
            'У вас нет прав для изменения другого пользователя.'
        ])


class UserDeleteTest(SetUpTestCase):
    def test_status_delete_view(self):
        response = self.client.get(
            reverse_lazy('delete_user',
                         kwargs={'pk': self.user.pk})
        )

        self.assertEqual(response.status_code, 200)

    def test_status_delete_success(self):
        response = self.client.post(
            reverse_lazy('delete_user',
                         kwargs={'pk': self.user.pk})
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            User.objects.filter(pk=self.user.pk).first(),
            None
        )
        self.assertIn(str(messages[0]), [
            'the user has been deleted',
            'Пользователь успешно удален'
        ])

    def test_protect_status_delete(self):
        response = self.client.post(reverse_lazy('delete_user',
                                                 kwargs={'pk': self.user2.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            "You can't change this profile, this is not you",
            'У вас нет прав для изменения другого пользователя.'
        ])
