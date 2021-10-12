import gzip as gz, csv, sqlite3 as sql, os, sys
import resources.dbtools as dbt, resources.progressbar as progbar

#start params
all_results = sys.argv.__contains__('all')
# init globals
processed_files = 0
number_files = 0
revenue_path = ''

# get path to revenues
while True:
    revenue_path = input('Please specify the path to the \'./all_revenues/\' folder of the twitch leak.\nDesired format is e.g. \'C:/.../twitch-payouts/all_revenues\'\033[0m')
    if os.path.exists(revenue_path):
        print('\033[92mAccepted.\033[0m')
        break
    else:
        print('\033[93mPlease enter a valid path\033[0m')

# make output dir
try: os.mkdir('./db_out/')
except OSError:
    if not os.path.exists('./db_out/'): print('\033[91mCould not create output folder. You can try manually creating ./db_out/ and restarting.\033[0m')

# db prep
con = sql.connect('./db_out/database.db')
cur = con.cursor()
dbt.createTables(cur)

# at path read from csv inside gz 
def processCSV(path):
    with gz.open(path, 'rt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count, month, year = 0, 0, 0
        for row in csv_reader:
            if line_count == 0: # skip header 
                line_count += 1
            elif line_count == 1: # convert date only once
                date = row[11].split('/')
                month, year = date[0], date[2]
                dbt.writeToDb(row, year, month, cur, all_results)
                line_count += 1
            else:
                dbt.writeToDb(row, year, month, cur, all_results)
                line_count += 1
            progbar.printProgressBar(iteration=processed_files, total=number_files, suffix=f'(line {line_count} for {month}/{year}) - File {processed_files} of {number_files}')
            
# count number of files #!(optional)
for root, dirs, files in os.walk(revenue_path):
    if files: number_files += 1

# walk folder tree recursively, initiating csv processing for each file
for root, dirs, files in os.walk(revenue_path):
    if files: 
        processed_files += 1
        processCSV(root+os.sep+files[0])

print('\n\033[92mTask succeeded. SQLite .db file can be found in \'./db_out/database.db\'\033[0m')

#db close
con.commit()
con.close()