import re
from functools import partial
from parsing.enums import *

'''
Example of a basic structure of the curve request:
{
    "refDate": "2020-01-01",
    "curves": [
        {
            "curveName": "PiecewiseCurveExample",
            "curveConfig": {
                "curveType": "Piecewise",                
                "dayCounter": "Actual360",
                "enableExtrapolation": True,
                "rateHelpers": [
                    {                        
                        "helperConfig": {
                            ...
                        },
                        "marketConfig": {
                            ...
                        },
                    }
                ]
            },
            "curveIndex":{
                ...
            }
        },
        {
            "curveName": "DiscountCurveExample",
            "curveConfig": {
                "curveType": "Discount",
                "dayCounter": "Actual360",
                "enableExtrapolation": True,
                "nodes": [
                    {
                        "date": "2020-01-01",
                        "discount": 0.01
                    },
                    {
                        "date": "2020-02-01",
                        "discount": 0.02
                    }
                ]
            },
            "curveIndex":{
                ...
            }
        }
    ]
}
'''


class ConfigurationError(Exception):
    '''
    Exception raised when the request is invalid
    '''

    def __init__(self, message):
        self.message = message


class RateIndexError(ConfigurationError):
    '''
    Exception raised when the index is invalid
    '''

    def __init__(self, message):
        self.message = message


class RateHelperConfigurationError(ConfigurationError):
    '''
    Exception raised when the rate helper is invalid
    '''

    def __init__(self, message):
        self.message = message


class MarketConfigurationError(ConfigurationError):
    '''
    Exception raised when the market configuration is invalid
    '''

    def __init__(self, message):
        self.message = message


## Check available enums and possible instances#


def checkDate(value) -> None:
    '''
    Check if the date is valid

    Parameters
    ----------
    value: str
        The date

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If the date is invalid
    '''
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', value):
        raise ValueError(f'{value} is not a valid date')


def checkIsInEnum(value: str, enum: list) -> None:
    '''
    Check if the value is in the enum

    Parameters
    ----------
    value: str
        The value to check
    enum: list
        The enum

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If the value is not in the enum
    '''
    if value not in enum:
        raise ValueError(f'{value} is not in {enum}')


def checkDayCounter(value) -> None:
    '''
    Check if the day counter is valid

    Parameters
    ----------
    value: str
        The day counter. It can be Actual360, Actual365 or Thirty360

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If the day counter is invalid
    '''
    checkIsInEnum(value, ["Actual360", "Actual365", "Thirty360"])


def checkFrequency(value) -> None:
    '''
    Check if the frequency is valid

    Parameters
    ----------
    value: str
        The frequency, it can be Annual, Semiannual, Quarterly, Monthly, Weekly, Daily or Once.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If the frequency is invalid
    '''
    checkIsInEnum(value, ["Annual", "Semiannual",
                  "Quarterly", "Monthly", "Weekly", "Daily", "Once"])


def checkCompounding(value) -> None:
    '''
    Check if the compounding is valid

    Parameters
    ----------
    value: str
        The compounding, it can be Simple, Compounded, Continuous or SimpleThenCompounded.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If the compounding is invalid
    '''
    checkIsInEnum(value, ["Simple", "Compounded",
                  "Continuous", "SimpleThenCompounded"])


def checkConvention(value) -> None:
    '''
    Check if the convention is valid

    Parameters
    ----------
    value: str
        The convention, it can be ModifiedFollowing, Following, ModifiedPreceding, Preceding or Unadjusted.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If the convention is invalid
    '''
    checkIsInEnum(value, ["ModifiedFollowing", "Following",
                  "ModifiedPreceding", "Preceding", "Unadjusted"])


def checkCalendar(value) -> None:
    '''
    Check if the calendar is valid

    Parameters
    ----------
    value: str
        The calendar, it can be UnitedStates, Chile, TARGET, Brazil or NullCalendar.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If the calendar is invalid
    '''
    checkIsInEnum(value, ["UnitedStates", "Chile",
                  "TARGET", "Brazil", "NullCalendar"])


def checkCurrency(value) -> None:
    '''
    Check if the currency is valid

    Parameters
    ----------
    value: str
        The currency, it can be USD, CLP, EUR, BRL, COP, MXN or CLF.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If the currency is invalid
    '''
    checkIsInEnum(value, ["USD", "CLP", "EUR", "BRL", "COP", "MXN", "CLF"])


