#!/bin/bash

secrets_file="sk-secrets-dev.json"

# The 'read' command pauses execution of the script until the user is ready to continue.
echo "press key to continue to next step:"
read -rp "1. restore app config"

cf set-env sk-esconfigs SK_SECRETS "$(cat "$secrets_file")"
cf set-env sk-events SK_SECRETS "$(cat "$secrets_file")"
cf set-env sk-events-read SK_SECRETS "$(cat "$secrets_file")"
cf set-env sk-analytics SK_SECRETS "$(cat "$secrets_file")"

read -rp "2. restart apps"

cf restart sk-events
cf restart sk-events-read
cf restart sk-analytics

read -rp "3. delete es"	

cf delete eph-es
