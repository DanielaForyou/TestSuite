'''
Exerciții obligatorii - grad de dificultate: Usor spre Mediu .
1. Faceti o suita care sa contina testele voastre de la tema 9 + testele de la
intalnirea 10 (care au clasa). Generati raportul
2. Ganditi voi o clasa de test din paginile sugerate in tema 8
- Scrieti cel putin 3 functii de test intr-o clasa (cum am facut la clasa)
Folositi firefox in loc de chrome (ce doriti voi, cate functii de test doriti,
freestyle ca sa incepeti sa ganditi si singuri niste scenarii de test).
Bine de stiut: o functie de test este echivalentul unui test case
Mai multe aici:
https://www.tutorialspoint.com/software_testing_dictionary/test_case.htm
https://www.phptravels.net/
http://automationpractice.com/index.php
https://the-internet.herokuapp.com/
https://www.techlistic.com/p/selenium-practice-form.html
Sau puteti alege voi ce pagina doriti
'''

import unittest  #  am importat toata libraria unittest
import HTMLTestRunner

from TestareAutomataWeb_Selenium.tema_09 import Login
from TestareAutomataWeb_Selenium.tema_10.test_firefox import Firefox
from TestareAutomataWeb_Selenium.tema_10.test_context_menu import ContextMenu
from TestareAutomataWeb_Selenium.tema_10.test_keys import Keyboard
from TestareAutomataWeb_Selenium.tema_10.test_auth import Authentication
from TestareAutomataWeb_Selenium.tema_10.test_alerts import Alerts
from TestareAutomataWeb_Selenium.tema_10.test_edge import Edge


class TestSuite(unittest.TestCase):  # pentru ca am importat toata libraria este nevoie sa specificam in fata clasei TestCase
    # libraria din care sa fie extrasa
    # Daca importam doar libraria, sistemul va avea doar adresa de identificare a librariei, nu si a clasei TestCase
 # Suita de teste = un set de teste care pot fi rulate in acelasi timp

    def test_suite(self):
        lista_teste=unittest.TestSuite()
        lista_teste.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Edge),
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(Firefox),

        ])
        runner = HTMLTestRunner.HTMLTestRunner \
                (
                combine_reports=True,
                report_title='TestReport',
                report_name='Smoke Test Result'
            )

        runner.run(lista_teste)