def checkTenor(tenor: str) -> None:
    '''
    Check if the tenor is valid

    Parameters
    ----------
    tenor: str
        The tenor, it can be a number followed by D, W, M or Y

    Returns
    -------
    None

    Raises
    ------
    ConfigurationError
        If the tenor is invalid
    '''
    regex = r'^\d+[DWMY]$'
    if not re.match(regex, tenor):
        raise ValueError(f'The tenor {tenor} is invalid')


def checkDictStructure(input: dict, reference: dict) -> None:
    for key in reference.keys():
        if key not in input.keys():
            raise KeyError(
                f'The required key "{key}" is missing.')
    for key in input.keys():
        if key in reference.keys():
            reference[key](input[key])


def checkInstance(value: any, type: type) -> None:
    '''
    Check if the value is an instance of the type

    Parameters
    ----------
    value: any
        The value to check
    type: type
        The type to check

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If the value is not an instance of the type
    '''

    if not isinstance(value, type):
        raise ValueError(f'The value {value} is not an instance of {type}.')


## Rate helpers checks ##

def checkOISRateHelper(data: dict) -> None:
    '''
    Check if the OIS rate helper is valid

    Parameters
    ----------
    data: dict
        The OIS rate helper

    Returns
    -------
    None

    Raises
    ------
    RateHelperConfigurationError
        If the rate helper is invalid

    Details
    -------
    The OIS rate helper should have the following example structure:
    ```
    "helperConfig": {
                        "tenor": "1W",
                        "dayCounter": "Actual360",
                        "calendar": "NullCalendar",
                        "convention": "Following",
                        "endOfMonth": True,
                        "frequency": "Annual",
                        "settlementDays": 2,
                        "paymentLag": 2,
                        "telescopicValueDates": True,
                        "index": "SOFR",
                        "fixedLegFrequency": "Semiannual",
                        "fwdStart": "0D"
                    }
    ```
    '''

    reference = {
        "tenor": checkTenor,
        "dayCounter": checkDayCounter,
        "calendar": checkCalendar,
        "convention": checkConvention,
        "endOfMonth": partial(checkInstance, type=bool),
        "frequency": checkFrequency,
        "settlementDays": partial(checkInstance, type=int),
        "paymentLag": partial(checkInstance, type=int),
        "telescopicValueDates": partial(checkInstance, type=bool),
        "index": partial(checkInstance, type=str),
        "fixedLegFrequency": checkFrequency,
        "fwdStart": checkTenor
    }
    try:
        checkDictStructure(data, reference)
    except Exception as exc:
        raise RateHelperConfigurationError('Invalid OIS rate helper') from exc


def checkDepositRateHelper(data: dict) -> None:
    '''
    Check if the deposit rate helper is valid

    Parameters
    ----------
    data: dict
        The deposit rate helper

    Returns
    -------
    None

    Raises
    ------
    RateHelperConfigurationError
        If the rate helper is invalid

    Details
    -------
    The deposit rate helper should have the following example structure:
    ```
    "helperConfig": {
                    "dayCounter": "Actual360",
                    "tenor": "1D",
                    "calendar": "NullCalendar",
                    "settlementDays": 0,
                    "endOfMonth": False,
                    "convention": "Unadjusted"
                }
    ```
    '''
    reference = {
        "dayCounter": checkDayCounter,
        "tenor": checkTenor,
        "calendar": checkCalendar,
        "settlementDays": partial(checkInstance, type=int),
        "endOfMonth": partial(checkInstance, type=bool),
        "convention": checkConvention
    }
    try:
        checkDictStructure(data, reference)
    except Exception as exc:
        raise RateHelperConfigurationError(
            'Invalid deposit rate helper') from exc


