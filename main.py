from pathlib import Path

from src.parser import DocumentParser
from src.extractor import FieldExtractor
from src.validator import ClaimValidator
from src.router import ClaimRouter
from src.json_builder import JsonBuilder


def main():

    # Initialize all components
    parser = DocumentParser()
    extractor = FieldExtractor()
    validator = ClaimValidator()
    router = ClaimRouter()
    json_builder = JsonBuilder()

    input_folder = Path("input")

    # Check if input folder exists
    if not input_folder.exists():
        print("Input folder not found!")
        return

    # Get all files from input folder
    files = [file for file in input_folder.iterdir() if file.is_file()]

    if not files:
        print("No documents found in the input folder.")
        return

    # Process each document
    for file in files:

        print("\n" + "=" * 70)
        print(f"Processing File: {file.name}")
        print("=" * 70)

        try:

            # -----------------------------
            # Step 1: Read Document
            # -----------------------------
            text = parser.read_document(file)

            # -----------------------------
            # Step 2: Extract Fields
            # -----------------------------
            extracted_fields = extractor.extract_fields(text)

            # -----------------------------
            # Step 3: Validate Fields
            # -----------------------------
            validation_result = validator.validate(extracted_fields)

            # -----------------------------
            # Step 4: Determine Route
            # -----------------------------
            routing_result = router.determine_route(
                extracted_fields,
                validation_result
            )

            # -----------------------------
            # Step 5: Build JSON Output
            # -----------------------------
            output_json = json_builder.build_output(
                extracted_fields,
                validation_result,
                routing_result
            )

            # -----------------------------
            # Step 6: Save JSON File
            # -----------------------------
            saved_file = json_builder.save_output(
                output_json,
                file.name
            )

            # -----------------------------
            # Display Results
            # -----------------------------
            print("\nExtracted Fields")
            print("-" * 40)

            for field, value in extracted_fields.items():
                print(f"{field}: {value}")

            print("\nMissing Fields")
            print("-" * 40)
            print(validation_result["missing_fields"])

            print("\nInconsistent Fields")
            print("-" * 40)
            print(validation_result["inconsistent_fields"])

            print("\nRecommended Route")
            print("-" * 40)
            print(routing_result["recommendedRoute"])

            print("\nReason")
            print("-" * 40)
            print(routing_result["reasoning"])

            print("\nJSON Saved To")
            print("-" * 40)
            print(saved_file)

        except Exception as e:

            print(f"\nError processing {file.name}")
            print(f"Reason: {e}")

    print("\n" + "=" * 70)
    print("All documents processed successfully.")
    print("=" * 70)


if __name__ == "__main__":
    main()