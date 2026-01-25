key1 = "issueSummary"
key2 = "XY&^$#*@!1234%^&"

data = {
    "id": "AWcvsjx864kVeDHDi2gB",
    "instanceId": "E-NETWORK-EVENT-AWcvsjx864kVeDHDi2gB-1542693469197",
    "category": "Warn",
    "status": "NEW",
    "timestamp": 1542693469197,
    "severity": "P1",
    "domain": "Availability",
    "source": "DNAC",
    "priority": "P1",
    "type": "Network",
    "title": "Device unreachable",
    "description": "This network device leaf2.abc.inc is unreachable from controller. The device role is ACCESS.",
    "actualServiceId": "10.10.20.82",
    "assignedTo": "",
    "enrichmentInfo": {
        "issueDetails": {
            "issue": [
                {
                    "issueId": "AWcvsjx864kVeDHDi2gB",
                    "issueSource": "Cisco DNA",
                    "issueCategory": "Availability",
                    "issueName": "snmp_device_down",
                    "issueDescription": "This network device leaf2.abc.inc is unreachable from controller. The device role is ACCESS.",
                    "issueEntity": "network_device",
                    "issueEntityValue": "10.10.20.82",
                    "issueSeverity": "HIGH",
                    "issuePriority": "",
                    "issueSummary": "Network Device 10.10.20.82 Is Unreachable From Controller",
                    "issueTimestamp": 1542693469197,
                    "suggestedActions": [
                        {
                            "message": "Verify device reachability",
                            "steps": [
                                "Check device power",
                                "Verify network connectivity",
                                "Check SNMP configuration"
                            ]
                        }
                    ]
                }
            ]
        }
    }
}