def checkSwapRateHelper(data: dict) -> None:
    '''
    Check if the swap rate helper is valid

    Parameters
    ----------
    data: dict
        The swap rate helper

    Returns
    -------
    None

    Raises
    ------
    RateHelperConfigurationError
        If the rate helper is invalid

    Details
    -------
    The swap rate helper should have the following example structure:
    ```
    "helperConfig": {
                    "tenor": "2Y",
                    "dayCounter": "Thirty360",
                    "calendar": "NullCalendar",
                    "frequency": "Semiannual",
                    "settlementDays": 2,
                    "discountCurve": "SOFR",
                    "index": "LIBOR3M",
                    "endOfMonth": False,
                    "convention": "Unadjusted",
                    "fixedLegFrequency": "Semiannual",
                    "fwdStart": "0D"
                }
    ```
    '''
    reference = {
        "tenor": checkTenor,
        "dayCounter": checkDayCounter,
        "calendar": checkCalendar,
        "frequency": checkFrequency,
        "settlementDays": partial(checkInstance, type=int),
        "discountCurve": partial(checkInstance, type=str),
        "index": partial(checkInstance, type=str),
        "endOfMonth": partial(checkInstance, type=bool),
        "convention": checkConvention,
        "fixedLegFrequency": checkFrequency,
        "fwdStart": checkTenor
    }
    try:
        checkDictStructure(data, reference)
    except Exception as exc:
        raise RateHelperConfigurationError('Invalid swap rate helper') from exc


def checkFixedRateBondRateHelper(data: dict) -> None:
    '''
    Check if the bond rate helper is valid

    Parameters
    ----------
    data: dict
        The bond rate helper

    Returns
    -------
    None

    Raises
    ------
    RateHelperConfigurationError
        If the rate helper is invalid

    Details
    -------
    The bond rate helper should have the following example structure:
    ```
    "helperConfig": {
                    "calendar": "NullCalendar",
                    "convention": "Following",
                    "settlementDays": 2,
                    "couponDayCounter": "Actual360",
                    "couponRate": 0.05,
                    "frequency": "Annual",
                    "startDate": "2020-01-01",
                    "endDate": "2022-01-01",
                    "tenor": "2Y" # needed if start date and end date are not provided
                }
    ```
    '''
    reference = {
        "calendar": checkCalendar,
        "convention": checkConvention,
        "settlementDays": partial(checkInstance, type=int),
        "couponDayCounter": checkDayCounter,
        "couponRate": partial(checkInstance, type=float),
        "frequency": checkFrequency,
    }

    # check if the start date and end date are provided
    if "startDate" in data or "endDate" in data:
        reference["startDate"] = checkDate
        reference["endDate"] = checkDate
    else:
        reference["tenor"] = checkTenor

    try:
        checkDictStructure(data, reference)
    except Exception as exc:
        raise RateHelperConfigurationError('Invalid bond rate helper') from exc


def checkFxSwapRateHelper(data: dict) -> None:
    '''
    Check if the FX swap rate helper is valid

    Parameters
    ----------
    data: dict
        The FX swap rate helper

    Returns
    -------
    None

    Raises
    ------
    RateHelperConfigurationError
        If the rate helper is invalid

    Details
    -------
    The FX swap rate helper should have the following example structure:
    ```
    "helperConfig": {
                        "calendar": "NullCalendar",
                        "fixingDays": 0,
                        "endOfMonth": False,
                        "baseCurrencyAsCollateral": False,
                        "convention": "Following",
                        "discountCurve": "CLP_COLLUSD",                       
                        "endDate": "2023-04-09",
                        "tenor": "1Y", # need if no end date is provided
                        "settlementDays": 0
                    }
    ```
    '''

    reference = {
        "calendar": checkCalendar,
        "fixingDays": partial(checkInstance, type=int),
        "endOfMonth": partial(checkInstance, type=bool),
        "baseCurrencyAsCollateral": partial(checkInstance, type=bool),
        "convention": checkConvention,
        "discountCurve": partial(checkInstance, type=str),
        "settlementDays": partial(checkInstance, type=int)
    }

    # check if the end date is provided
    if "endDate" in data:
        reference["endDate"] = checkDate
    else:
        reference["tenor"] = checkTenor

    try:
        checkDictStructure(data, reference)
    except Exception as exc:
        raise RateHelperConfigurationError(
            'Invalid FX swap rate helper') from exc


