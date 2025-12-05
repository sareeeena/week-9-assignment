def filter_alerts(alerts,min_severity):
    result=[]

    if min_severity=="ADVISORY":
        level=1
    elif min_severity=="WATCH":
        level=2
    else:
        level=3

    for alert in alerts:
        if alert =="":
            continue
    
        parts=alert.split(" - ")
        if len(parts)<3:
            continue

        first_two_data=parts[0]
        explanation=parts[2]
        splitted_data=first_two_data.split(" ")

        if len(splitted_data)<2:
            continue

        severity=splitted_data[0]
        location=splitted_data[1]
        severity_nobrackets=severity.replace("[","").replace("]","")

        if severity_nobrackets=="ADVISORY":
            severity_level=1
        elif severity_nobrackets=="WATCH":
            severity_level=2
        elif severity_nobrackets=="WARNING":
            severity_level=3
        else:
            continue

        if severity_level<level:
            continue

        summary=f"{severity_nobrackets} ({location}): {explanation}"
        result.append(summary)
    return result

weather_data = [
    "[ADVISORY] Austin - 11/05 08:00 - Dense fog reported.",
    "[ADVISORY] Dallas - 11/05 08:15 - Light rain expected.",
    "[WATCH] Houston - 11/05 12:00 - Conditions favorable for tornadoes.",
    "",
    "[WARNING] Galveston - 11/05 14:30 - Hurricane making landfall.",
    "[WARNING] Miami - 11/05 15:00 - Flash flooding imminent.",
    "[ADVISORY] Seattle - 11/05 16:00 - Light drizzle."
]
watches_and_warnings = filter_alerts(weather_data, "WATCH")
print(watches_and_warnings)

warnings_only = filter_alerts(weather_data, "WARNING")
print(warnings_only)
