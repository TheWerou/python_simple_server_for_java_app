import unittest

from Decode_com.internal_facade import Comends


class TestComRec(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.com = None

    def test_ask(self):
        self.com = Comends("MACIEK")
        self.com.translate("ASK MICHAL")
        self.assertEqual(self.com.line_list, "ASK MICHAL")
        self.assertEqual(self.com.type, "ASK")
        self.assertEqual(self.com.from_who, "MACIEK")
        self.assertEqual(self.com.to_who, "MICHAL")

    def test_chk(self):
        self.com = Comends("MACIEK")
        self.com.translate("CHK")
        self.assertEqual(self.com.line_list, "ASK MICHAL")
        self.assertEqual(self.com.type, "CHK")
        self.assertEqual(self.com.from_who, "MACIEK")
        self.assertEqual(self.com.to_who, "None")

    def test_noo(self):
        self.com = Comends("MACIEK")
        self.com.translate("NOO MICHAL")
        self.assertEqual(self.com.line_list, "ASK MICHAL")
        self.assertEqual(self.com.type, "NOO")
        self.assertEqual(self.com.from_who, "MACIEK")
        self.assertEqual(self.com.to_who, "MICHAL")

    def test_akc(self):
        self.com = Comends("MACIEK", "AKC MICHAL")
        self.assertEqual(self.com.line_list, "ASK MICHAL")
        self.assertEqual(self.com.type, "AKC")
        self.assertEqual(self.com.from_who, "MACIEK")
        self.assertEqual(self.com.to_who, "MICHAL")
