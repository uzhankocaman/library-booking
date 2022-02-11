from enum import Enum
from enum import auto


class course_id(Enum):
    BIB1_0800 = "BS_Kursid_181911"
    BIB1_1400 = "BS_Kursid_181912"
    BIB2_0800 = "BS_Kursid_181913"
    BIB2_1400 = "BS_Kursid_181914"
    UNIKLINIK = "BS_Kursid_181915"
    
class gender(Enum):
    M = auto()
    F = auto()
    D = auto()
    
class status(Enum):
    STUDENT_RWTH = "StudentIn der RWTH"
    STUDENT_FH = "StudentIn der FH"
    STUDENT_NRW = "StudentIn in NRW"
    STUDENT_OTHER = "StudentIn einer anderen Hochschule"
    AZUBI = "Azubi RWTH/UKA"
    SCHUELER = "Schüler"
    
    

    

