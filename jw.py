from justwatch import JustWatch

just_watch_obj = JustWatch(country='US')
provider_count = 0 # keep track of amount of providers available in country

#prints list of service providers based on country 
for result in just_watch_obj.get_providers():
    print(result.get('clear_name')) # prints full name of service provider
    provider_count = provider_count + 1
#print(provider_count)