def checkCrossCcyFixFloatSwapHelperHelper(data: dict) -> None:
    '''
    Check if the cross currency rate helper is valid

    Parameters
    ----------
    data: dict
        The cross currency rate helper

    Returns
    -------
    None
        no return, raise RateHelperConfigurationError if the request is invalid

    Raises
    ------
    RateHelperConfigurationError
        If the rate helper is invalid

    Details
    -------
    The cross currency rate helper should have the following example structure:
    ```
    "helperConfig":  {
                    "tenor": "2Y",
                    "dayCounter": "Actual360",
                    "calendar": "NullCalendar",
                    "convention": "ModifiedFollowing",
                    "endOfMonth": False,
                    "settlementDays": 2,
                    "discountCurve": "CLP_COLLUSD",
                    "index": "ICP",
                    "fixedLegCurrency": "CLF",
                    "fwdStart": "0D",
                    "fixedLegFrequency": "Semiannual"
                }
    ```
    '''

    reference = {
        "tenor": checkTenor,
        "dayCounter": checkDayCounter,
        "calendar": checkCalendar,
        "convention": checkConvention,
        "endOfMonth": partial(checkInstance, type=bool),
        "settlementDays": partial(checkInstance, type=int),
        "discountCurve": partial(checkInstance, type=str),
        "index": partial(checkInstance, type=str),
        "fixedLegCurrency": partial(checkInstance, type=str),
        "fwdStart": checkTenor,
        "fixedLegFrequency": checkFrequency
    }

    try:
        checkDictStructure(data, reference)
    except Exception as exc:
        raise RateHelperConfigurationError(
            'Invalid cross currency rate helper') from exc


def checkTenorBasisRateHelper(data: dict) -> None:
    '''
    Check if the tenor basis rate helper is valid

    Parameters
    ----------
    data: dict
        The tenor basis rate helper

    Returns
    -------
    None

    Raises
    ------
    RateHelperConfigurationError
        If the rate helper is invalid

    Details
    -------
    The tenor basis rate helper should have the following example structure:
    ```
    "helperConfig": {
                    "tenor": "3M",
                    "longIndex": "LIBOR3M",
                    "shortIndex": "LIBOR1M",
                    "discountCurve": "SOFR",
                    "spreadOnShort": True
                }
    ```
    '''

    reference = {
        "tenor": checkTenor,
        "longIndex": partial(checkInstance, type=str),
        "shortIndex": partial(checkInstance, type=str),
        "discountCurve": partial(checkInstance, type=str),
        "spreadOnShort": partial(checkInstance, type=bool)
    }

    try:
        checkDictStructure(data, reference)
    except Exception as exc:
        raise RateHelperConfigurationError(
            'Invalid tenor basis rate helper') from exc


def checkCrossCcyBasisSwapRateHelper(data: dict) -> None:
    '''
    Check if the cross currency basis rate helper is valid

    Parameters
    ----------
    data: dict
        The cross currency basis rate helper

    Returns
    -------
    None

    Raises
    ------
    RateHelperConfigurationError
        If the rate helper is invalid

    Details
    -------
    The cross currency basis rate helper should have the following example structure:
    ```
    "helperConfig": {
                    "tenor": "3M",
                    "calendar": "NullCalendar",
                    "settlementDays": 2,
                    "endOfMonth": False,
                    "convention": "ModifiedFollowing",
                    "flatIndex": "LIBOR3M",
                    "spreadIndex": "LIBOR1M",
                    "discountCurve": "SOFR"
                }
    ```
    '''

    reference = {
        "tenor": checkTenor,
        "calendar": checkCalendar,
        "settlementDays": partial(checkInstance, type=int),
        "endOfMonth": partial(checkInstance, type=bool),
        "convention": checkConvention,
        "flatIndex": partial(checkInstance, type=str),
        "spreadIndex": partial(checkInstance, type=str),
        "discountCurve": partial(checkInstance, type=str),
    }

    try:
        checkDictStructure(data, reference)
    except Exception as exc:
        raise RateHelperConfigurationError(
            'Invalid cross currency basis rate helper') from exc


