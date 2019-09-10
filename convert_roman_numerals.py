
#%%
from itertools import groupby
from copy import copy

def romanToInt(s: str) -> str:
    """Given a string, this function validates the string as a Roman numeral and returns
    an explanation of why the string may not represent a valid Roman numeral or returns
    the corresponding integer value."""
    symbols = ['_', 'I', 'V', 'X', 'L', 'C', 'D', 'M']
    num_list = [0, 1, 5, 10, 50, 100, 500, 1000]
    mapping = dict(zip(symbols, num_list))

    s = s.upper()
    s_1 = '_' + s + '_'

    groups = groupby(s_1)
    result = [(label, sum(1 for _ in group)) for label, group in groups]

    # Check for inappropriate use of consecutive symbols
    for symbol, count in result:
        if symbol not in symbols:
            return(f"{ s }: Contains invalid characters.")
        if count > 1 and symbol in ['V', 'L', 'D']:
            return(f"{ s }: Not a valid Roman numeral. There are too many consecutive {symbol}'s.")
        if count > 3:
            return(f"{ s }: Not a valid Roman numeral. There are too many consecutive {symbol}'s.")

    # Loop through each symbol's value; include the previous and next values
    i = total = 0
    for idx, sym in enumerate(s, 1):
        prv = mapping[s_1[idx - 1]]
        val = mapping[sym]
        nxt = mapping[s_1[idx + 1]]
        # print(idx, sym, prv, val, nxt)

        # Check to see if a value is being subtracted that is smaller than one-tenth of the proceeding value (not valid)        
        if .1*val > prv > 0:
            return(f"{ s }: Not a valid Roman numeral. A value is being inappropriately subtracted.")

        # If the previous symbol is worth less, then it's subtracted
        if prv < val:
            total -= prv
            # If the next symbol is worth more, a flag is raised
            if nxt >= val and i > 0:
                return(f"{ s }: Not a valid Roman numeral. The order is incorrect.")

        # If the previous symbol is worth the same or more, then it's added
        else:
            total += prv

        # Check to see if there are redundant symbols that sum to a number that is better represented in another way
        for n in num_list:
            if i > 1 and total == n:
                return(f"{ s }: Not a valid Roman numeral. There are symbols that could be condensed.")

        i += 1
    total += val
    return(f"{ s }: { total }")

def intToRoman(a_num: int):
        """Returns the Roman numeral representation of a b10 integer"""
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

        return(f"{ original_num }: {r_num}")

#%%
for num in ['xxxi', 'MMMDCDLXIV', 'IVX', 'XLV', 'XM',
            'xxivx', 'Mcx', 'XLVII', 'XLXI', 'MCMCD', 'DD', 'Xiiiii',
            'CMM', 'IVXLCDM', 'qwer']:
    print(romanToInt(num))

for num in [3958, 3333, 256, 48, 23, 17, 987]:
    print(intToRoman(num))
#%%
