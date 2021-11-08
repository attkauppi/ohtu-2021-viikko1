import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_tilavuus_vahintaan_nolla(self):
        """ Varmistaa, etta tilavuus määritellään 
        vähintään nollaksi """
        self.varasto = Varasto(-1)
        self.assertAlmostEqual(0.0, self.varasto.tilavuus)

    def test_alkusaldo_ei_ole_negatiivinen(self):
        """ Testaa ettei alkusaldo voi olla negatiivinen """
        self.varasto = Varasto(tilavuus=10, alku_saldo=-1)
        
        self.assertAlmostEqual(0.0, self.varasto.saldo)

    def test_tilavuus_ei_ylity(self):
        """ Testaa ettei varaston tilavuus ylity """
        self.varasto = Varasto(tilavuus=10, alku_saldo=100)

        self.assertEqual(10, self.varasto.saldo)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    
    def test_negatiivisen_ottaminen_ei_vaikuta_saldoon(self):
        """ Testaa, että negatiivisen määrän lisääminen
        varastoon ei vaikuta saldoon """
        exp_result = 0
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(0.0, self.varasto.saldo)
    
    def test_varastoon_ei_voi_lisata_enemman_kuin_mahtuu(self):
        """ Testaa, ettei varastoon voi lisätä enemmän
        kuin mahtuu """
        exp_result = 10
        self.varasto.lisaa_varastoon(100)

        self.assertAlmostEqual(exp_result, self.varasto.saldo)
    
    def test_varastosta_ei_voi_ottaa_negatiivista_maaraa(self):
        """ Testaa, että varastosta ei voi ottaa 
        negatiivista määrää """
        self.varasto.lisaa_varastoon(2)

        # Oletuksena on, että varastossa on 2 kpl
        # vielä ottamisen jälkeenkin
        exp_result = 2

        self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(exp_result, self.varasto.saldo)
    
    def test_varastosta_ei_voida_ottaa_enemman_kuin_on(self):
        """ Testaa, ettei varastosta voida ottaa enempää
        kuin siellä on """
        self.varasto.lisaa_varastoon(2)
        
        # Oletuksena on, että varastossa on 0, kun sinne
        # on lisätty 2 ja kaikki on viety.
        exp_result = 0

        self.varasto.ota_varastosta(100)
        self.assertAlmostEqual(exp_result, self.varasto.saldo)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_str(self):
        """ Tests __str__ """
        exp_result = "saldo = 0, vielä tilaa 10"
        result = self.varasto.__str__()

        self.assertEqual(exp_result, result)
