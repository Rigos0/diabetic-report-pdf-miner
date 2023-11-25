# zlatokop descriptions
VELMI_VYSOKA = "velmi vysoká"
VYSOKA = "vysoká"
CILOVE = "v cílovém rozmezí"
NIZKA = "nízká"
VELMI_NIZKA = "velmi nízká"

PRUMERNA_GLUKOZA = "průměrná glukóza"
GLUKOZA_S_ODCHYLKA = "glukóza - směrodatná odchylka"
GMI = "GMI"
GLUKOZA_K_VARIACE = "glukóza - koeficient variace"
CDDI = "celková denní dávka inzulinu (CDDI)"
BOLUS = "denní dávka inzulinu - bolus"
BAZAL = "denní dávka inzulinu - bazal"
DOBA_AKTIV_INZULINU = "odhadovaná doba aktivního inzulinu"
PRUMERNY_SACHAR_POMER = "průměrný sacharidový poměr (SP)"
PRUMERNA_CITLIVOST_INZULIN = "průměrná citlivost na inzulin (CI)"

ORDER = [VELMI_VYSOKA, VYSOKA, CILOVE, NIZKA, VELMI_NIZKA, PRUMERNA_GLUKOZA, GLUKOZA_K_VARIACE,
         GLUKOZA_S_ODCHYLKA, CDDI, BAZAL, BOLUS, PRUMERNY_SACHAR_POMER, PRUMERNA_CITLIVOST_INZULIN]

SACHARIDOVA_KONSTANTA = 350
INZULIN_KONSTANTA = 110

# regex patterns:

CONTAINS_PERCENTAGE_SIGN = r'%'
CONTAINS_JEDN = r'jedn'
CONTAINS_PLUSMINUS_SIGN = r'±'
CONTAINS_LETTER_H_AND_DOUBLE_DOT = r'(?=.*h)(?=.*:)'
