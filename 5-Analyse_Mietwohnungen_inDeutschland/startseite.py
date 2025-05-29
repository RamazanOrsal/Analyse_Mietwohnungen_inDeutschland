import data_proje as dt


while True:
    wahl=input('1-Zeige die Gesamtzahl der Mietwohnungen nach Bundesland\n2-Zeige die durchschnittliche Miete nach Bundesland. \n3-Zeige die durchschnittliche Miete nach Merkmalen\n4-Zeige die Zahl der Mietwohnungen\n5-Zeige die Miete nach Wohnfläche und Zeige Durchschnittlicher m²-Preis nach Bundesland\n6-Zeige die Verteilung der Wohnungen nach Heizungsart\n7-Beenden\nAuswahl: ')

    if wahl=='7':
        break
    else:
        if wahl=='1':
            dt.gesamtzahlnachBundesland()

        elif wahl=='2':
            dt.durchschinitlichMietnachBundesland()

        elif wahl=='3':
            dt.durchschinttlichMietenachMerkmale()


        elif wahl=='4':
            dt.zahlderMietwohnung()

        elif wahl=='5':
            dt.mietenachLivingspace()

        elif wahl=='6':
            dt.heatingtypePieplot()


        else:
            print('Sie haben eine falsche Taste eingegeben. Bitte geben Sie sie noch einmal ein.')
