from src.constants import REQUIRED_FIELDS


class ClaimValidator:
    """
    Validates extracted claim information.
    """

    def validate(self, extracted_fields):

        missing_fields = []
        inconsistent_fields = []

        # ----------------------------
        # Check for missing fields
        # ----------------------------
        for field in REQUIRED_FIELDS:

            value = extracted_fields.get(field)

            if value is None or str(value).strip() == "":
                missing_fields.append(field)

        # ----------------------------
        # Numeric Validation
        # ----------------------------

        numeric_fields = [
            "Estimated Damage",
            "Initial Estimate"
        ]

        for field in numeric_fields:

            value = extracted_fields.get(field)

            if value is None:
                continue

            try:
                int(str(value).replace(",", "").strip())

            except ValueError:

                inconsistent_fields.append(
                    f"{field} should be numeric"
                )

        return {
            "missing_fields": missing_fields,
            "inconsistent_fields": inconsistent_fields
        }