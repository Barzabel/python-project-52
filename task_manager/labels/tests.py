from django.test import TestCase
from django.contrib.messages import get_messages
from django.urls import reverse_lazy
from task_manager.users.models import User
from task_manager.status.models import Status
from task_manager.labels.models import Label
from task_manager.tasks.models import Task
# Create your tests here.


class SetUpTestCase(TestCase):

    def setUp(self):
        # Create user author
        self.user = User.objects.create(
            first_name='Tony', last_name='Soprano',
            username='boss_of_newark',
        )
        self.user.set_password('dqweRty21')
        self.user.save()

        # Create user executor
        self.user2 = User.objects.create(
            first_name='Cris', last_name='Moltisanti',
            username='real_og',
        )
        self.user2.set_password('Alsfkqwo21')
        self.user2.save()

        # Create status

        self.status = Status.objects.create(name='status')
        self.status.save()

        # Create label

        self.label = Label.objects.create(name='IMPORTANT')
        self.label.save()

        # Create task
        self.task = Task.objects.create(
            name='go to home',
            description='a need to go home',
            status=Status.objects.get(pk=self.status.pk),
            executor=User.objects.get(pk=self.user.pk),
            author=self.user
        )
        self.client.login(
            username='boss_of_newark', password='dqweRty21',
        )


class LabelCreateTest(SetUpTestCase):
    def test_label_create_view(self):
        response = self.client.get(reverse_lazy('create_label'))
        self.assertEqual(response.status_code, 200)

    def test_label_create_success(self):
        response = self.client.post(reverse_lazy('create_label'), {
            'name': 'oracle_db',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('labels_list'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'Label successfully created',
            'Метка успешно создана',
        ])


class LabelUpdateTest(SetUpTestCase):
    def test_label_update_view(self):
        response = self.client.get(reverse_lazy('update_label', kwargs={'pk': self.label.pk}))  # noqa: E501
        self.assertEqual(response.status_code, 200)

    def test_label_update_success(self):
        response = self.client.post(reverse_lazy('update_label', kwargs={'pk': self.label.pk}), {'name': 'NOT IMPORTANT', })  # noqa: E501
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('labels_list'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'Label successfully updated',
            'Метка успешно изменена'
        ])


class LabelDeleteTest(SetUpTestCase):
    def test_label_delete_view(self):
        response = self.client.get(reverse_lazy('delete_label',
                                                kwargs={'pk': self.label.pk}))
        self.assertEqual(response.status_code, 200)

    def test_label_delete_success(self):
        response = self.client.post(reverse_lazy('delete_label',
                                                 kwargs={'pk': self.label.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('labels_list'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'Label successfully deleted',
            'Метка успешно удалена'
        ])
