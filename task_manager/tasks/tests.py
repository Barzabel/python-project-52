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

        # Create label
        self.label = Label.objects.create(name='IMPORTANT')
        self.label.save()

        # Create task
        self.task = Task.objects.create(
            name='test tasks',
            description='a description test tasks',
            status=Status.objects.get(pk=self.status.pk),
            executor=User.objects.get(pk=self.user.pk),
            author=self.user
        )
        self.task.save()
        self.another_task = Task.objects.create(
            name='test tasks2',
            description='a description test tasks2',
            status=Status.objects.get(pk=self.status.pk),
            executor=User.objects.get(pk=self.user2.pk),
            author=self.user2
        )
        self.another_task.save()
        self.client.login(
            username='Test_user1', password='dqweRty21',
        )


class CreateTaskTest(SetUpTestCase):
    def test_task_create_view(self):
        response = self.client.get(reverse_lazy('create_task'))
        self.assertEqual(response.status_code, 200)

    def test_task_create_success(self):
        response = self.client.post(reverse_lazy('create_task'), {
            "name": "TestTask3",
            "description": "description TestTask3",
            "status": self.status.pk,
            "executor": self.user.pk,
            "labels": [self.label.pk],
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks_list'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'the new task has been successfully created',
            'Задача успешно создана',
        ])


class TaskUpdateTest(SetUpTestCase):
    def test_task_update_view(self):
        response = self.client.get(reverse_lazy('update_task',
                                                kwargs={'pk': self.task.pk}))
        self.assertEqual(response.status_code, 200)

    def test_task_update_success(self):
        new_data = {
            "name": "TestTask3",
            "description": "description TestTask3",
            "status": self.status.pk,
            "executor": self.user.pk,
            "labels": [self.label.pk],
        }
        response = self.client.post(reverse_lazy('update_task',
                                    kwargs={'pk': self.user.pk}),
                                    new_data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks_list'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'the task has been successfully changed',
            'Задача успешно изменена'
        ])

    def test_protect_task_update(self):
        response = self.client.post(
            reverse_lazy('update_task', kwargs={'pk': self.another_task.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks_list'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            "you can't change this task, you are not author",
            'вы не можете изменить эту задачу, у вас нет прав доступа'
        ])


class TaskDeleteTest(SetUpTestCase):
    def test_task_delete_view(self):
        response = self.client.get(
            reverse_lazy('delete_task',
                         kwargs={'pk': self.user.pk})
        )

        self.assertEqual(response.status_code, 200)

    def test_task_delete_success(self):
        response = self.client.post(
            reverse_lazy('delete_task',
                         kwargs={'pk': self.task.pk})
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks_list'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            Task.objects.filter(pk=self.task.pk).first(),
            None
        )
        self.assertIn(str(messages[0]), [
            'the task has been successfully delete',
            'Задача успешно удалена'
        ])

    def test_protect_task_delete(self):
        response = self.client.post(
            reverse_lazy('delete_task', kwargs={'pk': self.another_task.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks_list'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            "you can't delete this task, you are not author",
            'вы не можете удалить это задание, вы не являетесь автором'
        ])
