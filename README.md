Przyjmijmy uproszczony model dysponowania jednostek Państwowej Straży Pożarnej na obszarze miasta Krakowa.
Pod nadzorem Stanowiska Kierowania Komendanta Miejskiego w Krakowie (SKKM) znajduje się siedem ponumerowanych jednostek ratowniczo-gaśniczych (JRG-1:JRG-7), JRG Szkoły Aspirantów PSP, JRG Skawina oraz LSP Lotniska w Balicach. 
Dla uproszczenia modelu problemu przyjmijmy, że każda jednostka posiada 5 samochodów, które mogą być dysponowane do zdarzeń, niezależnie od ich charakteru.

Do SKKM co jakiś czas drogą telefoniczną napływają zgłoszenia różnych zdarzeń takich jak:
-pożary (PZ),
-alarmy fałszywe (AF),
-inne miejscowe zagrożenia (MZ).

70 procent zgłoszeń dotyczy miejscowych zagrożeń, a 30 procent pożarów. 
Na potrzeby tego modelu przyjmijmy, że dowolne zdarzenie charakteryzuje się rodzajem (PZ, AF, MZ) oraz jego położeniem (współrzędne geograficzne w stopniach dziesiętnych układu WGS-84).

SKKM powiadamia o zdarzeniu jednostki jej podległe o zaistnieniu zdarzenia. 
W przypadku charakteru PZ wyjeżdżają trzy samochody, a MZ dwa (z jednostki znajdującej się najbliżej miejsca zdarzenia). 
W momencie wyjazdu do zdarzenia samochody zmieniają swój stan z wolnego na zajęty, do momentu zakończenia działań i powrotu do jednostki macierzystej. 
Tylko samochody w stanie wolnym mogą zostać zadysponowane do zdarzenia. W momencie, w którym w najbliższej miejscu zdarzenia jednostce braknie wolnych pojazdów, dysponowane są te z kolejnych najbliższych jednostek.

Po dojeździe na miejsce zdarzenia (losowy czas 0-3 s) zdarzenie może okazać się alarmem fałszywym (prawdopodobieństwo 5 procent). 
W sytuacji alarmu fałszywego samochody automatycznie powracają do swoich jednostek (losowy czas dojazdu 0-3 s). 
W przypadku przeciwnym, podejmują działania, które trwają losowy czas w przedziale (5-25 s), po czym wracają do swoich jednostek (losowy czas dojazdu 0-3 s). 
Po powrocie ich stan ustawiany jest na wolny.
