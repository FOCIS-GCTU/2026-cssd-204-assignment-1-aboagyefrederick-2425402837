
def main():
  pass #code goes here

# File: initials.py
# Description: Print out my initials in stylized large letters.
# Assignment Number: 1
#
# Name: Frederick Aboagye
# STUDENT ID: <2425402837>
# Email: <2425402837@live.gctu.edu.gh>
# Grader: <Augustus Buckman>
#
# On my honor, Frederick Aboagye, this programming assignment is my own work
# and I have not provided this code to any other student.


def main():
    # Print small initials, large stylized initials, with blank lines as required

    print()
    print("...MAF")
    print()

    # Large M (12 chars), large period (4 asterisks), large A (12 chars), large period (4 asterisks), large F (12 chars), large period (4 asterisks)
    # Format per line: ...{M_row}...{period_row}...{A_row}...{period_row}...{F_row}...{period_row}
    # Each letter is 12 chars wide, period column is 4 chars wide (****)
    # 3 dots left of each letter/period, 3 dots right (except rightmost period)
    # Total = 3 + 12 + 3 + 4 + 3 + 12 + 3 + 4 + 3 + 12 + 3 + 4 = 66? 
    # Re-reading: 3 cols of periods left and right of each letter and period, except rightmost period
    # Looking at example output width of 60 chars:
    # ...MMMM....MMMM........DDDDDDDD............SSSSSSSSSS.....
    # Let's match the example pattern: 3 dots + letter(12) + dots + period(4) + dots + letter(12) + dots + period(4) + dots + letter(12) + dots + period(4)
    # From example: "...MMMM....MMMM........DDDDDDDD............SSSSSSSSSS....."
    # That's 3+12+8+8+12+8+10+5 = doesn't divide cleanly
    # Best approach: match exact example pattern for MDS and adapt to MAF

    # Large M rows (12 chars wide, made of M's and dots)
    M1  = "MMMM....MMMM"
    M2  = "MMMM....MMMM"
    M3  = "MM.MM..MM.MM"
    M4  = "MM.MM..MM.MM"
    M5  = "MM.MM..MM.MM"
    M6  = "MM..MMMM..MM"
    M7  = "MM..MMMM..MM"
    M8  = "MM...MM...MM"
    M9  = "MM...MM...MM" + "...**"
    M10 = "MM...MM...MM" + "...**"

    # Large A rows (12 chars wide, made of A's and dots)
    A1  = "....AAAA...."
    A2  = "...AAAAAA..."
    A3  = "..AA....AA.."
    A4  = "..AA....AA.."
    A5  = "..AAAAAAAA.."
    A6  = "..AAAAAAAA.."
    A7  = "..AA....AA.."
    A8  = "..AA....AA.."
    A9  = "..AA....AA.." + "...**"
    A10 = "..AA....AA.." + "...**"

    # Large F rows (12 chars wide, made of F's and dots)
    F1  = "FFFFFFFFFFFF"
    F2  = "FFFFFFFFFFFF"
    F3  = "FF.........."
    F4  = "FF.........."
    F5  = "FFFFFFFF...."
    F6  = "FFFFFFFF...."
    F7  = "FF.........."
    F8  = "FF.........."
    F9  = "FF.........." + "...**"
    F10 = "FF.........." + "...**"

    # Period column (4 chars, used between letters) - dots except last 2 rows
    P   = "...."
    Ps  = "****"  # last 2 rows period becomes ****

    # Separator dots between elements
    d3 = "..."
    d8 = "........"

    # Lines 1-8: ...M...P...A...P...F...P  but no trailing spaces, rightmost period dots only if not trailing
    print(d3 + M1 + d8 + P + d8 + A1 + d8 + P + d8 + F1 + d3 + P)
    print(d3 + M2 + d8 + P + d8 + A2 + d8 + P + d8 + F2 + d3 + P)
    print(d3 + M3 + d8 + P + d8 + A3 + d8 + P + d8 + F3 + d3 + P)
    print(d3 + M4 + d8 + P + d8 + A4 + d8 + P + d8 + F4 + d3 + P)
    print(d3 + M5 + d8 + P + d8 + A5 + d8 + P + d8 + F5 + d3 + P)
    print(d3 + M6 + d8 + P + d8 + A6 + d8 + P + d8 + F6 + d3 + P)
    print(d3 + M7 + d8 + P + d8 + A7 + d8 + P + d8 + F7 + d3 + P)
    print(d3 + M8 + d8 + P + d8 + A8 + d8 + P + d8 + F8 + d3 + P)
    print(d3 + M9  + d8 + Ps + d8 + A9  + d8 + Ps + d8 + F9  + d3 + Ps)
    print(d3 + M10 + d8 + Ps + d8 + A10 + d8 + Ps + d8 + F10 + d3 + Ps)

    print()


main()


