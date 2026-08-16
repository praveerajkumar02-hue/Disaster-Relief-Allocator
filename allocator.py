def allocate_resource(requests, resources):
    allocations = []

    # Process vulnerable requests first
    sorted_requests = sorted(
        requests,
        key=lambda r: r.get("vulnerable", False),
        reverse=True
    )

    for request in sorted_requests:

        resource_type = request["resource_type"]
        quantity = int(request["quantity"])

        # Reject zero and negative quantities
        if quantity <= 0:
            allocations.append({
                "requester_id": request["requester_id"],
                "location": request["location"],
                "resource_type": resource_type,
                "quantity": 0,
                "status": "Pending",
                "priority": (
                    "HIGH"
                    if request.get("vulnerable", False)
                    else "NORMAL"
                )
            })
            continue

        # Get available resource quantity
        available = resources.get(resource_type, 0)

        # Full allocation
        if available >= quantity:
            resources[resource_type] -= quantity

            allocations.append({
                "requester_id": request["requester_id"],
                "location": request["location"],
                "resource_type": resource_type,
                "quantity": quantity,
                "status": "Allocated",
                "priority": (
                    "HIGH"
                    if request.get("vulnerable", False)
                    else "NORMAL"
                )
            })

        # Partial allocation
        elif available > 0:
            allocations.append({
                "requester_id": request["requester_id"],
                "location": request["location"],
                "resource_type": resource_type,
                "quantity": available,
                "status": "Partially Allocated",
                "priority": (
                    "HIGH"
                    if request.get("vulnerable", False)
                    else "NORMAL"
                )
            })

            resources[resource_type] = 0

        # No resource available
        else:
            allocations.append({
                "requester_id": request["requester_id"],
                "location": request["location"],
                "resource_type": resource_type,
                "quantity": 0,
                "status": "Pending",
                "priority": (
                    "HIGH"
                    if request.get("vulnerable", False)
                    else "NORMAL"
                )
            })

    return allocations
