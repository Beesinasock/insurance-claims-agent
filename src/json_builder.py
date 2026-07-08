import json
from pathlib import Path


class JsonBuilder:
    """
    Builds and saves the final JSON output.
    """

    def build_output(
        self,
        extracted_fields,
        validation_result,
        routing_result
    ):

        return {

            "extractedFields": extracted_fields,

            "missingFields":
                validation_result["missing_fields"],

            "recommendedRoute":
                routing_result["recommendedRoute"],

            "reasoning":
                routing_result["reasoning"]
        }

    def save_output(
        self,
        output_data,
        input_filename
    ):

        output_folder = Path("output")
        output_folder.mkdir(exist_ok=True)

        output_file = output_folder / (
            Path(input_filename).stem + ".json"
        )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                output_data,
                file,
                indent=4,
                ensure_ascii=False
            )

        return output_file