def checkMarketConfig(data: dict, helperType: HelperType) -> None:
    '''
    Check if the market config is valid

    Parameters
    ----------
    data: dict
        The market config

    Returns
    -------
    None

    Raises
    ------
    ConfigurationError
        If the market config is invalid

    Details
    -------
    The market config should have the following example structure:
    ```
    "marketConfig": {
                        "rate": {
                            "ticker" : "CLP_CU",
                            "value" : 0.01
                        },
                        "spread": {
                            "ticker" : "CLP_CU",
                            "value" : 0.01
                        },
                        "fxSpot": {
                            "ticker" : "CLP_CU",
                            "value" : 0.01
                        },
                        "fxPoints": {
                            "ticker" : "CLP_CU",
                            "value" : 0.01
                        }
                    }
    ```

    Where each field has at least a value. The ticker is optional.    
    Each field is dependent on the helper type. The following table shows the required fields for each helper type:

    |Helper type             | Required fields                  |
    |----------------------- | ---------------------------------|
    |Deposit                 | rate                             |
    |Swap                    | rate, spread                     |    
    |FxSwap                  | fxSpot, fxPoints                 |    
    |Xccy                    | rate, spread, fxSpot, fxPoints   |
    |TenorBasis              | spread                           |
    |XccyBasis               | spread, fxSpot, fxPoints         |
    |OIS                     | spread                           |
    |Bond                    | rate                             |
    '''

    def checkPrice(data: dict) -> None:
        if not isinstance(data, dict):
            raise ConfigurationError(
                'Invalid price, should be a dictionary')
        if 'value' not in data:
            raise ConfigurationError(
                'Invalid price, missing value')
        if not isinstance(data['value'], float):
            raise ConfigurationError(
                'Invalid price, value should be a float')
        if 'ticker' in data and not isinstance(data['ticker'], str):
            raise ConfigurationError(
                'Invalid price, ticker should be a string')

    reference = {}
    if helperType == HelperType.Deposit:
        reference = {
            "rate": checkPrice
        }
    elif helperType == HelperType.Swap:
        reference = {
            "rate": checkPrice,
            "spread": checkPrice
        }
    elif helperType == HelperType.FxSwap:
        reference = {
            "fxSpot": checkPrice,
            "fxPoints": checkPrice
        }
    elif helperType == HelperType.Xccy:
        reference = {
            "rate": checkPrice,
            "spread": checkPrice,
            "fxSpot": checkPrice,
            "fxPoints": checkPrice
        }
    elif helperType == HelperType.TenorBasis:
        reference = {
            "spread": checkPrice
        }
    elif helperType == HelperType.XccyBasis:
        reference = {
            "spread": checkPrice,
            "fxSpot": checkPrice,
            "fxPoints": checkPrice
        }
    elif helperType == HelperType.OIS:
        reference = {
            "spread": checkPrice
        }
    elif helperType == HelperType.Bond:
        reference = {
            "rate": checkPrice
        }
    else:
        raise ConfigurationError('Invalid helper type')

    try:
        checkDictStructure(data, reference)
    except Exception as exc:
        raise ConfigurationError(
            'Invalid market config') from exc


def checkRateHelper(data: dict) -> None:
    '''
    Check if the rate helper is valid

    Parameters
    ----------
    data: dict
        The rate helper

    Returns
    -------
    None

    Raises
    ------
    RateHelperConfigurationError
        If the rate helper is invalid

    Details
    -------
    The rate helper should have the following example structure:
    ```
    "rateHelper": {
                        "helperType": "OIS",
                        "helperConfig": {
                           ...
                        },
                        "marketConfig": {
                            ...
                        }
                    }
    ```
    '''

    reference = {
        "helperType": partial(checkIsInEnum, enum=[r.value for r in HelperType]),
    }
    try:
        checkDictStructure(data, reference)
    except Exception as exc:
        raise ConfigurationError(
            'Invalid rate helper configuration or helper type') from exc

    helperType = HelperType[data['helperType']]

    reference["marketConfig"] = partial(
        checkMarketConfig, helperType=helperType)
    if helperType == HelperType.Deposit:
        reference["helperConfig"] = checkDepositRateHelper
    elif helperType == HelperType.Swap:
        reference["helperConfig"] = checkSwapRateHelper
    elif helperType == HelperType.FxSwap:
        reference["helperConfig"] = checkFxSwapRateHelper
    elif helperType == HelperType.Xccy:
        reference["helperConfig"] = checkCrossCcyFixFloatSwapHelperHelper
    elif helperType == HelperType.TenorBasis:
        reference["helperConfig"] = checkTenorBasisRateHelper
    elif helperType == HelperType.XccyBasis:
        reference["helperConfig"] = checkCrossCcyBasisSwapRateHelper
    elif helperType == HelperType.OIS:
        reference["helperConfig"] = checkOISRateHelper
    elif helperType == HelperType.Bond:
        reference["helperConfig"] = checkFixedRateBondRateHelper

    try:
        checkDictStructure(data, reference)
    except Exception as exc:
        raise ConfigurationError('Invalid rate helper configuration') from exc


