from datetime import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    today = datetime.strptime(today, "%Y.%m.%d")
    
    expiry_date = {}
    
    for i in terms:
        terms, months = i.split()
        expiry_date[terms] = int(months)
    
    idx = 1
    for i in privacies:
        date, terms_type = i.split()
        months = expiry_date[terms_type]
        date = datetime.strptime(date, "%Y.%m.%d")
        result =  date + relativedelta(months=months) 
        if today >= result:
            answer.append(idx)
        idx += 1
        
    return answer

