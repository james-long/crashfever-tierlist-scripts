# crashfever-tierlist-scripts
Python 3 scripts used to access an Excel document and scrape data from a Japanese mobile game information website, game8.

## What is this for?
These scripts are used in maintaining the Crash Fever Global Version Reddit tier list (https://www.reddit.com/r/crash_fever/comments/6rwqfb/gl_updated_tier_list/), more specifically the unit ratings.

`Compare game8 ratings to xlsx.py` will scrape ratings off game8 and compare them to the Excel file, outputting results.

`Convert xlsx to txt.py` will convert information from the Excel file into a .txt in the format of the table in the Reddit post.

`Create tier list backup.py` will, as expected, create a backup on the tier list in a local folder.

## Dependencies
These scripts are reliant on the following Python 3 packages: `lxml, requests, openpyxl, pandas`

## To Do
* Update script conditions to be more bulletproof
* Transfer discrepancies onto Excel directly instead of outputting it in the console
