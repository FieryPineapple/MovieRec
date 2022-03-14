from justwatch import JustWatch

just_watch = JustWatch(title_id=10)

results = just_watch.get_providers()
for r in results:
    #x = slice(3, 4)
    prov = r[:2, :2]
print(prov)