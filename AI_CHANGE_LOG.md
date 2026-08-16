# AI Change Loop Evidence

## AI Tool
ChatGPT

## Feature Request

Add validation to the Disaster Relief Resource Allocator so that
resource requests with zero or negative quantities are rejected
and marked as Pending with quantity 0.

Valid positive-quantity allocation behavior should remain unchanged.

## Initial Test Status

Before the feature change:

7 tests passed.

## Attempt 1 — Feature Implementation

The allocator was updated to check the requested quantity before
performing resource allocation.

If the quantity is zero or negative, the request is marked as
Pending with quantity 0.

## Test After Implementation

Command:

python -m pytest

Result:

1 failed, 6 passed

Failed test:

test_zero_quantity_request

Reason:

The existing test expected a zero-quantity request to be
"Allocated", while the new feature requires it to be
"Pending".

## Correction

The zero-quantity test was updated to expect "Pending".

A new test was added for negative quantities.

## Final Test

Command:

python -m pytest

Result:

8 passed

## Application Verification

The Streamlit application was started successfully using:

python -m streamlit run app.py

A normal vulnerable Water request was successfully allocated.

Result:

Requested quantity: 10
Priority: HIGH
Status: Allocated
Remaining Water: 990

## Final Status

The new quantity validation feature was successfully implemented.

Positive quantities continue to follow the existing allocation
logic.

Zero and negative quantities are rejected and marked as Pending.

All 8 automated tests pass.