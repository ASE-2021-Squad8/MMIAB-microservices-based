#!/bin/bash

echo "This tests are intended to be used with an empty database."
echo "Please make sure you have deleted every volume of the app."
echo ""

read -r -p "Do you want to continue? [y/n] " yn
case $yn in
	N|n )
		exit
	;;
	Y|y )
		docker-compose rm -f -v -s
		echo "Starting the app with docker"
		docker-compose build
		docker-compose up -d
		echo "Sleeping for 2 minutes to make sure docker has started the app"
		sleep 120
		echo "Starting integration tests"
		echo ""
		python3.9 ./integration_test.py
		docker-compose rm -f -v -s
		exit
	;;
	* )
		echo "Unrecognized option"
		exit
	;;
esac
