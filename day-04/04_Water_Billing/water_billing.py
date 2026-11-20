def validate_household(line, households):
    fields = line.strip().split(",")
    if len(fields) != 5:
        return None, "Expected exactly five comma-separated fields"

    meter = fields[0].strip()
    name = fields[1].strip()
    previous_text = fields[2].strip()
    current_text = fields[3].strip()
    area = fields[4].strip()

    if meter == "" or name == "" or previous_text == "" or current_text == "" or area == "":
        return None, "One or more required fields are missing"
    if meter in households:
        return None, "Duplicate meter number: " + meter

    try:
        previous = float(previous_text)
        current = float(current_text)
    except ValueError:
        return None, "Previous or current reading is not numeric"

    if not (previous >= 0 and current >= 0 and previous < float("inf") and current < float("inf")):
        return None, "Readings must be non-negative, finite numbers"
    if current < previous:
        return None, "Current reading is below previous reading"

    return {"meter": meter, "name": name, "previous": previous,
            "current": current, "area": area}, ""

def calculate_consumption(previous, current):
    return current - previous

def calculate_bill(consumption):
    if consumption <= 6:
        return 0.0
    elif consumption <= 20:
        return (consumption - 6) * 8.50
    else:
        return 14 * 8.50 + (consumption - 20) * 12.00

def classify_consumption(consumption):
    if consumption <= 20:
        return "LOW"
    elif consumption <= 50:
        return "MODERATE"
    else:
        return "HIGH"

def rank_households(records):
    i = 0
    while i < len(records):
        highest = i
        j = i + 1
        while j < len(records):
            if records[j]["consumption"] > records[highest]["consumption"]:
                highest = j
            j += 1
        records[i], records[highest] = records[highest], records[i]
        i += 1

def main():
    households = {}  
    errors = []      
    line_count = 0
    try:
        with open("water_readings.txt", "r", encoding="utf-8") as source:
            for original_line in source:
                line_count += 1
                line = original_line.strip()
                record, reason = validate_household(line, households)
                if reason != "":
                    errors.append("Line " + str(line_count) + ": " + reason + " | " + line)
                    continue

               
                record["consumption"] = calculate_consumption(record["previous"], record["current"])
                
                record["bill"] = calculate_bill(record["consumption"])
                
                record["category"] = classify_consumption(record["consumption"])
                households[record["meter"]] = record
    except FileNotFoundError:
        print("ERROR: water_readings.txt is missing from the working folder.")
        return

    ranking = []
    total_consumption = 0.0
    total_billing = 0.0
    low_count = 0
    moderate_count = 0
    high_count = 0
    for meter in households:
        record = households[meter]
        ranking.append(record)
        total_consumption += record["consumption"]
        total_billing += record["bill"]
        if record["category"] == "LOW":
            low_count += 1
        elif record["category"] == "MODERATE":
            moderate_count += 1
        else:
            high_count += 1

    
    rank_households(ranking)

    
    with open("billing_report.txt", "w", encoding="utf-8") as report:
        report.write("COMMUNITY WATER CONSUMPTION AND BILLING REPORT\n")
        report.write("=" * 90 + "\n")
        report.write(f'{"METER":<9} {"HOUSEHOLD":<24} {"AREA":<17} {"USAGE kL":>9} {"BILL (R)":>12} {"CATEGORY":<9}\n')
        report.write("-" * 90 + "\n")
        for record in ranking:
            report.write(f'{record["meter"]:<9} {record["name"]:<24} {record["area"]:<17} '
                         f'{record["consumption"]:>9.2f} {record["bill"]:>12.2f} {record["category"]:<9}\n')

        report.write("\nTOP FIVE HIGHEST WATER CONSUMERS\n")
        report.write("-" * 55 + "\n")
        index = 0
        for record in ranking:
            if index == 5:
                break
            index += 1
            report.write(f'{index}. {record["meter"]} - {record["name"]} ({record["area"]}): '
                         f'{record["consumption"]:.2f} kL | R{record["bill"]:.2f}\n')

        report.write("\nSUMMARY\n")
        report.write(f'Total input records: {line_count}\n')
        report.write(f'Accepted records: {len(ranking)}\n')
        report.write(f'Rejected records: {len(errors)}\n')
        report.write(f'LOW: {low_count} | MODERATE: {moderate_count} | HIGH: {high_count}\n')
        report.write(f'Total water consumption: {total_consumption:.2f} kL\n')
        report.write(f'Total billing: R{total_billing:.2f}\n')

   
    with open("errors.log", "w", encoding="utf-8") as error_file:
        for error in errors:
            error_file.write(error + "\n")

    print("COMMUNITY WATER BILLING PROCESSOR")
    print("Input records:", line_count)
    print("Accepted:", len(ranking), "Rejected:", len(errors))
    print("LOW:", low_count, "MODERATE:", moderate_count, "HIGH:", high_count)
    print("Total billing: R" + f"{total_billing:.2f}")
    print("Files created: billing_report.txt, errors.log")



if __name__ == "__main__":
    main()
