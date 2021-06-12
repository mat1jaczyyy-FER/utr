#!/bin/bash

for i in {01..20}
do
	echo "Testing $i"
	python3 Parser.py < test/test$i/test.in | diff test/test$i/test.out -
done
