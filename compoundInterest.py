def calculateCompoundInterest():
    getLoanDetails()
    print("---")
    getLoanDetails()
    print("---")
    getLoanDetails()
    
def getLoanDetails():
    # This first 3 lines are provided for you 
    # This first 3 lines are provided for you
    error_msg = "Please enter numerical characters."
    try:
        client_one_principal = float(input("Principle (amount): "))
    except:
        print (error_msg)      
    try: 
        client_one_time = float(input("Time:               "))
    except:
        print (error_msg)  
    try:    
        client_one_rate = float(input("Rate:               "))
    except:
        print (error_msg)

    ptr = (getACompoundInterest(client_one_principal, client_one_time, client_one_rate))
    return ptr

def getACompoundInterest(p, t, r):
    r = r / 100 + 1
    rtp = pow(r, t)
    a = p * rtp
    ci = a - p
    interest = "Compound Interest: "+str(round(ci, 2))
    print(interest)

    # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
