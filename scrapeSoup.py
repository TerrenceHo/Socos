import requests

countynumber = 1#used to increment through counties
statenumber = 1000#used to increment through states
notCounty = 0#counts how many are not counties

for i in range(0,5): #state numbers go up to 56000
    for y in range (0,255): #Most number of counties is 254
        base_url = 'http://opportunityindex.org/data/county?fips='+ str(statenumber+countynumber) + ''
        #Base url that can also increment
        response = requests.get(base_url)#Gets the url data
        results = response.json()["data"]

        if(results == []):#Ends if there is nothing, or no state
            notCounty = notCounty + 1
            countynumber= countynumber+1
            continue
        
        if(notCounty == 8):
            notCounty = 0
            break
        
        print(response.json()["name"])#prints name of counties.  Below are loops that print out the stats
        
        print('Unemployment Rate:', end = " ")
        for x in results:
            print(x['jobs'], end = ", ")
        print('')
        
        print('Median Household Income:', end = " ")
        for x in results:
            print(x['wages'], end = ", ")
        print('')

        print('Pop. Below Poverty Line:', end = " ")
        for x in results:
            print(x['poverty'], end = ", ")
        print('')

        print('Ratio of Income 80th vs 20th Percentile:', end = " ")
        for x in results:
            print(x['inequality'], end = ", ")
        print('')

        print('Banking Institutions Per 10000 Pop.:', end = " ")
        for x in results:
            print(x['assets'], end = ", ")
        print('')

        print('Household Spending <30% of income on housing:', end = " ")
        for x in results:
            print(x['housing'], end = ", ")
        print('')

        print('High-Speed Internet:', end = " ")
        for x in results:
            print(x['internet_pct'], end = ", ")
        print('')

        print('Preschool Enrollment:', end = " ")
        for x in results:
            print(x['preschool'], end = ", ")
        print('')

        print('On-time HS Graduation:', end = " ")
        for x in results:
            print(x['k12'], end = ", ")
        print('')

        print('Associate Degree or Higher:', end = " ")
        for x in results:
            print(x['degrees'], end = ", ")
        print('')

        print('Violent Crime per 100000 Pop.:', end = " ")
        for x in results:
            print(x['inclusion'], end = ", ")
        print('')

        print('Youth Not In School Or Working:', end = " ")
        for x in results:
            print(x['crime'], end = ", ")
        print('')

        print('Primary Care Providers Per 100000 Pop.:', end = " ")
        for x in results:
            print(x['health_care'], end = ", ")
        print('')

        print('Grocery Stores and Supermarkets per 10000 Pop.:', end = " ")
        for x in results:
            print(x['health_food'], end = ", ")
        print('')

        countynumber = countynumber + 1
        notCounty = 0
        print('')
    
    print('')
    
    countynumber = 1#Resets countynumber
    statenumber= statenumber + 1000#increments the state


