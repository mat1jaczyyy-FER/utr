#!/bin/bash

for i in {01..33}
do
	echo "Testing $i"
	python3 SimEnka.py < test/test$i/test.a | diff test/test$i/test.b -
done

