from shutil import copyfile
import datetime

print("Backing up, please wait...")

copyfile("Tier List.xlsx", "Backups\Tier List Backup " + str(datetime.date.today()) + ".xlsx")

input("Data transfer complete!")
