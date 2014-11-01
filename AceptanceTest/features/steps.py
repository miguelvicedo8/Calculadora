#!/usr/bin/python
# -*- coding: utf-8 -*-

from lettuce import step, world
import sys
sys.path.append('../')
from calculator import Calculator


@step(u'Given: que se tienen "([^"]*)" y "([^"]*)"')
def given_los_numeros(step, num1, num2):
    world.num1 = float(num1)
    world.num2 = float(num2)


@step(u'When: se realiza la suma')
def when_se_realiza_la_suma(step):
    calc = Calculator()
    world.resultado = calc.suma(world.num1, world.num2)


@step(u'When: se realiza la resta')
def when_se_realiza_la_resta(step):
    calc = Calculator()
    world.resultado = calc.resta(world.num1, world.num2)


@step(u'When: se realiza la multiplicacion')
def when_se_realiza_la_multiplicacion(step):
    calc = Calculator()
    world.resultado = calc.multiplica(world.num1, world.num2)


@step(u'When: se realiza la division')
def when_se_realiza_la_division(step):
    calc = Calculator()
    world.resultado = calc.divide(world.num1, world.num2)


@step(u'then: obtengo el resultado "([^"]*)"')
def then_obtengo_el_resultado(step, result):
    assert world.resultado == float(result)
