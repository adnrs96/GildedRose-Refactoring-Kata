# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def decrement_sell_in(self, item):
        item.sell_in -= 1

    def has_sell_in_passed(self, item):
        return item.sell_in <= 0
    
    def make_worthless(self, item):
        if item.quality != 0:
            item.quality = 0

    def decrement_item_quality(self, item, by=1):
        item.quality -= by
        if self.has_reached_min_quality(item):
            item.quality = 0
    
    def increment_item_quality(self, item, by=1):
        item.quality += by
        if self.has_reached_max_quality(item):
            item.quality = 50

    def has_reached_max_quality(self, item):
        return item.quality >= 50

    def has_reached_min_quality(self, item):
        return item.quality <= 0

    def update_quality_aged_brie(self, item):
        if self.has_reached_max_quality(item):
            return
        if self.has_sell_in_passed(item):
            self.increment_item_quality(item, by=2)
        else:  
            self.increment_item_quality(item)
    
    def update_quality_backstage_passes(self, item):
        if self.has_sell_in_passed(item):
            self.make_worthless(item)
            return
        if item.sell_in < 11:
            self.increment_item_quality(item, by=2)
        elif item.sell_in < 6:
            self.increment_item_quality(item, by=3)
        else:
            self.increment_item_quality(item)

    def update_quality_sulfuras(self, item):
        return

    def update_quality_generic(self, item):
        if self.has_reached_min_quality(item):
            return
        if self.has_sell_in_passed(item):
            self.decrement_item_quality(item, by=2)
        else:
            self.decrement_item_quality(item)
    
    def update_quality_conjured(self, item):
        if self.has_reached_min_quality(item):
            return
        if self.has_sell_in_passed(item):
            self.decrement_item_quality(item, by=4)
        else:
            self.decrement_item_quality(item, by=2)
        
    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self.update_quality_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_quality_backstage_passes(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                self.update_quality_sulfuras(item)
            elif item.name == "Conjured Mana Cake":
                self.update_quality_conjured(item)
            else:
                self.update_quality_generic(item)
            if item.name != "Sulfuras, Hand of Ragnaros":
                self.decrement_sell_in(item)
            # if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
            #     if item.quality > 0:
            #         if item.name != "Sulfuras, Hand of Ragnaros":
            #             item.quality = item.quality - 1
            # else:
            #     if item.quality < 50:
            #         item.quality = item.quality + 1
            #         if item.name == "Backstage passes to a TAFKAL80ETC concert":
            #             if item.sell_in < 11:
            #                 if item.quality < 50:
            #                     item.quality = item.quality + 1
            #             if item.sell_in < 6:
            #                 if item.quality < 50:
            #                     item.quality = item.quality + 1
            # if item.name != "Sulfuras, Hand of Ragnaros":
            #     item.sell_in = item.sell_in - 1
            # if item.sell_in < 0:
            #     if item.name != "Aged Brie":
            #         if item.name != "Backstage passes to a TAFKAL80ETC concert":
            #             if item.quality > 0:
            #                 if item.name != "Sulfuras, Hand of Ragnaros":
            #                     item.quality = item.quality - 1
            #         else:
            #             item.quality = item.quality - item.quality
            #     else:
            #         if item.quality < 50:
            #             item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
