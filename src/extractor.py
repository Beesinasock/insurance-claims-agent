import re

from src.constants import REQUIRED_FIELDS


class FieldExtractor:

    def __init__(self):

        self.patterns = {

            "Policy Number":
                r"Policy Number:\s*(.*)",

            "Policyholder Name":
                r"Policyholder Name:\s*(.*)",

            "Effective Dates":
                r"Effective Dates:\s*(.*)",

            "Incident Date":
                r"Incident Date:\s*(.*)",

            "Incident Time":
                r"Incident Time:\s*(.*)",

            "Location":
                r"Location:\s*(.*)",

            "Description":
                r"Description:\s*([\s\S]*?)\nClaimant:",

            "Claimant":
                r"Claimant:\s*(.*)",

            "Third Parties":
                r"Third Parties:\s*(.*)",

            "Contact Details":
                r"Contact Details:\s*(.*)",

            "Asset Type":
                r"Asset Type:\s*(.*)",

            "Asset ID":
                r"Asset ID:\s*(.*)",

            "Estimated Damage":
                r"Estimated Damage:\s*(.*)",

            "Claim Type":
                r"Claim Type:\s*(.*)",

            "Attachments":
                r"Attachments:\s*(.*)",

            "Initial Estimate":
                r"Initial Estimate:\s*(.*)"
        }

    def extract_fields(self, text):

        extracted = {}

        for field, pattern in self.patterns.items():

            match = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if match:

                extracted[field] = match.group(1).strip()

            else:

                extracted[field] = None

        return extracted