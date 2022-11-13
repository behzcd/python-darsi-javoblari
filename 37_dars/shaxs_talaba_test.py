# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 03:58:17 2022

@author: Bekhzod
"""

import unittest
from shaxs_talaba import Shaxs, Talaba

class ShaxsTalabaTest(unittest.TestCase):
    def setUp(self):
        ism = 'Bekhzod'
        familiya = 'Mukhammadaliev'
        passport = "FA0228821"
        tyil = 1999
        self.idraqam = 12194852
        manzil = '46, Mustqillik st, Namangan, Uzbekistan'
        self.subject = 'AI'
        self.shaxs1 = Shaxs(ism,familiya,passport,tyil)
        self.talaba1 = Talaba(ism,familiya,passport,tyil,self.idraqam,manzil)
        
    def test_create(self):
        self.assertIsNotNone(self.shaxs1.ism)
        self.assertIsNotNone(self.shaxs1.familiya)
        self.assertIsNotNone(self.shaxs1.passport)
        self.assertIsNotNone(self.shaxs1.tyil)
        self.assertIsNotNone(self.talaba1.ism)
        self.assertIsNotNone(self.talaba1.familiya)
        self.assertIsNotNone(self.talaba1.passport)
        self.assertIsNotNone(self.talaba1.tyil)
        self.assertIsNotNone(self.talaba1.idraqam)
        self.assertIsNotNone(self.talaba1.manzil)
        
    def test_get_info(self):
        shaxs1_info = 'Bekhzod Mukhammadaliev. Passport:FA0228821, 1999-yilda tug`ilgan'
        self.assertEqual(shaxs1_info, self.shaxs1.get_info())
        talaba1_info = 'Bekhzod Mukhammadaliev. 1-bosqich. ID raqami: 12194852, Manzili: 46, Mustqillik st, Namangan, Uzbekistan'
        self.assertEqual(talaba1_info, self.talaba1.get_info())
        
    def test_get_age(self):
        self.assertEqual(23, self.shaxs1.get_age(2022))
    
    def test_get_id(self):
        self.assertEqual(self.idraqam, self.talaba1.get_id())
        
    def test_fanga_yozil(self):
        self.talaba1.fanga_yozil(self.subject)
        self.assertEqual(self.subject, self.talaba1.fanlar[-1])
        
    def test_get_fanlar(self):
        fanlar = ['AI']
        self.talaba1.fanga_yozil(self.subject)
        self.assertEqual(fanlar,self.talaba1.get_fanlar())
    
    def test_remove_fan(self):
        no_fan = 'Business Management'
        self.talaba1.fanga_yozil(self.subject)
        self.assertEqual("Siz bu fanga yozilmagansiz", self.talaba1.remove_fan(no_fan))
        self.assertEqual("Bu fan ochirildi", self.talaba1.remove_fan(self.subject))

              
unittest.main()