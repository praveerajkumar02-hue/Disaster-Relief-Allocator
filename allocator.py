def allocate_resource(requests, resources):
    allocations = []

    # HIGH priority requests first
    sorted_requests = sorted(
        requests,
        key=lambda r: r.get("vulnerable", False),
        reverse=True
    )

    for request in sorted_requests:

        resource_type = request["resource_type"]
        quantity = int(request["quantity"])

        available = resources.get(resource_type, 0)

        if available >= quantity:
            resources[resource_type] -= quantity

            allocations.append({
                "requester_id": request["requester_id"],
                "location": request["location"],
                "resource_type": resource_type,
                "quantity": quantity,
                "status": "Allocated",
                "priority": "HIGH" if request["vulnerable"] else "NORMAL"
            })

        elif available > 0:
            allocations.append({
                "requester_id": request["requester_id"],
                "location": request["location"],
                "resource_type": resource_type,
                "quantity": available,
                "status": "Partially Allocated",
                "priority": "HIGH" if request["vulnerable"] else "NORMAL"
            })

            resources[resource_type] = 0

        else:
            allocations.append({
                "requester_id": request["requester_id"],
                "location": request["location"],
                "resource_type": resource_type,
                "quantity": 0,
                "status": "Pending",
                "priority": "HIGH" if request["vulnerable"] else "NORMAL"
            })

    return allocations