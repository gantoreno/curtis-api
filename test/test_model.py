from app.model.patient_info import PatientInfo


def test_patient_info():
    """ Should correctly instantiate a patient's info. """
    patient_info = PatientInfo(**{
        "sex": 0,
        "age": 31,
        "height": 170.0,
        "weight": 100.0,
        "HR": 82.0,
        "Pd": 106.0,
        "PQ": 138.0,
        "QRS": 88.0,
        "QT": 350.0,
        "QTcFra": 392.0
    })

    assert isinstance(patient_info, PatientInfo)
