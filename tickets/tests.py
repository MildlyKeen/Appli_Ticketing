from django.test import TestCase
from django.contrib.auth.models import User
from .models import Ticket, Group
from django.urls import reverse

class GroupModelTest(TestCase):
	def test_create_group(self):
		user = User.objects.create_user(username='testuser', password='testpass')
		group = Group.objects.create(name='Test Group', description='A test group')
		group.members.add(user)
		self.assertEqual(group.name, 'Test Group')
		self.assertIn(user, group.members.all())

class TicketModelTest(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='creator', password='testpass')
		self.group = Group.objects.create(name='Project X')

	def test_create_ticket(self):
		ticket = Ticket.objects.create(
			title='Test Ticket',
			description='Test description',
			created_by=self.user,
			group=self.group
		)
		self.assertEqual(ticket.title, 'Test Ticket')
		self.assertEqual(ticket.group, self.group)

class TicketViewsTest(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='creator', password='testpass')
		self.client.login(username='creator', password='testpass')
		self.group = Group.objects.create(name='Project Y')
		self.ticket = Ticket.objects.create(
			title='View Ticket',
			description='View test',
			created_by=self.user,
			group=self.group
		)

	def test_ticket_list_view(self):
		response = self.client.get(reverse('tickets:ticket_list'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'View Ticket')

	def test_ticket_detail_view(self):
		response = self.client.get(reverse('tickets:ticket_detail', args=[self.ticket.pk]))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'View Ticket')
