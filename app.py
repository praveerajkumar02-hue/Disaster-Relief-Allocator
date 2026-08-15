import streamlit as st
from allocator import allocate_resource
from validation import validate_identity, check_duplicate


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Disaster Relief Resource Allocator",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 Disaster Relief Resource Allocator")

st.write(
    "Allocate limited food, water, and shelter resources "
    "to verified disaster relief requests."
)


# -----------------------------
# Session State
# -----------------------------

if "requests" not in st.session_state:
    st.session_state.requests = []

if "resources" not in st.session_state:
    st.session_state.resources = {
        "Food": 500,
        "Water": 1000,
        "Shelter": 200
    }

if "allocations" not in st.session_state:
    st.session_state.allocations = []


# -----------------------------
# Dashboard
# -----------------------------

st.subheader("📊 Relief Operations Dashboard")

total_requests = len(st.session_state.requests)

high_priority = sum(
    1
    for request in st.session_state.requests
    if request["vulnerable"]
)

allocated_requests = sum(
    1
    for allocation in st.session_state.allocations
    if allocation["status"] in ["Allocated", "Partially Allocated"]
)

pending_requests = sum(
    1
    for allocation in st.session_state.allocations
    if allocation["status"] == "Pending"
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📋 Total Requests",
        total_requests
    )

with col2:
    st.metric(
        "🔴 High Priority",
        high_priority
    )

with col3:
    st.metric(
        "✅ Allocated",
        allocated_requests
    )

with col4:
    st.metric(
        "⏳ Pending",
        pending_requests
    )


st.divider()


# -----------------------------
# Available Resources
# -----------------------------

st.subheader("📦 Available Resources")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Food Kits",
        st.session_state.resources["Food"]
    )

with col2:
    st.metric(
        "Water Bottles",
        st.session_state.resources["Water"]
    )

with col3:
    st.metric(
        "Shelter Spaces",
        st.session_state.resources["Shelter"]
    )


st.divider()


# -----------------------------
# Relief Request Form
# -----------------------------

st.subheader("📋 Create Relief Request")

with st.form("relief_request_form"):

    requester_id = st.text_input(
        "Requester ID",
        placeholder="Example: NGO001"
    )

    location = st.text_input(
        "Disaster Location",
        placeholder="Example: Trichy"
    )

    resource_type = st.selectbox(
        "Resource Required",
        ["Food", "Water", "Shelter"]
    )

    quantity = st.number_input(
        "Quantity Required",
        min_value=1,
        step=1
    )

    vulnerable = st.selectbox(
        "Is this request for a vulnerable group?",
        ["No", "Yes"]
    )

    submitted = st.form_submit_button(
        "Submit Relief Request"
    )


# -----------------------------
# Process Request
# -----------------------------

if submitted:

    valid, message = validate_identity(requester_id)

    if not valid:

        st.error(message)

    elif not location.strip():

        st.error(
            "Please enter a disaster location."
        )

    elif check_duplicate(
        st.session_state.requests,
        requester_id,
        location,
        resource_type
    ):

        st.warning(
            "⚠️ Duplicate request detected."
        )

    else:

        request = {
            "requester_id": requester_id.strip().upper(),
            "location": location.strip(),
            "resource_type": resource_type,
            "quantity": int(quantity),
            "vulnerable": vulnerable == "Yes"
        }

        st.session_state.requests.append(request)

        st.success(
            "✅ Relief request submitted successfully!"
        )


# -----------------------------
# Submitted Requests
# -----------------------------

st.divider()

st.subheader("📋 Submitted Relief Requests")

if st.session_state.requests:

    for i, request in enumerate(
        st.session_state.requests,
        start=1
    ):

        st.write(f"### Request {i}")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.write(
                f"**Requester:** "
                f"{request['requester_id']}"
            )

            st.write(
                f"**Location:** "
                f"{request['location']}"
            )

        with col2:

            st.write(
                f"**Resource:** "
                f"{request['resource_type']}"
            )

            st.write(
                f"**Quantity:** "
                f"{request['quantity']}"
            )

        with col3:

            priority = (
                "HIGH"
                if request["vulnerable"]
                else "NORMAL"
            )

            st.write(
                f"**Priority:** {priority}"
            )

        st.divider()

else:

    st.info(
        "No relief requests submitted yet."
    )


# -----------------------------
# Resource Allocation
# -----------------------------

st.subheader("🚑 Resource Allocation")

if st.button("🚑 Allocate Resources"):

    if not st.session_state.requests:

        st.warning(
            "⚠️ Please submit at least one "
            "relief request first."
        )

    else:

        st.session_state.allocations = allocate_resource(
            st.session_state.requests,
            st.session_state.resources
        )

        st.success(
            "✅ Resource allocation completed!"
        )


# -----------------------------
# Allocation Results
# -----------------------------

if st.session_state.allocations:

    st.subheader("📊 Allocation Results")

    for i, allocation in enumerate(
        st.session_state.allocations,
        start=1
    ):

        st.write(f"### Allocation {i}")

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:

            st.write(
                f"**Requester:** "
                f"{allocation['requester_id']}"
            )

        with col2:

            st.write(
                f"**Resource:** "
                f"{allocation['resource_type']}"
            )

        with col3:

            st.write(
                f"**Quantity:** "
                f"{allocation['quantity']}"
            )

        with col4:

            st.write(
                f"**Priority:** "
                f"{allocation['priority']}"
            )

        with col5:

            st.write(
                f"**Status:** "
                f"{allocation['status']}"
            )

        st.divider()


# -----------------------------
# Remaining Resources
# -----------------------------

st.subheader("📦 Remaining Resources")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Food Remaining",
        st.session_state.resources["Food"]
    )

with col2:

    st.metric(
        "Water Remaining",
        st.session_state.resources["Water"]
    )

with col3:

    st.metric(
        "Shelter Remaining",
        st.session_state.resources["Shelter"]
    )
    # -----------------------------
# Reset Demo
# -----------------------------

st.divider()

st.subheader("🔄 Demo Controls")

if st.button("🗑️ Reset All Data"):

    st.session_state.requests = []

    st.session_state.allocations = []

    st.session_state.resources = {
        "Food": 500,
        "Water": 1000,
        "Shelter": 200
    }

    st.success("✅ All demo data has been reset.")

    st.rerun()