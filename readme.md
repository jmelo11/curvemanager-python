# CurveEngine

A simple curve bootstrapping tool. It uses ORE as backend and parses configuration files (see example below) and transform them into QL/ORE objects.


### Example
For a more detail example, visit the example folder.

´´´
{
    "refDate": "2023-02-14",
    "curves": [
        {
            "curveName": "SOFR",
            "curveConfig": {
                "curveType": "Piecewise",
                "dayCounter": "Actual360",
                "enableExtrapolation": true,
                "rateHelpers": [
                    {
                        "helperType": "Deposit",
                        "helperConfig": {
                            "dayCounter": "Actual360",
                            "tenor": "1D",
                            "calendar": "NullCalendar",
                            "settlementDays": 0,
                            "endOfMonth": false,
                            "convention": "Unadjusted"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.0455,
                                "ticker": "SOFRRATE CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "1W",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.045555000000000005,
                                "ticker": "USOSFR1Z CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "2W",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.045568,
                                "ticker": "USOSFR2Z CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "3W",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.045591999999999994,
                                "ticker": "USOSFR3Z CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "1M",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.04564,
                                "ticker": "USOSFRA CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "2M",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.046838,
                                "ticker": "USOSFRB CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "3M",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.047723,
                                "ticker": "USOSFRC CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "4M",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.048595,
                                "ticker": "USOSFRD CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "5M",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.049455,
                                "ticker": "USOSFRE CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "6M",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.050135,
                                "ticker": "USOSFRF CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "7M",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.050730000000000004,
                                "ticker": "USOSFRG CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "8M",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.051129,
                                "ticker": "USOSFRH CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "9M",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.051465,
                                "ticker": "USOSFRI CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "10M",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.051711,
                                "ticker": "USOSFRJ CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "11M",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.051815,
                                "ticker": "USOSFRK CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "12M",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.051856,
                                "ticker": "USOSFR1 CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "18M",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.049669,
                                "ticker": "USOSFR1F CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "2Y",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.046877,
                                "ticker": "USOSFR2 CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "3Y",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.042443,
                                "ticker": "USOSFR3 CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "4Y",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.039656,
                                "ticker": "USOSFR4 CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "5Y",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.037866,
                                "ticker": "USOSFR5 CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "6Y",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.036718,
                                "ticker": "USOSFR6 CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "7Y",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.035910000000000004,
                                "ticker": "USOSFR7 CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "8Y",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.035323,
                                "ticker": "USOSFR8 CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "9Y",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.03492,
                                "ticker": "USOSFR9 CURNCY"
                            }
                        }
                    },
                    {
                        "helperType": "OIS",
                        "helperConfig": {
                            "tenor": "10Y",
                            "dayCounter": "Actual360",
                            "calendar": "NullCalendar",
                            "convention": "Following",
                            "endOfMonth": true,
                            "frequency": "Annual",
                            "settlementDays": 2,
                            "paymentLag": 2,
                            "telescopicValueDates": true,
                            "index": "SOFR",
                            "fixedLegFrequency": "Semiannual",
                            "fwdStart": "0D"
                        },
                        "marketConfig": {
                            "rate": {
                                "value": 0.03464,
                                "ticker": "USOSFR10 CURNCY"
                            }
                        }
                    }
                ]
            },
            "curveIndex": {
                "indexType": "OvernightIndex",
                "tenor": "1D",
                "dayCounter": "Actual360",
                "currency": "USD",
                "fixingDays": 0,
                "calendar": "NullCalendar",
                "endOfMonth": false,
                "convention": "Unadjusted"
            }
        }
    ]
}
´´´