# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_conjured(self):
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Conjured Mana Cake", items[0].name)
        self.assertEquals(4, items[0].quality)

if __name__ == '__main__':
    unittest.main()
