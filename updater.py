import coreapi
import tokenfile
import pandas as pd

TOKEN = tokenfile.token
TOME_RAID_VARS = ('head','body','hands','legs','feet','ears','neck','wrists')
RAID_GEAR_NAME = "Dark Horse"

auth = coreapi.auth.TokenAuthentication(TOKEN, scheme='Bearer', domain='etro.gg')
client = coreapi.Client(auth=auth)
schema = client.get("https://etro.gg/api/docs/")

bis_data = client.action(schema, ["gearsets","bis"])

datatable = []
cache = {}
for x in bis_data:
  row = [x["jobAbbrev"],x["name"]]
  for y in TOME_RAID_VARS:
    if x[y] in cache:
      text = cache[x[y]]
    else:
      text = client.action(schema, ["equipment", "read"], params={"id":x[y]})["name"]
      cache[x[y]] = text
    row.append(RAID_GEAR_NAME in text)
    print(text)
  datatable.append(row)

cols = ["Job","Set"]
cols.extend(TOME_RAID_VARS)
df = pd.DataFrame(datatable,columns=cols)
df = df[df["Job"]!="BLU"]

df.to_csv("tome_raid.csv",index=False)