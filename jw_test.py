from justwatch import JustWatch

just_watch = JustWatch(query='the matrix')
# the_matrix = just_watch.search_title_id(query='the matrix')
# print(the_matrix)

#just_watch = JustWatch()
results = just_watch.get_providers()
print(results)