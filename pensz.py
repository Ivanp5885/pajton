while True:
    print("penzugyi program")
    balance = int(input("cippi+===????"))
    balanceHist = balance
    print("kiadasok?????ghjkl")
    kiadas = {"kaja": 0, "pia": 0, "kutya": 0, "indukciosFozolap": 0}
    log = []
    while True:
        x = int(input("szam [99 <- break]"))
        if (x == 99):
            break
        else:
            print("[str] valaszd ki a kategoriat:\n1. kaja\n2. pia\n3. kutya\n 4. indukcios fozolap")
            kiadas[str("{}".format(input()))] += x
            log.append(x)
            if x > 50000:
                print("teso szallj le az egekbol lassaban picit")
    print(kiadas)
    print(str(kiadas["kaja"] + kiadas["pia"] + kiadas["kutya"] + kiadas["indukciosFozolap"]) + str(
        " teso sokat koltesz nm keresel orvosold"))
    balance -= kiadas["kaja"] + kiadas["pia"] + kiadas["kutya"] + kiadas["indukciosFozolap"]
    print(str(balance) + " mennyisegu cippid van komam")
    verybig = 0
    for i in range(int(len(log))):
        if log[i] > verybig:
            verybig = log[i]
    print("te komoly koltottel " + str(verybig) + " et egyszerre teso ehenhalsz..")
    print("pensz arany=" + str((balance / balanceHist) * 100))
    if input("gonext (barmi)/reset (99)?" + "//////amugy mind2 ugyanazt csin") == 99:
        kiadas = {"kaja": 0, "pia": 0, "kutya": 0, "indukciosFozolap": 0}
