lijst = open("lijstopgave2.txt").read().split()

teller = 0
tteller = 0
antwoord1 = 0
antwoord2 = 0
aantal_deel_2 = 0
lengte_array = int(len(lijst) / 3)

while tteller < lengte_array:
    input = lijst[1 + teller]
    if input.__contains__:
        input = lijst[1 + teller].replace(":", "")
    checker = lijst[2 + teller]
    between = lijst[0 + teller].split("-")
    lo = int(between[0])
    hi = int(between[1])
    aantal_keer = checker.count(input)

    letter_1 = False
    if checker.find(input, lo - 1, lo) != -1:
        letter_1 = True

    letter_2 = False
    if checker.find(input, hi - 1, hi) != -1:
        letter_2 = True

    if letter_1 ^ letter_2 is True:
        antwoord2 += 1

    if lo <= aantal_keer <= hi:
        print(checker, input, lo, hi, aantal_keer)
        antwoord1 += 1

    tteller += 1
    teller += 3


print("aantal: juist via min x, max y: ", antwoord1)
print("aantal via deel 2: ", antwoord2)
