from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from lists.models import Item, List


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

    def test_cannot_save_null_list_items(self):
        mylist = List.objects.create()
        item = Item(list=mylist, text=None)
        with self.assertRaises(IntegrityError):
            item.save()

    def test_cannot_save_empty_list_items(self):
        mylist = List.objects.create()
        item = Item(list=mylist, text="")
        with self.assertRaises(ValidationError):
            item.full_clean()

    def test_get_absolute_url(self):
        mylist = List.objects.create()
        self.assertEqual(mylist.get_absolute_url(), f"/lists/{mylist.id}/")