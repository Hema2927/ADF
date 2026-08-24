from fastapi import FastAPI

app = FastAPI(
    title="Enterprise Orders API",
    description="REST API for the Enterprise Integration Pipeline",
    version="1.0.0"
)


# --------------------------------------------------
# Sample Orders Data
# --------------------------------------------------

orders = [
    {
        "id": 1001,
        "created_at": "2026-08-20T10:30:00Z",
        "customer": {
            "id": 501,
            "email": "customer1@example.com"
        },
        "line_items": [
            {
                "sku": "ABC-001",
                "quantity": 2,
                "price": 150.00
            },
            {
                "sku": "XYZ-001",
                "quantity": 1,
                "price": 100.00
            }
        ]
    },
    {
        "id": 1002,
        "created_at": "2026-08-20T11:15:00Z",
        "customer": {
            "id": 502,
            "email": "customer2@example.com"
        },
        "line_items": [
            {
                "sku": "ABC-002",
                "quantity": 3,
                "price": 200.00
            }
        ]
    },
    {
        "id": 1003,
        "created_at": "2026-08-21T09:45:00Z",
        "customer": {
            "id": 503,
            "email": "customer3@example.com"
        },
        "line_items": [
            {
                "sku": "XYZ-002",
                "quantity": 5,
                "price": 75.00
            }
        ]
    }
]


# --------------------------------------------------
# Home API
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Enterprise Orders API is running",
        "version": "1.0.0"
    }


# --------------------------------------------------
# Orders API
# --------------------------------------------------

@app.get("/v1/orders")
def get_orders(
    limit: int = 100,
    cursor: int = 0
):
    """
    Get orders using cursor-based pagination.
    """

    # Make sure limit is valid
    if limit <= 0:
        limit = 100

    # Get the requested page
    start = cursor
    end = start + limit

    page_orders = orders[start:end]

    # Check whether more records exist
    has_more = end < len(orders)

    # Calculate next cursor
    next_cursor = end if has_more else None

    return {
        "orders": page_orders,
        "has_more": has_more,
        "next_cursor": next_cursor
    }