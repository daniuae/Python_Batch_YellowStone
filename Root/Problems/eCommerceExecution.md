# EcommerceAnalyzer - Step-by-Step Execution in VS Code

Copy the entire code below into a file named:

```text
main.py
```

and run:

```bash
python main.py
```

---

```python
import pandas as pd

# ==========================================
# E-Commerce Order Analysis
# ==========================================

class EcommerceAnalyzer:

    # Method 1
    def create_order_df(self, data: list) -> pd.DataFrame:
        return pd.DataFrame(
            data,
            columns=["CustomerID", "Category", "OrderDate", "OrderStatus"]
        )

    # Method 2
    def monthly_delivery_rate(self, df: pd.DataFrame) -> pd.DataFrame:

        temp = df.copy()
        temp["Month"] = temp["OrderDate"].str[:7]

        total_orders = (
            temp.groupby(["CustomerID", "Month"])
            .size()
            .reset_index(name="TotalOrders")
        )

        delivered_orders = (
            temp[temp["OrderStatus"] == "Delivered"]
            .groupby(["CustomerID", "Month"])
            .size()
            .reset_index(name="DeliveredOrders")
        )

        result = total_orders.merge(
            delivered_orders,
            on=["CustomerID", "Month"],
            how="left"
        )

        result["DeliveredOrders"] = (
            result["DeliveredOrders"]
            .fillna(0)
            .astype(int)
        )

        result["Delivery Rate"] = (
            result["DeliveredOrders"]
            / result["TotalOrders"]
            * 100
        )

        return result[["CustomerID", "Month", "Delivery Rate"]]

    # Method 3
    def add_return_flag(self, df: pd.DataFrame) -> pd.DataFrame:

        result = df.copy()

        result["IsReturned"] = (
            result["OrderStatus"] == "Returned"
        ).astype(int)

        return result

    # Method 4
    def frequent_returners(
        self,
        df: pd.DataFrame,
        threshold: int
    ) -> pd.DataFrame:

        result = (
            df[df["OrderStatus"] == "Returned"]
            .groupby("CustomerID")
            .size()
            .reset_index(name="ReturnCount")
        )

        return result[result["ReturnCount"] > threshold]

    # Method 5
    def category_order_summary(
        self,
        df: pd.DataFrame
    ) -> pd.DataFrame:

        summary = pd.crosstab(
            df["Category"],
            df["OrderStatus"]
        )

        summary = summary.reindex(
            columns=["Delivered", "Cancelled", "Returned"],
            fill_value=0
        )

        return summary.reset_index()


# =====================================================
# STEP 1 - Create Object
# =====================================================

analyzer = EcommerceAnalyzer()

print("\n" + "=" * 60)
print("STEP 1 - OBJECT CREATED")
print("=" * 60)
print(analyzer)

# =====================================================
# STEP 2 - Create Sample Data
# =====================================================

data = [
    [101, "Electronics", "2026-06-01", "Delivered"],
    [101, "Electronics", "2026-06-05", "Returned"],
    [102, "Fashion", "2026-06-03", "Delivered"],
    [102, "Fashion", "2026-06-08", "Cancelled"],
    [103, "Books", "2026-06-10", "Delivered"],
    [103, "Books", "2026-06-15", "Delivered"],
    [101, "Books", "2026-07-01", "Delivered"],
    [101, "Books", "2026-07-05", "Returned"]
]

print("\n" + "=" * 60)
print("STEP 2 - SAMPLE DATA")
print("=" * 60)

for row in data:
    print(row)

# =====================================================
# STEP 3 - Create DataFrame
# =====================================================

df = analyzer.create_order_df(data)

print("\n" + "=" * 60)
print("STEP 3 - DATAFRAME CREATED")
print("=" * 60)
print(df)

# =====================================================
# STEP 4 - Monthly Delivery Rate
# =====================================================

delivery_rate_df = analyzer.monthly_delivery_rate(df)

print("\n" + "=" * 60)
print("STEP 4 - MONTHLY DELIVERY RATE")
print("=" * 60)
print(delivery_rate_df)

# =====================================================
# STEP 5 - Add Return Flag
# =====================================================

return_flag_df = analyzer.add_return_flag(df)

print("\n" + "=" * 60)
print("STEP 5 - RETURN FLAG")
print("=" * 60)
print(return_flag_df)

# =====================================================
# STEP 6 - Frequent Returners
# =====================================================

returners_df = analyzer.frequent_returners(
    df,
    threshold=1
)

print("\n" + "=" * 60)
print("STEP 6 - FREQUENT RETURNERS")
print("=" * 60)
print(returners_df)

# =====================================================
# STEP 7 - Category Order Summary
# =====================================================

summary_df = analyzer.category_order_summary(df)

print("\n" + "=" * 60)
print("STEP 7 - CATEGORY ORDER SUMMARY")
print("=" * 60)
print(summary_df)

print("\n" + "=" * 60)
print("PROGRAM EXECUTED SUCCESSFULLY")
print("=" * 60)
```

---

## Expected Learning Flow

```text
Create Object
      │
      ▼
Create Sample Data
      │
      ▼
Create DataFrame
      │
      ▼
monthly_delivery_rate()
      │
      ▼
add_return_flag()
      │
      ▼
frequent_returners()
      │
      ▼
category_order_summary()
```

This version is ideal for VS Code because every step is clearly separated and printed, making it easy for trainees to understand the execution flow.
