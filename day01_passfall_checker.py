# Day 1 - Pass/Fail Checker
# Checks RSRP values against a threshold and reports status
# Part of Apple Modem System Test Engineer prep

test_results = {
    "RRC_Setup": -85.0,
    "Handover": -103.0,
    "NAS_Attach": -78.5,
    "PDCP_Throughput": -92.0
}

for test, rsrp in test_results.items():
    status = "PASS" if rsrp >= -90 else "FAIL"
    print(f"{test}: {rsrp} dBm -- {status}")
