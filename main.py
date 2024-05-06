import webbrowser

EXTERNAL= "1"
FIXED_COST="1"
FaaS="1"
MAX_INPUT = 2
AZURE_URL = "https://azure.microsoft.com/en-us/pricing/calculator/"
SECTIONS_LIST = [
    {"section": "A", "prices": ["Cost Of Ownership", "Application"]},
    {"section": "B", "prices": ["Procurement"]},
    {"section": "C", "prices": ["Internal"]},  # internal
    {"section": "D", "prices": ["CSP1", "CSP2"]}  # external
]
# SECTIONS_LIST = [
#     {"section": "A", "prices": ["Cost Of Ownership", "Application"]},
#     {"section": "B", "prices": ["Procurement", "Migration", "Software Development"]},
#     {"section": "C", "prices": ["Internal", "usage", "upgrade"]},  # internal
#     {"section": "D", "prices": ["CSP1", "CSP2","test"]}  # external
# ]

def get_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Input cannot be negative")
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_each_section(eachItem):
    section_total = 0
    print("Let's enter price values for Section:", eachItem["section"])
    
    for price in eachItem["prices"]:
        print("**********************Let's get values for :",price)
        # Get inputs for cost & service Type
        cost_type = input("\nEnter type of (Fixed cost/monthly). Enter  " + FIXED_COST + " if Fixed, else monthly would be assumed: ").strip().lower()
        service_type = input("\nEnter type of (FaaS/PaaS). Enter " + FaaS + "  if FaaS, else PaaS would be assumed: ").strip().lower()
        if cost_type == FIXED_COST:
            isFixed = True
        else:
            isFixed = False

        if service_type == FaaS:
            isFaaS = True
        else:
            isFaaS = False

        if(price==SECTIONS_LIST[3]['prices'][0] or price==SECTIONS_LIST[3]['prices'][1]):
            webbrowser.open_new(AZURE_URL)
        
        if not isFixed and isFaaS:
            cost_per_hr=get_input(f"Enter cost per hour : ")
            time_to_execute=get_input(f"Time to execute the function in hour : ")
            value =cost_per_hr*time_to_execute
        else:
            value = get_input(f"Enter value {price}: ")
        print(f"For price total value is ={value}")
        section_total = section_total + value
    print(f"For section {eachItem['section']} total value is ={section_total}")
    return section_total

def main():
    total = 0
    section_type = input("\nEnter type of (internal/external). Enter  " + EXTERNAL + "  if external, else internal would be assumed: ").strip().lower()
    if section_type == "1":
        isExternal = True
    else:
        isExternal = False

    # iterate through all sections and get me value
    for eachItem in SECTIONS_LIST:
        if isExternal:
            total=total+calculate_each_section(eachItem)
        else:
            if eachItem["section"] != SECTIONS_LIST[3]["section"]:
                total=total+calculate_each_section(eachItem)

    print("\nTotal spending on cloud service:", total)


if __name__ == "__main__":
    main()
