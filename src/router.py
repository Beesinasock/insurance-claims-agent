class ClaimRouter:

    def determine_route(
        self,
        extracted_fields,
        validation_result
    ):

        description = (
            extracted_fields.get("Description") or ""
        ).lower()

        claim_type = (
            extracted_fields.get("Claim Type") or ""
        ).lower()

        damage = extracted_fields.get(
            "Estimated Damage"
        )

        missing_fields = validation_result[
            "missing_fields"
        ]

        # ----------------------------------
        # Rule 1 - Investigation
        # ----------------------------------

        fraud_keywords = [
            "fraud",
            "staged",
            "inconsistent"
        ]

        if any(
            word in description
            for word in fraud_keywords
        ):

            return {
                "recommendedRoute":
                    "Investigation Flag",

                "reasoning":
                    "Description contains potential fraud indicators."
            }

        # ----------------------------------
        # Rule 2 - Manual Review
        # ----------------------------------

        if missing_fields:

            return {
                "recommendedRoute":
                    "Manual Review",

                "reasoning":
                    "Mandatory fields are missing."
            }

        # ----------------------------------
        # Rule 3 - Specialist Queue
        # ----------------------------------

        if claim_type == "injury":

            return {
                "recommendedRoute":
                    "Specialist Queue",

                "reasoning":
                    "Claim type is Injury."
            }

        # ----------------------------------
        # Rule 4 - Fast Track
        # ----------------------------------

        try:

            if int(damage) < 25000:

                return {
                    "recommendedRoute":
                        "Fast-track",

                    "reasoning":
                        "Estimated damage is below ₹25,000."
                }

        except:

            pass

        # ----------------------------------
        # Default
        # ----------------------------------

        return {
            "recommendedRoute":
                "Normal Processing",

            "reasoning":
                "Claim meets standard processing criteria."
        }