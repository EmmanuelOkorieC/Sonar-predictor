import pandas as pd

marks = pd.Series([12, 24, 34, 54], index = ["anna", "emma", "yemi", "jide"])

marks["teacher"] = "Sir Ratcliffe"

print(marks)

aggregate = pd.DataFrame({     
 'marks': [23, 34, 56, 74],
 'course':["Biology", "chemistry", "physics", "maths"]
})

countries = ["Brazil", "Peru", "Nigeria", "UK"]
aggregate.index = countries

sports = pd.Series([1,2,4,2], index = countries)
aggregate['sports'] = sports

aggregate['aggregate'] = aggregate['marks'] / aggregate['sports']
print(aggregate)

# print(aggregate[['marks', 'course']].plot(figsize=(8,3), title='Moving average', ylim=(0,30), style=['-','--']))

# fr = aggregate['marks']

rdf = pd.read_csv('CSV Test.csv')


rdf['Average'] = round(rdf['Waybill Number']/2)
rdf.set_index('Waybill Number', inplace=True)
print(rdf.head())
# print(rdf.loc('10000016112189'))
# print(set(rdf['Customer']))
print(rdf.count())
# print(rdf.info())

# q=[5,4,3,2,1]
# z = [1,2,3,4,5]

# t= pd.DataFrame.from_dict({
#     'as': q-z
# })
# print(t["as"])

# print(t)

# print(pd.to_datetime(rdf['Delivery Confirmation']).head())

# print(rdf.plot())

