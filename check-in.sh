#!/bin/bash

add_time() {
	FILE_NAME='worked_hours.csv'
	DATE=`date +%Y-%m-%d`

	if [ ! -f $FILE_NAME ]; then
		echo "Date,Start,End" >> $FILE_NAME
	fi

	if [ $1 ]; then
		HOUR=${1}
	else
		HOUR=`date +%H:%M`
	fi

	LAST_LINE=$(tail -n 1 ${FILE_NAME})
	TMP=($(echo "$LAST_LINE" | tr ',' '\n'))

	if [ ${#TMP[1]} -gt 0 ] && [ ${#TMP[2]} -eq 0 ]; then
		echo "$HOUR" >> $FILE_NAME
	else
		echo -n "$DATE,$HOUR," >> $FILE_NAME
	fi

	echo "Hour saved with success"
}

display_help() {
	echo "Usage: $0 [option]">&2
	echo
	echo "usage: $0 -t [hour]"
	echo
	echo "Options:"
	echo "  -h, --help display help message and exit"
	echo "  -t, --time=hour change the hour  manually"
}

if [ ! $1 ]; then
	add_time
	exit 0
fi

case "$1" in
	-h | --help)
		display_help
		exit 0
		;;
	-t | --time)
		add_time $2
		;;
	--* | *)
		echo "Error: Unknown option  $1">&2
		exit 1
		;;
esac