Feature: Realizar operaciones basicas
	Como matematico 
	quiero calcular el resultado de operaciones basicas
	para facilitarme la vida


	Scenario: La suma de "3" mas "5"
		Given: que se tienen "3" y "5"
		When: se realiza la suma
		then: obtengo el resultado "8"

	Scenario: La suma de "43" mas "76"
		Given: que se tienen "43" y "76"
		When: se realiza la suma
		then: obtengo el resultado "119"

	Scenario: La suma de "22" mas "75"
		Given: que se tienen "22" y "75"
		When: se realiza la suma
		then: obtengo el resultado "97"

	Scenario: La resta de "10" menos "3"
		Given: que se tienen "10" y "3"
		When: se realiza la resta
		then: obtengo el resultado "7"

	Scenario: La resta de "100" menos "40"
		Given: que se tienen "100" y "40"
		When: se realiza la resta
		then: obtengo el resultado "60"

	Scenario: La resta de "75" menos "12"
		Given: que se tienen "75" y "12"
		When: se realiza la resta
		then: obtengo el resultado "63"

	Scenario: La multiplicacion de "3" por "5"
		Given: que se tienen "3" y "5"
		When: se realiza la multiplicacion
		then: obtengo el resultado "15"

	Scenario: La multiplicacion de "43" por "76"
		Given: que se tienen "43" y "76"
		When: se realiza la multiplicacion
		then: obtengo el resultado "3268"

	Scenario: La multiplicacion de "22" por "75"
		Given: que se tienen "22" y "75"
		When: se realiza la multiplicacion
		then: obtengo el resultado "1650"

	Scenario: La division de "10" entre "3"
		Given: que se tienen "10" y "3"
		When: se realiza la division
		then: obtengo el resultado "3.33"

	Scenario: La division de "100" entre "40"
		Given: que se tienen "100" y "40"
		When: se realiza la division
		then: obtengo el resultado "2.5"

	Scenario: La division de "75" entre "12"
		Given: que se tienen "75" y "12"
		When: se realiza la division
		then: obtengo el resultado "6.25"