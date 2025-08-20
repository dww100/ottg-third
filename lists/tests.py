from django.test import TestCase
from lists.models import Item, List

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")


    def test_renders_input_form(self):
        response = self.client.get("/")
        self.assertContains(response, '<form method="POST" action="/lists/new">')
        self.assertContains(response, '<input name="item_text"')


class NewListTest(TestCase):

    def test_can_save_a_POST_request(self):
        self.client.post("/lists/new", data={"item_text": "A new list item"})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.get()
        self.assertEqual(new_item.text, "A new list item")


    def test_redirects_after_POST(self):
        response = self.client.post("/lists/new", data={"item_text": "A new list item"})
        self.assertRedirects(response, "/lists/the-only-list-in-the-world/")



class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get("/lists/the-only-list-in-the-world/")
        self.assertTemplateUsed(response, "list.html")


    def test_renders_input_form(self):
        response = self.client.get("/lists/the-only-list-in-the-world/")
        self.assertContains(response, '<form method="POST" action="/lists/new">')
        self.assertContains(response, '<input name="item_text"')


    def test_displays_all_items(self):
        mylist = List.objects.create()
        Item.objects.create(text="itemey 1", list=mylist)
        Item.objects.create(text="itemey 2", list=mylist)

        response = self.client.get("/lists/the-only-list-in-the-world/")

        self.assertContains(response, "itemey 1")
        self.assertContains(response, "itemey 2")


class ListAndItemModelsTest(TestCase):

    def test_saving_and_retrieving_items(self):

        mylist = List()
        mylist.save()

        item1 = Item()
        item1.text = "The first (ever) list item"
        item1.list = mylist
        item1.save()

        item2 = Item()
        item2.text = "Item the second"
        item2.list = mylist
        item2.save()

        saved_list = List.objects.get()
        self.assertEqual(saved_list, mylist)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        self.assertEqual(saved_items[0].text, "The first (ever) list item")
        self.assertEqual(saved_items[0].list, mylist)
        self.assertEqual(saved_items[1].text, "Item the second")
        self.assertEqual(saved_items[1].list, mylist)
