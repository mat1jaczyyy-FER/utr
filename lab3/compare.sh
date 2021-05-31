#!/bin/bash

for i in {01..25}
do
	echo "Testing $i"
	python3 SimPa.py < test/test$i/primjer.in | diff test/test$i/primjer.out -
done
