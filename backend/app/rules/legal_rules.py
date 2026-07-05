from app.schemas.rule import Rule, Severity

LEGAL_RULES = [

    Rule(
        name="Automatic Renewal",

        category="Automatic Renewal",

        severity=Severity.HIGH,

        explanation="This clause may automatically renew the agreement without requiring explicit confirmation.",

        patterns=[
            "automatic renewal",
            "automatically renew",
            "renew automatically",
            "auto renew",
            "renewal term"
        ],
    ),

    Rule(
        name="Data Sharing",

        category="Data Sharing",

        severity=Severity.MEDIUM,

        explanation="The agreement allows sharing personal information with third parties.",

        patterns=[
            "share your information",
            "third parties",
            "affiliates",
            "marketing partners",
            "data sharing"
        ],
    ),
]

