import News
import pandas as pd



'''
company = CompanyProcessor.CompanyProcessor(company="Apple", wiki_url=request.form['url'])
is_forbes_2000 = company.IsForbes2000
status, wiki_data = company.WikiData()
'''


'''
news = News.News()
df2 = news.google(start_date='05/01/2020',end_date='05/10/2020',keyword='Apple')
'''

# %% Testing the News object
'''
company = "Apple"

news = News.News()
print(f"processing the company {company}...")
news.google(start_date='01/01/2017', end_date='01/31/2017', company=company, keyword='Sustainability')
'''


# %% Data for top 100 brands - 2017 to 2020 - Sustainability


companies_df = pd.read_csv("/ProjectData/Top100BrandsData.csv")

news = News.News()

try:
    for company in companies_df.Brand[65:70]:
        news.fetch(start_date='01/01/2017', end_date='12/31/2020', company=company, keyword="Sustainability")
finally:
    news.close_db_connection()

# completed from 20 to 23.. completed Marlboro...
# stopped in between for Netflix, Completed from BMW to LOreal (26:30).. completed until Nescafe.. stopped at home Depot
# %%
# Done list
#35-40 Neutral, Starbucks, Mastercard, Frito-Lay (error)
#40-45: Zara,Gillete, HSBC, Audi(error)
#45-50: Deloitte - Chase completed
#50-55: Added until Siemens... stopped at Nestle
#55-60: completed until ESPN... stopped at Citi
#60-65:completed from Adobe to Ebay...
#65-70: completed from Chevrolet to PwC

