#!/bin/bash

date=""
message=""

while getopts ":d:m:" opt; do
  case $opt in
    d)
      date="$OPTARG"
      ;;
    m)
      message="$OPTARG"
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

if [ -z "$date" ] || [ -z "$message" ]; then
  echo "Both -d (date) and -m (message) options are required." >&2
  exit 1
fi

git add .
git commit -m "solution for [$date] $message"
git push origin main