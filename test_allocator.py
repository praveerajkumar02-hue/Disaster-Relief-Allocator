from allocator import allocate_resource


def test_full_allocation():
    requests = [
        {
            "requester_id": "R001",
            "location": "Chennai",
            "resource_type": "Water",
            "quantity": 10,
            "vulnerable": True
        }
    ]

    resources = {"Water": 20}

    result = allocate_resource(requests, resources)

    assert result[0]["status"] == "Allocated"
    assert result[0]["quantity"] == 10
    assert result[0]["priority"] == "HIGH"
    assert resources["Water"] == 10


def test_partial_allocation():
    requests = [
        {
            "requester_id": "R002",
            "location": "Trichy",
            "resource_type": "Food",
            "quantity": 20,
            "vulnerable": False
        }
    ]

    resources = {"Food": 10}

    result = allocate_resource(requests, resources)

    assert result[0]["status"] == "Partially Allocated"
    assert result[0]["quantity"] == 10
    assert resources["Food"] == 0


def test_pending_allocation():
    requests = [
        {
            "requester_id": "R003",
            "location": "Madurai",
            "resource_type": "Medicine",
            "quantity": 5,
            "vulnerable": False
        }
    ]

    resources = {"Medicine": 0}

    result = allocate_resource(requests, resources)

    assert result[0]["status"] == "Pending"
    assert result[0]["quantity"] == 0


def test_vulnerable_request_gets_priority():
    requests = [
        {
            "requester_id": "NORMAL",
            "location": "Chennai",
            "resource_type": "Water",
            "quantity": 10,
            "vulnerable": False
        },
        {
            "requester_id": "HIGH",
            "location": "Chennai",
            "resource_type": "Water",
            "quantity": 10,
            "vulnerable": True
        }
    ]

    resources = {"Water": 10}

    result = allocate_resource(requests, resources)

    assert result[0]["requester_id"] == "HIGH"
    assert result[0]["status"] == "Allocated"
    assert result[1]["status"] == "Pending"


def test_empty_requests():
    requests = []
    resources = {"Water": 20}

    result = allocate_resource(requests, resources)

    assert result == []


def test_unknown_resource_type():
    requests = [
        {
            "requester_id": "R004",
            "location": "Salem",
            "resource_type": "Blankets",
            "quantity": 5,
            "vulnerable": False
        }
    ]

    resources = {"Water": 20}

    result = allocate_resource(requests, resources)

    assert result[0]["status"] == "Pending"
    assert result[0]["quantity"] == 0


def test_zero_quantity_request():
    requests = [
        {
            "requester_id": "R005",
            "location": "Erode",
            "resource_type": "Water",
            "quantity": 0,
            "vulnerable": False
        }
    ]

    resources = {"Water": 20}

    result = allocate_resource(requests, resources)

    assert result[0]["status"] == "Pending"
    assert result[0]["quantity"] == 0


def test_negative_quantity_request():
    requests = [
        {
            "requester_id": "R006",
            "location": "Coimbatore",
            "resource_type": "Food",
            "quantity": -5,
            "vulnerable": False
        }
    ]

    resources = {"Food": 20}

    result = allocate_resource(requests, resources)

    assert result[0]["status"] == "Pending"
    assert result[0]["quantity"] == 0
    
