# This program convert a Roman numeral to an Arabic number equivalent

def main():
    roman_q = input("Pls type in a Roman numeral for conversion ").strip()
    arab_num = romantoint(roman_q)
    print(f"The Arabic numnber for the Roman numeral {roman_q} is {arab_num}")

def romantoint(s):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0                             
    for i in range(0, len(s) - 1):             
            now = roman[s[i]]
            next = roman[s[i + 1]]
            
            if now >= next:
                result = result + now    
            else:
                result = result - now
    result = result + roman[s[-1]]        
    return result

if __name__ == "__main__":
    main()
