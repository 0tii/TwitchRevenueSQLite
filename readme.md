
# 💾 Twitch Revenue SQLite

Python Script to generate a SQLite database including all revenues from the great Twitch leak. 
This script takes the path to the 'all_revenues' subfolder of the leaked folder tree and an optional parameter.
The script was written in Python3.9 but should run on 3.x. Tested on both Windows and Linux with Python 3.9.7.

The script relies solely on vanilla libraries. **Should you want to run this on linux or with SQLite <3.24.0, refer to the usage options**

## Usage
Navigate to the folder where main.py resides.

```C:\...\\EarningsTool> py main.py [--all]```

You will be prompted to enter the path to the 'all_revenues' subfolder of the twitch leak folder tree. In order for this script to properly work, you must not alter the original folder tree. Both the full path to the target folder, as well as the relative path from the script directory are valid.

Update as of commit [44f7a60](https://github.com/0tii/TwitchRevenueSQLite/commit/44f7a60a1787f806dcbb11b634eeac820370be6b): Path now gets checked not only for existence but for validity by subsequent sample validation.

### Options
### `--all` 
Write all channel data, even ones without any revenues, to the database. Else only channels that have revenues > 0 will be stored.

### `--legacy` 
If you plan to run this on a linux installation or system that has SQLite version <3.24.0, you will need to specify this option, else the execution will fail.

## Output

The script will create a folder `./db_out/` in its directory which will contain the full SQLite database file (database.db) once the script has finished running.

## Structure
The database structure is highly rudimentary. There are two tables:

- earnings - A table with PK of user_id (the twitch channel id), year and month as well as one field for every revenue source and one field for the total_gross of the revenue shares
- user - A table with PK user_id (twitch channel id) and field user_name. Do with this what you will, I use it to fetch username-id connections on request and cache names.