## Index checks ##


def checkIndex(data: dict) -> None:
    '''
    Check if the index is valid

    Parameters
    ----------
    data: dict
        The index

    Returns
    -------
    None

    Raises
    ------
    RateIndexError
        If the index is invalid

    Details
    -------
    The index should have the following example structure:
    ```
    "curveIndex": {
                "indexType": "IborIndex",
                "tenor": "6M",
                "dayCounter": "Actual360",
                "currency": "CLP",
                "fixingDays": 0,
                "calendar": "NullCalendar",
                "endOfMonth": False,
                "convention": "Unadjusted"
            }
    ```
    '''

    reference = {
        "indexType": partial(checkIsInEnum, enum=IndexType),
        "tenor": checkTenor,
        "dayCounter": checkDayCounter,
        "currency": checkCurrency,
        "fixingDays": partial(checkInstance, type=int),
        "calendar": checkCalendar,
        "endOfMonth": partial(checkInstance, type=bool),
        "convention": checkConvention
    }

    try:
        checkDictStructure(data, reference)
    except Exception as exc:
        raise RateIndexError('Invalid index configuration') from exc


## Curve checks ##

def checkPiecewiseCurve(data: dict) -> None:
    '''
    Check if the piecewise curve is valid

    Parameters
    ----------
    data: dict
        The piecewise curve

    Returns
    -------
    None

    Raises
    ------
    InvalidCurve
        If the curve is invalid

    Details
    -------
    The piecewise curve should have the following example structure:

    ```
    "example": {
            "curveType": "Piecewise",
            "dayCounter": "Actual360",
            "enableExtrapolation": True,
            "rateHelpers": [
                ...
            ]
        }
    ```
    '''
    def checkRateHelperList(l: list) -> None:
        checkInstance(l, type=list)
        if len(l) == 0:
            raise ConfigurationError(
                'Invalid piecewise curve configuration, rateHelpers should not be empty')
        for helper in l:
            checkRateHelper(helper)

    reference = {
        "curveType": partial(checkIsInEnum, enum=[r.value for r in CurveType]),
        "dayCounter": checkDayCounter,
        "enableExtrapolation": partial(checkInstance, type=bool),
        "rateHelpers": checkRateHelperList
    }

    try:
        checkDictStructure(data, reference)
    except Exception as exc:
        raise ConfigurationError(
            'Invalid piecewise curve configuration') from exc


def checkDiscountCurve(data: dict) -> None:
    '''
    Check if the discount curve is valid

    Parameters
    ----------
    data: dict
        The discount curve

    Returns
    -------
    None

    Raises
    ------
    InvalidCurve
        If the curve is invalid

    Details
    -------
    The discount curve should have the following example structure:

    ```
    "example": {
            "curveType": "Discount",
            "dayCounter": "Actual360",
            "enableExtrapolation": True,
            "nodes": [
                {
                    "date": "2020-01-01",
                    "value": 0.99
                }
            ]
        }
    ```
    '''
    def checkNodeList(l: list) -> None:
        ref = {
            "date": checkDate,
            "value": partial(checkInstance, type=float)
        }
        checkInstance(l, type=list)
        if len(l) == 0:
            raise ConfigurationError(
                'Invalid discount curve configuration, discountFactors should not be empty')
        for node in l:
            checkDictStructure(node, ref)

    reference = {
        "curveType": partial(checkIsInEnum, enum=[r.value for r in CurveType]),
        "dayCounter": checkDayCounter,
        "enableExtrapolation": partial(checkInstance, type=bool),
        "discountFactors": checkNodeList
    }

    try:
        checkDictStructure(data, reference)
    except Exception as exc:
        raise ConfigurationError(
            'Invalid discount curve configuration') from exc