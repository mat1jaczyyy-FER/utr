#!/bin/bash

for i in {01..14}
do
	echo "Testing $i"
	python3 MinDka.py < test/test$i/t.ul | diff test/test$i/t.iz -
done
