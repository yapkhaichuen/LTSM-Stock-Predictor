# Summary function
def short_summary():
    summary = [
        {
            "Ticker": 1,
        }
    ]
    """save data to json file"""
    with open("temp.json", "w") as outfile:
        json.dump(summary, outfile, indent=4, sort_keys=False)
    return summary


# Call function
short_summary()
