

# %%
from itertools import tee, chain, islice, groupby
from copy import copy

class Solution:
    def previous_and_next(num_list):
        """Helper function to return symbols that surround a particular symbol"""
        prevs, items, nexts = tee(num_list, 3)
        prevs = chain([0], prevs)
        nexts = chain(islice(nexts, 1, None), [0])
        return zip(prevs, items, nexts)
    # %%


    def roman_to_arabic(r_num: str):
        """Returns the arabic numeral representation of a roman numeral"""
        # Convert to uppercase
        r_num = r_num.upper()

        values = [1, 5, 10, 50, 100, 500, 1000]
        symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        value_dict = dict(zip(symbols, values))
        # Check for inappropriate use of consecutive symbols
        groups = groupby(r_num)
        result = [(label, sum(1 for _ in group)) for label, group in groups]
        for symbol, count in result:
            if symbol not in symbols:
                return(f"{ num.upper() }:\t Contains invalid characters.")
            if count > 1 and symbol in ['V', 'L', 'D']:
                return(f"{ num.upper() }:\t Not a valid Roman numeral. There are too many consecutive {symbol}'s.")
            if count > 3:
                return(f"{ num.upper() }:\t Not a valid Roman numeral. There are too many consecutive {symbol}'s.")

        

        # Create a list of the numeric values
        num_list = []
        for r in r_num.upper():
            num_list.append(value_dict[r])

        # Iterate through pairs and compare previous values
        total = 0
        i = 0
        for prev, item, nxt in Solution.previous_and_next(num_list):
            # print(prev, item, nxt)

            # Checks to see if the subtractor is within the appropriate range
            if .1*item > prev > 0:
                return(f"{ num.upper() }:\t Not a valid Roman numeral. A value is being inappropriately subtracted.")

            # If the previous symbol is worth less, then it's subtracted
            if prev < item:
                total -= prev
                # If the next symbol is worth more, a flag is raised
                if nxt >= item and i > 0:
                    return(f"{ num.upper() }:\t Not a valid Roman numeral. The order is incorrect.")

            else:
                total += prev

            for n in value_dict.values():
                if i > 1 and total == n:
                    return(f"{ num.upper() }:\t Not a valid Roman numeral. There are symbols that could be condensed.")

            i += 1
        total += item

        return (f"{ num.upper() }:\t { total }")



    def arabic_to_roman(a_num: int):
        """Returns the Roman numeral representation of a b10 Arabic integer"""
        value_dict = {num: sym for num, sym in zip(
            [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
            ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        )}

        r_num = ''
        original_num = copy(a_num)
        for i in value_dict:
            while True: 
                a_num -= i
                r_num += value_dict[i]
                # print(a_num, r_num)       
                if (a_num < 0):
                    a_num += i
                    r_num = r_num[:-1*len(value_dict[i])]
                    break

        return(f"{ original_num }:\t {r_num}")




# Test cases
for num in ['xxxi', 'MMMDCDLXIV', 'IVX', 'XLV', 'XM',
            'xxivx', 'Mcx', 'XLVII', 'XLXI', 'MCMCD', 'DD', 'Xiiiii',
            'CMM', 'IVXLCDM', 'qwer']:
    print(Solution.roman_to_arabic(num))

# %%
for num in [3958, 3333, 256, 48, 23, 17, 987]:
    print(Solution.arabic_to_roman(num))

#%%
