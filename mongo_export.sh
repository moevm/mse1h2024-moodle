#!/bin/bash

mongoexport --uri="mongodb://user:pass@localhost:27017/moodle-statistics?authSource=admin" --collection=statistics --db=moodle-statistics --out=statistics.json --authenticationDatabase=admin

mongoexport --uri="mongodb://user:pass@localhost:27017/moodle-statistics?authSource=admin" --collection=users --db=moodle-statistics --out=users.json --authenticationDatabase=admin

mongoexport --uri="mongodb://user:pass@localhost:27017/moodle-statistics?authSource=admin" --collection=sessions --db=moodle-statistics --out=sesssions.json --authenticationDatabase=admin

