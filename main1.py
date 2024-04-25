import webbrowser
MAX_INPUT=2
AZURE_URL="https://azure.microsoft.com/en-us/pricing/calculator/"
SECTIONS_LIST = [
    {"section": "Section A", "prices": ["Cost Of Ownership", "Application"]},
    {"section": "Section B", "prices": ["Procurement", "Migration","Software Development"]},
    {"section": "Section C", "prices": ["Internal", "usage","upgrade"]}, # internal
    {"section": "Section D", "prices": ["CSP1","CSP2"]} # external
]

def get_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Input cannot be negative")
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_section_total(section_name, section_inputs):
    print("calculate_section_total start hoga")
    total = 0
    print(f"\n{section_name}:")
    for i in range(1, section_inputs + 1):
        print(f"Now am running on counter {i} and total value ={total}")
        value = get_input(f"Enter value {i}: ")
        total += value
    return total

def calculate_external_section():
    csp = input("Enter CSP value (leave blank or enter 0 for none): ").strip()
    if not csp or csp == "0":
        webbrowser.open_new(AZURE_URL)
        csp = get_input("Enter CSP value after adding from the URL: ")
    else:
        csp = float(csp)
    return csp

def main():
    print("Main main me hu start")
    total_a = calculate_section_total("Section A", 3)
    total_b = calculate_section_total("Section B", MAX_INPUT)
    
    section_c_type = input("\nEnter type of Section C (internal/external): ").strip().lower()
    if section_c_type == "external":
        section_c_total = calculate_external_section()
    elif section_c_type == "internal":
        section_c_total = calculate_section_total("Section C", 2)
    else:
        print("Invalid section type. Please enter 'internal' or 'external'.")
        return
    
    total = total_a + total_b + section_c_total
    print("\nTotal spending on cloud service:", total)

if __name__ == "__main__":
    main()