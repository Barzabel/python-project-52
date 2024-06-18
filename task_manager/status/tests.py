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


class CreateStatusTest(SetUpTestCase):
    def test_status_create_view(self):
        response = self.client.get(reverse_lazy('create_status'))
        self.assertEqual(response.status_code, 200)

    def test_status_create_success(self):
        response = self.client.post(reverse_lazy('create_status'), {
            'name': 'new_test_status',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('status_list'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'the new status has been successfully created',
            'Статус успешно создан',
        ])


class StatusUpdateTest(SetUpTestCase):
    def test_label_update_view(self):
        response = self.client.get(reverse_lazy('update_status',
                                                kwargs={'pk': self.status.pk}))
        self.assertEqual(response.status_code, 200)

    def test_label_update_success(self):
        response = self.client.post(reverse_lazy('update_status',
                                                 kwargs={'pk': self.status.pk}),
                                    {'name': 'change status', })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('status_list'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'the status has been successfully changed',
            'Статус успешно изменен'
        ])


class LabelDeleteTest(SetUpTestCase):
    def test_status_delete_view(self):
        response = self.client.get(
            reverse_lazy('delete_status',
                         kwargs={'pk': self.status_for_delete.pk})
        )

        self.assertEqual(response.status_code, 200)

    def test_status_delete_success(self):
        response = self.client.post(
            reverse_lazy('delete_status',
                         kwargs={'pk': self.status_for_delete.pk})
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('status_list'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            Status.objects.filter(pk=self.status_for_delete.pk).first(),
            None
        )
        self.assertIn(str(messages[0]), [
            'the status has been deleted',
            'Статус успешно удален'
        ])

    def test_protect_status_delete(self):
        response = self.client.post(reverse_lazy('delete_status',
                                                 kwargs={'pk': self.status.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('status_list'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'It is not possible to delete a status because it is in use',
            'Невозможно удалить статус, потому что он используется'
        ])
