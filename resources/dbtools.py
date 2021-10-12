def createTables(cur):
    cur.execute(f'''DROP TABLE IF EXISTS earnings''')
    cur.execute(f'''DROP TABLE IF EXISTS user''')
    cur.execute(f'''
    CREATE TABLE "earnings" (
        "user_id"	INTEGER NOT NULL,
        "month"	INTEGER NOT NULL,
        "year"	INTEGER NOT NULL,
        "ad_share"	NUMERIC,
        "sub_share"	NUMERIC,
        "bit_share"	NUMERIC,
        "bit_developer_share"	NUMERIC,
        "bit_extension_share"	NUMERIC,
        "prime_sub_share"	NUMERIC,
        "bit_share_ad"	NUMERIC,
        "fuel_rev"	NUMERIC,
        "bb_rev"	NUMERIC,
        "total_gross"	NUMERIC,
        PRIMARY KEY("user_id","month","year")
    )''')
    cur.execute(f'''
    CREATE TABLE "user" (
        "user_id"	INTEGER NOT NULL,
        "user_name"	TEXT,
        PRIMARY KEY("user_id")
    )''')

# perform sql query
def writeToDb(row, year, month, cur, all_results):
    sum = _arraySum(row)
    if sum <= 0 and not all_results: return

    query = f'''INSERT INTO earnings (user_id, month, year, ad_share, sub_share, bit_share, bit_developer_share, bit_extension_share, prime_sub_share, bit_share_ad, fuel_rev, bb_rev, total_gross) 
                    VALUES({row[0]}, {month}, {year}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[7]}, {row[8]}, {row[9]}, {row[10]}, {sum})
                    ON CONFLICT(user_id, month, year) 
                    DO UPDATE SET 
                    ad_share = ad_share + {row[2]}, 
                    sub_share = sub_share + {row[3]}, 
                    bit_share = bit_share + {row[4]},
                    bit_developer_share = bit_developer_share + {row[5]}, 
                    bit_extension_share = bit_extension_share + {row[6]}, 
                    prime_sub_share = prime_sub_share + {row[7]},
                    bit_share_ad = bit_share_ad + {row[8]}, 
                    fuel_rev = fuel_rev + {row[9]}, 
                    bb_rev = bb_rev + {row[10]}, 
                    total_gross = total_gross + {sum}'''
    cur.execute(query)      

# indexed array sum between 2 and 10 to gross all revenues
def _arraySum(arr):
    index = 0.0;
    sum = 0.0;
    for num in arr:
        if index >= 2 and index <= 10:
            sum += float(num)
        index += 1
    return sum