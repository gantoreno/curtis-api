from curtis import CurtisEngine, CurtisFacts
from curtis.exceptions import CurtisParameterError
from curtis.utils.encoding import diagnosis_indexes

from fastapi import APIRouter, Response, status, HTTPException

from ..model.patient_info import PatientInfo

router = APIRouter()


@router.post('/api/diagnose', status_code=status.HTTP_200_OK)
async def diagnose(patient_info: PatientInfo, response: Response):
    """
    Perform a diagnosis

    Receive data as a `PatientInfo` object which contains all the
    necessary data for the engine to infer a diagnostic on the
    given values.

    Parameters
    ----------
    :param patient_info: The patient's information & ECG values

    Returns
    -------
    :return: A diagnosis for the given values
    """
    try:
        curtis = CurtisEngine()

        curtis.declare_facts(
            CurtisFacts(
                sex=patient_info.sex,
                age=patient_info.age,
                height=patient_info.height,
                weight=patient_info.weight,
                HR=patient_info.HR,
                Pd=patient_info.Pd,
                PQ=patient_info.PQ,
                QRS=patient_info.QRS,
                QT=patient_info.QT,
                QTcFra=patient_info.QTcFra
            )
        )

        diagnosis = curtis.diagnose()

        return diagnosis_indexes[diagnosis]
    except CurtisParameterError as e:
        raise HTTPException(status_code=400, detail=str(e))
