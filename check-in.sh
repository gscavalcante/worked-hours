#!/bin/bash

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
