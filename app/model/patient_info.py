from pydantic import BaseModel


class PatientInfo(BaseModel):
    """
    A patient's info

    Stores all the necessary values for a fact to be delcared
    in a `CurtisEngine` instance in order to perform analysis
    and diagnosis on the given patient.
    """
    sex: int
    age: int
    height: float
    weight: float
    HR: float
    Pd: float
    PQ: float
    QRS: float
    QT: float
    QTcFra: float
