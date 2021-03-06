import csv
import requests

countynumber = 1 #used to increment through counties
statenumber = 1000 #used to increment through states
notCounty = 0 #counts how many are not counties

with open('countyData2015.csv', 'w') as file:
    fieldnames = ['County Name','Unemployment Rate','Median Household Income','Pop. Below Poverty Line','Ratio of Income 80th vs 20th Percentile:','Banking Institutions Per 10000 Pop.','Household Spending <30% of income on housing','High-Speed Internet','Preschool Enrollment','On-time HS Graduation','Associate Degree or Higher','Violent Crime per 100000 Pop.','Youth Not In School Or Working','Primary Care Providers Per 100000 Pop.','Grocery Stores and Supermarkets per 10000 Pop.']
    
    writer = csv.DictWriter(file, fieldnames = fieldnames)
    writer.writeheader()#writes the header
    
    for i in range(0,56): #state numbers go up to 56000
        for y in range (0,255): #Most number of counties is 254
            base_url = 'http://opportunityindex.org/data/county?fips='+ str(statenumber+countynumber) + ''
            #Base url that can also increment
            response = requests.get(base_url)#Gets the url data
            results = response.json()["data"]
            
            if(notCounty == 8):
                notCounty = 0
                break
            
            if(results == []):#Ends if there is nothing, or no state
                notCounty = notCounty + 1
                countynumber= countynumber+1
                continue
            
            county = response.json()["name"]#stores name of counties.  Below are loops that print out the stats
            
            jobs = ''
            for x in results:
                if(x["year"]== "2015"):
                    jobs = str(x['jobs'])
            
            wages = ''
            for x in results:
                if(x['year']=='2015'):
                    wages = str(x['wages'])
            
            poverty = ''
            for x in results:
                if(x["year"]== "2015"):
                    poverty = str(x['poverty'])
            
            inequality = ''
            for x in results:
                if(x["year"]== "2015"):
                    inequality = str(x['inequality'])
            
            assets = ''
            for x in results:
                if(x["year"]== "2015"):
                    assets = str(x['assets'])
            
            housing = ''
            for x in results:
                if(x["year"]== "2015"):
                    housing = str(x['housing'])
            
            internet_pct = ''
            for x in results:
                if(x["year"]== "2015"):
                    internet_pct = str(x['internet_pct'])
            
            preschool = ''
            for x in results:
                if(x["year"]== "2015"):
                    preschool = str(x['preschool'])
            
            k12 = ''
            for x in results:
                if(x["year"]== "2015"):
                    k12 = str(x['k12'])
            
            degrees = ''
            for x in results:
                if(x["year"]== "2015"):
                    degrees = str(x['degrees'])
            
            inclusion = ''
            for x in results:
                if(x["year"]== "2015"):
                    inclusion = str(x['inclusion'])
            
            crime = ''
            for x in results:
                if(x["year"]== "2015"):
                    crime = str(x['crime'])
            
            health_care = ''
            for x in results:
                if(x["year"]== "2015"):
                    health_care = str(x['health_care'])
            
            health_food = ''
            for x in results:
                if(x["year"]== "2015"):
                    health_food = str(x['health_food'])

            writer.writerow({'County Name': county,'Unemployment Rate':jobs,'Median Household Income':wages,'Pop. Below Poverty Line':poverty,'Ratio of Income 80th vs 20th Percentile:':inequality,'Banking Institutions Per 10000 Pop.':assets,'Household Spending <30% of income on housing':housing,'High-Speed Internet':internet_pct,'Preschool Enrollment':preschool,'On-time HS Graduation':k12,'Associate Degree or Higher':degrees,'Violent Crime per 100000 Pop.':crime,'Youth Not In School Or Working':inclusion,'Primary Care Providers Per 100000 Pop.':health_care,'Grocery Stores and Supermarkets per 10000 Pop.':health_food})

        
            countynumber = countynumber + 1
            notCounty = 0

        
        countynumber = 1 #Resets countynumber
        statenumber= statenumber + 1000 #increments the state
